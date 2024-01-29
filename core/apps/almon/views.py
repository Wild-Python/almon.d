from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView, ListView

from .models import Almon
from .forms import AlmonForm
# from .cryptor import Cryptor
from .utils import generate_random_password

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

from core.apps.users.forms import UpdatePasswordForm  # user app


@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'almon/home.html'


@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class AddNewPasswordView(LoginRequiredMixin, CreateView):
    model = Almon
    form_class = AlmonForm
    template_name = 'almon/add-new-password.html'
    success_url = reverse_lazy('almon:add-password')

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(self.request, f"New password added for {form.cleaned_data['application_name']}")
        return super().form_valid(form)


@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class UpdatePasswordView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Almon
    form_class = UpdatePasswordForm
    template_name = 'almon/update-password.html'
    success_message = 'Password updated successfully.!'

    def get_object(self, queryset=None):
        return get_object_or_404(Almon, id=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('almon:update-password', kwargs={'pk': self.object.id})


@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class DeletePasswordView(LoginRequiredMixin, DeleteView):
    model = Almon
    template_name = 'almon/manage-passwords.html'
    success_url = reverse_lazy('almon:manage-passwords')
    context_object_name = 'password'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Password Deleted.!')
        return super().delete(request, *args, **kwargs)


@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class SearchPasswordView(LoginRequiredMixin, ListView):
    queryset = Almon
    template_name = 'almon/search.html'
    context_object_name = 'passwords'

    def get_queryset(self):
        queryset = Almon.objects.filter(user=self.request.user)
        return queryset

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        searched = self.request.POST.get("password_search", "")
        self.object_list = queryset
        if searched:
            queryset = queryset.filter(Q(username__icontains=searched) | Q(email__icontains=searched))
        return self.render_to_response(self.get_context_data(object_list=queryset))


class ManagePasswordsView(LoginRequiredMixin, ListView):
    model = Almon
    context_object_name = 'all_passwords'
    template_name = 'almon/manage-passwords.html'

    def get_queryset(self, queryset=None):
        return Almon.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_passwords = self.get_queryset()

        sort_order = self.request.GET.get('sort_order', 'desc')
        if sort_order == 'asc':
            user_passwords = user_passwords.order_by('date_created')
        else:
            user_passwords = user_passwords.order_by('-date_created')

        context['all_passwords'] = user_passwords
        context['sort_order'] = sort_order

        if not user_passwords:
            context['no_password'] = "No password available. Please add password."

        return context


# generate random password
def generate_password(request):
    password = generate_random_password()
    return JsonResponse(
        {'password': password}
    )

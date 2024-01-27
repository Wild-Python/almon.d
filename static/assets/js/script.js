function generatePasswordHandler() {
    $.ajax({
        type: 'GET',
        url: '/generate-password/',
        success: function (data) {
            document.getElementsByName('password')[0].value = data.password;
        }
    });
}

function toggleView(id) {
    const input = document.getElementById(id);
    const icon = document.getElementById(`icon-${id}`)
    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("fa-eye")
        icon.classList.add("fa-eye-slash")
    } else {
        input.type = "password";
        icon.classList.remove("fa-eye-slash")
        icon.classList.add("fa-eye")
    }
}
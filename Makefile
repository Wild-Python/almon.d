.PHONY: runserver
runserver:
ifeq ($(port),)
	python -m manage runserver
else
	python -m manage runserver $(port)
endif

.PHONY: superuser
superuser:
	python -m manage createsuperuser

.PHONY: migrations
migrations:
ifeq ($(app),)
	python -m manage makemigrations
else
	python -m manage makemigrations $(app)
endif

.PHONY: migrate
migrate:
	python -m manage migrate

.PHONY: shell
shell:
	python -m manage shell

.PHONY: dbshell
dbshell:
	python -m manage dbshell



from django.contrib import admin
from django.apps import apps

# Register your models here.
models = apps.get_models()

for model in models:
    if not admin.site.is_registered(model):
        try:
            admin.site.register(model)
        except Exception as e:
            continue
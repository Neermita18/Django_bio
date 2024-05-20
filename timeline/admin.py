from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(MoleculeDisc)
class DeptAdmin(admin.ModelAdmin):
    pass

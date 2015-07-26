from django.contrib import admin

# Register your models here.

from .models import PersonalInfo
from .forms import PersonalInfoForm

class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = PersonalInfoForm
    # class Meta:
    #     model = PersonalInfo

admin.site.register(PersonalInfo, PersonalInfoAdmin)
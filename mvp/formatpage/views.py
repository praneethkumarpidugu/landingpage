from django.shortcuts import render

# Create your views here.

from .forms import PersonalInfoForm

def home(request):
    title = 'You are not logged in'
    form = PersonalInfoForm(request.POST or None)
    context = {
        "template_title": title,
        "form": form
    }

    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        #     instance.full_name = "Praneeth"
        instance.save()
        context = {
            "template_title": "Thank you"
        }

    return render(request, "home.html", context)
from django.shortcuts import render

# Create your views here.

from .forms import ContactForm, PersonalInfoForm

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

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value

        # email = form.cleaned_data.get("email")
        # message = form.cleaned_data.get("message")
        # full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name

    context = {
        "form": form,
    }

    return render(request, "forms.html", context)
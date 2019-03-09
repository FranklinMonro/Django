from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'thirdapp/index.html')

def forms_view(request):
    form = forms.Formsname()
    if request.method == "POST":
        form = forms.Formsname(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("NAME:", form.cleaned_data['name'])
            print("EMAIL:", form.cleaned_data['email'])
            print("TEXT:", form.cleaned_data['text'])

    return render(request, 'thirdapp/forms_page.html', {'form':form})

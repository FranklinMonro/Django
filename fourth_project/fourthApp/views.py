from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number':100}
    return render(request, 'fourthApp/index.html', context_dict)

def other(request):
    return render(request, 'fourthApp/other.html')

def relative(request):
    return render(request, 'fourthApp/relative_url_templates.html')

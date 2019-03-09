from django.shortcuts import render
from second_app.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def users(request):
    my_user = User.objects.order_by('user_first_name')
    my_dict = {'users_dict': my_user}
    return render(request, 'users/users.html', context = my_dict )

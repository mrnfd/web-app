from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        print(1)
    else:
        return render(request,'buyer/register.html', {
            'form': UserCreationForm()
        })
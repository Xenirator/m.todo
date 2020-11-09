from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'todolist/index.html', {
        'todo_items': todo_items
    })


def login(request):
    return render(request, './registration/login.html')


def logout(request):
    return render(request, './registration/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, './registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, './registration/register.html', {'user_form': user_form})

@csrf_exempt
def add_todo(request):
    poster = request.user
    current_date = datetime.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=current_date, text=content, author=poster)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
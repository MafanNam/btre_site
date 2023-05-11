from django.shortcuts import render, redirect
from forms import CustomUserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        # Register User
        # first_name = request.GET['first_name']
        # last_name = request.GET['last_name']
        # username = request.GET['username']
        # email = request.GET['email']
        # password = request.GET['password']
        # password2 = request.GET['password2']
        #
        #     # Check if passwords match
        #     if password == password2:
        #         pass
        #     else:
        #         messages.error(request, 'Passwords do not match')
        #         return redirect('register')
        # else:
        #     return render(request, 'accounts/register.html')
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            return redirect('edit-account')

        else:
            messages.success(request, 'An error has occurred during registration')

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def login(request):
    if request.method == 'POST':
        # Login User
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

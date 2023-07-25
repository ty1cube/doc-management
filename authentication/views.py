from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser, Profile
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        email = request.POST['email']
        password = request.POST['password']
        try:
            email = CustomUser.objects.get(email=email)
            print(email)
        except:
            messages.error(request,'User does not exist')
        # Check username and password combination if correct
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            # return redirect('dashboard:dashboard-page')
            return render(request, 'dashboard/dashboard.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'authentication/index.html', {
                'error_message': 'Incorrect username and / or password.'
                })
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'authentication/index.html')


class LoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
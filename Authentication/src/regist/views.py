from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


from .forms import UserForm, LoginForm


#home
class home(View):
	def get(self, request):
		if request.user.is_authenticated():
			template_name= 'success.html'
			return render(request, template_name)
		else:
			template_name = 'logout.html'
			return render(request, template_name)

#logout
def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('home')
	else:	
		return render(request, 'not_logged_in.html')


#registration
class UserFormView(View):
	form_class = UserForm
	template_name = 'form.html'

	def get(self, request): 
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
            # cleaned data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.save()
			auth_user = authenticate(username=username, password=password)
			
			if auth_user is not None:

				if auth_user.is_active:
					login(request, auth_user)
					return  redirect('home.html')

			# redirect works for
		return render(request, self.template_name, {'form': form})   

#login
class LoginView(View):
	form_class = LoginForm
	template_name = 'login.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
       			print 'logged in'
       			return redirect('home')
       	     # Redirect to a success page.
		else:
			template_name = 'invalid_login.html'
			return render(request, template_name)
            # Return a 'disabled account' error message
		# else:
		# 		print 'invalid account'
  #       	# Return an 'invalid login' error message.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate
from .models import CustomUser

def home(request):
	return render(request, "home.html")


def signup(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			user = form.save(commit = False)
			user.is_active = False
			user.save()

			current_site = get_current_site(request)
			mail_subject = "Activate your account"
			message = render_to_string('acc_activation_email.html',{
					'user': user,
					'domain': current_site.domain,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
					'token': account_activation_token.make_token(user),
				})
			print(message)
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
					mail_subject, message, to = [to_email]
				)
			email.send()
			print("sent")
			return redirect('home')

	form = CustomUserCreationForm()
	print("no")
	context = {
		'form': form,
	}

	return render(request, "signup.html", context)


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = CustomUser.objects.get(pk = uid)
	except(TypeError, ValueError, OverflowError):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		# login(request, user)
		return HttpResponse("Thank you, your email has been confirmed!")

	else:
		return HttpResponse("Invalid Activation Link")
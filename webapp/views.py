from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, HttpResponse	
from django.http import JsonResponse 
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import timedelta

# from 
from webapp.models import Signin 
from webapp.models import Contact
import csv
import time
# Initialize Signin Table
userTable = User.objects.all()
# Create your views here.
def	index(request):
	if request.user.is_anonymous:
		return redirect('/login')	
	else:
		return render(request, 'index.html')


def	signin(request):
	return render(request, 'signin.html')

def llogin(request):
	return render(request, 'login.html')

def cyber(request):
	return render(request, 'cyber.html')

def code(request):
	return render(request, 'code.html')

def amazon(request):
	# ! - Affiliate capture Logic
	codeHTML = ''
	with open('amazon.csv', 'r') as prods:
		lines = csv.reader(prods)
		next(lines) 
		print(lines)
		for values in lines:
			link = values[0]
			product_name = values[1]
			price = values[2]
			discription = values[3]
			image_link = values[4]
			codeHTML = codeHTML + f'<div class="product"><span class="price">~{price}Rs.</span><img href="{link}" src="{image_link}" alt="product"><h3>{product_name}</h3><p>{discription}</p><a href="{link}" target="_blank" class="buy-now">Buy Now</a></div>'

	return render(request,'amazon.html', {'codeHTML' : mark_safe(codeHTML)})

# return

def contact(request):
	return render(request, 'contact.html')	

def about(request):
	return render(request, 'about.html')	

def product(request):
	return render(request, 'product.html')	


# note: Forms

# note: login
def	slogin(request):
	musername = request.POST.get('name')
	mpassword = request.POST.get('passwd')
	user = authenticate(username=musername, password=mpassword)
	print(user)
	# print("###########################################################################")
	if user is not None:
		
		messages.success(request, "Successfully logged in")
		login(request, user)
		return redirect('/home') 
	else:
		return render(request, 'login.html')


# note: Contact 
def	fContact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		contact_form = Contact(cname=name, cemail=email, csubject=subject, cdisc=message)
		contact_form.save()
		if 'join' in subject.lower() and 'class' in subject.lower():
			messages.success(request, "I will Contact you soon...")
		else:
			messages.success(request, "Form Successfully Submitted")
		return redirect('/')


# credentials = service_account.Credentials.from_service_account_file('path/to/client_secret.json')
# note: Signin
# signin
def signIn(request):
	

	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		# password = request.POST.get('passwd')
		conf = request.POST.get('c_passwd')
		user = User.objects.create(username=name, email=email)
		try:
			user.set_password(conf)	
			user.save()
			messages.success(request, "Successfully logged in")
			return redirect('/')
		except:
			return render(request, 'signin')
			
	

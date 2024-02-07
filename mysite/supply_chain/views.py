
from email.message import EmailMessage
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from supply_chain.models import seller_data1
from django.contrib.auth import logout
from django.contrib.auth.models import User
import smtplib
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def HomePage(request):
    try:
        return render(request, 'homepage.html')
    except Exception as e:
        return HttpResponseBadRequest(e)


def sales_form(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            mail_id = request.POST.get('mail_id')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            data = User.objects.all()
            print(data)
            for row in data:
                print(row)
                if(row.username==username):
                    return HttpResponse("Username is already been used")
                continue
            if password != confirm_password:
                    return HttpResponse("Your password and confirm password are not the same!!")
            else:
                email = EmailMessage('Successful Signup Confirmation','Dear '+str[username]+'\n\nCongratulations! You have successfully signed up for our platform. \n\nYour account is now ready to use.\n\nThank you for joining us.','supplychain587@gmail.com',[mail_id],)
                email.send()
                en=User.objects.create_user(username,mail_id,password)
                en.save()
                return HttpResponseRedirect(reverse('login'))
    except Exception as e:
        return HttpResponseBadRequest(e)
    return render(request, "signup.html")
# yyttfvh123  supplychain587@gmail.com


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login'))
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response



def seller(request):
    try:
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            user = request.user
            email = user.email
            shopname=request.POST.get('shopname')
            gst_number = request.POST.get('gst_number')
            category = request.POST.get('category')
            subcategory = request.POST.get('subcategory')
            product_number = request.POST.get('product_number')
            product_price = request.POST.get('product_price')
            sellerdata = seller_data1(first_name=first_name, last_name=last_name, phone_number=phone_number,
                              email=email,shopname=shopname,gst_number=gst_number, category=category, subcategory=subcategory,
                              product_number=product_number,product_price=product_price)
            sellerdata.save()
    except Exception as e:
        return HttpResponseBadRequest(e)
    return render(request, 'seller.html')

# def customer(request):
#     try:
#         if request.method == "POST":
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             phone_number = request.POST.get('phone_number')
#             user = request.user
#             email = user.email
#             shopname=request.POST.get('shopname')
#             gst_number = request.POST.get('gst_number')
#             category = request.POST.get('category')
#             subcategory = request.POST.get('subcategory')
#             product_number = request.POST.get('product_number')
#             product_price = request.POST.get('product_price')
#             sellerdata = seller_data1(first_name=first_name, last_name=last_name, phone_number=phone_number,
#                               email=email,shopname=shopname,gst_number=gst_number, category=category, subcategory=subcategory,
#                               product_number=product_number,product_price=product_price)
#             sellerdata.save()
#     except Exception as e:
#         return HttpResponseBadRequest(e)
#     return render(request, 'seller.html')

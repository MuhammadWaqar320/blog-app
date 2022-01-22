from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    allpost=Post.objects.all()
    context={"allpost":allpost}
    return render(request,"home/home.html",context)
def about(request):
    return render(request,"home/about.html")
def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        desc=request.POST.get('des')
        email=request.POST.get('email')
        if len(name)<3 or len(phone)<7 or len(desc)<3 or len(email)<5:
            messages.success(request,"Please fill the form correctly")
        else:
            contact=Contact(name=name,email=email,desc=desc,phone=phone)
            contact.save()
            messages.success(request,"Your message has been submitted")

    return render(request,"home/contact.html")
def Search(request):
    query=request.GET['search']
    allpostTitle=Post.objects.filter(title__icontains=query)
    allpostContent= Post.objects.filter(content__icontains=query)
    allpost=allpostTitle.union(allpostContent)
    context={"allpost":allpost,"query":query}
    return render(request,"home/search.html",context)
def handleSignUp(request):
    if request.method=='POST':
        username=request.POST['nameS']
        email=request.POST['emailS']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username)<2:
            messages.success(request, "Username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.success(request, "Username must be alphabet")
            return redirect('home')
        if pass1!=pass2:
            messages.success(request, "Password must match with confirmed password")
            return redirect('home')
        else:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name="ali"
            myuser.last_name="asif"
            myuser.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('home')

    else:
        return HttpResponse("404 - Not Found")
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
def handleLogin(request):
    if request.method=="POST":
        Username=request.POST['nameL']
        Password=request.POST['passL']
        isUser=authenticate(username=Username,password=Password)
        if isUser is not None:
            login(request,isUser)
            messages.success(request,"Logged in")
            return redirect('home')
        else:
            messages.error(request,"You have to register first")
            return redirect('home')

    else:
        return HttpResponse("404 - Not Found")
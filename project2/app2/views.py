from django.shortcuts import render,redirect
from .models import RegistrationData,ImageData,ProductData
from .forms import RegistrationForm,LoginForm,ImageForm,Inserting_data
from django.http.response import HttpResponse

def registration_view(request):
    if request.method=='POST':
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
           firstname= request.POST.get('firstname')
           lastname= request.POST.get('lastname')
           username= request.POST.get('username')
           password= request.POST.get('password')
           location= request.POST.get('location')
           mobile= request.POST.get('mobile')
           email= request.POST.get('email')

           data=RegistrationData(
               firstname=firstname,
               lastname=lastname,
               username=username,
               password=password,
               location=location,
               mobile=mobile,
               email=email
           )
           data.save()
           lform=LoginForm()
           return render(request,'login.html',{'lform':lform})
        else:
            return HttpResponse("No Data")
    else:
        rform=RegistrationForm()
        return render(request,'register.html',{'rform':rform})

def login_view(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            uname=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password=password)

            if uname and pwd :
                return redirect(home_view)
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse("User Invaild Data")
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})

def home_view(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            name=request.POST.get('name')
            image=request.POST.get('image')
            img=ImageData(
                name=name,
                image=image
            )
            img.save()
            form=ImageForm()
            return render(request,'home.html',{'form':form})
    else:
        form=ImageForm()
        return render(request,'home.html',{'form':form})

def contact_view(request):
        if request.method == 'POST':
            iform = Inserting_data(request.POST)
            if iform.is_valid():
                product_id = request.POST.get('product_id')
                product_name = request.POST.get('product_name')
                product_class = request.POST.get('product_class')
                product_color = request.POST.get('product_color')
                product_cost = request.POST.get('product_cost')

                data1 = ProductData(
                    product_id=product_id,
                    product_name=product_name,
                    product_class=product_class,
                    product_color=product_color,
                    product_cost=product_cost
                )
                data1.save()
                iform = Inserting_data()
                return render(request, 'contact.html', {'iform': iform})
            else:
                return HttpResponse("User Invaild Data")

        else:
            iform = Inserting_data()
            return render(request, 'contact.html', {'iform': iform})

def about_view(request):
    return render(request,'about.html')

def feedback_view(request):
    product = ProductData.objects.all()
    return render(request, 'feedback.html', {'product': product})

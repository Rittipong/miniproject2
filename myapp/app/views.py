from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
from app.models import person, minecrafe, cyberpunk, spiderman, blackmyt, doom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password


# Create your views here.

def index(request):
    all_person = person.objects.all()
    return render(request, 'index.html', {"all_person":all_person})


def adduser(request):
    if request.method == "POST":      # ถ้าคลิก submit if จะเป็นจริง
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["fname"]
        last_name =request.POST["lname"]
        user_name = request.POST["username"]

        user = person.objects.create(
            email=email,
            password=password,
			first_name=first_name,
			last_name=last_name,
			user_name=user_name,
			
        )
        user.save()

        #print(name, age)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/")       # เมื่อกรอกข้อมูลและ submit แล้วให้ไปเปิดหน้า index
    else:      #ถ้าไม่คลิก submit
        return render(request,"signup.html")


def custom_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # ตรวจสอบอีเมลและรหัสผ่านในฐานข้อมูล
        try:
            user = person.objects.get(email=email, password=password)
            request.session['user_id'] = user.id  # เก็บ user_id ใน session
            messages.success(request, 'เข้าสู่ระบบสำเร็จ')
            return redirect('/home')
        except person.DoesNotExist:
            messages.error(request, 'อีเมลหรือรหัสผ่านไม่ถูกต้อง')
            return redirect('/log')
    else:
        return render(request, 'login.html')
    
def Reminecraf(request):
    if request.method == "POST":      # ถ้าคลิก submit if จะเป็นจริง
        name = request.POST["name"]
        des = request.POST["des"]
        score = request.POST["score"]
        platform = request.POST["platform"]

        user = minecrafe.objects.create(
           name = name,
            des = des,
            score = score,
            platform = platform,
			
        )
        user.save()

        #print(name, age)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/re")       # เมื่อกรอกข้อมูลและ submit แล้วให้ไปเปิดหน้า index
    else:      #ถ้าไม่คลิก submit
        return render(request,"comment.html")

def Redoom(request):
    if request.method == "POST":      # ถ้าคลิก submit if จะเป็นจริง
        name = request.POST["name"]
        des = request.POST["des"]
        score = request.POST["score"]
        platform = request.POST["platform"]

        user = doom.objects.create(
           name = name,
            des = des,
            score = score,
            platform = platform,
			
        )
        user.save()

        #print(name, age)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/re")       # เมื่อกรอกข้อมูลและ submit แล้วให้ไปเปิดหน้า index
    else:      #ถ้าไม่คลิก submit
        return render(request,"comment.html")
    
def Recyberpunk(request):
    if request.method == "POST":      # ถ้าคลิก submit if จะเป็นจริง
        name = request.POST["name"]
        des = request.POST["des"]
        score = request.POST["score"]
        platform = request.POST["platform"]

        user = cyberpunk.objects.create(
           name = name,
            des = des,
            score = score,
            platform = platform,
			
        )
        user.save()

        #print(name, age)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/re")       # เมื่อกรอกข้อมูลและ submit แล้วให้ไปเปิดหน้า index
    else:      #ถ้าไม่คลิก submit
        return render(request,"comment.html")
    
def Respiderman(request):
    if request.method == "POST":      # ถ้าคลิก submit if จะเป็นจริง
        name = request.POST["name"]
        des = request.POST["des"]
        score = request.POST["score"]
        platform = request.POST["platform"]

        user = spiderman.objects.create(
           name = name,
            des = des,
            score = score,
            platform = platform,
			
        )
        user.save()

        #print(name, age)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/re")       # เมื่อกรอกข้อมูลและ submit แล้วให้ไปเปิดหน้า index
    else:      #ถ้าไม่คลิก submit
        return render(request,"comment.html")

def Reblackmyt(request):
    if request.method == "POST":      # ถ้าคลิก submit if จะเป็นจริง
        name = request.POST["name"]
        des = request.POST["des"]
        score = request.POST["score"]
        platform = request.POST["platform"]

        user = blackmyt.objects.create(
           name = name,
            des = des,
            score = score,
            platform = platform,
			
        )
        user.save()

        #print(name, age)
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        return redirect("/re")       # เมื่อกรอกข้อมูลและ submit แล้วให้ไปเปิดหน้า index
    else:      #ถ้าไม่คลิก submit
        return render(request,"comment.html")
    

def repassword(request):
    if request.method == "POST": 
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            # ตรวจสอบว่าอีเมลมีในฐานข้อมูลหรือไม่
            user = person.objects.get(email=email)
            
            # เข้ารหัสรหัสผ่านใหม่ก่อนบันทึก
            user.password = password
            user.save()
            
            messages.success(request, "อัพเดตรหัสผ่านเรียบร้อย")
            return redirect("/")
        except person.DoesNotExist:
            messages.error(request, "ไม่พบผู้ใช้งานที่มีอีเมลนี้")
            return render(request, 'repassword.html')
    
    else:
          return render(request, 'repassword.html')




def form(request):
	return render(request, 'form.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def news(request):
	return render(request, 'news.html')

def reviews(request):
	return render(request, 'reviews.html')

def mk(request):
	return render(request, 'mk.html')

def minecraft(request):
	return render(request, 'minecraft.html')
	
def doomm(request):
	return render(request,'doom.html')

def cy(request):
	return render(request,'cy.html')

def si(request):
	return render(request,'si.html')




def recy(request):
        comment =  cyberpunk.objects.all()  
        return render(request,'recy.html',{'comment':comment})

def redoom(request):
        comment =  doom.objects.all()
        return render(request,'redoom.html',{'comment':comment})

def remine(request):
        comment =  minecrafe.objects.all()
        return render(request,'remine.html',{'comment':comment})

def remk(request):
        comment =  blackmyt.objects.all()
        return render(request,'remk.html',{'comment':comment})

def resi(request):
        comment =  spiderman.objects.all()
        return render(request,'resi.html',{'comment':comment})




def home(request):
        return render(request,'home.html')




def commine(request):
        return render(request,'comminecrafe.html')

def comdoom(request):
        return render(request,'comdoom.html')

def comspider(request):
        return render(request,'comspider.html')

def comcyber(request):
        return render(request,'comcyberpunk.html')

def comblackmyt(request):
        return render(request,'comblack.html')
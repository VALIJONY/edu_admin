from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import LoginForm,AddPupilForm,AddTeacherForm,NewGroupForm,OpenGroupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from .models import Uquvchilar,Kurslar,Uqituvchilar,guruh,kunlar,guruh_kunlari,Dars_xonalari,Vaqtlar
# Create your views here.

class MainView(View):
    def get(self,request):
        return render(request,'index.html')
    
class AdminView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'admin.html')
    
class LoginView(View):
    def get(self,request):
        userlogin=LoginForm()
        return render(request,'login.html',{'form':userlogin})
    
    def post(self,request):
        check=AuthenticationForm(data=request.POST)
        if check.is_valid():
            user=check.get_user()
            login(request,user)
            return redirect('for_admin')
        else:
            return redirect('login')
        
        
#LOGOUT CLASSIDAN TAYYOR OLINADI HECH QANDAY TEMPLATE VA BOSHQA NARSALAR KERAK BO`LMAYDI.LOGOUT CLASSINI DJANGO KUTUBXONALARIDAN CHAQIRIB OLINADI

class LogoutView(LoginRequiredMixin,View):
         def get(self,request):
             logout(request)
             return redirect('main')
         
         
class UqituvchiQushishView(LoginRequiredMixin,View):
    def get(self,request):
        teacher=Uqituvchilar.objects.all()
        Form=AddTeacherForm()
        return render(request,'admin_services/uqituvchi_qush.html',{'teachers':teacher,'form':Form})
    def post(self,request):
        teacher=Uqituvchilar.objects.all()
        Form=AddTeacherForm(data=request.POST)
        
        if Form.is_valid():
            Form.save()
            return redirect('add_teacher')
        else:
            return redirect('add_teacher')
        
        
    
class UquvchiQushView(LoginRequiredMixin,View):
    def get(self,request):
        pupil=Uquvchilar.objects.all()
        Forma=AddPupilForm()
        return render(request, 'admin_services/uquvchi_qush.html',{'pupil':pupil,'form':Forma})
    
    def post(self, request):
        user = AddPupilForm(data=request.POST)
        Forma=AddPupilForm()
        pupil=Uquvchilar.objects.all()

        if user.is_valid():
            user.save()
            return redirect("add_pupil")
        else:
            return render(request, "admin_services/uquvchi_qush.html", {'pupil':pupil,'form':Forma})

class UquvchiKurslariView(LoginRequiredMixin,View):
    def get(self, request):
        name = request.GET.get('q','')
        kurslar = Kurslar.objects.all()
        u = Uquvchilar.objects.filter(ism__icontains=name).values('id')
        if name:
            try:
                courses = guruh.objects.filter(uquvchi_id=u[0]['id'])
                if courses:
                    print(courses.values())
                    kurslar = Kurslar.objects.filter(id__in=[ i.kurs_id_id for i in courses])
                    print(kurslar)
            except:
                pass

        return render(request, 'admin_services/uquvchi_kurslari.html', {'kurslar': kurslar,'name':name})

class NewGroupView(LoginRequiredMixin,View):
    def get(self,request):
        group=NewGroupForm()
        return render(request, 'admin_services/guruh_shakllantirish.html',{'group':group})
    
    def post(self, request):
        user = NewGroupForm(data=request.POST)
        if user.is_valid():
            user.save()
            return redirect("add_pupil")
           
        else:
            return render(request, "admin_services/yangi_guruh.html", {'group':user})
        
class OpenGroupView(LoginRequiredMixin,View):
    def get(self,request):
        form=OpenGroupForm()
        return render(request,'admin_services/opengroup.html',{'form':form})
        
        
    def post(self,request):
        form=OpenGroupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('opengroup')
        else:
            return redirect('opengroup',{'message':"Xatolik yuz berdi"})
        
class ManitoringView(LoginRequiredMixin,View):
    def get(self,request):
        xonalar=Dars_xonalari.objects.all()
        return render(request,"admin_services/manitoring.html",{'xonalar':xonalar})

class RoomView(LoginRequiredMixin,View):
    def get(self,request,xona_raqami=101):
        hafta = kunlar.objects.all()
        soatlar = Vaqtlar.objects.all()
        guruhlar = guruh_kunlari.objects.filter(xona_id__xona_raqami=xona_raqami)
        malumot=[]
        for i  in hafta:
            a=[]
            for j in soatlar:
                f=True
                h=0
                for k in guruhlar:
                    if i.nomi == k.kun_id.nomi and j.vaqt_start == k.vaqt_id.vaqt_start:
                        f=False
                        h+=1
                        if h==1:
                            a.append({'guruh':k.guruh_id.guruh,'vaqt_start':k.vaqt_id.vaqt_start,'kun':k.kun_id.nomi})
                if f:
                    a.append({'guruh':None,'vaqt_start':j.vaqt_start,'kun':i.nomi})
            malumot.append({'hafta_kuni':a})
        return render(request,"admin_services/room.html",{'hafta':hafta,'soatlar':soatlar,'guruhlar':guruhlar,'malumot':malumot})



from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import LoginForm,AddPupilForm,AddTeacherForm,NewGroupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from .models import Uquvchilar,Kurslar,Uqituvchilar,guruh,kunlar,guruh_kunlari,Dars_xonalari
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

        return render(request, 'admin_services/uquvchi_kurslari.html', {'kurslar': kurslar})

class NewGroupView(LoginRequiredMixin,View):
    def get(self,request):
        group=NewGroupForm()
        return render(request, 'admin_services/yangi_guruh.html',{'group':group})
    
    def post(self, request):
        user = NewGroupForm(data=request.POST)
        print(user)
        if user.is_valid():
            user.save()
            return redirect("add_pupil")
           
        else:
            return render(request, "admin_services/yangi_guruh.html", {'group':user})
        
class ManitoringView(LoginRequiredMixin,View):
    def get(self,request):
        mat=[]
        Dars_xonalari_s=Dars_xonalari.objects.all()
        for i in Dars_xonalari_s:
            xona=[{'xona_r_k':[i.xona_raqami,'Dushanba','Seshanba','Chorshanba','Payshanba','Juma','Shanba','Yakshanba']}]
            xonadagi_guruhlar=guruh.objects.filter(xona_id=i.id) 
            for j in xonadagi_guruhlar:
                guruhlar=guruh_kunlari.objects.filter(guruh_id=j.id)
                for p in guruhlar: 
                    kunlar_hammasi=kunlar.objects.filter(id=p.kun_id.id)
                    for jj in kunlar_hammasi:
                        xona.append({'moslash':{'guruh_nomi':p.guruh_id.guruh,'kun_nomi':jj.nomi,'guruh_vaqti':p.guruh_id.vaqt_start,'guruh_vaqti_tugashi':p.guruh_id.vaqt_end}})
            mat.append(xona)
        matritsa = []
        for k in mat:
            row = []
            for i in range(1, 8):
                if len(k) > 0 and 'xona_r_k' in k[0]:
                    xona_raqami = k[0]['xona_r_k'][0]
                    kun = k[0]['xona_r_k'][i]
                    time = None
                    end_time=None
                    guruh_raqami = None
                    for obj in k:
                        if 'moslash' in obj and obj['moslash']['kun_nomi'] == kun:
                            time = obj['moslash']['guruh_vaqti']
                            end_time=obj['moslash']['guruh_vaqti_tugashi']
                            guruh_raqami = obj['moslash']['guruh_nomi']
                            break
                    row.append({'xona': xona_raqami, 'kun': kun, 'vaqt': time, 'end_vaqt':end_time, 'guruh': guruh_raqami})
                else:
                    row.append(None)
            matritsa.append(row)
        return render(request,"admin_services/manitoring.html",{'matritsa':matritsa})



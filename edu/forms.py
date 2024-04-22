from django import forms
from .models import Uquvchilar,Uqituvchilar,guruh

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=128)
    
class AddPupilForm(forms.ModelForm):
    class Meta:
        model=Uquvchilar    
        fields=['ism','familiya','t_sana','tel_raqam']
        labels = {
            'ism': 'Ismi',
            'familiya': 'Familiyasi:',
            't_sana':"Tug'ilgan sana:",
            'tel_raqam': 'Telefon raqam:',
        }
        
class AddTeacherForm(forms.ModelForm):
    class Meta:
        model=Uqituvchilar
        fields=['ism','familiya','yunalishi','tel_raqam']
        labels = {
            'ism': 'Ismi',
            'familiya': 'Familiyasi:',
            'yunalishi':"Mutaxasisligi:",
            'tel_raqam': 'Telefon raqam:',
        }
        
class NewGroupForm(forms.ModelForm):
    class Meta:
        model=guruh
        fields=['guruh','uquvchi_id','kurs_id','uqituvchi_id','vaqt_start','vaqt_end','xona_id']
        labels={
            'guruh':'Guruhni kiriting',
            'uquvchi_id':'Uquvchini kiriting',
            'kurs_id':'Kursni tanlang',
            'uqituvchi_id':'Uqituvchini tanlang',
            'vaqt_start':'Boshlanish vaqtni kiriting',
            'vaqt_end':'Tugash vaqtini kiriting',
            'xona_id':'Xonani tanlang'
        }
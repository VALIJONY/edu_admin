from django import forms
from .models import Uquvchilar,Uqituvchilar,guruh,guruh_kunlari

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=128)
    
class AddPupilForm(forms.ModelForm):
    class Meta:
        model=Uquvchilar    
        fields=['ism','familiya','t_sana','tel_raqam']
        labels = {
            'ism': 'Имя:',
            'familiya': 'Фамилия:',
            't_sana':"Дата рождения:",
            'tel_raqam': 'Номер телефона:',
        }
        
class AddTeacherForm(forms.ModelForm):
    class Meta:
        model=Uqituvchilar
        fields=['ism','familiya','yunalishi','tel_raqam']
        labels = {
            'ism': 'Имя:',
            'familiya': 'Фамилия:',
            'yunalishi':"Специальность:",
            'tel_raqam': 'Номер телефона:',
        }
        
class NewGroupForm(forms.ModelForm):
    class Meta:
        model=guruh
        fields=['guruh','uquvchi_id','kurs_id','uqituvchi_id']
        labels={
            'guruh':'Введите номера группы:',
            'uquvchi_id':'Выберите студента:',
            'kurs_id':'Выберите курс:',
            'uqituvchi_id':'Выберите учителья:',
        }
        
class OpenGroupForm(forms.ModelForm):
    class Meta:
        model=guruh_kunlari
        fields=['guruh_id','kun_id','vaqt_id','xona_id']
        labels={
            'guruh_id':'Выберите группу:',
            'kun_id':'Выберите день:',
            'vaqt_id':'Выберите время:',
            'xona_id':'Выберите номер:',
        }
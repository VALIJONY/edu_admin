from django.contrib import admin
from .models import *
# Register your models here.
class UqituvchilarAdmin(admin.ModelAdmin):
    search_fields=['ism','familiya','yunalishi','tel_raqam']
    list_display=['ism','familiya','yunalishi','tel_raqam']
class UquvchilarAdmin(admin.ModelAdmin):
    search_fields=['ism','familiya','t_sana','tel_raqam']
    list_display=['ism','familiya','t_sana','tel_raqam']
class KurslarAdmin(admin.ModelAdmin):
    search_fields=['kurs_nomi','narxi','davomiyligi']
    list_display=['kurs_nomi','narxi','davomiyligi']
class TulovlarAdmin(admin.ModelAdmin):
    search_fields=['uquvchi_id','tulov','kurs_id','vaqt']
    list_display=['uquvchi_id','tulov','kurs_id','vaqt']
class Dars_xonalariAdmin(admin.ModelAdmin):
    search_fields=['xona_raqami','qavat']
    list_display=['xona_raqami','qavat']
class Guruh_kunlariAdmin(admin.ModelAdmin):
    search_fields=['guruh_id','kun_id','vaqt_id','xona_id']
    list_display=['guruh_id','kun_id','vaqt_id','xona_id']
class GuruhAdmin(admin.ModelAdmin):
    search_fields=['guruh','uquvchi_id','kurs_id','uqituvchi_id']
    list_display=['guruh','uquvchi_id','kurs_id','uqituvchi_id']
class KunlarAdmin(admin.ModelAdmin):
    search_fields=['nomi']
    list_display=['nomi']
class VaqtlarAdmin(admin.ModelAdmin):
    search_fields=['vaqt_start','vaqt_end']
    list_display=['vaqt_start','vaqt_end']
admin.site.register(Uqituvchilar,UqituvchilarAdmin)
admin.site.register(Uquvchilar,UquvchilarAdmin)
admin.site.register(Kurslar,KurslarAdmin)
admin.site.register(Tulovlar,TulovlarAdmin)
admin.site.register(Dars_xonalari,Dars_xonalariAdmin)
admin.site.register(guruh_kunlari,Guruh_kunlariAdmin)
admin.site.register(guruh,GuruhAdmin)
admin.site.register(kunlar,KunlarAdmin)
admin.site.register(Vaqtlar,VaqtlarAdmin)

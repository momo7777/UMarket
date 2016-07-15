from django.contrib import admin
from models import Used_stuff

# Register your models here.
class Used_stuffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'selling_price', 'description', 'category', 'source')

admin.site.register(Used_stuff, Used_stuffAdmin)

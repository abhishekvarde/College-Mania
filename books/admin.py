from django.contrib import admin

# Register your models here.
from .models import Ad
from .models import Email
from .models import mydb

admin.site.register(Ad)
admin.site.register(Email)
admin.site.register(mydb)

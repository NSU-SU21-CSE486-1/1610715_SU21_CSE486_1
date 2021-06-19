from django.contrib import admin
from .models import Users, Projects, Teams, Document_Folder, Document_File
# Register your models here.
admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(Document_Folder)
admin.site.register(Teams)
admin.site.register(Document_File)

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no',)

admin.site.register(Student, StudentAdmin)

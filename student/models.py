from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    age=models.IntegerField()
    comp_fees=models.IntegerField()
    lib_fees=models.IntegerField()
    def __unicode__(self):
        return self.name          

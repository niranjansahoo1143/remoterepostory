from django.db import models

class studentdata(models.Model):
    student_name=models.CharField(max_length=100)
    class_name=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    school_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    odia_mark=models.IntegerField()
    hindi_mark=models.IntegerField()
    english_mark=models.IntegerField()
    math_mark=models.IntegerField()
    science_mark=models.IntegerField()
    social_mark=models.IntegerField()
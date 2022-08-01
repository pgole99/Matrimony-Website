from django.db import models

# Create your models here.
gender1=(
    ('Male','male'),
    ('Female','female'),
    ('Other','other')
)
class personinfo(models.Model):
 name=models.CharField(max_length=120)
 email=models.EmailField()
 gender=models.CharField(choices=gender1, max_length=89)
 date=models.DateField(auto_now=False,auto_now_add=False)
 religion=models.CharField(max_length=78)
 city=models.CharField(max_length=67)
 age=models.PositiveIntegerField()
 physical_disability=models.CharField(max_length=120)
 education=models.CharField(max_length=120)
 occupation=models.CharField(max_length=120)
 img=models.ImageField(upload_to='img/')
 biodata=models.FileField(upload_to='doc/')



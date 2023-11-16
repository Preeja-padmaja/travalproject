from django.db import models

# Create your models here.
class traval_table(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()
    def __str__(self):
        return self.name

class team_table(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()
    def __str__(self):
        return self.name
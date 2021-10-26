from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=300)
    no_of_pages=models.IntegerField(default=10)
    author=models.CharField(max_length=300)
    body=models.TextField()
    isbn=models.CharField(max_length=42,null=True,blank=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.title


class Students(models.Model):
    name=models.TextField()
    department=models.TextField()
    matric_no=models.CharField(max_length=10)
    date=models.DateTimeField()

    def __str__(self):
        return self.name
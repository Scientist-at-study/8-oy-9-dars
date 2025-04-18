from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    classes  = models.ManyToManyField(Class, related_name="teachers")

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=250)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"F.I.O {self.full_name} sinfiz {self.class_group}"
from django.db import models

# Create your models here.
from django.urls import reverse


class Dept(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='department'

    def get_url(self):
        return reverse('Dept_Details',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Doctor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    dept=models.ForeignKey('Dept',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='doctor',blank=True)
    detail=models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctor'

    def get_url(self):
        return reverse('DocDetail',args=[self.dept.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
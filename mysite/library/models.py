from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image
import uuid
from datetime import date


class Fencing(models.Model):
    title = models.CharField(verbose_name=("Title"), max_length=200)
    summary = models.TextField(verbose_name=("Summary"), max_length=1000)
    cover = models.ImageField(verbose_name=("Cover"), upload_to="covers", null=True, blank=True)
    price = models.FloatField(verbose_name=("Price"), max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Fencing")


class Product(models.Model):
    title = models.CharField(verbose_name=("Title"), max_length=200)
    summary = models.TextField(verbose_name=("Summary"), max_length=1000)
    cover = models.ImageField(verbose_name=("Cover"), upload_to="covers", null=True, blank=True)
    price = models.FloatField(verbose_name=("Price"), max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ('Products')


class Paslauga(models.Model):
    title = models.CharField(verbose_name=("Title"), max_length=200)
    summary = models.TextField(verbose_name=("Summary"), max_length=1000)
    cover = models.ImageField(verbose_name=("Cover"), upload_to="covers", null=True, blank=True)
    price = models.FloatField(verbose_name=("Price"), max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Paslauga")
        verbose_name_plural = ('Paslaugos')


class Profilis(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)


class QuoteInstance(models.Model):
    email = models.CharField(verbose_name=("Email"), max_length=30)
    due_back = models.DateField(verbose_name="Time to get in tuch", null=True, blank=True)
    reader = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.TextField(verbose_name=("Summary"), max_length=1000)

    def is_overdue(self):
        return self.due_back and self.due_back < date.today()

    def __str__(self):
        return f"{self.email} - {self.summary}"


class Hotel(models.Model):
    hotel_Main_Img = models.ImageField(upload_to='images/')



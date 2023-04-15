from django.db import models


# Create your models here.


class Service(models.Model):
    name = models.CharField(verbose_name="Название услуги", max_length=100)
    description = models.TextField(verbose_name="Описание услуги")
    photo = models.ImageField(verbose_name="Фото", upload_to="services/", blank=True, null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание")
    service = models.ForeignKey(verbose_name="Услуга", to=Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

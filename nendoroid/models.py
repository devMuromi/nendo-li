from django.db import models
import re
from user.models import User


class Series(models.Model):
    name_ko = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_en = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_ja = models.CharField(max_length=128, blank=True, null=True, unique=True)

    def __str__(self):
        if self.name_ko:
            return self.name_ko
        elif self.name_en:
            return self.name_en
        else:
            return self.name_ja


class Manufacturer(models.Model):
    name_ko = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_en = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_ja = models.CharField(max_length=128, blank=True, null=True, unique=True)

    def __str__(self):
        if self.name_ko:
            return self.name_ko
        elif self.name_en:
            return self.name_en
        else:
            return self.name_ja


class Sculptor(models.Model):
    name_en = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_ja = models.CharField(max_length=128, blank=True, null=True, unique=True)
    name_ko = models.CharField(max_length=128, blank=True, null=True, unique=True)

    def __str__(self):
        if self.name_ko:
            return self.name_ko
        elif self.name_en:
            return self.name_en
        else:
            return self.name_ja


class Nendoroid(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name_ko = models.CharField(max_length=256, blank=True)
    name_en = models.CharField(max_length=256, blank=True)
    name_ja = models.CharField(max_length=256, blank=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, blank=True, null=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL, blank=True, null=True
    )
    sculptor = models.ManyToManyField(Sculptor, related_name="nendoroid", blank=True)
    release_date = models.JSONField(blank=True, null=True)
    # image = models.ImageField(null=True)
    image_link = models.CharField(max_length=256, blank=True)
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    # price = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    owner = models.ManyToManyField(User, related_name="nendoroid_owned", blank=True)

    def numbering_init(self):
        value = re.sub(r"[^0-9]", "", self.number)
        if len(value) >= 2:
            value = value[:-2] + "00"
        return value

    def save(self, *args, **kwargs):
        self.numbering = self.numbering_init()
        super().save(*args, **kwargs)

    numbering = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.number + " " + self.name_ko


class NendoroidPhoto(models.Model):
    photo = models.URLField(max_length=256, blank=True)
    nendoroid = models.ForeignKey(Nendoroid, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

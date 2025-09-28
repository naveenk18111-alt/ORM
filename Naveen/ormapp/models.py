from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
    Brand_Name = models.CharField(max_length=10)
    Model_No = models.IntegerField(primary_key=True)
    Customer_name = models.CharField(max_length=10)
    Mfg_Date = models.DateField()
class Car_DBAdmin(admin.ModelAdmin):
    list_display = ["Brand_Name","Model_No","Customer_name","Mfg_Date"]
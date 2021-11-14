from django.db import models

# Create your models here.
class Inout(models.Model):
    short = models.IntegerField(default=5,verbose_name = "短い移動平均線")
    long = models.IntegerField(default=14,verbose_name = "長い移動平均線")
    val = models.IntegerField(default = 30,verbose_name = "取引量")
    start = models.IntegerField(default=1000000,verbose_name="初期投資額")
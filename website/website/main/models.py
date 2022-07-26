from django.db import models


class Printer(models.Model):
    printer_name = models.CharField(max_length=200)
    printer_status = models.CharField(max_length=50)
    printer_progress = models.CharField(max_length=20)
    t0_temp_actual = models.CharField(max_length=20)
    t0_temp_set = models.CharField(max_length=20)
    bed_temp_actual = models.CharField(max_length=20)
    bed_temp_set = models.CharField(max_length=20)

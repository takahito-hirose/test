from django.db import models

# Create your models here.
# reservations/models.py

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    table_type = models.CharField(max_length=50, choices=[('none', '指定なし'), ('sofa', 'ソファ'), ('vip', 'VIP席')], default='none')
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

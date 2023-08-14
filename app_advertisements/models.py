from django.db import models

class Advertisement(models.Model):
    title=models.CharField('название', max_length=100)
    description=models.TextField("описание")
    price=models.DecimalField("цена",max_digits=10, decimal_places=2)
    auction=models.BooleanField("торг",help_text='Отметьте, возможен ли торг')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

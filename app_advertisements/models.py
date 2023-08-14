from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
class Advertisement(models.Model):
    title=models.CharField('название', max_length=100)
    description=models.TextField("описание")
    price=models.DecimalField("цена",max_digits=10, decimal_places=2)
    auction=models.BooleanField("торг",help_text='Отметьте, возможен ли торг')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'


    class Meta:
        db_table='advertisements'


    @admin.display(description='Дата создания')
    def created_data(self):
        if self.created_at.date() == timezone.now().date():
            created_time=self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color:green; font-weight:bold">Сегодня в {}</span>',created_time
            )
        return self.created_at.time().strftime("%d.%m.%Y at %H:%M:%S")
    

    @admin.display(description='Дата обновления')
    def updated_time(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time=self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color:green; font-weight:bold">Сегодня в {}</span>',updated_time
            )
        return self.updated_at.time().strftime("%d.%m.%Y at %H:%M:%S")
#from app_advertisements.models import Advertisement
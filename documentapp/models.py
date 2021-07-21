from django.db import models
from uuid import uuid4
from usersapp.models import Department, CorpUser


# Create your models here.
class DocType(models.Model):
    name = models.CharField(verbose_name='Название типа документа', max_length=100, blank=True)
    def __str__(self):
        return str(self.name)

class Document(models.Model):
    number = models.UUIDField(primary_key=True, default=uuid4, verbose_name='Номер документа')
    name = models.CharField(verbose_name='Название документа', max_length=100, blank=True)
    date = models.DateField(verbose_name='Дата создания документа', null=True, blank=True)
    type = models.ForeignKey(DocType, verbose_name='Тип документа', on_delete=models.SET_NULL,
                                     null=True, blank=True)
    department = models.ForeignKey(Department, verbose_name='Подразделение', on_delete=models.SET_NULL,
                                     null=True, blank=True)
    author = models.ForeignKey(CorpUser, verbose_name='Автор документа', on_delete=models.SET_NULL,
                                     null=True, blank=True)
    document = models.FileField(verbose_name='Документ', upload_to='media', blank=True)
    def __str__(self):
        return str(self.number)



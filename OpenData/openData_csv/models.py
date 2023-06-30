from django.db import models
# from phonenumber_field.phonenumber import PhoneNumber


class Tipe(models.Model):
    """Справочник для хранения типа организации"""
    tipe = models.CharField('Тип организации', max_length=100)


class Post(models.Model):
    """Справочник для хранения должности"""
    post = models.CharField('Должность', max_length=50)


class Orgfunc(models.Model):
    """Справочник для хранения деятельности организации"""
    orgfunc = models.TextField('Деятельность организации')


class OpenData(models.Model):
    is_published = models.BooleanField('Опубликовано')
    orgname = models.TextField('Организация')
    orgsokrname = models.TextField('Сокращенное наименование')
    orgpubname = models.TextField('Публичное наименование')
    tipe = models.ForeignKey(
        Tipe,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    rukfio = models.CharField('Должностное лицо ФИО', max_length=50)
    orgfunc = models.ForeignKey(
        Orgfunc,
        on_delete=models.CASCADE
    )
    index = models.CharField('Индекс', max_length=6)
    region = models.CharField('Субъект РФ', max_length=60)
    area = models.CharField('Область', max_length=100)
    town = models.CharField('Город', max_length=100)
    street = models.CharField('Улица', max_length=100, null=True, blank=True)
    house = models.CharField('Дом', max_length=20, null=True, blank=True)
    latitude = models.FloatField('Широта', max_length=8)
    longitude = models.FloatField('Долгота', max_length=8)
    mail = models.EmailField()
    telephone = models.CharField('Номер телефона', max_length=6)
    fax = models.CharField('Fax', max_length=6)
    telephonedop = models.CharField('Доп. номер телефона', max_length=6)
    url = models.CharField('URL', max_length=200)
    okpo = models.CharField('ОКПО', max_length=8)
    ogrn = models.CharField('ОГРН', max_length=14)
    inn = models.CharField('ИНН', max_length=10)
    # schedule =
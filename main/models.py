from django.db import models


class Foremans(models.Model):
    name = models.CharField("Имя", max_length=20, blank=False)
    secondname = models.CharField("Фамилия", max_length=20, blank=False)
    patronymic = models.CharField("Отчество", max_length=20, blank=False)
    number = models.CharField("Номер телефона", max_length=10, blank=False)
    password = models.CharField("Пароль", max_length=15)
    status = models.CharField("Cтатус работника",max_length= 100 , blank=True)
    def __str__(self):
        return f'{self.secondname} {self.name} {self.patronymic}'
class man(models.Model):
    name = models.CharField("Имя", max_length=20, blank=False)
    secondname = models.CharField("Фамилия", max_length=20, blank=False)
    patronymic = models.CharField("Отчество", max_length=20, blank=True)
    number = models.CharField("Номер телефона", max_length=10, blank=False)
    status = models.CharField("Cтатус работника", max_length=100, blank=True)
    hourweek = models.IntegerField("Часы работника за неделю",default=0)
    def __str__(self):
        return f'{self.secondname} {self.name} {self.patronymic}'
class Builder(models.Model):
    name = models.CharField("Имя", max_length=20, blank=False)
    secondname = models.CharField("Фамилия", max_length=20, blank=False)
    patronymic = models.CharField("Отчество", max_length=20, blank=True)
    number = models.CharField("Номер телефона", max_length=10, blank=False)
    status = models.CharField("Cтатус работника", max_length=100, blank=True)
    def __str__(self):
        return f'{self.secondname} {self.name} {self.patronymic}'



class Equipment(models.Model):
    names = models.CharField("Имя", max_length=20, blank=False)
    expirydate = models.DateField("Дата окончания")
    owner = models.CharField("Владелец", max_length=100, blank = False)
    registersdate = models.DateField("Дата регистрации", auto_now=True, blank = False)
    equipmentphoto = models.ImageField("Фото", blank = False)
    def __str__(self):
        return self.names
class passport_object(models.Model):
    name_object = models.CharField("Имя объекта",max_length= 100 , blank = False)
    orderer = models.CharField("Заказчик",max_length= 100 , blank = False)
    location = models.FloatField("Локация в координатах", blank = False)

class plane(models.Model):
    Task = models.CharField("Задачи", max_length= 100, blank = False)
    quantityday = models.IntegerField("Количество дней",blank = False)
    secondnamebuilders = models.TextField("Фамилия рабочего", max_length=200)
    equip = models.TextField("Техника" , max_length= 200)
    description = models.TextField("Описание", max_length=500)


class Foremans2(models.Model):
    name = models.CharField("Имя", max_length=20, blank=False)
    secondname = models.CharField("Фамилия", max_length=20, blank=False)
    patronymic = models.CharField("Отчество", max_length=20, blank=False)
    number = models.CharField("Номер телефона", max_length=10, blank=False)
    status = models.CharField("Cтатус работника",max_length= 100 , blank=False)
    def __str__(self):
        return f'{self.secondname} {self.name} {self.patronymic}'




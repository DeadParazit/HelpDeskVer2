from django.db import models
from datetime import datetime

#Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=50) #Имя
    surname = models.CharField(max_length=50) #Фамилия
    patronymic = models.CharField(max_length=50) #Отчество
    # department = #Департамент
    email = models.CharField(max_length=70) #Почта
    phone = models.CharField(max_length=20) #Номер телефона

    def __str__(self):
        return 'Сотрудник: {} {}.{}.'.format(self.surname, self.name[:1], self.patronymic[:1])

#Подразделение
class Department(models.Model):
    name = models.CharField(max_length=100) #Название подразделения
    employers = models.ManyToManyField(Employee) #Список сотрудников департамента

    def __str__(self):
        return 'Департамент: {}'.format(self.name)

#Тип заявки
class Type_Of_Request(models.Model):
    name = models.CharField(max_length=50) #Название типа заявки(например: "починка принтера")
    responsible = models.OneToOneField(Employee) #Отвечающий за выполнение
    priority = models.IntegerField() #Приоритет выполнения от 1 до 5

    def __str__(self):
        return 'Тип заявки: {}'.format(self.name)


#Заявка
class Request(models.Model):
    date = models.DateField(default=datetime.now()) #Дата заявки
    applicant_is_notified = models.BooleanField(default=False) #Заявитель оповещён
    executor_is_notified = models.BooleanField(default=False)  #Исполнитель оповещён
    operator_is_notified = models.BooleanField(default=False)  #Оператор оповещён
    author = models.OneToOneField(Employee) #Автор заявки
    applicant = models.OneToOneField(Employee) #Заявитель(ФИО, подразделение, почта, телефон)
    building = models.CharField(max_length=20) #Здание
    room = models.CharField(max_length=5) #Кабинет
    type = models.OneToOneField(Type_Of_Request) #Тип заявления
    sap = models.IntegerField() #Id оборудования
    description = models.CharField(max_length=255) #Описание проблемы
    file = models.FileField(blank=True) #Приложенный файл

    def __str__(self):
        return 'Заявление: {} {}.{}. - {}'.format(self.applicant.surname, self.applicant.name[:1], self.applicant.patronymic[:1], self.type.name)





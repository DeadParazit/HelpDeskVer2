from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

#Подразделение
class Department(models.Model):
    name = models.CharField(max_length=100) #Название подразделения

    def __str__(self):
        return 'Департамент: {}'.format(self.name)

#Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=50) #Имя
    surname = models.CharField(max_length=50) #Фамилия
    patronymic = models.CharField(max_length=50) #Отчество
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  #Подразделение
    # department = #Департамент
    email = models.CharField(max_length=70) #Почта
    phone = models.CharField(max_length=20) #Номер телефона

    def __str__(self):
        return 'Сотрудник: {} {}.{}.'.format(self.surname, self.name[:1], self.patronymic[:1])

#Тип заявки
class Type_Of_Request(models.Model):
    name = models.CharField(max_length=50) #Название типа заявки(например: "починка принтера")
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True) #Отвечающий за выполнение

    def __str__(self):
        return 'Тип заявки: {}'.format(self.name)


#Заявка
class Request(models.Model):

    date = models.DateField(auto_now_add=True) #Дата заявки
    time = models.TimeField(auto_now_add=True) # Время заявки
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='requests_authors', null=True, blank=True) #Автор заявки
    sap = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True) #Id оборудования




    applicant_is_notified = models.BooleanField(default=False)  # Заявитель оповещён
    performer_is_notified = models.BooleanField(default=False)  # Исполнитель оповещён
    operator_is_notified = models.BooleanField(default=False)  # Оператор оповещён
    storage = models.BooleanField(default=False)  # Требуется отметка склада
    STATUS = [
        ('Выполнена', 'Выполнена'),
        ('В процессе', 'В процессе')
    ]  # Варианты статуса заявки
    status = models.CharField(max_length=15 ,choices=STATUS, default="")  # Статус заявки


    applicant = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='requests_applicant',
                                  null=True)  # Заявитель(ФИО, подразделение, почта, телефон)
    building = models.CharField(max_length=20)  # Здание
    room = models.IntegerField()  # Кабинет


    WAY_TO_TREAT = [
        ('Lotus', 'Lotus'),
        ('Телефон', 'Телефон'),
        ('Визит', 'Визит'),
        ('Чат', 'Чат'),
    ]  # Варианты способа обращения
    way_to_treat = models.CharField(max_length=15 ,choices=WAY_TO_TREAT)  # Способ обращения

    TYPE_OF_REQUEST = [
        ('Инцидент', 'Инцидент'),
        ('Информация', 'Информация'),
        ('Сервис', 'Сервис'),
        ('Сигнал', 'Сигнал'),
        ('Жалоба', 'Жалоба'),
        ('RFC', 'RFC'),
    ]  # Варианты типа заявки
    type_of_request = models.CharField(max_length=15,choices=TYPE_OF_REQUEST)  # Тип заявки


    type = models.ForeignKey(Type_Of_Request, on_delete=models.SET_NULL, null=True)  # Тип заявления
    PRIORITY = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),]  # Варианты приоритета
    priority = models.CharField(max_length=2, choices=PRIORITY)  # Приоритет выполнения
    description = models.CharField(max_length=255)  # Описание проблемы
    file = models.FileField(blank=True)  # Приложенный файл

    def __str__(self):
        return 'Заявление({}): {} {}.{}. - {}'.format(self.date, self.applicant.surname, self.applicant.name[:1], self.applicant.patronymic[:1], self.type.name)





from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

#Подразделение
class Department(models.Model):
    name = models.CharField(max_length=100) #Название подразделения

    def __str__(self):
        return '{}'.format(self.name)

#Сотрудник
class Employee(models.Model):
    name = models.CharField(max_length=50) #Имя
    surname = models.CharField(max_length=50) #Фамилия
    patronymic = models.CharField(max_length=50) #Отчество
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  #Подразделение
    # department = #Департамент
    email = models.CharField(max_length=70) #Почта
    phone = models.CharField(max_length=20) #Номер телефона
    password = models.CharField(max_length=20, default='12345678') #Пароль пользователя

    def __str__(self):
        return '{} {}.{}.'.format(self.surname, self.name[:1], self.patronymic[:1])

#Тип заявки
class Type_Of_Request(models.Model):
    name = models.CharField(max_length=50) #Название типа заявки(например: "починка принтера")
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True) #Отвечающий за выполнение

    def __str__(self):
        return '{}'.format(self.name)


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
        ('В работе', 'В работе'),
        ('Исполнено', 'Исполнено'),
        ('SLA', 'SLA'),
    ]  # Варианты статуса заявки
    status = models.CharField(max_length=15 ,choices=STATUS, default="В работе")  # Статус заявки


    applicant = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='requests_applicant',
                                  null=True)  # Заявитель(ФИО, подразделение, почта, телефон)
    building = models.CharField(max_length=20)  # Здание
    room = models.IntegerField(null=True)  # Кабинет


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


    type = models.ForeignKey(Type_Of_Request, on_delete=models.SET_NULL, null=True)  # Тип
    performer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True) #Исполнитель
    PRIORITY = [
        ('1', 'В течении дня'),
        ('2', 'В течении 3 дней'),
        ('3', 'В течении недели'),
        ('4', 'В течении 2-х недель'),
        ('5', 'До поставок оборудования'),
        ('6', 'По договоренности с заявителем'),]  # Варианты приоритета
    priority = models.CharField(max_length=30, choices=PRIORITY)  # Приоритет выполнения
    deadline = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)  # Описание проблемы
    file = models.FileField(blank=True)  # Приложенный файл

    #Инфа от исполнителя
    materials_usage_comment = models.CharField(max_length=250, null=True, blank=True)  # Комментарий
    is_new = models.BooleanField(default=False, null=True, blank=True) #Новизна материала
    performer_comment = models.CharField(max_length=250, default='') #Комментарий
    STORAGE_TYPE = [
        ('1', 'Товарно-материальные запасы'),
        ('2', 'Основное средство'), ]  # Варианты обращения к складу
    storage_type = models.CharField(max_length=1, choices=STORAGE_TYPE, null=True, blank=True)  #Обращение к складу
    EXIT_CODE = [
        ('1', 'Успешно'),
        ('2', 'С замечаниями'),
        ('3', 'Не выполнено'),
        ('4', 'Нет сервиса SLA'), ]  # Варианты кода закрытия
    exit_code = models.CharField(max_length=1, choices=EXIT_CODE, null=True)  #Код закрытия
    COMPLEXITY = [
        ('1', '5'),
        ('2', '10'),
        ('3', '15'),
        ('4', '20'), ]  # Варианты сложности заявки
    complexity = models.CharField(max_length=1, choices=COMPLEXITY, null=True)  #Сложность заявки
    performer_file = models.FileField(blank=True)  # Приложенный файл исполнителя

    def __str__(self):
        return 'Заявление({}): {} {}.{}. - {}'.format(self.date, self.applicant.surname, self.applicant.name[:1], self.applicant.patronymic[:1], self.type.name)





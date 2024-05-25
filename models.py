from django.db import models

class Animal(models.Model):
    name = models.CharField('Название', max_length=100)
    TYPE_CHOICES = (
        ('mammal', 'Млекопитающее'),
        ('fish', 'Рыба'),
        ('reptilia', 'Рептилия'),
    )
    type = models.CharField('Род', max_length=14, choices=TYPE_CHOICES, default='mammal')
    information = models.TextField('Информация', null=True, blank=True)
    population = models.PositiveIntegerField('Популяция', default=0)
    is_rare = models.BooleanField('Вымирающее животное', default=False)
    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животное'
    def __str__(self)-> str:
        return self.name
# Create your models here.
class Employee(models.Model):
    name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    TYPE_CHOICES = (
        ('men', 'мужчина'),
        ('women', 'женжина'),
        ('trans', 'трансгендер')
    )
    gender = models.CharField('Пол', max_length=100, choices=TYPE_CHOICES, default='men')
    date_of_birth = models.DateField('Дата рождения', max_length=100)
    picture = models.ImageField('Фото сотрудника', upload_to='picturec', null=True, blank=True)
    salary = models.DecimalField('Заработная плата', max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    def __str__(self)-> str:
        return f'{self.name} {self.last_name}'

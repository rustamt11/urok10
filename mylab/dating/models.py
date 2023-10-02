from django.db import models


# Create your models here.
class Person(models.Model):
    objects = None
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField(blank=True)

    STATUS = (
        ("st", "Учусь"),
        ("wk", "Работаю"),
        ("sd", "Туплю"),
        ("mm", "Мамкин миллиардер"),
        ("mp", "Мамин бродяга, папин симпотяга"),
    )

    status = models.CharField(max_length=50, choices=STATUS)
    salary = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"

    def get_absolute_url(self):
        return f"/{self.pk}"

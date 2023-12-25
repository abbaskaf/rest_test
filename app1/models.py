from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.last_name}-{self.age}"


class Work(models.Model):
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20, verbose_name='name_job')

from django.db import models


class User(models.Model):
    # может и не понадобиться, т.к. везде одинаковый
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_used = models.BooleanField()

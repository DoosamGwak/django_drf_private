from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    SEX_CHOICE = [
        ('M', '남'),
        ('W','여'),
    ]

    first_name = None
    last_name = None

    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birthday = models.DateField()

    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default=None)
    introduce = models.TextField(blank=True)
    
    @property
    def age(self):
        today = timezone.now()
        age = int(
            today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.today))
        )
        return age

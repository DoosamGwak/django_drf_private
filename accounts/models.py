from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# from django.utils import timezone


class User(AbstractUser):
    SEX_CHOICE = [
        ("M", "남"),
        ("W", "여"),
    ]

    first_name = None
    last_name = None

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birthday = models.DateField()

    sex = models.CharField(max_length=1, choices=SEX_CHOICE, default="N")
    introduce = models.TextField(blank=True)

    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False, blank=True
    )

    # @property
    # def age(self):
    #     today = timezone.now()
    #     age = int(
    #         today.year
    #         - self.birthday.year
    #         - ((today.month, today.day) < (self.birthday.month, self.birthday.today))
    #     )
    #     return age

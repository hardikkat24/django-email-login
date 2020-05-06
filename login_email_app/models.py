from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	email = models.EmailField(max_length = 256, unique = True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		verbose_name = 'user'

	
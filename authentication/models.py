from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Recruiters(User):
    # Add your custom fields here
    company_name = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name




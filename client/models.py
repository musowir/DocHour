from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    age = models.IntegerField()
    health_history = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user.first_name)

class Uploads(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    link = models.FileField(upload_to='media/uploads/')
    filename = models.CharField(max_length=150)
    caption = models.CharField(max_length=150)
    date_of_issue = models.DateField()
    def __str__(self) -> str:
        return str(self.client)
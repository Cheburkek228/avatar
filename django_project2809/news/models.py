from django.db import models
from django.conf import settings

# Create your models here. ЛОГИКА ПРИЛОЖЕНИЯ
User = settings.AUTH_USER_MODEL

class Commentaries(models.Model):
    class Meta:
        ordering = ['-date']

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=True)

class Likes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    like = models.BooleanField(default=False)

class News(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # УКАЗАНИЕ АВТОРА
    article = models.CharField(max_length=100) # ЗАГОЛОВОК НОВОСТИ
    body = models.TextField(blank=True, null=True) # ТЕКСТ НОВОСТИ
    commentary = models.ManyToManyField(Commentaries)
    likes = models.ManyToManyField(Likes)
    def __str__(self):
        return self.article

    def get_likes(self):
        return self.likes.count()
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

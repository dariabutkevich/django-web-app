from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Toy(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField('Название игрушки', max_length=100)
    height = models.CharField('Высота', max_length=50)
    design = models.CharField('Дизайн', max_length=100)
    material = models.CharField('Материал', max_length=100)
    description = models.TextField('Описание', blank=True)
    image = models.FileField('Изображение', upload_to='toys/')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрушка'
        verbose_name_plural = 'Игрушки'



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'toy')

    def __str__(self):
        return f"{self.user.username} -> {self.toy.name}"

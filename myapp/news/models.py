from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=100)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text article')
    date = models.DateTimeField('Publication data ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
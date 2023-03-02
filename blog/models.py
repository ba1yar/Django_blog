from django.db import models


class Post(models.Model):
    """Данные о посте"""
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('текст записи')
    img = models.ImageField('Изображение', upload_to='image/%Y')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

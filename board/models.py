from django.db import models


class Bd(models.Model):
    rubric = models.ForeignKey(
        'Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика'
    )
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявлениe'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Название', db_index=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

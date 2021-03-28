from django.db import models
from django.core.validators import FileExtensionValidator

class Company(models.Model):
    name = models.CharField(max_length = 100)
    memo = models.CharField(max_length = 100)


class Company2(models.Model):
    name = models.CharField(max_length = 100)
    memo = models.CharField(max_length = 100)

from django.urls import reverse_lazy


class BaseModel(models.Model):
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        abstract = True


class Books(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()

    class Meta:
        db_table = 'books'

    #def get_absolute_url(self):
    #    return reverse_lazy('store:detail_book', kwargs={'pk': self.pk})
class Post(models.Model):
    """投稿モデル"""
    class Meta:
        db_table = 'post'
    title = models.CharField(verbose_name='タイトル', max_length=10)
    comment = models.CharField(verbose_name='コメント', max_length=100)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    attach = models.FileField(null=True,
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        validators=[FileExtensionValidator(['pdf', 'jpeg','jpg',])],
    )
    def __str__(self):
        return self.title + ',' + self.comment

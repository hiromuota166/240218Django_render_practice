from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title

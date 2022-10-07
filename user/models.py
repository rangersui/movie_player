from django.db import models


# Create your models here.
class User(models.Model):

    def __str__(self):
        return self.name

    gender = (
        ('male', '男'),
        ('female', '女'),
        ('non-binary', '非二元')
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
        db_table = 'user'  # 数据库中的名字

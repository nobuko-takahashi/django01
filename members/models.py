from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, verbose_name="名前")
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name="メールアドレス")
    password = models.CharField(max_length=300, blank=False, null=False, verbose_name="パスワード")
    status = models.IntegerField(blank=False, null=False, default=0, verbose_name='状態')
    created = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated= models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        db_table = 'members'
        verbose_name = "会員"
        verbose_name_plural = "会員"

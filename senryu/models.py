from django.db import models

class Senryu(models.Model):
    # Todo: uidとcommentはなぜかdefault=nullが不可能だったためnull=Trueに書き換え
    uid = models.IntegerField(null=True, verbose_name="uid")
    name = models.CharField(max_length=30, default='', verbose_name="雅号")
    ku1 = models.CharField(max_length=30, null=False, blank=False, verbose_name="初句")
    ku2 = models.CharField(max_length=30, null=False, blank=False, verbose_name="二句")
    ku3 = models.CharField(max_length=30, null=False, blank=False, verbose_name="結句")
    comment = models.TextField(null=True, verbose_name="コメント")
    delete_flag = models.BooleanField(default=False, verbose_name="削除フラグ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")
    updated= models.DateTimeField(auto_now=True, verbose_name="更新日")

    class Meta:
        db_table = 'senryu'
        verbose_name = "川柳"
        verbose_name_plural = "川柳"

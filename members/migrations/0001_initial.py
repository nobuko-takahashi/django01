# Generated by Django 4.0.2 on 2022-04-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名前')),
                ('email', models.EmailField(max_length=100, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=300, verbose_name='パスワード')),
                ('status', models.IntegerField(default=0, verbose_name='状態')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
            options={
                'verbose_name': '会員',
                'verbose_name_plural': '会員',
                'db_table': 'members',
            },
        ),
    ]

# Generated by Django 2.0.1 on 2018-10-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='姓名')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='邮箱')),
                ('add_time', models.DateTimeField(blank=True, max_length=19, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, max_length=19, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '测试模型',
                'verbose_name_plural': '测试模型',
            },
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0012_auto_20180118_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apis',
            name='apimethod',
            field=models.CharField(choices=[('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch')], default='0', max_length=200, verbose_name='请求方法'),
        ),
        migrations.AlterField(
            model_name='apistep',
            name='apimethod',
            field=models.CharField(choices=[('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch')], default='0', max_length=200, verbose_name='请求方法'),
        ),
    ]

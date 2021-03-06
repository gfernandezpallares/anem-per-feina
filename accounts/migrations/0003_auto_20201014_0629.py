# Generated by Django 3.0.7 on 2020-10-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='User email, also used as username.', max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, default='', help_text='User gender.', max_length=10, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(error_messages={'required': 'Role must be provided'}, help_text='User role.', max_length=12, verbose_name='Role'),
        ),
    ]

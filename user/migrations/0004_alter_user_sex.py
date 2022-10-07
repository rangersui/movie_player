# Generated by Django 4.1.1 on 2022-09-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_options_rename_c_time_user_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女'), ('non-binary', '非二元')], default='男', max_length=32),
        ),
    ]
# Generated by Django 3.2.19 on 2023-05-10 12:47

from django.db import migrations, models
import exceptions_demos.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, validators=[exceptions_demos.web.models.validate_letters_numbers_space])),
            ],
        ),
    ]

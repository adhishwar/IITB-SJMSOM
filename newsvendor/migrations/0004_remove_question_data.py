# Generated by Django 3.0.8 on 2020-08-04 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsvendor', '0003_question_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='data',
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-02 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_snippet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='user',
        ),
        migrations.DeleteModel(
            name='Code',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]

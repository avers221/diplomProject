# Generated by Django 3.0.7 on 2020-06-21 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200621_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('publish',)},
        ),
        migrations.AlterModelManagers(
            name='contact',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]

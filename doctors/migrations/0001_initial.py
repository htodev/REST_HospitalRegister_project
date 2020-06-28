# Generated by Django 2.1.15 on 2020-03-29 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('specialty', models.CharField(choices=[('Urologist', 'Urologist'), ('Gynecologist', 'Gynecologist'), ('Dermatologist', 'Dermatologist'), ('Nephrologist', 'Nephrologist'), ('Endocrinologist', 'Endocrinologist')], max_length=20)),
            ],
        ),
    ]

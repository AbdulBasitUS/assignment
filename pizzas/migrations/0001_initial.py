# Generated by Django 3.2.8 on 2021-10-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('type_name', models.CharField(max_length=30)),
            ],
        ),
    ]

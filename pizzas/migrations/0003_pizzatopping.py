# Generated by Django 3.2.8 on 2021-10-18 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_pizzasize'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('topping_name', models.CharField(max_length=50)),
            ],
        ),
    ]
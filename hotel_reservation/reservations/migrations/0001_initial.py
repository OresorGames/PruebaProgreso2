# Generated by Django 5.0.4 on 2024-12-16 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed', max_length=20)),
            ],
        ),
    ]

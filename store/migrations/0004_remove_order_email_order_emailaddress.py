# Generated by Django 5.0.3 on 2024-04-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.AddField(
            model_name='order',
            name='emailAddress',
            field=models.EmailField(blank=True, max_length=250, verbose_name='Email Address'),
        ),
    ]
# Generated by Django 3.1.7 on 2022-01-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20220119_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDelayYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_delay_year', models.CharField(max_length=30)),
                ('effective_date', models.DateField(null=True)),
                ('ineffective_date', models.DateField(null=True)),
            ],
        ),
    ]

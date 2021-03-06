# Generated by Django 2.1.2 on 2018-11-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyCirculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('debit', models.DecimalField(decimal_places=2, default=0,
                 max_digits=7)),
                ('credit', models.DecimalField(decimal_places=2, default=0,
                 max_digits=7)),
                ('money', models.DecimalField(decimal_places=2, default=0,
                 max_digits=7)),
                ('balance', models.DecimalField(decimal_places=2, default=0,
                 max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='TaskRelatedNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0,
                 max_digits=7)),
            ],
        ),
    ]

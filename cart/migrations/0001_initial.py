# Generated by Django 2.1 on 2019-07-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True)),
                ('total', models.IntegerField()),
                ('shipping_address', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(blank=True, to='listings.Listing')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-16 17:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('users_like', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
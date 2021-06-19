# Generated by Django 3.2.2 on 2021-05-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0003_auto_20210508_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers/')),
            ],
        ),
    ]

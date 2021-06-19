# Generated by Django 3.2.2 on 2021-05-08 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document_File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=20)),
                ('file_name', models.CharField(max_length=200)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.document_folder')),
            ],
        ),
    ]

# Generated by Django 3.2.2 on 2021-05-08 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_document_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='team_name',
            new_name='team_members',
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.users'),
        ),
    ]

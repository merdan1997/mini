# Generated by Django 4.0.5 on 2023-09-13 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alertlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='role_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alertlog.roles')),
            ],
        ),
    ]

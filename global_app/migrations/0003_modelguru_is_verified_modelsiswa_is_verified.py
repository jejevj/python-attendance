# Generated by Django 5.0.1 on 2024-01-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_app', '0002_modelabsensi_encrypted_text_modelabsensi_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelguru',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelsiswa',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

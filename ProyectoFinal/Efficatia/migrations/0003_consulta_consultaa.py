# Generated by Django 4.0.3 on 2022-04-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Efficatia', '0002_consulta_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='consultaa',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]

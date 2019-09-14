# Generated by Django 2.2.5 on 2019-09-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.TextField()),
                ('processed_text', models.TextField()),
                ('processing', models.BooleanField(default=False)),
            ],
        ),
    ]

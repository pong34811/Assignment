# Generated by Django 5.0.6 on 2024-07-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name_th', models.CharField(max_length=100)),
                ('book_name_en', models.CharField(max_length=100)),
                ('number_si', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('detail_book', models.CharField(max_length=100)),
                ('bookshop', models.CharField(choices=[('B2S', 'B2S'), ('Inthon', 'Inthon'), ('Se-ed', 'Se-ed'), ('Meb', 'Meb')], default='B2S', max_length=20)),
                ('sale_book', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

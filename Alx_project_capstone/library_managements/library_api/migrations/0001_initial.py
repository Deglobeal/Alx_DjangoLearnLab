# Generated by Django 5.1.7 on 2025-03-09 13:37

import django.db.models.deletion
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
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('publication_date', models.DateField()),
                ('is_available', models.BooleanField(default=True)),
                ('in_stock', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('user_id', models.CharField(max_length=10, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('identification', models.CharField(choices=[('student', 'Student'), ('staff', 'Staff'), ('none_staff', 'None_staff')], default='student', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('amount_due', models.DecimalField(decimal_places=2, default=0.0, max_digits=25)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_api.user')),
            ],
        ),
    ]

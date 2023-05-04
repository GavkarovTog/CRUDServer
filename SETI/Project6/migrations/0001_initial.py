# Generated by Django 3.2.18 on 2023-04-24 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('country', models.TextField(null=True)),
                ('square', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('income', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('nationality', models.TextField(null=True)),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project6.city')),
                ('job', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project6.firm')),
                ('religion', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project6.religion')),
            ],
        ),
    ]
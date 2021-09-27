# Generated by Django 3.2.7 on 2021-09-27 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adventure', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=2000, null=True)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(default='no path text', max_length=100)),
                ('photo_url', models.TextField(max_length=2000, null=True)),
                ('adventure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paths', to='findingyourway.adventure')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(default='there is no path', max_length=200)),
                ('text', models.CharField(default='no path text', max_length=100)),
                ('photo_url', models.TextField(max_length=2000, null=True)),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='findingyourway.path')),
            ],
        ),
        migrations.CreateModel(
            name='Ending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ending', models.CharField(default='there is no ending', max_length=200)),
                ('text', models.CharField(default='no path text', max_length=100)),
                ('photo_url', models.TextField(max_length=2000, null=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endings', to='findingyourway.path')),
            ],
        ),
    ]

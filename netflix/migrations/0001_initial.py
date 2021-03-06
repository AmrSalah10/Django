# Generated by Django 3.1.7 on 2021-03-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='movies/posters')),
                ('video', models.FileField(blank=True, null=True, upload_to='movies/videos')),
                ('categories', models.ManyToManyField(to='netflix.Category')),
            ],
        ),
    ]

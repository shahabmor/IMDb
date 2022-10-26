# Generated by Django 4.1.2 on 2022-10-26 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (0, 'Female')], null=True)),
                ('birthday', models.DateField(blank=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='actors/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('crew', models.ManyToManyField(to='imdb.crew')),
                ('genres', models.ManyToManyField(to='imdb.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(null=True)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.crew')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.movie')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.role')),
            ],
        ),
    ]
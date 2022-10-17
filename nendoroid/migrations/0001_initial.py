# Generated by Django 4.1 on 2022-10-15 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ko', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name_ja', models.CharField(blank=True, max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sculptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name_ja', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name_ko', models.CharField(blank=True, max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ko', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name_en', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('name_ja', models.CharField(blank=True, max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nendoroid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('name_ko', models.CharField(blank=True, max_length=64)),
                ('name_en', models.CharField(blank=True, max_length=64)),
                ('name_ja', models.CharField(blank=True, max_length=64)),
                ('release_date', models.JSONField(blank=True, null=True)),
                ('image_link', models.CharField(blank=True, max_length=256)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nendoroid.manufacturer')),
                ('sculptor', models.ManyToManyField(blank=True, related_name='nendoroid', to='nendoroid.sculptor')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nendoroid.series')),
            ],
        ),
    ]

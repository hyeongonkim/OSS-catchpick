# Generated by Django 2.2.6 on 2019-11-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccumulateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(default=0, max_length=100)),
                ('maxRank', models.CharField(default=21, max_length=100)),
                ('toNewsTest', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmailData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NewsTestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(default=0, max_length=100)),
                ('maxRank', models.CharField(default=21, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TitleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(default=0, max_length=100)),
                ('nowRank', models.CharField(default=21, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VerifiedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(default=0, max_length=100)),
                ('maxRank', models.CharField(default=21, max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('news_KH_title', models.CharField(max_length=500)),
                ('news_KH_link', models.CharField(max_length=500)),
                ('news_HKR_title', models.CharField(max_length=500)),
                ('news_HKR_link', models.CharField(max_length=500)),
                ('news_CS_title', models.CharField(max_length=500)),
                ('news_CS_link', models.CharField(max_length=500)),
                ('news_CA_title', models.CharField(max_length=500)),
                ('news_CA_link', models.CharField(max_length=500)),
                ('news_KBS_title', models.CharField(max_length=500)),
                ('news_KBS_link', models.CharField(max_length=500)),
                ('news_MBC_title', models.CharField(max_length=500)),
                ('news_MBC_link', models.CharField(max_length=500)),
                ('news_SBS_title', models.CharField(max_length=500)),
                ('news_SBS_link', models.CharField(max_length=500)),
                ('news_YTN_title', models.CharField(max_length=500)),
                ('news_YTN_link', models.CharField(max_length=500)),
            ],
        ),
    ]

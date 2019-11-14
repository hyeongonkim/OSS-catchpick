# Generated by Django 2.2.6 on 2019-11-12 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsCatch', '0003_auto_20191112_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
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
            name='VerifiedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('time', models.CharField(default=0, max_length=100)),
                ('maxRank', models.CharField(default=21, max_length=100)),
                ('news_KH_title', models.CharField(max_length=100)),
                ('news_KH_link', models.CharField(max_length=100)),
                ('news_HKR_title', models.CharField(max_length=100)),
                ('news_HKR_link', models.CharField(max_length=100)),
                ('news_CS_title', models.CharField(max_length=100)),
                ('news_CS_link', models.CharField(max_length=100)),
                ('news_CA_title', models.CharField(max_length=100)),
                ('news_CA_link', models.CharField(max_length=100)),
                ('news_SU_title', models.CharField(max_length=100)),
                ('news_SU_link', models.CharField(max_length=100)),
                ('news_HK_title', models.CharField(max_length=100)),
                ('news_HK_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='accumulatedata',
            name='maxRank',
            field=models.CharField(default=21, max_length=100),
        ),
        migrations.AddField(
            model_name='accumulatedata',
            name='toNewsTest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='titledata',
            name='nowRank',
            field=models.CharField(default=21, max_length=100),
        ),
        migrations.AlterField(
            model_name='accumulatedata',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='titledata',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

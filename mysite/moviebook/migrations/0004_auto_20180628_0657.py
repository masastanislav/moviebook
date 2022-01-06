# Generated by Django 2.0.4 on 2018-06-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0003_auto_20180626_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=30, verbose_name='Tagy')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tagy',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='tagy',
            field=models.ManyToManyField(to='moviebook.Tag'),
        ),
    ]

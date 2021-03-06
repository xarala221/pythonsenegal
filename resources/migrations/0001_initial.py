# Generated by Django 2.1 on 2019-06-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('resource_type', models.CharField(choices=[('Livre', 'Livre'), ('Vidéo', 'Vidéo'), ('Article', 'Article')], default='Livre', max_length=50)),
                ('link', models.URLField(blank=True, null=True)),
                ('img_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

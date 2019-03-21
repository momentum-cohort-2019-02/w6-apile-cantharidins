# Generated by Django 2.1.7 on 2019-03-19 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190319_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='voted_by',
            field=models.ManyToManyField(related_name='votes', through='core.Vote', to='core.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='voted_for',
            field=models.ManyToManyField(related_name='votes', through='core.Vote', to='core.Post'),
        ),
        migrations.AddField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
        migrations.AddField(
            model_name='vote',
            name='voted_at',
            field=models.DateTimeField(default='2019-03-19 20:00'),
        ),
    ]
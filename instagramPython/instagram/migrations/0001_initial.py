# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 15:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=100, null=True)),
                ('video', models.CharField(max_length=100, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.CharField(max_length=100, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('photo', models.CharField(max_length=100, null=True)),
                ('follow', models.ManyToManyField(related_name='_user_follow_+', to='instagram.User')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.User'),
        ),
        migrations.AddField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.User'),
        ),
    ]

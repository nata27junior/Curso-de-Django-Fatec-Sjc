# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('arquivo', models.FileField(upload_to='media/')),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='datacadastro',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]

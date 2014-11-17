# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='language',
            field=models.CharField(max_length=200, choices=[(b'Java', b'Java'), (b'C', b'C'), (b'Python', b'Python'), (b'Lisp', b'Lisp'), (b'C++', b'C++')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]

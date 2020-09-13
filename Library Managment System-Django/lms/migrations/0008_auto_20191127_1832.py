

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_auto_20191127_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookissue',
            name='issue_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 27, 18, 32, 23, 111088)),
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]

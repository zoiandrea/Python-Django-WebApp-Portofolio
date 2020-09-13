

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_merge_20191127_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='description',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='member',
            name='token_books',
        ),
        migrations.AlterField(
            model_name='bookissue',
            name='issue_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 27, 18, 3, 15, 485171)),
        ),
    ]

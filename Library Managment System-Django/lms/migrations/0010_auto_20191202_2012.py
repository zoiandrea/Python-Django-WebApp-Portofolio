
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0009_auto_20191127_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissue',
            name='issue_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 2, 20, 12, 41, 352486)),
        ),
    ]

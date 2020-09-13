

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_dt', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 19, 12, 17, 20, 87661))),
                ('return_dt', models.DateTimeField(blank=True, default=None)),
                ('issue_cmnt', models.TextField(null=True)),
                ('return_cmnt', models.TextField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.Book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.Member')),
            ],
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_auto_20191018_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('birth_date', models.DateField(null=True)),
                ('death_date', models.DateField(null=True)),
                ('bio', models.TextField(null=True)),
                ('nationality', models.CharField(max_length=255)),
            ],
        ),
    ]

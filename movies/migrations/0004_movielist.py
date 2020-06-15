from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movielist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('vote_average', models.IntegerField()),
            ],
        ),
    ]

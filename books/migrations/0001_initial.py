# Generated by Django 4.0.10 on 2025-01-31 17:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('fiction', 'Fiction'), ('nonfiction', 'Nonfiction'), ('children', "Children's Books")], default='fiction', max_length=20)),
            ],
        ),
    ]

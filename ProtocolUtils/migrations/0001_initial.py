# Generated by Django 3.0.2 on 2020-01-14 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('deleted_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('message', models.TextField(default='')),
                ('protocolId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProtocolUtils.Protocol')),
            ],
        ),
    ]
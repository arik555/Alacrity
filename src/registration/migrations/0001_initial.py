# Generated by Django 2.0.2 on 2018-03-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, unique=True)),
                ('event_cost', models.CharField(default='0', help_text='Leave empty if zero.', max_length=4)),
                ('event_reg_type', models.CharField(choices=[('1', 'SINGLE'), ('2', 'GROUP')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('leader_name', models.CharField(max_length=60)),
                ('persons', models.CharField(max_length=200)),
                ('institute_type', models.CharField(choices=[('School', 'SCHOOL'), ('College', 'COLLEGE')], max_length=8)),
                ('institute_name', models.CharField(max_length=110)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('registered_events', models.ManyToManyField(related_name='g_events', to='registration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('institute_type', models.CharField(choices=[('School', 'SCHOOL'), ('College', 'COLLEGE')], max_length=8)),
                ('institute_name', models.CharField(max_length=110)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('registered_events', models.ManyToManyField(related_name='u_events', to='registration.Event')),
            ],
        ),
    ]

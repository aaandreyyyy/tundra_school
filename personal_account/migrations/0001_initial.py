# Generated by Django 4.0.6 on 2022-07-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('text', models.CharField(max_length=4095, verbose_name='Условие')),
                ('answer', models.FloatField(verbose_name='Ответ')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Название темы')),
                ('theory', models.CharField(max_length=4095, verbose_name='Теория')),
                ('tasks', models.ManyToManyField(blank=True, to='personal_account.task')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email_adress', models.EmailField(max_length=254, verbose_name='Email')),
                ('solved', models.ManyToManyField(blank=True, to='personal_account.task')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Название курса')),
                ('themes', models.ManyToManyField(blank=True, to='personal_account.theme')),
                ('users', models.ManyToManyField(blank=True, to='personal_account.student')),
            ],
        ),
    ]
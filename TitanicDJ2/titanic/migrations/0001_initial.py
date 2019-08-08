# Generated by Django 2.1.4 on 2019-07-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PassengerId', models.CharField(max_length=50)),
                ('Pclass', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Sex', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('SibSp', models.IntegerField()),
                ('Parch', models.IntegerField()),
                ('Ticket', models.CharField(max_length=50)),
                ('Fare', models.FloatField()),
                ('Cabin', models.CharField(blank=True, max_length=50, null=True)),
                ('Embarked', models.CharField(max_length=50)),
                ('Survived', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

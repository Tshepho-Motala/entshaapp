# Generated by Django 3.2.9 on 2021-12-02 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delphius', '0005_new_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Public_P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Public_PR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shareable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New_Validation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=200, null=True)),
                ('cont_person', models.CharField(max_length=200, null=True)),
                ('cont_no', models.CharField(max_length=13, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('region', models.CharField(max_length=200, null=True)),
                ('latitude', models.CharField(max_length=200, null=True)),
                ('longitude', models.CharField(max_length=200, null=True)),
                ('solution', models.CharField(max_length=200, null=True)),
                ('duration_ppr', models.CharField(max_length=200, null=True)),
                ('est_municipal', models.CharField(max_length=200, null=True)),
                ('power_connection', models.CharField(max_length=200, null=True)),
                ('lead_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Operator_interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.operator')),
                ('del_connect_interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.interest')),
                ('dusk_dawn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.months')),
                ('municapal_approval', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.municipality')),
                ('public_p', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.public_p')),
                ('public_pr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.public_pr')),
                ('solution_share', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delphius.shareable')),
            ],
        ),
    ]
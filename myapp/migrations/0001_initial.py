# Generated by Django 4.1.1 on 2022-12-03 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('state', models.CharField(max_length=40, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('dob', models.CharField(max_length=20, null=True)),
                ('pic', models.ImageField(upload_to='myapp/image/Patient')),
                ('bloodgroup', models.CharField(max_length=30, null=True)),
                ('disease', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('contact', models.IntegerField(null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mastertable')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('state', models.CharField(max_length=40, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('dob', models.CharField(max_length=20, null=True)),
                ('pic', models.ImageField(upload_to='myapp/image/Doctor')),
                ('contact', models.IntegerField(null=True)),
                ('qualification', models.CharField(max_length=40, null=True)),
                ('Experience', models.CharField(max_length=100, null=True)),
                ('Department', models.CharField(max_length=100, null=True)),
                ('department_id', models.CharField(default=0, max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mastertable')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('doctor', models.CharField(max_length=50, null=True)),
                ('message', models.CharField(max_length=400, null=True)),
                ('pat_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ABC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('app_day', models.CharField(max_length=20, null=True)),
                ('app_time', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('doctor_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor')),
            ],
        ),
    ]
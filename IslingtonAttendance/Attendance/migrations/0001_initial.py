# Generated by Django 2.1 on 2018-09-26 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.AutoField(default=1, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_detail',
            fields=[
                ('attendance_detail_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('entry_time', models.DateTimeField(max_length=6)),
                ('status', models.CharField(max_length=2)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Attendance')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom_name', models.CharField(max_length=55)),
                ('block', models.CharField(max_length=55)),
                ('capacity', models.IntegerField()),
                ('device_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Module_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Fingerprints',
            fields=[
                ('enroll_no', models.AutoField(primary_key=True, serialize=False)),
                ('fingerprint', models.TextField()),
                ('finger_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('year', models.CharField(max_length=5)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Group_Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75)),
                ('period', models.CharField(max_length=5)),
                ('level', models.CharField(max_length=25)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField()),
                ('component_title', models.CharField(max_length=120)),
                ('period', models.CharField(max_length=5)),
                ('agreed_marks', models.IntegerField()),
                ('agreed_grade', models.CharField(max_length=3)),
                ('attempts', models.IntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('routine_id', models.AutoField(primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField(max_length=6)),
                ('endTime', models.DateTimeField(max_length=6)),
                ('day_of_the_week', models.CharField(max_length=9)),
                ('class_type', models.CharField(max_length=15)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('student_first_name', models.CharField(max_length=50)),
                ('student_last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('current_address', models.CharField(max_length=95)),
                ('permanent_address', models.CharField(max_length=95)),
                ('photo', models.CharField(max_length=255, null=True)),
                ('qr_code', models.CharField(max_length=255)),
                ('nfc', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('enroll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Fingerprints')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(default='', max_length=50)),
                ('lastname', models.CharField(default='', max_length=50)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Module')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('users_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='routine',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Teacher'),
        ),
        migrations.AddField(
            model_name='results',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Student'),
        ),
        migrations.AddField(
            model_name='group_routine',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Routine'),
        ),
        migrations.AddField(
            model_name='faculty_module_group',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Module'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Module'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Student'),
        ),
        migrations.AddField(
            model_name='attendance_detail',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Classroom'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attendance.Routine'),
        ),
    ]
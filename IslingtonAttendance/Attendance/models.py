from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, max_length=10)
    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    type = models.IntegerField()


    def __str__(self):
        return self.teacher_id

class Users(models.Model):
    users_id = models.CharField(max_length=15, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return self.users_id+", "+self.username


class Module(models.Model):
    module_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=75)
    period = models.CharField(max_length=5)
    level = models.CharField(max_length=25)
    credit = models.IntegerField()

    def __str__(self):
        return self.module_id

class Teacher_Module(models.Model):
    module = models.ForeignKey("Module", on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True, max_length=5)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Faculty_Module_Group(models.Model):
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE)
    module = models.ForeignKey("Module", on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty+", "+self.module

class Group(models.Model):
    group_id = models.CharField(primary_key=True, max_length=6)
    semester = models.IntegerField(null=False)
    year = models.CharField(null=False,max_length=5)
    faculty=models.ForeignKey("Faculty",on_delete=models.CASCADE)

    def __str__(self):
        return self.group_id+", "+self.semester

class Routine(models.Model):
    routine_id=models.AutoField(primary_key=True)
    startTime=models.TimeField(max_length=6)
    endTime=models.TimeField(max_length=6)
    day_of_the_week = models.CharField(max_length=9)
    class_type = models.CharField(max_length=15)
    module = models.ForeignKey("Module",on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teacher",on_delete=models.CASCADE)

    def __str__(self):
        return self.routine_id

class Group_Routine(models.Model):
    routine = models.ForeignKey("Routine", on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)

    def __str__(self):
        return self.routine+", "+self.group

class Classroom(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    classroom_name = models.CharField(max_length=55)
    block = models.CharField(max_length=55)
    capacity = models.IntegerField()
    device_id = models.IntegerField()

    def __str__(self):
        return self.module_id

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True, default=1)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    def __str__(self):
        return self.attendance_id

class Fingerprints(models.Model):
    enroll_no = models.AutoField(primary_key=True)
    fingerprint = models.TextField()
    finger_number = models.IntegerField() #finger number starting from thumb finger of right hand

    def __str__(self):
        return self.enroll_no


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=16)
    group = models.ForeignKey("Group",on_delete=models.CASCADE);
    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=15)
    current_address = models.CharField(max_length=95)
    permanent_address = models.CharField(max_length=95)
    photo = models.CharField(max_length=255, null=True)
    enroll_no=models.ForeignKey("Fingerprints",on_delete=models.CASCADE)
    qr_code=models.CharField(max_length=255,blank=True,default="")
    nfc=models.CharField(max_length=255,blank=True,default="")
    barcode=models.CharField(max_length=255,blank=True,default="")

    def __str__(self):
        return self.student_id + ", " + self.student_first_name+ ", " +self.student_last_name

class Enrollment(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    module = models.ForeignKey("Module", on_delete=models.CASCADE)

    def __str__(self):
        return self.student+", "+self.module


class Attendance_detail(models.Model):
    attendance_detail_id = models.BigAutoField(primary_key=True)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    entry_time=models.TimeField(max_length=6)
    status=models.CharField(max_length=2)


    def __str__(self):
        return self.attendance_detail_id

class Results(models.Model):
    result_id = models.IntegerField()
    student=models.ForeignKey("Student",null=False,on_delete=models.CASCADE)
    module = models.ForeignKey("Module",null=False,on_delete=models.CASCADE);
    component_title = models.CharField(max_length=120)
    period = models.CharField(max_length=5)
    agreed_marks = models.IntegerField()
    agreed_grade = models.CharField(max_length=3)
    attempts=models.IntegerField()

    def __str__(self):
        return self.result_id
















        
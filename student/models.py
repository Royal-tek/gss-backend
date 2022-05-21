from django.db import models


subjects = (
    ("Sos","Social Studies"),
    ("Maths", "Mathematics"),
    ("Eng", "English"),
    ("Phy", "Physics"),
    ("Chem", "Chemistry"),
    ("Bio", "Biology"),
)

year = (
    ("ss1", "ss1"),
    ("ss2", "ss2"),
    ("ss3", "ss3"),
)





class Parent(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Classes(models.Model):
    year = models.CharField(choices=year, max_length=10)
    def __str__(self):
        return self.year



class Pupil(models.Model):
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    dob = models.DateField()
    phone_number = models.IntegerField()
    email = models.CharField(max_length=256)
    state_of_origin = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    next_of_kin_number = models.IntegerField()
    disabilities = models.BooleanField(default=False)
    year = models.ForeignKey(Classes, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"



class Teacher(models.Model):
    class_teacher = models.ForeignKey(Classes, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    subject = models.CharField(choices=subjects, max_length=20)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname} ---- {self.class_teacher}"

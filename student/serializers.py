from rest_framework import serializers
from .models import Pupil, Parent, Teacher

class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
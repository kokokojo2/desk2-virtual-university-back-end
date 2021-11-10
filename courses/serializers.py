from courses.models import Course, CourseMember, Material, Task, Grade, Chapter, Attachment, StudentWork
from rest_framework import serializers

from utils.serializers import NormalizedModelSerializer, WriteOnCreationMixin
from utils.normalizers import Normalizer


class CourseSerializer(NormalizedModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = '__all__'
        normalize_for_field = {'title': Normalizer.first_capital}


class CourseMemberSerializer(WriteOnCreationMixin, serializers.ModelSerializer):
    class Meta:
        model = CourseMember
        fields = '__all__'
        create_only_fields = ['course']
        read_only_fields = ['user']


class PostSerializer(NormalizedModelSerializer):

    # TODO: check if is_planned property is included
    class Meta:
        fields = '__all__'
        read_only_fields = ['author']
        normalize_for_field = {'title': Normalizer.first_capital}


class MaterialSerializer(PostSerializer):
    class Meta:
        model = Material


class TaskSerializer(PostSerializer):
    class Meta:
        model = Task


class ChapterSerializer(WriteOnCreationMixin, NormalizedModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        create_only_fields = ['course']
        normalize_for_field = {'title': Normalizer.first_capital}


class AttachmentSerializer(serializers.ModelSerializer):
    # TODO: add more user friendly serialization
    class Meta:
        model = Attachment
        fields = '__all__'


class StudentWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWork
        fields = '__all__'
        read_only_fields = ['owner']
        create_only_fields = ['task']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        read_only_fields = ['grader']

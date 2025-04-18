from rest_framework import serializers
from .models import Teacher, Class, Student


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name']


# StringRelatedField
class StudentStringSerializer(serializers.ModelSerializer):
    class_group = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'class_group']


# PrimaryKeyRelatedField
class StudentPrimaryKeySerializer(serializers.ModelSerializer):
    class_group = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'class_group']


# SlugRelatedField
class StudentSlugSerializer(serializers.ModelSerializer):
    class_group = serializers.SlugRelatedField(slug_field='name', queryset=Class.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'class_group']


# HyperlinkedRelatedField
class StudentHyperlinkedRelatedSerializer(serializers.HyperlinkedModelSerializer):
    class_group = serializers.HyperlinkedRelatedField(view_name='class-detail', queryset=Class.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'url', 'full_name', 'class_group']


# HyperlinkedIdentityField
class StudentHyperlinkedIdentitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='student-detail')

    class Meta:
        model = Student
        fields = ['id', 'url', 'full_name', 'class_group']


# Nested relationship (Class -> Students)
class ClassWithStudentsSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True, source='student_set')

    class Meta:
        model = Class
        fields = ['id', 'name', 'students']


# Teacher with PrimaryKey
class TeacherWithPrimaryKeySerializer(serializers.ModelSerializer):
    classes = serializers.PrimaryKeyRelatedField(many=True, queryset=Class.objects.all())

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'price', 'classes']


# Teacher with nested class
class TeacherWithNestedClassesSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'price', 'classes']

    def create(self, validated_data):
        classes_data = validated_data.pop('classes')
        teacher = Teacher.objects.create(**validated_data)
        for class_data in classes_data:
            class_obj, _ = Class.objects.get_or_create(**class_data)
            teacher.classes.add(class_obj)
        return teacher

    def update(self, instance, validated_data):
        classes_data = validated_data.pop('classes')
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        instance.classes.clear()
        for class_data in classes_data:
            class_obj, _ = Class.objects.get_or_create(**class_data)
            instance.classes.add(class_obj)
        return instance

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.employees import models

USER_MODEL = get_user_model()


class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('username', 'id')


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = models.Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password])
    username = serializers.CharField(validators=[UnicodeUsernameValidator()])

    @transaction.atomic
    def create(self, validated_data):
        """ Create employee with user. """
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        validated_data['user'] = USER_MODEL.objects.create_user(
            username=username, password=password, is_active=True)
        return super(EmployeeCreateSerializer, self).create(validated_data)

    class Meta:
        model = models.Employee
        exclude = ('user',)


class ChangePasswordSerializer(serializers.Serializer):
    employee = serializers.IntegerField(required=False)
    old_password = serializers.CharField()
    password = serializers.CharField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePasswordSerializer, self).__init__(*args, **kwargs)

    def validate_employee(self, validated_data):
        try:
            return models.Employee.objects.get(id=validated_data)
        except models.Employee.DoesNotExist:
            raise serializers.ValidationError(_('Employee does not exists'))

    def validate(self, attrs):
        if 'employee' in attrs:
            self.user = attrs['employee'].user
        validate_password(attrs['password'], user=self.user)
        if not self.user.check_password(attrs['old_password']):
            raise serializers.ValidationError(_('Incorrect old password'))
        return attrs


class EmployeeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        exclude = ('user', 'position', 'specializations')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'middle_name': {'required': False},
            'notes': {'required': False},
            'birthday': {'required': False},
            'specializations': {True},
            'position': {'read_only': True},
            'work_started': {'required': False}
        }


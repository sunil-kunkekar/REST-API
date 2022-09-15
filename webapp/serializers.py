from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.FloatField()
    age = serializers.IntegerField(required=False, default=1)
    phone_no = serializers.IntegerField(required=False)
    gender = serializers.CharField(max_length=10)
    address_Details = serializers.CharField(max_length=200)
    home_no = serializers.IntegerField(required=False)
    street = serializers.CharField(max_length=40)
    city = serializers.CharField(max_length=20)
    state = serializers.CharField(max_length=30)
    work_experience = serializers.FloatField()
    company_name = serializers.CharField(max_length=40)
    from_date = serializers.DateField()
    to_date = serializers.DateField()
    address = serializers.CharField(max_length=200)
    qualifications = serializers.CharField(max_length=30)

    class Meta:
        model = Employee
        fields = '__all__'

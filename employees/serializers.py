from rest_framework import serializers
from .models import Employee
from .utils import convert_to_timezone
import pytz

class EmployeeSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    modified_at = serializers.SerializerMethodField()

    # def get_created_at(self, obj):
    #     return convert_to_timezone(obj.created_at, 'Asia/Kolkata')  # Example timezone

    # def get_modified_at(self, obj):
    #     return convert_to_timezone(obj.modified_at, 'Asia/Kolkata')  # Example timezone

    def get_timezone(self):
        request = self.context.get('request')
        tz_name = request.headers.get('Timezone', 'UTC')
        print("tz_name>>>>>>>>>>>>>>>>", tz_name)
        return pytz.timezone(tz_name)

    def get_created_at(self, obj):
        tz = self.get_timezone()
        return obj.created_at.astimezone(tz)

    def get_modified_at(self, obj):
        tz = self.get_timezone()
        return obj.modified_at.astimezone(tz)

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['employee_id', 'created_at', 'modified_at']

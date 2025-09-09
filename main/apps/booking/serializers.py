from rest_framework import serializers
from .models import Booking




class BookingCreateSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M"]
    )
    end_time = serializers.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M"]
    )
    class Meta:
        model = Booking
        fields = (
            "field",
            "user",
            "start_time",
            "end_time"
        )








class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "id",
            "field",
            "user",
            "start_time",
            "end_time"
        )
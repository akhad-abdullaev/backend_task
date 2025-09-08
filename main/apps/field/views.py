from main.apps.common.permissions import IsRoleOwner
from ..field.serializers import FieldSerializer
from ..field.models import Field
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import ValidationError
from django.db.models import Q
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.utils import timezone



class FieldCreateAPIView(generics.CreateAPIView):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsRoleOwner]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user) 
        response_data = {
            "message": "Field created successfully!",
            "field": serializer.data
        }
        return Response(status=status.HTTP_201_CREATED, data=response_data)

field_create_api_view = FieldCreateAPIView().as_view()



class FieldListAPIView(generics.ListAPIView):
    serializer_class = FieldSerializer
    permission_classes = [permissions.IsAuthenticated, IsRoleOwner]

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')

        queryset = Field.objects.all()

        if start_time and end_time:
            start_time = timezone.make_aware(timezone.datetime.fromisoformat(start_time))
            end_time = timezone.make_aware(timezone.datetime.fromisoformat(end_time))

            queryset = queryset.exclude(
                Q(booking_field__start_time__lt=end_time, booking_field__end_time__gt=start_time, booking_field__is_active=True)
            )

        if latitude and longitude:
            try:
                user_location = Point(float(longitude), float(latitude))
                queryset = queryset.annotate(
                    distance=Distance('longitude', user_location.x)
                ).order_by('distance')
            except (TypeError, ValueError):
                raise ValidationError("Invalid latitude or longitude format.")
        return queryset
    
field_list_api_view = FieldListAPIView().as_view()



class FieldDetailAPIView(generics.RetrieveAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [permissions.AllowAny]

field_detail_api_view = FieldDetailAPIView.as_view()


class FieldUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [permissions.IsAuthenticated, IsRoleOwner]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response_data = {
                "message": "Field updated successfully!",
                "field": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

field_update_api_view = FieldUpdateAPIView().as_view()
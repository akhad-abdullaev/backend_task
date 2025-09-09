from main.apps.booking.models import Booking
from main.apps.common.permissions import IsOwnerOrAdmin
from ..booking.serializers import BookingCreateSerializer, BookingSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status



class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

booking_create_api_view = BookingCreateAPIView.as_view()



class BookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(user=user)

    
booking_list_api_view = BookingListAPIView().as_view()



class BookingUpdateAPIView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)

        if instance.user != request.user:
            return Response(
                {"detail": "You do not have permission to update this booking."},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().update(request, *args, **kwargs)

booking_update_api_view = BookingUpdateAPIView.as_view()



class BookingDeleteAPIView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_superuser:
            self.perform_destroy(instance)
            return Response({"message": "Booking deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        
        if instance.user != request.user:
            return Response({"detail": "You do not have permission to delete this booking."}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Booking deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

booking_delete_api_view = BookingDeleteAPIView().as_view()
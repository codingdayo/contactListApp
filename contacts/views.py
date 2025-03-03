from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ContactList(ListCreateAPIView):
    
    serializer_class = ContactSerializer
    permission_classes=(IsAuthenticated, )


    filterset_fields = ['id', 'country_code', 'first_name', 'last_name', 'phone_number', 'contact_picture', 'is_favorite']


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ContactSerializer
    permission_classes=(IsAuthenticated, )
    
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

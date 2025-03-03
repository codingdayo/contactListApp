from rest_framework.serializers import ModelSerializer

from contacts.models import Contact



class ContactSerializer(ModelSerializer):

    class Meta:
        model=Contact
        fields=( 'id', 
        'country_code', 'first_name', 'last_name', 'phone_number', 'contact_picture', 'is_favorite', )
from rest_framework import serializers
from .models import Book
# Create your views here.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id','cover_image','title','description','author',
            'quantity','author','status'
            ]
    
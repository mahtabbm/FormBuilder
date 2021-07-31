from rest_framework import serializers
from customer_api import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id', 'name', 'form', 'created_on')
        #extra_kwargs = {'form': {'read_only': True}}


class CustomerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerChoice
        fields = ('id', 'text_field', 'number_field',
                  'decimal_field', 'datetime_field',
                  'date_field',
                  'part', 'option')
        # extra_kwargs = {'part': {'read_only': True},
        #                  'option': {read_only: True}}
from rest_framework import serializers
from records.models import Customer, Part, PartInstance, Operation, Wallet


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class PartInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartInstance
        fields = ['job_wallet', 'part_origin', 'serial_number']


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['processed_part', 'operation_name', 'date_signed', 'comments', 'operator']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

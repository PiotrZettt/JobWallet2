from django.shortcuts import render
from rest_framework import viewsets, serializers
from .serializers import CustomerSerializer, PartSerializer, PartInstanceSerializer, OperationSerializer, WalletSerializer
from records.models import Customer, Part, PartInstance, Operation, Wallet


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class PartInstanceViewSet(viewsets.ModelViewSet):
    queryset = PartInstance.objects.all()
    serializer_class = PartInstanceSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet, PartViewSet, PartInstanceViewSet, OperationViewSet, WalletViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'parts', PartViewSet)
router.register(r'part-instances', PartInstanceViewSet)
router.register(r'operations', OperationViewSet)
router.register(r'wallets', WalletViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='login' ),
    path('accounts/login', views.not_logged_in, name='not_logged_in'),
    path('logout', LogoutView.as_view(), name='logout' ),
    path('index', views.index, name='index' ),
    path('search-result', views.search, name='search'),
    path('add_operation', views.add_operation, name='add_operation' ),
    path('create_wallet', views.create_job_wallet, name='create_wallet'),
    path('parts', views.PartListView.as_view(), name='parts'),
    path('customers', views.CustomerListView.as_view(), name='customers'),
    path('operations', views.OperationListView.as_view(), name='operations'),
    path('wallets', views.WalletListView.as_view(), name='wallets'),
    path('wallet/<int:pk>', views.WalletDetailView.as_view(), name='wallet-detail'),
    path('part/<int:pk>', views.PartDetailView.as_view(), name='part-detail'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('operation/<int:pk>', views.OperationDetailView.as_view(), name='operation-detail'),
    path('partinstance/<int:pk>', views.PartInstanceDetailView.as_view(), name='partinstance-detail'),
    path('instances', views.PartInstanceListView.as_view(), name='instances'),
    path('create_job_wallet', views.create_job_wallet, name='create_job_wallet'),
    path('add_operation/<int:pk>', views.add_operation, name='add_operation_to_part' ),
]

"""motorcycle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from authentication import views
from authentication.views import ProfileUsersView
from inventory.views import ProductInventoryListView, ProductInventoryDetailView, PosmInventoryDetailView, \
    PosmInventoryListView
from sales.views import SalesListView, SalesDetailView, SalesTotalDetailView, SalesTotalListView
from store.views import SProductListView, SProductDetailView, SPosmListView, SPosmDetailView, IStoreListView, \
    IStoreDetailView
from task.views import TaskViews, TaskDetailView, GpsViews, GpsDetailView, TaskAll
from contract.views import ContractListView, ProductListView, PosmListView, ProductDetailView, PosmDetailView
from encounter.views import EncounterListView, CheckContractListView
from discovery.views import StoreListView, StoreDetailView, StoreAllListView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.RegisterUserAPIView.as_view()),
    path('users/<int:pk>/', views.RegisterUserView.as_view()),
    path('usersview/', ProfileUsersView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('store/', StoreListView.as_view()),
    path('store/<int:pk>/', StoreDetailView.as_view()),
    path('taskall/', TaskAll.as_view()),
    path('taskall/<int:pk>/', TaskDetailView.as_view()),
    path('task/', TaskViews.as_view()),
    path('gps/', GpsViews.as_view()),
    path('gps/<int:pk>/',GpsDetailView.as_view()),
    path('encounter/', EncounterListView.as_view()),
    path('checkcontract/', CheckContractListView.as_view()),
    path('contract/', ContractListView.as_view()),
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('posm/', PosmListView.as_view()),
    path('posm/<int:pk>/', PosmDetailView.as_view()),
    path('product_inventory/', ProductInventoryListView.as_view()),
    path('product_inventory/<int:pk>/', ProductInventoryDetailView.as_view()),
    path('posm_inventory/', PosmInventoryListView.as_view()),
    path('posm_inventory/<int:pk>/', PosmInventoryDetailView.as_view()),
    path('istore/', IStoreListView.as_view()),
    path('istore/<int:pk>/', IStoreDetailView.as_view()),
    path('sproduct/', SProductListView.as_view()),
    path('sproduct/<int:pk>/', SProductDetailView.as_view()),
    path('sposm/', SPosmListView.as_view()),
    path('sposm/<int:pk>/', SPosmDetailView.as_view()),
    path('sales/', SalesListView.as_view()),
    path('sale/<int:pk>/', SalesDetailView.as_view()),
    path('salestotal/', SalesTotalListView.as_view()),
    path('salestotal/<int:pk>/', SalesTotalDetailView.as_view()),
    path('allstore/', StoreAllListView.as_view()),
    re_path(r'^post_images/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

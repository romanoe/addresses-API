"""regbl_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', views.CHStrNameView, 'strname')
router.register(r'npa', views.CHNpaView, 'npa')
router.register(r'city', views.CHCityView, 'city')
router.register(r'address_nr', views.CHStrNrView, 'strname_nr')
router.register(r'complete_address',views.CHAddressesView,'complete_address')

urlpatterns = [
    path(r'api/', include(router.urls))

]

"""
URL configuration for django_diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import MainMenu, WorkersDetail, WorkersList, ManagerDetail, ManagerList, AddWorker, AddManager, AddCompany, \
    SellCompanyList, AddSellCompany

urlpatterns = [
    path('admin/', admin.site.urls),

    # MENU
    path('', MainMenu.as_view(), name='menu'),

    # WORKER
    path('worker_detail/<int:worker_id>/', WorkersDetail.as_view(), name='worker_detail'),
    path('worker_list/', WorkersList.as_view(), name='worker_list'),
    path('worker_form/', AddWorker.as_view(), name='worker_form'),

    # MANAGER
    path('manager_detail/<int:manager_id>/', ManagerDetail.as_view(), name='manager_detail'),
    path('manager_list/', ManagerList.as_view(), name='manager_list'),
    path('manager_form/', AddManager.as_view(), name='manager_form'),

    # COMPANY
    path('company_form/', AddCompany.as_view(), name='company_form'),
    path('sell_company_list/', SellCompanyList.as_view(), name='sell_company_list'),
    path('sell_company_form/', AddSellCompany.as_view(), name='sell_company_form')

]

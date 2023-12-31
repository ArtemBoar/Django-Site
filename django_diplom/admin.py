from django.contrib import admin
from .models import Manager, Worker, Company, SellCompany, User


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "age",
        "created_at",
        "company",
    )


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "age",
        "specialist",
        "language",
        "company",
    )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "balance",
        "next_meet",
    )


@admin.register(SellCompany)
class SellCompanyAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "price",
    )



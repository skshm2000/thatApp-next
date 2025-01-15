from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "name",
        "number",
        "knowledge_start_date",
        "knowledge_end_date",
        "is_active",
    ]
    search_fields = ["name", "number"]

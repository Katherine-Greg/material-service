from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from material_service_app.forms import CustomUserCreationForm
from material_service_app.models import (ItemCategory,
                                         Item,
                                         Unit,
                                         Customer,
                                         Order,
                                         CustomerCategory,
                                         Note)


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {"fields": ("username", "password1", "password2")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "role", "category", "brigade_num")}),
    )


@admin.register(Item)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("category",)


admin.site.register(ItemCategory)
admin.site.register(Unit)
admin.site.register(Order)
admin.site.register(CustomerCategory)
admin.site.register(Note)

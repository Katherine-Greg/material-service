from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class ItemCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomerCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    item_expiration_date = models.IntegerField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, related_name="item")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="item")
    count = models.IntegerField()
    note_number = models.ManyToManyField(Note, related_name="item")
    # expiration_date = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE, related_name="item")

    def __str__(self):
        return self.name


class Customer(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="customer_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions")

    BRIGADIER = "BR"
    SOLDIER = "SO"

    ROLE_CHOICES = [
        (BRIGADIER, "Бригадир"),
        (SOLDIER, "Солдат"),
    ]
    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=SOLDIER)
    category = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE, related_name="customer")
    brigade_num = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Order(models.Model):
    PENDING = "PD"
    APPROVED = "AP"
    REJECTED = "RJ"

    STATUS_CHOICES = [
        (PENDING, "В очікуванні"),
        (APPROVED, "Схвалено"),
        (REJECTED, "Відхилено"),
    ]
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="created_requests")
    created_for = models.ManyToManyField(Customer, related_name="requests_for")
    items = models.ManyToManyField(Item)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.title} by {self.created_by}"

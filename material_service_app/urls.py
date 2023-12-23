from django.urls import path

from material_service_app.views import index, ItemListView, OrderListView

urlpatterns = [
    path("", index, name="index"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
]

app_name = "material_service_app"

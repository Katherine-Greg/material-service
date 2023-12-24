from django.urls import path

from material_service_app.views import (index,
                                        ItemListView,
                                        OrderListView,
                                        CustomerListView,
                                        create_order,
                                        order_to_pdf)


urlpatterns = [
    path("", index, name="index"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/create/", create_order, name="order-create"),
    path("orders/download/", order_to_pdf, name="order-download"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
]

app_name = "material_service_app"

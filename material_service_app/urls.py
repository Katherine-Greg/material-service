from django.urls import path

from material_service_app.views import index, ItemListView, OrderListView, CustomerListView

urlpatterns = [
    path("", index, name="index"),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
]

app_name = "material_service_app"

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Item, ItemCategory, Order, Customer
from .forms import RequestForm

# def logout_view(request):
#     logout(request)
#     return redirect("index")

# def login_view(request):

def index(request):
    """View function for the home page of the site."""

    num_customers = Customer.objects.count()
    num_subjects = Item.objects.count()


    context = {
        "num_customers": num_customers,
        "num_subjects": num_subjects,
    }

    return render(request, "material_service_app/index.html", context=context)


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item
    paginate_by = 5


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    paginate_by = 5


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    paginate_by = 5


# @login_required
# def order_list(request):
#     user = request.user
#     if user.role == 'BR':
#         # Якщо користувач - бригадир, показати його заявки
#         requests = user.created_requests.all()
#     else:
#         # Якщо користувач - солдат, показати заявки для нього
#         requests = user.requests_for.all()
#
#     return render(request, 'order_list.html', {'orders': requests})

# @login_required
def create_order(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        new_request = form.save(commit=False)
        new_request.created_by = request.user
        new_request.save()
        form.save_m2m()  # Зберегти M2M поля (items, created_for)
        return redirect('request_list')

    return render(request, 'create_request.html', {'form': form})

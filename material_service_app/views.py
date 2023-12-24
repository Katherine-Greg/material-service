from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .models import Item, Order, Customer
from .forms import OrderForm


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


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user
            order.save()
            form.save_m2m()
            return redirect("/orders")
    else:
        form = OrderForm()
    
    return render(request, "material_service_app/order_create.html", {"form": form})


def order_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="orders.pdf"'

    pdf = canvas.Canvas(response)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Путь к шрифту Arial.ttf
    pdf.setFont("Arial", 12)
    orders = Order.objects.all()

    y_coordinate = 800

    for order in orders:
        pdf.drawString(100, y_coordinate, u"Order Title: {0}".format(order.title))
        pdf.drawString(100, y_coordinate - 20, u"Status: {0}".format(order.status))
        pdf.drawString(100, y_coordinate - 40, u"Created By: {0}".format(order.created_by))

        created_for = ', '.join(str(i) for i in order.created_for.all())
        items = u', '.join(u"{0}".format(item.name) for item in order.items.all())

        pdf.drawString(100, y_coordinate - 60, u"Created For: {0}".format(created_for))
        pdf.drawString(100, y_coordinate - 80, u"Items: {0}".format(items))

        pdf.drawString(100, y_coordinate - 100, u"Created At: {0}".format(order.created_at))

        y_coordinate -= 200

        if y_coordinate <= 100:
            pdf.showPage()
            y_coordinate = 800

    pdf.save()
    return response

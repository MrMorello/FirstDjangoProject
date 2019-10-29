from face.forms import OrderForm, ProductsForm
from django.shortcuts import render


def new_order(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        products_form = ProductsForm(request.POST)

        if order_form.is_valid() and products_form.is_valid():

            order = order_form.save()
            products = products_form.save(False)

            products.order = order
            products.save()
        else:
            print(order_form.errors)

    return render(request, 'index.html', locals())

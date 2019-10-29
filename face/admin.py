from django.contrib import admin
from .models import *
from django.http import HttpResponse
# Register your models here.


# export functions will go there
# export to excel
def export_xls_p(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=product_model.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Products")
    row_num = 0

    columns = [
        (u"ID", 2000),
        (u"name", 6000),
        (u"quantity", 8000),
        (u"price", 8000),
        (u"measurement", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.name,
            obj.quantity,
            obj.price,
            obj.measurement,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls_p.short_description = u"Export XLS"


def export_xls_o(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=order_model.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Order")
    row_num = 0

    columns = [
        (u"ID", 2000),
        (u"date", 6000),
        (u"subdivision", 8000),
        (u"reason", 8000),
        (u"where", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.date,
            obj.subdivision,
            obj.reason,
            obj.where,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls_o.short_description = u"Export XLS"
# end export to rxcel

#start export to csv

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=order.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"date"),
        smart_str(u"subdivision"),
        smart_str(u"reason"),
        smart_str(u"where"),
        # smart_str(u"name"),
        # smart_str(u"quantity"),
        # smart_str(u"price"),
        # smart_str(u"measurement"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.date),
            smart_str(obj.subdivision),
            smart_str(obj.reason),
            smart_str(obj.where),
            # smart_str(obj.name),
            # smart_str(obj.quantity),
            # smart_str(obj.price),
            # smart_str(obj.measurement)
        ])
    return response


export_csv.short_description = u"Export CSV"

# end of export function

class ProductInOrderInline(admin.TabularInline):
    model = Products
    extra = 0


class OrderAdmin (admin.ModelAdmin):
    actions = [export_xls_o]
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductsAdmin (admin.ModelAdmin):
    actions = [export_xls_p]
    list_display = [field.name for field in Products._meta.fields]

    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)

from django.contrib import admin
from .models import Part, Customer, Operation, PartInstance, Wallet

# Register your models here.

admin.site.register(Customer)


class PartAdmin(admin.ModelAdmin):
    model = Part
    list_display = ['customer', 'FGcode']


admin.site.register(Part, PartAdmin)


class OperationAdmin(admin.ModelAdmin):
    list_display = ['processed_part', 'operation_name', ]


admin.site.register(Operation, OperationAdmin)


class PartInstanceAdmin(admin.ModelAdmin):
    list_display = ['part_origin', 'serial_number']


admin.site.register(PartInstance, PartInstanceAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer_name', 'part_FG', 'pack_number', 'traceability_required']


admin.site.register(Wallet, WalletAdmin)


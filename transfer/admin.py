from django.contrib import admin

from .models import Transfer


# Register your models here.
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('ext_id','sender_card_number','receiver_card_number','sending_amount','created_at','confirmed_at','cancelled_at','sender_phone','state')
    search_fields = ['sender_card_number','receiver_card_number','sending_amount','created_at','confirmed_at','cancelled_at','sender_phone','state']



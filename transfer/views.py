import random
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.utils import timezone

from handlers import get_error_response
from transfer.models import Transfer
from .serializer import TransferSerializer
from utils import send_otp, format_card_number

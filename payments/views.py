import json
from django.shortcuts import render
from django.http import JsonResponse
import razorpay 
from django.conf import settings

def pay_page(request):
    return render(request, "paymentform.html")

def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)
        amount = int(data.get('amount')) * 100
        name = data.get('name')
        currency = 'INR'

        # Initialize Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        # Create order data
        data = {
            'amount': amount,
            'currency': currency,
            'receipt': "TutionFeesPayment",
            'notes': {
                "name": name,
                "payment_for": "Tution"
            }
        }

        # Create order with Razorpay
        response = client.order.create(data=data)
        order_id = response['id']

        return JsonResponse({'order_id': order_id, 'amount': amount , 'key' : settings.RAZORPAY_API_KEY})
    else:
        return JsonResponse({'error': 'Invalid request'})

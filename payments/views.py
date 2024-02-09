from django.shortcuts import render
from django.http import JsonResponse
import razorpay 
from django.conf import settings

# Create your views here.

def pay_page(request):

    return render(request,"paymentform.html")

def create_order(request):

    if request.method == 'POST':
        print(request.POST)

        amount = int(request.POST.get('amount')) * 100
        print(amount)
        currency = 'INR'

        client = razorpay.Client(auth=('rzp_test_VDpNNlne9cRS7A','WHIX59szAAGpZO34jtw2P7Dh'))

        Data = {
            'amount' : amount ,
            'currency' : currency ,
            'receipt' : "TutionFeesPayment",
            'notes' : {
                "name" : "suyash",
                "payment_for" : "Tution"
            }
        }

        response = client.order.create(data=Data)

        order_id = response['id']

        print(order_id)

        return JsonResponse({'order_id':order_id})
    else :
        return JsonResponse({'error':'Invalid request'})    
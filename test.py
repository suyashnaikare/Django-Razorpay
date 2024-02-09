import razorpay 

client = razorpay.Client(auth=('rzp_test_VDpNNlne9cRS7A','WHIX59szAAGpZO34jtw2P7Dh'))

datadict = {'razorpay_order_id': "order_NYhXaWyIFi4tmj",
        'razorpay_payment_id':"pay_NYhmCwDngKPx2N",
    'razorpay_signature':"ff8d28afbf553d0a1520c660fac57280cf683ccbfbf0ce6c69cae171fc22c3f3"}

var = client.utility.verify_payment_signature(datadict)
print(var)
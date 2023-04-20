from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Customer, Transfer

# Create your views here.

def home(request):
    return render(request, 'customer/home.html')

def about(request):
    return render(request,'customer/about.html')

def view_customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer/view_customers.html', context)

def view_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    transfers_sent = Transfer.objects.filter(sender=customer)
    transfers_received = Transfer.objects.filter(receiver=customer)
    context = {'customer': customer, 'transfers_sent': transfers_sent, 'transfers_received': transfers_received}
    return render(request, 'customer/view_customer.html', context)

def transfer(request):
    if request.method == 'POST':
        sender_id = request.POST['sender']
        receiver_id = request.POST['receiver']
        amount = request.POST['amount']
        sender = Customer.objects.get(pk=sender_id)
        receiver = Customer.objects.get(pk=receiver_id)
        if sender.current_balance >= float(amount):
            sender.current_balance -= float(amount)
            sender.save()
            receiver.current_balance += float(amount)
            receiver.save()
            transfer = Transfer(sender=sender, receiver=receiver, amount=float(amount))
            transfer.save()
            return redirect('view_transfers')
        else:
            error = "Insufficient Balance"
            customers = Customer.objects.all()
            context = {'customers': customers, 'error': error}
            return render(request, 'customer/transfer.html', context)
    else:
        customers = Customer.objects.all()
        context = {'customers': customers}
        return render(request, 'customer/transfer.html', context)

def view_transfers(request):
    transfers = Transfer.objects.all().order_by('-date')
    context = {'transfers': transfers}
    return render(request, 'customer/view_transfers.html', context)


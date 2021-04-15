from django.shortcuts import render,redirect
from .models import *

def home(request):
    profile = Profile.objects.filter(user = request.user).first()
    expences = Expense.objects.filter(user = request.user)

    if request.method=='POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')

        expense = Expense(name = text,amount = amount,expence_type = expense_type,user = request.user)
        expense.save()
        
        if expense_type=='Positive':
            profile.balance+=float(amount)
        if expense_type=='Negative':
            profile.expences+=float(amount)
            profile.balance-=float(amount)

        profile.save()
        return redirect('/')

    
    context = {'profile' : profile,'expenses' : expences}
    return render(request,'home.html',context)
    
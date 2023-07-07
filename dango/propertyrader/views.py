from django.shortcuts import render
from  accounts.models import InvestmentPlan

def investment_plan(request):
    plans = InvestmentPlan.objects.all()
    return render(request, 'propertyrader/investment/investment/plan.html', {'plans': plans})

def contact(request):
    return render(request, 'propertyrader/contact/contact.html')
 
def about(request):
    return render(request, 'propertyrader/about/about.html')

def blogs(request):
    return render(request, 'propertyrader/blog/blogs.html')
from django.shortcuts import render
from datetime import date

# Create your views here.

def check_independence_day(request):

    today = date.today()
    is_it_independence_day = (today.month == 3 and today.day == 5)

    return render(request, 'index.html', {
        'is_it_independence_day': is_it_independence_day,
        'today': today
    })

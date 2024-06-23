from django.shortcuts import render
from django.views.decorators.http import require_POST

# Create your views here.
def add(request):
    total = None
    if request.method == 'POST':
        value1 = int(request.POST.get('value1'))
        value2 = int(request.POST.get('value2'))
        total = value1 + value2
    return render(request, 'add.html', {'total': total})

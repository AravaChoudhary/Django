from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

def all_dj(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'dj/all_dj.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'dj/chai_detail.html',{'chai':chai})

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={}
    return render(request,'tradeJpyUsd/index.html',context)
def Sma(request):
    return render(request,'tradeJpyUsd/results.html')

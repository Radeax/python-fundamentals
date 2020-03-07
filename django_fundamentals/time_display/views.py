from django.shortcuts import render
from datetime import datetime
from time import time

# Create your views here.
def index(request):
    currentDT = datetime.now()
    context = {
        "date": currentDT.strftime("%B %d, %Y"),
        "time": currentDT.strftime("%I:%M%p"),
    }
    return render(request, "index.html", context)

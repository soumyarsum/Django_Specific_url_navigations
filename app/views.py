from django.shortcuts import render

# Create your views here.
def wish(request):
    d = {"name" : "working.."}
    return render(request, "wish.html", context=d)

def a(request):
    return render(request, "a.html", context={"v" : "running well"})
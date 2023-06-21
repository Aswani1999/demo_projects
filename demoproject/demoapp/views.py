from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,"homepage.html")
# def abouts(request):
#     return render(request,"abouts.html")
# def contacts(request):
#     return render(request,"contacts.html")
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse("Thank you for visiting")

def demo(request):
    return render(request,"home.html")

def calculation(request):
    x=int(request.GET['num1'])
    y = int(request.GET['num2'])
    add=x+y
    mult=x*y
    sub=x-y
    div=x/y

    return render(request,"result.html",{'result':add,
                                         'result1':mult,
                                         'result2':sub,
                                         'result3':div})







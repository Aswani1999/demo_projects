from travelnewapp.models import work, member
from django.shortcuts import render


def demo(request):
    # name="india"
    # return render(request,"home.html",{'obj':name})
    obj = work.objects.all()
    obj1=member.objects.all()
    return render(request, "index.html", {'result': obj,'result1':obj1})


# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
def friend(request):
    return render(request,'friend.html')

def friend2(request):
    return render(request,'friend2.html')


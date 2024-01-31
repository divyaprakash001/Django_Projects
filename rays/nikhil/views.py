from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Index page</h1>')
    return render(request,'home.html')

def intern(request):
    return render(request,'intership.html')

def application(request):
    return render(request,'development.html')


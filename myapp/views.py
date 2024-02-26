from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def collection(request):
    return render(request, 'collection.html')

def innerpage(request):
    return render(request, 'inner-page.html')
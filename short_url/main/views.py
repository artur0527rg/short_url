from django.shortcuts import render, HttpResponse

# Create your views here.
def short_link(request):
    return render(request, 'main/index.html')
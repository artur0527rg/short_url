from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import LinkForm
from .models import LinksModel

import random
import string

chars = chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
size = 6

def random_slug(chars=chars, size=size):
    value = ''.join(random.choice(chars) for _ in range(size))
    return value

# Create your views here.
def short_link(request):
    if request.method == "GET":
        form = LinkForm()
        return render(request, 'main/index.html', {"form":form})
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            switch = True
            while switch:
                value = random_slug()
                obj = LinksModel.objects.filter(gen_link=value)
                if not obj.exists():
                    switch = False
            form.instance.gen_link = value
            form.save()
            return render(request, 'main/successful.html', {'link':value})
        return render(request, 'main/index.html', {'form':form})

def open_link(request, value):
    page = get_object_or_404(LinksModel, gen_link=value)
    print(page.cl_link)
    return render(request, 'main/redirect_js.html', {'page':page})


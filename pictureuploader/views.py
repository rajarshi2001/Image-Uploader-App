from django.shortcuts import render
from .forms import imageForms
from .models import Image

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        form = imageForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = imageForms()
    img = Image.objects.all()
    return render(request, 'home.html', {'form': form, 'img': img})

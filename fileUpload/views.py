from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
from .models import Image

from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.

@csrf_exempt

def image_list(request):
  images = Image.objects.all()
  return render(request, 'paginas/image_list.html', {'images': images})

def image_upload(request):
  if request.method =='POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('image_list')
  else:
    form = ImageForm()
  return render(request, 'paginas/image_upload.html', {'form': form})

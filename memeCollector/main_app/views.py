from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

class MemeCreate(CreateView):
    model = Meme
    fields = '__all__'
    success_url = '/memes/'

class MemeUpdate(UpdateView):
    model = Meme
    fields = '__all__'
    success_url = '/memes/'

class MemeDelete(DeleteView):
    model = Meme
    success_url = '/memes/'

# Define the home view
def home(request):
    return render(request, 'home.html')
def memes_index(request):
    memes = Meme.objects.all()
    return render(request, 'memes/index.html', {'memes': memes})
def memes_detail(request, meme_id):
    meme = Meme.objects.get(id=meme_id)

    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        meme_form = MemeForm()

    return render(request, 'memes/detail.html', { 'meme': meme,})
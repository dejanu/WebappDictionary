from django.shortcuts import render
from appone.models import DictWord
from appone.forms import FirstForm, SecondForm
from django.contrib import messages



# Create your views here.

def index(request):
    query_list = DictWord.objects.all()
    dict_DictWord = {'words': query_list}

    form = SecondForm()
    if request.method == "POST":
        form = SecondForm(request.POST)
        if form.is_valid():
            ##delete object from data base
            #DictWord.objects.filter(name=form.cleaned_data['name'])
            print("OK")
            return render(request, 'appone/index.html', context=dict_DictWord)
        else:
            messages.error(request, "Error")

    return render(request,'appone/index.html', context=dict_DictWord)



def FormView(request):
    form = FirstForm()
    if request.method == "POST":
        form = FirstForm(request.POST)
        if form.is_valid():
            ##save the form into db
            form.save(commit=True)
            # after submit on users page we redirect the user to index page
            return index(request)
        else:
            print(form.error)
    ##return from view form = FirstForm() the first encounter of the page
    return render(request, 'appone/form_page.html', {'form': form})
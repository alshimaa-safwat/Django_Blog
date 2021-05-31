from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#for testing
def index(request):
    return render(request,'layouts/dashboard/base.html')
    
    

    
def words(request):
    word = BadWord.objects.all()
    mainContentVar = "Forbidden Words"
    context = {'word': word, 'mainContentVar': mainContentVar}



def deleteWord(request, id):
    word = BadWord.objects.get(id=id)
    word.delete()



def addWord(request):
    if request.method == "POST":
        badWord_form = createBadWordForm(request.POST)
        if badWord_form.is_valid():
            badWord_form.save()

    else:
        badWord_form = createBadWordForm()
        context = {'badWord_form': badWord_form}



def editWord(request, id):
    word = BadWord.objects.get(id=id)
    if request.method == "POST":
        badWord_form = createBadWordForm(request.POST, instance=word)
        if badWord_form.is_valid():
            badWord_form.save()

    else:
        badWord_form = createBadWordForm(instance=word)
        context = {'badWord_form': badWord_form}




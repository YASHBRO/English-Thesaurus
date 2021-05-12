from django.shortcuts import render
from django.http import HttpResponse
from main_function import Test

# Create your views here.

def main(request):
    if request.method == "GET":
        word=(request.GET.get('search'))
        if word != '' and word != None:
            content= Test().dummy(word)
            content['line'] = True
            print(word, len(word))
            return render(request,'home.html', content)
        
    return render(request,'home.html')
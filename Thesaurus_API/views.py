from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    content = {
        "word" : "Include",
        "definitions" : [{
            "part_of_speech" : "verb" ,
            "meaning" : "This is meaning of 1st" ,
            "example" : "This is example of 1st"
        } ,
        {
            "part_of_speech" : "noun" ,
            "meaning" : "This is meaning of 2nd" ,
            "example" : "This is example of 2nd"
        },
        {
            "part_of_speech" : "adjective" ,
            "meaning" : "This is meaning of 3rd" ,
            "example" : "This is example of 3rd"
        },
        {
            "part_of_speech" : "pronoun" ,
            "meaning" : "This is meaning of 4th" ,
            "example" : "This is example of 4th"
        }]
    }
    if request.GET.get('SearchBtn'):
        print("OK")
    return render(request,'home.html', content)
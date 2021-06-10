import requests
import urllib
from bs4 import BeautifulSoup as bs


class Test:
    def __init__(self):
        pass

    def dummy(self,word):
        content = {
        "word" : "Include",
        "definitions" : [{
            "part_of_speech" : "verb" ,
            "meaning" : "This is meaning of 1st" ,
            "example" : "This is example of 1st" ,
            "synonyms" : "This is synonyms of 1st"
        } ,
        {
            "part_of_speech" : "noun" ,
            "meaning" : "This is meaning of 2nd" ,
            "example" : "This is example of 2nd" ,
            "synonyms" : "This is synonyms of 2nd"
        },
        {
            "part_of_speech" : "adjective" ,
            "meaning" : "This is meaning of 3rd" ,
            "example" : "This is example of 3rd" ,
            "synonyms" : "This is synonyms of 3rd"
        },
        {
            "part_of_speech" : "pronoun" ,
            "meaning" : "This is meaning of 4th" ,
            "example" : "This is example of 4th" ,
            "synonyms" : "This is synonyms of 4th"
        }] ,
    }
        return content

class Dictionary:
    def __init__(self):
        pass

    def search(self,txt):

        url = "https://www.vocabulary.com/dictionary/" + txt
        htmlfile = urllib.request.urlopen(url)
        soup = bs(htmlfile, 'lxml')

        soup1 = soup.find(class_="short")

        try:
            soup1 = soup1.text
        except AttributeError:
            print('Cannot find such word! Please check spelling')
            exit()

        #print short meaning
        print("SHORT MEANING: \n\n",soup1)
        print("\n")
        #print long meaning
        soup2 = soup.find('h1',class_="word-area")
        soup2 = soup2.get_text()
        print("LONG MEANING: \n\n",soup2)
        print("\n")

        #print instances like synonyms, antonyms etc.

        soup3 = soup.find(class_="instances")
        txt = soup3.get_text()
        txt1 = txt.rstrip()

        print(' '.join(txt1.split()))
        

if __name__=="__main__":
    data=Dictionary().search("cat")

    print(data)
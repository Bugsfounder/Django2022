# I have created this file - Manisha
from django.http import HttpResponse
from django.shortcuts import render


# views here
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # GET THE TEXT FROM GET REQUEST PARAMS
    reqText = request.GET.get('text', 'default')

    # CHECK BOX VALUES
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    lowercase = request.GET.get('lowercase', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charactercounter = request.GET.get('charactercounter', 'off')
    charactercounterwithspaces = request.GET.get('charactercounterwithspaces', 'off')

    # IF CHECK WHICH CHECKBOX IS ON
    if removepunc == "on":
        # ANALYZE TEXT
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in reqText:
            if char not in punctuations:
                analyzed += char
        params = {
            "purpose": "Remove Punctuations", 'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    elif uppercase == "on":
        analyzed = reqText.upper()
        params = {
            "purpose": "CONVERT TO UPPER CASE", 'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in reqText:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif lowercase == "on":
        analyzed = reqText.lower()
        params = {
            "purpose": "New Line Remover - TextUtils", 'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    elif spaceremover == "on":
        analyzed = ''
        for index, char in enumerate(reqText):
            if not ((reqText[index] == " ") and (reqText[index + 1] == " ")):
                analyzed += char
        params = {
            "purpose": "Space Remover - TextUtils", 'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    elif charactercounter == "on":
        analyzed = 0
        for char in reqText:
            if char != " ":
                analyzed += 1
        params = {
            "purpose": "Character Count Without spaces - TextUtils", 'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    elif charactercounterwithspaces == "on":
        analyzed = len(reqText)
        params = {
            "purpose": "Character Count With spaces - TextUtils", 'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    return HttpResponse("Select the checkbox to see some actions with your text")

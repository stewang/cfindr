#from django.shortcuts import render
from django.shortcuts import render

def index(request):
    resultsList = ['cat', 'dog', 'boy', 'girl', 'hippopotamus']
    context = { 'resultsList': resultsList }
    try:
        inputStr = request.POST['input']
        if inputStr:
            context['inputStr'] = inputStr
    except:
        pass
    return render(request, 'textsearch/index.html', context)

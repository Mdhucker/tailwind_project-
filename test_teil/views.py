from django.shortcuts import render

# Create your views here.


def Home(request):
    # Fetch company info (assuming you're only interested in the first entry)
   
    context = {

    }
    return render(request, 'base/index.html', context)

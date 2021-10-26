from django.shortcuts import render, HttpResponse

# Create your views here.


def test_view(request):
    return render(request, 'test.html')

def homepage(request):
    return HttpResponse('This is the homepage!')
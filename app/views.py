from django.shortcuts import render
d={'a':100,'b':200,'c':50}
# Create your views here.
def conditional(request):
    return render(request,'conditional.html',d)
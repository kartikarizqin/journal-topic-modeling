from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# pages
def index(request):
    return render(request, 'index.html')
def index2010(request):
    return render(request, 'tahun2010.html')
def index2011(request):
    return render(request, 'tahun2011.html')
def index2012(request):
    return render(request, 'tahun2012.html')
def index2013(request):
    return render(request, 'tahun2013.html')
def index2014(request):
    return render(request, 'tahun2014.html')
def index2015(request):
    return render(request, 'tahun2015.html')
def index2016(request):
    return render(request, 'tahun2016.html')
def index2017(request):
    return render(request, 'tahun2017.html')
def index2018(request):
    return render(request, 'tahun2018.html')

# range pages
def indexrange2(request):
    return render(request, 'range-2.html')
def indexrange3(request):
    return render(request, 'range-3.html')
def indexrange4(request):
    return render(request, 'range-4.html')
def indexrange5(request):
    return render(request, 'range-5.html')
def indexrange6(request):
    return render(request, 'range-6.html')
def indexrange7(request):
    return render(request, 'range-7.html')
def indexrange8(request):
    return render(request, 'range-8.html')
def indexrange9(request):
    return render(request, 'range-9.html')
def indexrange10(request):
    return render(request, 'range-10.html')        

# pyLDAvis
def indexpy2010(request):
    return render(request, 'pyldavis2010.html')
def indexpy2011(request):
    return render(request, 'pyldavis2011.html')
def indexpy2012(request):
    return render(request, 'pyldavis2012.html')
def indexpy2013(request):
    return render(request, 'pyldavis2013.html')
def indexpy2014(request):
    return render(request, 'pyldavis2014.html')
def indexpy2015(request):
    return render(request, 'pyldavis2015.html')
def indexpy2016(request):
    return render(request, 'pyldavis2016.html')
def indexpy2017(request):
    return render(request, 'pyldavis2017.html')
def indexpy2018(request):
    return render(request, 'pyldavis2018.html')
def indexpy2019(request):
    return render(request, 'pyldavis2019.html')

# range pyLDAvis
def indexrangepy2(request):
    return render(request, 'pyldavis-2.html')
def indexrangepy3(request):
    return render(request, 'pyldavis-3.html')
def indexrangepy4(request):
    return render(request, 'pyldavis-4.html')
def indexrangepy5(request):
    return render(request, 'pyldavis-5.html')
def indexrangepy6(request):
    return render(request, 'pyldavis-6.html')
def indexrangepy7(request):
    return render(request, 'pyldavis-7.html')
def indexrangepy8(request):
    return render(request, 'pyldavis-8.html')
def indexrangepy9(request):
    return render(request, 'pyldavis-9.html')
def indexrangepy10(request):
    return render(request, 'pyldavis-10.html')
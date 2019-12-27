"""topicmodeling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    # page index
    url(r'^tahun2010/$', views.index2010),
    url('tahun2011/', views.index2011),
    url('tahun2012/', views.index2012),
    url('tahun2013/', views.index2013),
    url('tahun2014/', views.index2014),
    url('tahun2015/', views.index2015),
    url('tahun2016/', views.index2016),
    url('tahun2017/', views.index2017),
    url('tahun2018/', views.index2018),

    # range page index
    url('range-2/', views.indexrange2),
    url('range-3/', views.indexrange3),
    url('range-4/', views.indexrange4),
    url('range-5/', views.indexrange5),
    url('range-6/', views.indexrange6),
    url('range-7/', views.indexrange7),
    url('range-8/', views.indexrange8),
    url('range-9/', views.indexrange9),
    url('range-10/', views.indexrange10),

    # pyLDAvis index
    url('pyldavis2010/', views.indexpy2010),
    url('pyldavis2011/', views.indexpy2011),
    url('pyldavis2012/', views.indexpy2012),
    url('pyldavis2013/', views.indexpy2013),
    url('pyldavis2014/', views.indexpy2014),
    url('pyldavis2015/', views.indexpy2015),
    url('pyldavis2016/', views.indexpy2016),
    url('pyldavis2017/', views.indexpy2017),
    url('pyldavis2018/', views.indexpy2018),
    url('pyldavis2019/', views.indexpy2019),

    # range pyLDAvis index
    url('pyldavis-2/', views.indexrangepy2),
    url('pyldavis-3/', views.indexrangepy3),
    url('pyldavis-4/', views.indexrangepy4),
    url('pyldavis-5/', views.indexrangepy5),
    url('pyldavis-6/', views.indexrangepy6),
    url('pyldavis-7/', views.indexrangepy7),
    url('pyldavis-8/', views.indexrangepy8),
    url('pyldavis-9/', views.indexrangepy9),
    url('pyldavis-10/', views.indexrangepy10),
    
]

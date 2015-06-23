from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Site
from django.db.models import Count
from django.db.models import Sum
import sys

def show_all_sites(request):
	#print "\n\nInside show_all_sites============================================================================================================="
	sites = Site.objects.raw('SELECT * FROM demoapp_site GROUP BY `name` ORDER BY `created_date`')
	return render(request, 'demoapp/show_all_sites.html',{'sites':sites})
	
	
def details(request, pk):
	#print "Inside details %d=========================================================================================" %pk
	site = get_object_or_404(Site, pk=pk)	
	sites = Site.objects.filter(name=site.name).order_by('created_date')
	return render(request, 'demoapp/site_details.html', {'sites':sites})
	
	
def summary(request):
	sites = Site.objects.values('name').annotate(sum_a=Sum('a_val'),sum_b=Sum('b_val'))
	return render(request, 'demoapp/summary.html', {'sites':sites})

	
def summary_average(request):
	sites = Site.objects.raw('SELECT id, name, AVG(a_val) AS a_v, AVG(b_val) AS b_v FROM demoapp_site GROUP BY `name`')
	return render(request, 'demoapp/summary_average.html', {'sites':sites})
# Create your views here.

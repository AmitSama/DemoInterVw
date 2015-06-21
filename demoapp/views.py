from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Site
from django.db.models import Count
from django.db.models import Sum
import sys

def show_all_sites(request):
	print "\n\nInside show_all_sites============================================================================================================="
	sites = Site.objects.raw('SELECT * FROM demoapp_site GROUP BY `name` ORDER BY `created_date`')
	return render(request, 'demoapp/show_all_sites.html',{'sites':sites})
	
	
def site_details(request, pk):
	print "Inside site_details %d=========================================================================================" %pk
	sites = get_object_or_404(Site,pk=pk)	
	return render(request,'demoapp/site_details.html',{'sites':sites})
	
	
def summary(request):
	
	# calculating the count of website
	site_count = Site.objects.raw('SELECT id, COUNT(name) AS count FROM demoapp_site GROUP BY `name`')
	sites = Site.objects.values('name').annotate(sum_a=Sum('a_val'),sum_b=Sum('b_val'))
	#for s in sites:
	#	print "\nAMIT ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++%s %d %d" %(s['name'], s['sum_a'],s['sum_b'])
	
	return render(request, 'demoapp/summary.html', {'sites':sites})
# Create your views here.

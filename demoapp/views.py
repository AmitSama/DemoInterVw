from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Site
from django.db.models import Count


def show_all_sites(request):
	sites = Site.objects.raw('SELECT * FROM demoapp_site')
	return render(request, 'demoapp/show_all_sites.html',{'sites':sites})
	
	#sites = Site.objects.values('name').annotate(count=Count('name')).order_by('count')
	
'''	
def site_details(request,pk):
	
	temp = get_object_or_404(Site,pk=pk)
	sites = Site.objects.filter(name=temp.name)
	return render(request,'demoapp/site_details.html',{'site':sites})
'''	
# Create your views here.

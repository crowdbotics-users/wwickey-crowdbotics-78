from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'aa_airtable', 'url': 'http://pypi.python.org/pypi/aa_airtable/0.2'},
    ]
    context = {
        'title': 'wwickey-crowdbotics-78',
        'packages': packages
    }
    return render(request, 'home/index.html', context)

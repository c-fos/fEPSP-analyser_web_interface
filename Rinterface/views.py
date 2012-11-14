from django.template import RequestContext
from django.shortcuts import render_to_response
from rpy2.robjects.packages import importr
import rpy2.robjects as ro


def rtest(request):
    importr("knitr")
    ro.r['stitch']("/home/pilat/workspace/django_templates/web_fEPSPA/test2.R", "/home/pilat/workspace/django_templates/knitr-template.Rhtml",output="/home/pilat/workspace/django_templates/web_fEPSPA/test2.html")
    return render_to_response('web_fEPSPA/test2.html', {},context_instance=RequestContext(request))


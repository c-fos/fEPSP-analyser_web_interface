#!/usr/bin/python2
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from rpy2.robjects.packages import importr
from rpy2.robjects import r

def report(configDict):
    r('.libPaths("/home/pilat/R/i486-pc-linux-gnu-library/2.15/")')
    r.setwd('/home/pilat/workspace/web_fEPSPA/media/')
    knitr=importr("knitr")
    md=importr("markdown")
    for i in configDict.keys():
        tmpString='%s<-"%s"' % (i,configDict[i])
        r(tmpString)
    o = knitr.spin("/home/pilat/workspace/PostProcessing_v.2/control.R", knit = r('FALSE'))
    out = knitr.knit(o, output="/home/pilat/workspace/web_fEPSPA/Rinterface/control.md")
    md.markdownToHTML("/home/pilat/workspace/web_fEPSPA/Rinterface/control.md","/home/pilat/workspace/web_fEPSPA/media/Routput.html")

def RConfig(request):
    input=request.POST
    dict={                                              'wname': 'filterdb',
                                                        'wuser': 'filteruser_local',
                                                        'wpass': 'filter123',
                                                        'wvar': 'ampl',
                                                        'wspike_num':'1',
                                                        'wresp_num':'1',
                                                        'wstage':'тетанизация',
                                                        'wtime_start':'0',
                                                        'wtime_stop':'240',
                                                        'wtime_step':'30',
                                                        'wtag':"control,detail",
                                                        'check':'0'}
    for i in input:
        try:
            dict[i]=input[i]
        except:
            pass
    print("test1")
    if dict['check']=='1':
        report(dict)
        print("test2")
    return render_to_response('web_fEPSPA/Rconfig.html', dict, context_instance=RequestContext(request))

#===============================================================================
# print("read control.R",os.access("/home/pilat/workspace/PostProcessing_v.2/control.R", 4))
#    print("execute django_templates/web_fEPSPA",os.access("/home/pilat/workspace/django_templates/web_fEPSPA", 1))
#    print("write to /PostProcessing_v.2",os.access("/home/pilat/workspace/PostProcessing_v.2", 2))
#    print("execute /PostProcessing_v.2",os.access("/home/pilat/workspace/PostProcessing_v.2", 1))
#    print("write to django_templates/web_fEPSPA",os.access("/home/pilat/workspace/django_templates/web_fEPSPA", 2))
#    print("write to /PostProcessing_v.2/control.Rmd",os.access("/home/pilat/workspace/PostProcessing_v.2/control.Rmd", 2))
#    print("read /PostProcessing_v.2/control.Rmd",os.access("/home/pilat/workspace/PostProcessing_v.2/control.Rmd", 4))
#    print("write to /PostProcessing_v.2/control.md",os.access("/home/pilat/workspace/PostProcessing_v.2/control.md", 2))
#    print("read /PostProcessing_v.2/control.md",os.access("/home/pilat/workspace/PostProcessing_v.2/control.md", 4))
#    print("execute /PostProcessing_v.2/control.md",os.access("/home/pilat/workspace/PostProcessing_v.2/control.md", 1))
#    print("write to /PostProcessing_v.2/Routput.html",os.access("/home/pilat/workspace/django_templates/web_fEPSPA/Routput.html", 2))
#    print("read /PostProcessing_v.2/Routput.html",os.access("/home/pilat/workspace/django_templates/web_fEPSPA/Routput.html", 4))
#    print("read figure/",os.access("/home/pilat/workspace/PostProcessing_v.2/figure",4))
#    print("write figure/",os.access("/home/pilat/workspace/PostProcessing_v.2/figure",2))
#    print("execute figure/",os.access("/home/pilat/workspace/PostProcessing_v.2/figure",1))
#===============================================================================

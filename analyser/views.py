
from django.template import RequestContext
from django.shortcuts import render_to_response
import os
from root.fEPSPanalyser import fepspAnalyser
#===============================================================================
# import root.filtering_lib2
# import root.dbAccess #good
# import root.externalFunctions #good
# import root.checkResult #good
# import root.clussterization #good
# import root.graph #good
# import root.objects #good
# import root.onClick #good
# import root.rInterface #good
# import root.simple #good
# import root.simple_gui #good
# import root.interpolation #good
# import scipy #good
# from scipy import polyval, polyfit #good
# from scipy import interpolate #good
#===============================================================================
from sheduler.main import shedule

def individual(request,path):
    test_filelist=os.listdir("/%s" % path)
    input=request.POST
    dict={                                              'list': test_filelist,
                                                        'path': path,
                                                        'frequency': '200000',
                                                        'tags': 'not defined2',
                                                        #'debug': '0',
                                                        #'cluster':'0',
                                                        'db':'0',
                                                        'check':'0',
                                                        'dict':input,}
    for i in input:
        try:
            dict[i]=input[i]
        except:
            pass
    if dict['check']=='1':
        analyserObject=fepspAnalyser([0,dict['path'],dict['frequency'],"data","1",dict['tags'],0,dict['db'],1,0])
    return render_to_response('web_fEPSPA/individual.html', dict, context_instance=RequestContext(request))

def sheduler(request,path):
    test_filelist=os.listdir(path)
    input=request.POST
    dict={                                              'list': test_filelist,
                                                        'path': path,
                                                        'frequency': '200000',
                                                        'tags': 'not defined2',
                                                        'check':'0',
                                                        'dict':input,}
    for i in input:
        try:
            dict[i]=input[i]
        except:
            pass
    print(dict['check'])
    if dict['check']=='1':
        shedule(dict['path'],dict['tags'],dict['frequency'])
    return render_to_response('web_fEPSPA/sheduler.html', dict, context_instance=RequestContext(request))

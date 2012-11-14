from sys import path
path.append('/home/pilat/workspace/fEPSP-analyser/filter_script/root')
path.append('/home/pilat/workspace/fEPSP-analyser/filter_script')

from django.template import RequestContext
from django.shortcuts import render_to_response
import os
from fEPSPanalyser import fepspAnalyser
from sheduler.main import shedule

def individual(request,path):
    test_filelist=os.listdir(path)
    input=request.POST
    dict={                                              'list': test_filelist,
                                                        'path': path,
                                                        'frequency': 'not defined1',
                                                        'tags': 'not defined2',
                                                        'debug': '0',
                                                        'cluster':'0',
                                                        'db':'0',
                                                        'check':'1',
                                                        'dict':input,}
    for i in input:
        try:
            dict[i]=input[i]
        except:
            pass
    if dict['check']!=1:
        analyserObject=fepspAnalyser([0,dict['path'],dict['frequency'],"data","1",dict['tags'],dict['debug'],dict['db'],dict['cluster']])
    return render_to_response('web_fEPSPA/individual.html', dict, context_instance=RequestContext(request))

def sheduler(request,path):
    test_filelist=os.listdir(path)
    input=request.POST
    dict={                                              'list': test_filelist,
                                                        'path': path,
                                                        'frequency': 'not defined1',
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

# Create your views here.
#from django.shortcuts import render_to_response, get_object_or_404
#from db_read.models import Experiment
#from django.template import RequestContext

#===============================================================================
# def index(request):
#        latest_experiments_list = Experiment.objects.all().order_by('-date')[:5]
#        return render_to_response('index.html',{'latest_experiments_list': latest_experiments_list})
# 
#def detail(request, experiment_id):
#    exp = get_object_or_404(Experiment,pk=experiment_id)
#    return render_to_response('detail.html', {'experiment': exp},
#                             context_instance=RequestContext(request))
# 
# def results(request, experiment_id):
#    exp = get_object_or_404(Experiment,pk=experiment_id)
#    return render_to_response('results.html', {'experiment': exp})
#===============================================================================

#def tags(request, experiment_id):
#    exp = get_object_or_404(Experiment,pk=experiment_id)
#    return render_to_response('detail.html', {'experiment': exp})

#    return HttpResponse("The tags peculiar to this experiment: %s." % experiment_id)


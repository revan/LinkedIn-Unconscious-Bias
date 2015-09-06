from django.shortcuts import render
from django.http import HttpResponse

from .models import Experiment, Pair
from .linkedin import getLinkedIn, getWhiteOut


def index(request):
    experiments = Experiment.objects.order_by('name')
    context = {'experiments': experiments}
    return render(request, 'experiment/index.html', context)


def profile(request, profile_id):
    return HttpResponse(getLinkedIn(profile_id))


def pick(request, experiment_id):
    pair = Pair.objects.filter(experiment_id=experiment_id)[0]
    context = {
        'pair': pair,
        'whiteout': getWhiteOut
    }
    return render(request, 'experiment/pick.html', context)

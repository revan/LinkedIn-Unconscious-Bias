from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate, Experiment, Pair
from .linkedin import getLinkedIn, getWhiteOut

import random


def index(request):
    experiments = Experiment.objects.order_by('name')
    context = {'experiments': experiments}
    return render(request, 'experiment/index.html', context)


def profile(request, profile_id):
    return HttpResponse(getLinkedIn(profile_id))


def pick(request, experiment_id):
	try:
		winner_id = request.POST['winner_id']
		loser_id = request.POST['loser_id']
		blind = request.POST['blind']

		winner = Candidate.objects.get(linkedin_id__exact=winner_id)
		loser = Candidate.objects.get(linkedin_id__exact=loser_id)

		if blind:
			winner.blind_wins += 1
			winner.blind_fights += 1
			loser.blind_fights += 1
		else:
			winner.full_wins += 1
			winner.full_fights += 1
			loser.full_fights += 1

		winner.save()
		loser.save()

		lesser = min((winner_id, winner), (loser_id, loser))[1]
		pair = Pair.objects.get(user1_id=lesser.id)
		if lesser.id == winner_id:
			if blind:
				pair.blind_wins_1 += 1
			else:
				pair.full_wins_1 += 1
		else:
			if blind:
				pair.blind_wins_2 += 1
			else:
				pair.full_wins_2 += 1
		pair.save()

	except (KeyError, Candidate.DoesNotExist, Pair.DoesNotExist):
		print('error')

	pair = Pair.objects.filter(experiment_id=experiment_id)[0]

	blind = random.choice([True, False])

	switch = random.choice([True, False])
	user1 = pair.user1
	user2 = pair.user2

	context = {
		'experiment_id': experiment_id,
		'pair': pair,
		'user1': user2 if switch else user1,
		'user2': user1 if switch else user2,
		'blind': blind,
		'whiteout': getWhiteOut(blind)
	}
	return render(request, 'experiment/pick.html', context)


def results(request, experiment_id):
	pairs = Pair.objects.filter(experiment_id=experiment_id)

	candidate_ids = set()
	for p in pairs:
		set.add(p.user1)



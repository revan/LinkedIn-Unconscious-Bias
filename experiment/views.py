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
		blind = request.POST['blind'] != 'false'

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
		greater= min((winner_id, winner), (loser_id, loser))[1]

		try1 = Pair.objects.filter(user1_id=loser.id).filter(user2_id=winner.id)
		try2 = Pair.objects.filter(user2_id=loser.id).filter(user1_id=winner.id)

		if len(try1) > 0:
			pair = try1[0]
			if blind:
				pair.blind_wins_2 += 1
			else:
				pair.full_wins_2 += 1
		else:
			pair = try2[0]
			if blind:
				pair.blind_wins_1 += 1
			else:
				pair.full_wins_1 += 1

		pair.save()

	except (KeyError, Candidate.DoesNotExist, Pair.DoesNotExist):
		print('error')

	pair = random.choice(list(Pair.objects.filter(experiment_id=experiment_id)))

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
		candidate_ids.add(p.user1)
		candidate_ids.add(p.user2)

	candidates = []
	for c in candidate_ids:
		# TODO: combine all these requests. This doesn't scale.
		candidates.append(Candidate.objects.get(linkedin_id__exact=c))

	biases = [c for c in candidates if (float(c.blind_wins)/(c.blind_fights+0.001) > float(c.full_wins)/(c.full_fights+0.001))]

	experiment = Experiment.objects.get(pk=experiment_id)

	context = {
		'candidates': list(candidates),
		'biases': biases,
		'pairs': pairs,
		'experiment': experiment
	}

	return render(request, 'experiment/results.html', context)


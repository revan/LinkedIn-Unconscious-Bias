from django.db import models


class Candidate(models.Model):
    linkedin_id = models.CharField(max_length=40)
    blind_wins = models.IntegerField(default=0)
    blind_fights = models.IntegerField(default=0)
    full_wins = models.IntegerField(default=0)
    full_fights = models.IntegerField(default=0)

    def __str__(self):
        return self.linkedin_id


class Experiment(models.Model):
    name = models.CharField(max_length=40)
    # TODO: configurable blocking
    times_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Pair(models.Model):
    experiment = models.ForeignKey(Experiment)
    user1  = models.ForeignKey(Candidate, related_name='pair_user1')
    user2 = models.ForeignKey(Candidate, related_name='pair_user2')
    blind_wins_1 = models.IntegerField(default=0)
    blind_wins_2 = models.IntegerField(default=0)
    full_wins_1 = models.IntegerField(default=0)
    full_wins_2 = models.IntegerField(default=0)

    def __str__(self):
        return "%s and %s in %s" % (self.user1, self.user2, self.experiment)

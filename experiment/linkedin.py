import requests
import html

from .secrets import COOKIE

def getWhiteOut():
	return [
		# "getElementsByClassName('profile-picture')[0].style.visibility = 'hidden'",
		# "getElementById('name-container').style.visibility = 'hidden'",
		"getElementsByClassName('profile-top-card top-card ')[0].style.visibility = 'hidden'",
		"getElementsByClassName('profile-card-extras')[0].style.visibility = 'hidden'",
		"getElementsByClassName('alert attention')[0].style.visibility = 'hidden'",
		"getElementsByClassName('remote-nav')[0].style.visibility = 'hidden'",
		"getElementsByClassName('insights')[0].style.visibility = 'hidden'",
		"getElementsByClassName('responsive-nav')[0].style.visibility = 'hidden'",
		"getElementsByClassName('global-header')[0].style.visibility = 'hidden'",
	]

def getLinkedIn(profile_id):
	url = "https://www.linkedin.com/profile/view?id=%s" % (profile_id)

	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.15 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Cookie': COOKIE,
		'Connection': 'keep-alive'
	}

	r = requests.get(url, headers=headers)

	return r.text
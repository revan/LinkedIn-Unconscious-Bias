import requests
import html

from .secrets import COOKIE

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
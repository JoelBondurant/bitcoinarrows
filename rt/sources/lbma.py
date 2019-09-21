"""
LBMA Data Ingress
======================
Metal data hijacking via:
http://www.lbma.org.uk/home
script_src=http://www.lbma.org.uk/js/feeds.js
feed_url=https://lbma.datanauts.co.uk/api/today/both.json
"""

import requests

from util import logger
from util import rock


# LBMA API Endpoints:
base_uri = "https://lbma.datanauts.co.uk/api/"


def spot():
	"""
	LBMA fixed prices.
	"""
	dat = requests.get(base_uri + "today/both.json").json()
	am_usd_per_toz = float(dat["gold"]["am"]["usd"])
	pm_usd_per_toz = float(dat["gold"]["pm"]["usd"])
	usd_per_toz = (am_usd_per_toz + pm_usd_per_toz)/2.0
	usd_per_gram = (usd_per_toz / rock.grams_per_toz)
	return usd_per_gram


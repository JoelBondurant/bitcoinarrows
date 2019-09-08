#!/usr/bin/env python3
import datetime
import json
import uuid

from flask import Flask, request, send_from_directory, render_template, make_response

from util import logger
from util import rock


logger.info("wap started.")
app = Flask("bitcoinarrows", static_url_path="", template_folder="rws")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1

rtdb = rock.Rock("rtdb")
devicedb = rock.Rock("devicedb")


@app.errorhandler(404)
def awol(err):
	return render_template("404.html"), 404

def gendeviceid():
	return str(uuid.uuid4())

@app.route("/")
def index():
	spot = rtdb.get("spot")
	gold_spot = rtdb.get("gold.spot")
	binance_spot = rtdb.get("binance.spot")
	coinbase_spot = rtdb.get("coinbase.spot")
	kraken_spot = rtdb.get("kraken.spot")
	now = datetime.datetime.now().replace(second=0, microsecond=0)
	now_iso = (now + datetime.timedelta(minutes=2)).isoformat()
	minute0_iso = (now + datetime.timedelta(minutes=-12*60)).isoformat()
	content = {
		"spot": spot,
		"gold_spot": gold_spot,
		"binance_spot": binance_spot,
		"coinbase_spot": coinbase_spot,
		"kraken_spot": kraken_spot,
		"now_iso": now_iso,
		"minute0_iso": minute0_iso
	}
	resp = make_response(render_template("index.html", **content))
	
	if "deviceid" in request.cookies:
		deviceid = request.cookies.get("deviceid")
		try:
			udat = devicedb.get(deviceid)
		except:
			udat = {"visits": 0}
		udat["visits"] += 1
		devicedb.put(deviceid, udat)
	else:
		deviceid = gendeviceid()
		devicedb.put(deviceid, {"visits":1})
		resp.set_cookie("deviceid", deviceid)

	return resp


@app.route("/about")
def about():
	return render_template("about.html")


@app.route("/ws/<file_name>")
def ws(file_name):
	"""
	web site resources (js/css/etc) loader.
	file_name - the filename to load.
	"""
	return send_from_directory("ws", file_name)


@app.route("/arrows/<arrow_name>")
def arrow(arrow_name):
	"""
	arrow loader (png/html).
	arrow_name - the filename to load.
	"""
	return send_from_directory("/data/arrows", arrow_name)


@app.after_request
def add_header(response):
	response.headers["Cache-Control"] = "public, max-age=0"
	response.headers["Pragma"] = "no-cache"
	response.headers["Expires"] = "-1"
	return response



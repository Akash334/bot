#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json
import os
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)

    	print 'Request:'
    	print json.dumps(req, indent=4)

    	res = processRequest(req)

    	res = json.dumps(res, indent=4)

    # print(res)

    	r = make_response(res)
    	r.headers['Content-Type'] = 'application/json'
    	return r


def processRequest(req):
    	if req.get('result').get('action') != 'yahooWeatherForecast':
        	return {}
   	data = "this is the response from webhook"
    	res = makeWebhookResult(data)
    	return res

def makeWebhookResult(data):
	
	speech = "This is the response from server" + "and" + data
    	print "Response:"
    	print speech
	
	message= {
    	 "attachment":{
      	   "type":"template",
            "payload":{
              "template_type":"generic",
              "elements":[{
              "title":"",
              "item_url":"https://aarz.pk/",
              "image_url":"https://www.aarz.pk/assets/images/properties/8666/8666.actual.0.jpg",
              "buttons":[
              {
                "type":"web_url",
                "url":"https://www.aarz.pk/",
                "title":"Get Real"
              }
            ]
          }
        ]
      }
    }
  }	
	
        return {
        "speech": speech,
        "displayText": speech,
        "data": {"facebook": message},
        # "contextOut": [],
        #"source": "apiai-weather-webhook-sample"
  }

if __name__ == '__main__':
        port = int(os.getenv('PORT', 5000))

        print 'Starting app on port %d' % port

        app.run(debug=False, port=port, host='0.0.0.0')

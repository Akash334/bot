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
              "title":"A Game to Go Deeper",
              "item_url":"https://www.getreal.life/",
              "image_url":"https://www.dropbox.com/s/9dj0ef2cuuezn9w/question1.jpg?raw=1",
              "buttons":[
              {
                "type":"web_url",
                "url":"https://www.getreal.life/",
                "title":"Get Real"
              },
	     {
       	        "type":"element_share"
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

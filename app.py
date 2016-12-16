#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json
import os
import re

from flask import Flask
from flask import request
from flask import make_response
from random import randint
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
	number=randint(1,5)
	speech = "This is the response from server" + "and" + number
	
	message= {
    	 "attachment":{
      	   "type":"template",
            "payload":{
              "template_type":"generic",
              "elements":[{
              "title":"A Game to Go Deeper",
              "item_url":"https://www.getreal.life/",
              "image_url":"https://www.aarz.pk/bot/images/qus"+number+".png",
              "buttons":[
              {
                "type":"web_url",
                "url":"https://www.getreal.life/",
                "title":"Download App"
              },
	     {
       	        "type":"element_share"
             },
	     {
        	"type":"web_url",
        	"url":"https://www.mcssl.com/WebForms/WebForm.aspx?wid=d8e7fdb0-0d0f-42a4-879a-253afd43e69b",
        	"title":"Download 50 Questions"
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

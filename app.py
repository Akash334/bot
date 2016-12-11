#!/usr/bin/env python

import urllib
import urllib2
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

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


#def processIntentName(req):
 #   result = req.get("result")
  #  parameters = result.get("metadata")
   # intent = parameters.get("intentName")
    #return intent


    speech = "Here are some properties with your choice:"
    print("Response:")
    print(speech)
     message= {
         "attachment": {
           "type": "template",
             "payload": {
               "template_type": "generic",
               "elements": [{
               "title": "Blah blah",
               "subtitle": "123123",
               "item_url": "http://www.aarz.pk/property-detail?id=1",               
               "image_url": "http://www.aarz.pk/assets/images/properties/1/1.actual.1.jpg" ,
                "buttons": [{
                "type": "web_url",
                "url": "www.aarz.pk",
                "title": "Open Web URL"
            }, 
                   ],
          }, 
                   {
                "title": "hello",
                "subtitle": "world",
                "item_url":  "http://www.aarz.pk/property-detail?id=2",               
                "image_url": "http://www.aarz.pk/assets/images/properties/2/2.actual.1.jpg",
                "buttons": [{
                "type": "web_url",
                "url": "www.aarz.pk",
                "title": "Open Web URL"
            },
                   ]
          }]
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

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
			

#!/usr/bin/python
import requests
import json
from flask import Flask, request
app = Flask(__name__)

"""
REQUIREMENTS

* A custom slash command on a Slack team
* A web server running something like Apache with mod_wsgi,
  with Python 2.7 installed

USAGE

* Place this script on a server with Python 2.7 installed.
* Set up a new custom slash command on your Slack team:
  http://my.slack.com/services/new/slash-commands
* Under "Choose a command", enter whatever you want for
  the command. /isitup is easy to remember.
* Under "URL", enter the URL for the script on your server.
* Leave "Method" set to "Post".
* Decide whether you want this command to show in the
  autocomplete list for slash commands.
* If you do, enter a short description and usage hint.

"""

# Replace this with the token from your slash command configuration page
TOKEN = ''


@app.route('/isitup', methods=['POST'])
def isitup():
    # isitup.org doesn't require you to use API keys, but they do
    # require that any automated script send in a user agent string.
    # You can keep this one, or update it to something that makes more sense for you.
    headers = {"user-agent": "IsitupForSlackPy/1.0"}

    # Check the token and make sure the request is from our team
    if request.form['token'] == TOKEN:
        # We're just taking the text exactly as it's typed by the user.
        # If it's not a valid domain, isitup.org will respond with a `3`.
        # We want to get the JSON version back (you can also get plain text).
        r = requests.get('https://isitup.org/' + request.form['text'] + '.json', headers=headers)
        response_json = json.loads(r.text)

        # Build our response
        # Note that we're using the text equivalent for an emoji at the start of each of the responses.
        # You can use any emoji that is available to your Slack team, including the custom ones.
        if not r.status_code:
        	# isitup.org could not be reached
            reply = "Ironically, isitup could not be reached."

        elif response_json['status_code'] == 1:
            # Yay, the domain is up!
            reply = ":thumbsup: I am happy to report that *<http://" + response_json['domain'] + "|" + response_json['domain'] + ">* is *up*!"

        elif response_json['status_code'] == 2:
            # Boo, the domain is down.
            reply = ":disappointed: I am sorry to report that *<http://" + response_json['domain'] + "|" + response_json['domain'] + ">* is *not up*!"

        elif response_json['status_code'] == 3:
            # Uh oh, isitup.org doesn't think the domain entered by the user is valid
            reply = ":interrobang: *" + request.form['text'] + "* does not appear to be a valid domain. \n"
            reply += 'Please enter both the domain name AND suffix (example: *amazon.com* or *whitehouse.gov*).'

    else:
        reply = "The token for the slash command doesn't match. Check your script."

    return reply


if __name__ == '__main__':
    app.run()

# isituppy
Custom slash command to use isitup.org to check if a site is up from within Slack

## REQUIREMENTS

* A custom slash command on a Slack team
* A web server running something like Apache with mod_wsgi,
  with Python 2.7 installed

## USAGE

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

_Derived from David McCreath's PHP version here: https://github.com/mccreath/isitup-for-slack_

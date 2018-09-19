# -*- encoding: utf-8 -*-
'''
Install the latest release of Python wrapper: $ pip install ovh

Usage:
1: Fill this script with your endpoint, application_key, application_secret and consumer_key
If you don't have your keys yet, consult consumerkey.py first.

2: Call this script like this: python redirector.py mysite.com from to
e.g: redirector.py mysite.com carrefour kevin
will create an alias carrefour@mysite.com and redirect the mails to kevin@mysite.com
'''
import json
import ovh
import sys

# Handle command line arguments
post_url = "/email/domain/" + sys.argv[1] + "/redirection"
from_str = sys.argv[2] + "@" + sys.argv[1]
to_str = sys.argv[3] + "@" + sys.argv[1]

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page https://eu.api.ovh.com/createApp/
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='APPKEY',    # Application Key
    application_secret='APPSECRET', # Application Secret
    consumer_key='CONSUMERKEY',       # Consumer Key
)

result = client.post(post_url, 
    _from=from_str, # Required: Name of redirection (type: string)
    localCopy=False, # Required: If true keep a local copy (type: boolean)
    to=to_str, # Required: Target of account (type: string)
)

# Pretty print
print json.dumps(result, indent=4)
# -*- encoding: utf-8 -*-
'''
This function is used to obtain your consumerKey from OVH. It should only be called once.
Install the latest release of Python wrapper: $ pip install ovh

Usage:
1: Create your keys here https://eu.api.ovh.com/createApp/
2: Create your ovh.conf (same dir as this script) and fill it with your endpoint, application_key and application_secret
3: Call this script like this: python consumerkey.py mysite.com
'''
import ovh
import sys
# create post url using command line arguments
post_url = "/email/domain/" + sys.argv[1] + "/redirection"

# create a client using configuration
client = ovh.Client()

# Request RO, /me API access + POST on /email/domain/{domain}/redirection
ck = client.new_consumer_key_request()
ck.add_rules(ovh.API_READ_ONLY, "/me")
ck.add_rules(["POST"], post_url)
# Request token
validation = ck.request()

print "Please visit %s to authenticate" % validation['validationUrl']
raw_input("and press Enter to continue...")

# Print nice welcome message
print "Welcome", client.get('/me')['firstname']
print "Btw, your 'consumerKey' is '%s'" % validation['consumerKey']
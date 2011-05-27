from pixnetlib import PixnetOAuth

consumer_key = "194f65eab45b79a186f47655376934f5"
consumer_secret = "4b4f6368334e2add978c9231f176479d"
api = PixnetOAuth( consumer_key, consumer_secret )
print( "Please visit %s to authorization." % api.get_auth_url() )
verifier_token = raw_input()
api.get_access_token( verifier_token )
print "ok"


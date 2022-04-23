import hmac
import hashlib
import time
import os
from werkzeug.wrappers import Request, Response

class slackAuth(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        """Function that authenticate requests from slack
           The function based on the slack guide:
           https://api.slack.com/authentication/verifying-requests-from-slack
        """
        request = Request(environ)
        slack_signing_secret = bytes(os.environ.get('SLACK_SIGN_TOKEN'), "utf-8")
        request_body = request.get_data().decode()

        slack_request_timestamp = request.headers["X-Slack-Request-Timestamp"]
        slack_signature = request.headers["X-Slack-Signature"]
        if (int(time.time()) - int(slack_request_timestamp)) > 60:
            print("Verification failed. Request is out of date.")
            res = Response(status=404)

            return res(environ, start_response)

        basestring = f"v0:{slack_request_timestamp}:{request_body}".encode("utf-8")
        # Hash the basestring using your signing secret, take the hex digest, and prefix with the version number
        my_signature = (
            "v0=" + hmac.new(slack_signing_secret, basestring, hashlib.sha256).hexdigest()
        )
        # Compare the resulting signature with the signature on the request to verify the request
        if hmac.compare_digest(my_signature, slack_signature):
            data = request.form
            environ['data'] = {
                'channel_id': data.get('channel_id'),
                'user_id': data.get('user_id'),
                'text': data.get('text')
            }

            return self.app(environ,start_response)
        else:
            print("Verification failed. Signature invalid.")
            # its better to return 404 so the attacker might think the server doesn't exist or working
            # if he would get 401 he will know for sure that he got to somewhere
            res = Response(status=404)
            return res(environ, start_response)
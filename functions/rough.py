def main(event, context):
    if len(event.request.session.length) == 0:
    # new request to log in
        event.response.issue_tokens = False
        event.response.fail_authentication = False
        event.response.challenge_name = "CUSTOM_CHALLENGE"
    elif (
    len(event.request.session) >= 3 and
    event.request.session[ len(event.request.session) - 1 ].challenge_result == False
    ):
    # user has incorrectly entered OTP 3 times
        event.response.issue_tokens = False
        event.response.fail_authentication = True
    elif (
        event.request.session.length >= 1 and
        event.request.session[ len(event.request.session) - 1 ].challenge_name == "CUSTOM_CHALLENGE" and
        event.request.session[ len(event.request.session) - 1 ].challenge_result == True
    ):
    # user correctly entered OTP
        event.response.issue_tokens = True
        event.response.fail_authentication = False
    else:
    # user incorrectly entered OTP 
        event.response.issue_tokens = False
        event.response.fail_authentication = False
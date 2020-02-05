from website_alive import make_request


def check(s):
    reference = s[1: -1]
    if make_request.get_response(reference).status_code == 200:
        return True
    else:
        return False

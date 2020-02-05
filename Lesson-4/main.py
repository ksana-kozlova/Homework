from website_alive import check_response
print('enter site address with quotes ')
s = input()
if check_response.check(s):
    print('website available')
else:
    print('site unavailable')

import time
class FooException(Exception):
    def __init__(self, text, *args):
        super ( FooException, self ).__init__ ( text, *args )
        self.text = text

def post_request(request):
    session = requests.Session()
    response = session.send(request.prepare(), timeout=5, verify=True)

    if response.status_code is not requests.codes.ok:
        raise FooException(response)

    session.close()
    return response

try:
   ...   #post_request(response)
except FooException as r:
       #print type(r)
       print r.text
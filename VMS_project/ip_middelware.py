from django.http import HttpResponseForbidden

class IPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1']  #  allowed IP address
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            return HttpResponseForbidden('<h1>Forbidden</h1>')
        response = self.get_response(request)
        return response

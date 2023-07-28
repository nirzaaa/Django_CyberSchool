from django.http import HttpResponseForbidden
from django.shortcuts import render

class LocalhostOnlyMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['REMOTE_ADDR'] not in ('127.0.0.1', '::1'):
            if 'secret' in request.path:  # Only restrict access to URLs containing 'secret'
                # return HttpResponseForbidden("Access Forbidden. This URL is only accessible from localhost.")
                return render(request, 'main/accessforbidden.html')
        
        return self.get_response(request)
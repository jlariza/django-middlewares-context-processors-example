from django.http import HttpResponse

def demo_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.GET.get("token","") != "valid_token":
            return HttpResponse("Invalid Token")

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

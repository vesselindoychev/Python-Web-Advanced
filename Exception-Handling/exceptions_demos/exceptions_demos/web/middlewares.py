from exceptions_demos.web.views import InternalErrorView


def handle_exception(get_respnose):
    def middleware(request):
        response = get_respnose(request)
        if response.status_code >= 500:
            return InternalErrorView.as_view()(request)

        return response

    return middleware

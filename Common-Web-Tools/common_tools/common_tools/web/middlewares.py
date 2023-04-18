import time


def measure_time_middleware(get_response):
    def middleware(request):
        start_time = time.time()

        response = get_response(request)

        end_time = time.time()

        print(f"Executed in {end_time - start_time}s")
        return response

    return middleware

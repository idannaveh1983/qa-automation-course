status_codes = {
    205: "OK",
    200: "Created",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable"}
for status_code, message in status_codes.items():
        if status_code == 200:
            print(f"Status code {status_code}: {message} - test passed")
        else:
            print(f"Status code {status_code}: {message} - test failed!")
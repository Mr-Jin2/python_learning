
# def application(environ, start_response):
#     status = '200 OK'
#     output = 'Hello World!'
#
#     response_headers = [('Content-type', 'text/plain'),
#                          ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)
#
#     return [output]

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
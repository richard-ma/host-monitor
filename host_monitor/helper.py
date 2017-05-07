import os

def on_heroku():
    return ('HEROKU' in os.environ)

def get_client_ip(request):
    ip = request.remote_addr

    if on_heroku():
        header = request.headers.get('X-Forwarded-For')
        ip = header
        #ip = header.split(',')[-1]

    return ip

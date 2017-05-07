# host-monitor
a Flask-RESTful api server for monitor my raspberry pi server host

# API
* *ALL URL MUST END WITH / !!!*
* *ALL INTERFACE RETURN JSON !!!*

## status
* curl http://api.domain.info/

## host
* List:     curl http://api.domain.info/hosts/
* Create:   curl http://api.domain.info/hosts/ -X POST -d 'host=host_name'
* Read:     curl http://api.domain.info/hosts/host_name
* Update:   curl http://api.domain.info/hosts/host_name -X PUT
* Delete:   curl http://api.domain.info/hosts/host_name -X DELETE

# Client Tools

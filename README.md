
This README would normally document whatever steps are necessary to get your application up and running.

### Dependencies ###

* Python 3.x
* mongodb

### Getting Started ###

* Create a db for the application : "use url_shortener"
* Set password for the database : <DB_PASSWORD>


### Virtual Environment Setup ###

* Setup uti virtualenv : "virtualenv -p python3 env"
* Move to virtualenv and activate its environment (source env/bin/activate)
* pip  install -r requirements.txt



### Code Setup ###


* Enter into terminal
* cd to project path
* Run python manage.py runserver


### Available APIs

1. /urls/encode

request: {
	"url": "http:://abc.com/abc"
}
Method: POST

2. /urls/decode

request: {
	"url": "6FcImAV1"
}

## running test cases

coverage run manage.py test shortener -v 2


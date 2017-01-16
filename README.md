![reactions logo](http://i.imgur.com/odjk7wh.png)

You'll never run out of reaction faces anymore!

# What is it? #

**reactions** is a simple web service that collects mfw / tfw images from [4chan](http://www.4chan.org/) boards.

Basically it just saves them to the disk and provides you an easy-to-use web interface with the "Randomize" button.

![web interface](http://i.imgur.com/JU89KRR.png)

## Usage ##

* Install :snake: [Python](https://www.python.org/)
* Install [Bower](https://bower.io/)
* git clone
* pip install -r requirements.txt

**Service**
* cd service
* vim config.ini
* crontab -e -> python /path/to/service/main.py &

**Web**
* cd web
* bower install
* vim config.ini
* python main.py &

### How can I help? ###

* Fork
* Make changes
* Create pull request

### How can I contact the author? ###

Send me an e-mail to b0r3d0mness [at] gmail [dot] com

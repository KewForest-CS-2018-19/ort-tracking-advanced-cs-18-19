ORT Tracker is an application developed by the Upper School Advanced Computer Science Class for the Kew Forest Community. It is coded to provide an easy, accessible way to track food waste and serves as an initiative to reduce the amount of food we waste here at the Kew Forest School. ORT Tracker allows for students to have an interactive experience while learning about the food they waste. In addition, ORT Tracker serves as an opportunity to bring the upper and lower school together to work in unison to provide an application that will benefit the whole Kew Forest Community.

The ORT tracker is a Python Flask application.


set up a virtual environment
$ python3 -m venv virt

activate it on Mac
$ . virt/bin/activate
on PC virt\Scripts\activate

run it: $ python application.py
(virt) Dn$ pip install flask==1.0.2

(virt) $ pip install awsebcli --upgrade

(virt) $ pip install -r requirements.txt


eb init -p python-3.6 ort-tracker --region us-east-2
eb deploy

# flask-app-da
# different from aws tutorial
$ python3 -m venv virt
$ . virt/bin/activate
(virt)$ pip install flask==1.0.2

(virt) $ pip install awsebcli --upgrade

(virt) $ pip install -r requirements.txt


eb init -p python-3.6 ort-tracker --region us-east-2
eb deploy


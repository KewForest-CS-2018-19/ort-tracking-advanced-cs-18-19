# flask-app-da
# different from aws tutoria

creat virt environment
$ python3 -m venv virt

activate  virt environment
$ . virt/bin/activate
(virt) $ pip install flask==1.0.2

(virt) $ pip install awsebcli --upgrade

(virt) $ pip install -r requirements.txt


eb init -p python-3.6 ort-tracker --region us-east-2
eb deploy


data.xml is a semi-structure data which is scraped from the website stackoverflow.com

following steps need to perform for creating data pipeline component.

i) creation and activation of virtual env 

virtualenv venv_name
.\venv_name\Scripts\activate 

ii) installing all deps

pip install -r requirements.txt

iii) create iam new user with s3,ec2 full access service then create access key
     
pip install awscli   
pip install awscli --upgrade 
pip install boto3 --upgrade
aws configure 
aws configure list

iv) creat bucket 
python s3_sync.py 
pip install xmltodict
python data_to_s3.py---> data sending to s3 bucket

v) interact with falsk and s3 and getting all the data to webpage. 
python api.py

vi) Create Ec2 machine

vii) connect to ec2 machine:
        inside vm terminal ---> cmd---> git clone https://github.com/chisah2x/stack-overflow-python-query-prediction.git
        cd stack-overflow-python-query-prediction
        sudo apt-get update
        sudo apt-get install python3
        sudo apt install python3-pip
        pip install -r requirements.txt
        nano api.py  -> open api.py file in terminal itself for editing purpose ---> change the port= 8000 and hostname=0.0.0.0 and debug = False ctrl+x  yes  enter

        nano .env  
        cat .env
        python3 api.py

        go back in instance and copy link of Public IPv4 DNS: ec2-13-235-114-24.ap-south-1.compute.amazonaws.com
        and http://ec2-13-235-114-24.ap-south-1.compute.amazonaws.com:8000  port number at end don't forget
        http://ec2-13-235-114-24.ap-south-1.compute.amazonaws.com:8000/xml_data

viii) create account on rapid api and follow the steps and deploy the hosted link
        data -> select any service -> python request -> copy and ctrl+A then ctrl+V in get_data.py and subscribe then
        python3 get_data.py
        
        if you want creat your on api, go to myapi  -> add api project : name-stack_overflow_data, description-something, category-data, personel, do not impact ;  after creating go to hub list then make api public then put hosting link into Base Url  save and go to endpoint: name, description and in GET /xml_data then save. View in hub it is reflected.
        select python language and copy code and paste it in get_data.py in vsc

        python3 get_data.py  in vsc

        now next time need to send new data to just s3 bucket.

        completed first component.



ix) ML operation pipeline:

        create src folder, for stage1_get_data, need params.yaml and config.yaml

        a) python3 src/stage_01_get_data.py  -> create artifacts folder in which data is there
        basically, it is fetching data from cloud and storing into local system. artifacts/data
        fetch all the data to the destination folder of artifacts this is data ingestion pipeline...
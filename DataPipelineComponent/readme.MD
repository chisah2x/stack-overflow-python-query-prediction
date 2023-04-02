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
                go to directory of data pipeline component
                sudo apt-get update
                sudo apt-get install python3
                sudo apt install python3-pip
                pip install -r requirements.txt
                nano api.py  -> port= 8000 and hostname=0.0.0.0 and debug = False 

                nano .env  
                cat .env
                python3 api.py

                go back in instance and copy link of Public IPv4 DNS: 
                and http://ec2-3-109-62-182.ap-south-1.compute.amazonaws.com:8000  
                http://ec2-3-109-62-182.ap-south-1.compute.amazonaws.com:8000/xml_data

        viii) create account on rapid api and follow the steps and deploy the hosted link
                data -> select any service -> python request -> copy and ctrl+A then ctrl+V in get_data.py and subscribe then
                python3 get_data.py
                
                if you want creat your on api, go to myapi  -> add api project -> hub list -> View in hub ->   select python language and copy code and paste it in get_data.py in vsc

                python get_data.py  in vsc   

                finally completed first component.

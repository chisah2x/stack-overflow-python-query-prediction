# stack-overflow-python-query-prediction

### 1st component: Data Pipeline Component:

#### data.xml is a semi-structure data which is scraped from the website stackoverflow.com

##### following steps need to perform for creating data pipeline component.

i) creation and activation of virtual env. <br>
ii) installing all dependencies. <br>
iii) create IAM user with s3,ec2 full access service on AWS then create access key. <br>
iv) create s3 bucket. <br>
v) interact with flask and s3 and getting all the data to webpage. <br>
vi) Create Ec2 machine . <br>
vii) connect to ec2 machine and create hosted link. <br>
viii) deploy the hosted link on rapid api. <br>

##### completed first component.

### 2nd component: ML Pipeline Component:

1-->make deps which are config.yml and params.yml and utils.yml <br>
2-->make dvc.yaml and write 5 stage script <br>
3-->install dvc 
4-->dvc add main_data/data.xml <br>
5-->dvc repro for 1 stage and again git add . and git commit -m "msg do for 5 times for 5 stages <br>
6-->dvc plots show generates html template for showing the plot curve <br>
7-->go to https://studio.iterative.ai and make account <br>
8-->add a project and then add the main repository <br>
9--> now u can able to track all the git commits wrt the data versions and also experiment and compare the models <br>
10-->End
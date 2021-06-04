# ```mgmt590-webapp``` Question Answering WebApp
I have created a web app for answering questions, and addition and deletion of models. If a user wants to upload a set of questions along with their context to get the answers for those questions, he/she can easily do that. 

## A system architecture diagram showing how the following things are connected:

○ REST API

○ Web App

○ User of the Web App

○ Backing database


![image](https://user-images.githubusercontent.com/20911800/120734132-5e4b0980-c4b6-11eb-9cbe-325c468f52b5.png)





## How this app works(with screenshots): 
_**1. 	Available models:**_

On the top of the app’s page, there is a button named “Available Models”. On clicking this button, it shows us all the available models in the web app I created.

_**2. 	Addition of models:**_

The next thing we see on our page are three text boxes named as “name”, “tokenizer”, and “model”. To add a model to our web app, we need to fill these text boxes appropriately as follows:

    a. Name: The name we would like to give our model.

    b. Tokenizer: The appropriate tokenizer we would like to use with this specific model.
  
    c. Model: The actual model that we are using.

After adding text to these boxes, we need to click on the “Add the Model” button given below these boxes. Once added, the user can see his added model, which is represented by the name that the user gave, by clicking on the “Available Models” button on the top. 

_**3. 	Deletion of models:**_

Further we see a drop-down text box named “select”. If we click on the drop-down menu, we can see all the available models, represented by the name we had assigned them. From those models we can select the model we would like to delete from our web app. For this, we need to select the model by clicking on the model we want to delete from the drop-down menu, the name of the selected model would show beneath the box after the “You Selected:” line, and then click on the “Delete the selected model” button given beneath. This would lead to the removal of the selected model from our web app.

The purpose of this web app is to allow the users to get the answers of the questions they input in the app. The app uses the google postgre SQL database and various ML algorithms to return the answers to users. The database consists of questions and contexts, and the ML algorithms uses these to extract the answers from the contexts and questions stored in the database.

_**4. 	Question-answering :**_

Next, we see are two text boxes named “Question” and “Context”. We can simply ask a question by typing a question in the “Question” text box, and some content from where we would like to look up an answer to that question in the “Context” box.
We then just need to click on the button given below, named as “Answer Question”.
Once clicked the model would run and give an answer to that question below.

_**5. 	File uploading:**_

Further we see a file uploader button. Here, by clicking on the “Browse files” button we can upload a .csv file with questions and context for the same inside it. Once uploaded, below the box our web app would give the questions and their answers from the associated context in a table form.



## Prerequisites and Installation:

To run this application, you'll need the following pre-requisites installed on your machine

| Library      | Version | Installation |
| ----------- | ----------- | --------- |
| Python | 3.9.1 or above  | <a href="https://www.python.org/downloads/"> Python </a> |
| Flask   | 2.0.1        | `pip install flask` |
| Transformers | 4.6.1 | `pip install transformers` |
| SQLite | 2.6.0 | `pip install sqlite3` |
| Docker Engine | NA | <a href="https://docs.docker.com/engine/"> Docker </a>|
| Tensor Flow | 2.5.0 | `pip install --upgrade tensorflow` |
| Pytorch | 1.8.1+cpu | `pip install torch` |
| streamlit | 0.82.0 | `pip install streamlit` |


## Container Deployment through Docker

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. To deploy the app on your local machine through docker, we need a docker file ,given we already have the application file created, that would be the recipe for docker to build the application

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. In the dockerfile, we will add the required dependency of tensorflow and pytorch to run the transformers model.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Once the dockerfile is created, we add the dependencies to be installed in the docker image in the requirements.txt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. After you add the dependencies in requirements.txt; you'll run it when the docker container would be published and deployed

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. We'll copy the application in the app folder and run the application once the docker image was deployed

*Sample Requirements.txt*
```
flask == 2.0.1
transformers == 4.6.1
```
*Sample Dockerfile*
````
FROM tensorflow/tensorflow

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY <aap-name>.py /app/<aap-name>.py

CMD ['python','/app/<aap-name>.py']

````
*Building the Docker Image in the Active Directory/Folder*
```
sudo docker build -t <image-name> . 
```

*Running the Docker Image - with ports defined for communication between local machine and docker image* 
```
sudo docker run -it -p 8080:8080 <image-name> /app/<aap-name>.py
```

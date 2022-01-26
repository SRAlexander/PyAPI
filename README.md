# PyAPI
Python template for a RESTFul API including DI, Flask, Flagger and Alembec

This is an attempt to bring multiple python libraries together to form a project template similar to a .Net c# project. There are plenty of simple examples for many of these libraries but not an indepth guide or example on how to get them working together.  

#### Setup

Create a Virtual Environment

> python3 -m venv venv

This will create a venv folder on the root level. This will not get commited to your GIT repository.

> source myvenv/bin/activate

Enable the virtual environment, once the command completes, you should see (venv) at the start of the terminal cli line.

> cd app
> pip install -r requirements.txt

This will install all required depedencies found in the requirements.txt file. This is only within the local venv. 

> export FLASK_APP=app-dev.py
> flask run

Your application should now be running on localhost:5000, to view the swagger page, head to localhost:5000/apidocs to list all api endpoints. 

You can also run on a different port using flask run --port xxxx


#### Creating a Database.

The template has Alembic or Flask Migrate installed and configured by default. 
Lets create the migration

> flask db migrate -m "Initial Commit"

This will of created a migration file under migrations > version. The base configuration of the template is set to run the migrations against an sql instance. The migrations will be detected from the imports in the root.py.

> flask db upgrade

As there is no database at the moment, the upgrade script will create a test_dev_database.db. 

#### Tests

All unit tests should be added into the tests folder. They can be run with the following command from the tests folder.

> python3 -m unittest discover -s tests -p "*_UnitTests.py"


#### Design Structure

###### DI

So to work inline with standard Dependency injection libaries, controls need to be configured in the root.py, this can be seen on line 21 of the root.py file. Top level injections then need to be done as a function vairable inside the controller which is not an ideal solution but it works and gets DI functional. Services and Repository level classes work as expected with constructor injection and our setup in the container.py file. 

###### DB Access

DB access is managed by AlchemySession class (alchemy.common.session) which can be injected into any repository. The connection string is managed in the instance >  config_env.py files pending on the environment set with the FLASK_APP environment variable. There is no reason why a second AlchemySession type class can be added to introduce another DB soruce. The query syntax can be explored through the SQL Alchemy docuementation. 


###### Dockerfile

The project can be built into a docker image by default. It is also environment configured through a BUILDENV variable. 

###### GitHub Actions

Two github actions have been provided, one for pull-requests-change which will test the image build and run all unit tests and pull-request-complete which will deploy to an Azure Web App if configured. You will however need to configure the following secrets...

AZURE_CREDENTIALS = { subscriptionId : "", tenantId: "", clientId: "", clientSecret: ""}
REGISTRY_LOGIN_SERVER = Azure ACR login server name, can be found on the ACR main overview page.
PYAPI_WEBHOOK_URL_DEV = Full webhook url found in an AppService
WEBHOOK_SECRET_ALL = just set to a " ", the secret is included in the WEBHOOK URL but the action requires two seperate fields

There are also two secret pulled through from a keyvault, if you don't want to use a keyvault, configure them to a Github secret but the example includes the KeyVault option to demonstrate how they are used. 

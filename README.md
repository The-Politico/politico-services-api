# Politico Services API

An API to handle multiple services endpoints.

## Usage

To start your own project, follow these steps:

1. Clone the repo into a new folder.

```
    $ git clone https://github.com/The-Politico/politico-services-api
```

2. Install requirements and setup your shell.

```
    $ pipenv install
    $ pipenv shell
```

## Servers

This template comes with plug-and-play Terraform configuration. In order to start setting up servers, you will need the following:

- POLITICO's .pem file for servers. See Jon or Tyler if you need this.
- Elastic IPs for staging and production servers.
- Your Django project in a **public** repo.
- You have a requirements file in your repo. If you don't, run `pip freeze > requirements.txt`

To configure for yourself, follow these steps:

1. In **both the `terraform/staging` and `terraform/production` folders**, fill out both `terraform.tfvars` and `.env`. These will be gitignored, so any secrets can go in here. The `.env` file will get placed onto the server you create.

2. Initialize onespot and terraform.

```
    $ python setup.py develop
    $ onespot server init
```

3. Launch the server.

```
    $ onespot server launch
```

This will take a few minutes to create a server on AWS. If all goes well, you can move forward setting up the new server.

4. Setup your shiny new server.

```
    $ onespot server setup
```

5. Start the Celery worker

```
    $ fab [staging|production] servers.restart_service:celery
```

6. Check if your server works! Visit STAGING_URL.com/admin to check out the Django admin.

### Updating the server

If you make a change to the Django project itself and need to update it on the server, commit your change and push it to Github. Then run:

```
    $ onespot server update
```

If you make a change to a component app, then you'll need to do the following:

1. Update the requirement in your local env. (If you're having weird caching issues with new versions not being found try running `export PIP_NO_CACHE_DIR=false`)

```
    $ pipenv install my-pluggable-app==0.1.0
```

2. Freeze your requirements to a file.

```
    $ pip freeze > requirements.txt
```

3. Commit and push your changes to Github.

4. Update the server.

```
    $ onespot server update
```

### Running Management Commands

You can run management commands on your server using fabric.

```
    $ fab [staging|production] django.management:[command]
```

### Logging

To tail the Celery Log ssh into the server and tail the following file.
```
    $ ssh ubuntu@url.com
    $ tail -f /var/log/politicoservicesapi/celery.log
```

### Debgging

Is the HTTPS certification not working? Try running:
```
    $ fab [staging|production] servers.setup_cert
```

Did you change the URL recently? You'll have to update the confs:
```
    $ fab [staging|production] servers.deploy_confs
```

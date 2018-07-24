# Django Project Template

This is a starter template for a Django project. Right now, it doesn't contain any Django. What it does give you is pre-baked server configuration with Terraform and Fabric.

## Usage

To start your own project, follow these steps:

1. Clone the repo into a new folder.

```
    $ git clone https://github.com/The-Politico/django-politico-project-template.git <name-of-project>
```

2. Install requirements and setup your shell.

```
    $ pipenv install
    $ pipenv shell
```

3. Fill out `server_config.py` with your project name and project URLs.

4. Run the bootstrap command, which will start a Django project and fill out some files based on your server configuration.

```
    $ fab bootstrap
```

You should have a shiny new `manage.py` file in the root directory and a folder named whatever you set `PROJECT_FILENAME` to with your settings and all in there. Start developing!

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

5. Check if your server works! Visit STAGING_URL.com/admin to check out the Django admin.

### Updating the server

If you make a change to the Django project itself and need to update it on the server, commit your change and push it to Github. Then run:

```
    $ onespot server update
```

If you make a change to a component app, then you'll need to do the following:

1. Update the requirement in your local env.

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
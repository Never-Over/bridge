# Getting Started

Bridge includes an SDK and CLI tool which operate within your Django project. This page will guide you through the process of installing and configuring Bridge.

## Requirements
Bridge requires **[Docker](https://docs.docker.com/get-docker/)** to be installed on your machine.
Verify your docker installation with:
```bash
> docker version
Client: ...
```

## Installation
Install bridge from PyPI:
```bash
pip install python-bridge
```

## Usage
Adding bridge to your project is incredibly simple.

Add the following code to the end of your `settings.py` file (or `DJANGO_SETTINGS_MODULE`):
```python
# Configure infrastructure with Bridge.
# All other settings should be above these lines.
from bridge import django

django.configure(locals())
```

The next time you start up your application, bridge will create and configure local infrastructure for you:
```bash
> ./manage.py runserver

Setting up service bridge_postgres...
[12:00:00] ✓ Image postgres:12 pulled
[12:00:00] ✓ Container bridge_postgres started
[12:00:00] ✓ bridge_postgres is ready
Service bridge_postgres started!
Setting up service bridge_redis...
[12:00:00] ✓ Image redis:7.2.4 pulled
[12:00:00] ✓ Container bridge_redis started
[12:00:00] ✓ bridge_redis is ready
Service bridge_redis started!
Setting up service bridge_celery...
[12:00:00] ✓ Local worker started
Service bridge_celery started!
Setting up service bridge_flower...
[12:00:00] ✓ Flower started
Service bridge_flower started!
Performing system checks...

System check identified no issues (0 silenced).
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
That's it! You now have all the local infrastructure you need to run your django application.

### Deploys
Bridge can handle deployed configuration for your app too! Simply run:
```bash
bridge init render
```
You may be prompted for the entrypoint of your application and settings file if bridge cannot detect them. 

Bridge will create all the configuration necessary for you to immediately deploy to [Render](https://render.com/). This includes a Blueprint `render.yaml` as well as build scripts and start scripts for your Django application.

After running `bridge init render`, commit the changes and visit your project on GitHub. You will see the following button at the end of your README in the root of your repository:

![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)

To deploy your application to the world, simply click the button! Bridge will configure everything needed for Render to deploy and host your app.

In the future, we'll look into supporting more deployment runtimes such as Heroku, AWS, GCP, Azure, and more.

### Project Structure

!!! note

    Bridge currently makes assumptions about your project structure as outlined below. If your project does not follow these conventions, you may need to adjust the generated files before deploying.

Bridge assumes the following project structure:
```
<project root>/
├── <your app>/
│   ├── settings.py
│   ├── [wsgi.py | asgi.py]
│   ├── ...
├── manage.py
├── [requirements.txt | poetry.lock | Pipfile.lock]
├── ...
```

This structure is the default for Django projects created with `django-admin startproject`. The generated build script in `bridge-django-render/build.sh` may need changes if your project structure differs significantly.

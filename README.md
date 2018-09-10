# Getting Started

1. Checkout this project and create a virtual environment.

    ```bash
    git clone https://github.com/machristie/interactwel-gui.git
    cd interactwel-gui
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install this project into the virtual environment

    ```bash
    python setup.py develop
    ```

3. Start the webpack JavaScript build:

    ```bash
    cd interactwel_gui
    npm run watch
    ```

## In the main Airavata Django Project

1. In a separate shell, activate the Django portal's virtual environment and then install interactwel-gui:

    ```bash
    cd ../airavata-django-portal
    source venv/bin/activate
    cd ../interactwel-gui
    python setup.py develop
    ```

2. Add interactwel_gui to INSTALLED_APPS. Edit settings_local.py and add:

    ```python
    INSTALLED_APPS = settings.INSTALLED_APPS + [
        'interactwel_gui'
    ]
    ```

3. Add interactwel_gui urls to the url config. Edit django_airavata/urls.py and add:

    ```python
        url(r'^interactwel/', include('interactwel_gui.urls')),
    ```


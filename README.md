# Messier Catalog

This project is a web application that displays the Messier Catalog and can be used to plan and log captured images.

The application includes a Vue.js frontend for displaying the objects and a Flask backend for serving data from an SQLite database.

## Table of Contents

- [Installation](#installation)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Database](#database)
- [Services](#services)
  - [Frontend Service](#frontend-service)
  - [Backend Service](#backend-service)
- [Operation](#operation)
  - [Code Update Procedure](#code-update-procedure)
  - [Testing and Bug Fixing](#testing-and-bug-fixing)
- [Deployment](#deployment)
  - [Automated Deployment](#automated-deployment)
- [Webhooks](#webhooks)

## Installation

### Frontend

1. Install npm packages:

    ```bash
    cd frontend
    npm install
    ```

2. Build the frontend:

    ```bash
    npm run build
    ```

3. Move the built files to the web root:

    ```bash
    sudo cp -r dist/* /var/www/hobunror/deepsky/
    ```

### Backend

1. Navigate to the backend directory:

    ```bash
    cd backend
    ```

2. Add environment variables:
    - Create and fill in `.env` keys using `example.env`:
    - Generate session key with this python code:
    ```python
    import os; 
    print(os.urandom(24).hex())
    ```
    - Generate salt with this python code:
    ```python
    import secrets
    # Generate a secure random string of 32 characters
    security_password_salt = secrets.token_urlsafe(32)
    print(security_password_salt)
    ```

      ```bash
      cp example.env .env
      ```

      - OpenWeatherMap api and app keys (<https://openweathermap.org/api>)
      - SESSION_KEY: Create Web session key with `python -c 'import os; print(os.urandom(24).hex())'`

3. Activate virtual environment for Python (venv):
    - Create a new virtual environment:

      ```bash
      python3 -m venv venv
      ```

    - Activate the new environment:

      ```bash
      source venv/bin/activate
      ```

    - Install dependencies:

      ```bash
      pip install -r requirements.txt
      ```

    - Update requirements after installing new packages
      `pipreqs`

4. Deactivate the current environment:

    ```bash
    deactivate
    ```

### Database

1. Run `sqlite3 AstroCaps.db` to create a new database file named `AstroCaps.db` or to start interacting with it:

    ```bash
    sqlite3 AstroCaps.db
    ```

    Example SQL commands:

    ```sql
    .tables
    SELECT * FROM MessierObjects LIMIT 10;
    ```

## Services

### Frontend Service

1. Serve the Vue application:

    ```bash
    cd frontend
    npm run serve
    ```

### Backend Service

1. Create the service file for the Flask application:

    ```bash
    sudo nano /etc/systemd/system/deepsky.service
    ```

    Add the following content:

    ```ini
    [Unit]
    Description=Messier Catalog Flask Service
    After=network.target

    [Service]
    Type=simple
    User=robert
    WorkingDirectory=/var/www/hobunror/deepsky/backend
    ExecStart=/var/www/hobunror/deepsky/backend/venv/bin/gunicorn --workers 3 --bind unix:/var/www/hobunror/deepsky/backend/deepsky.sock -m 007 wsgi:app
    Restart=always
    RestartSec=5
    StandardOutput=journal
    StandardError=inherit

    [Install]
    WantedBy=multi-user.target
    ```

2. Reload systemd, enable, and start the service:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable deepsky
    sudo systemctl start deepsky
    ```

## Operation

### Code Update Procedure

On RPi:

1. Commit and push changes:

    ```bash
    git commit -a -m "Update settings"
    git push
    ```

On development laptop:
2. Update and test code, then commit and push:
    ```bash
    git commit -a -m "Code update"
    git push
    ```

On RPi:
3. Pull the latest changes and restart services:
    ```bash
    git pull
    sudo systemctl restart deepsky
    sudo systemctl restart control
    ```

### Testing and Bug Fixing

#### On Development Laptop

- Use the script to generate serial data:

  ```bash
  python3 serial_test_data.py
  ```

#### On RPi (remote session)

1. Activate the virtual environment:

    ```bash
    source ~/github/skymonitor/venv/bin/activate
    ```

2. Check log files using `cat`:

    ```bash
    cat control.log
    cat app.log
    cat fetch_data.log
    cat store_data.log
    cat database_operations.log
    cat rain.log
    ```

3. Check journal logs:

    ```bash
    sudo journalctl -u control.service
    sudo journalctl -u app.service
    ```

## Deployment

### Automated Deployment

The deployment is automated using GitHub Actions.

1. Create a workflow file in your GitHub repository:

    ```yaml
    name: Deploy to Digital Ocean

    on:
      push:
        branches:
          - main

    jobs:
      deploy:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout code
            uses: actions/checkout@v2

          - name: Set up SSH
            uses: webfactory/ssh-agent@v0.5.3
            with:
              ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}

          - name: Copy files via SCP
            run: |
              scp -r * user@your_server_ip:/var/www/hobunror/deepsky

          - name: Restart Gunicorn
            run: |
              ssh user@your_server_ip 'sudo systemctl restart deepsky'
    ```

2. Ensure your GitHub repository is configured with the appropriate secrets for SSH.

## Webhooks

1. Create a webhook service file:

    ```bash
    sudo nano /etc/systemd/system/github-webhook.service
    ```

    Add the following content:

    ```ini
    [Unit]
    Description=GitHub Webhook Receiver

    [Service]
    ExecStart=/usr/bin/python3 /home/robert/github/deepsky/backend/webhook.py
    Restart=always
    User=robert
    Environment=PYTHONUNBUFFERED=1

    [Install]
    WantedBy=multi-user.target
    ```

2. Reload systemd, start, and enable the webhook service:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start github-webhook.service
    sudo systemctl enable github-webhook.service
    ```

3. Create a deployment script `deploy.sh`:

    ```bash
    nano ~/github/deepsky/deploy.sh
    ```

    Add the following content:

    ```bash
    #!/bin/bash

    # Log the execution
    echo "Deployment script executed at $(date)" >> /var/log/deploy.log

    # Stop script on error
    set -e

    # Navigate to the project directory
    cd ~/github/deepsky

    # Pull the latest changes from the repository
    git pull origin main

    # Navigate to the frontend directory
    cd frontend

    # Remove old build files
    rm -rf dist

    # Install dependencies
    npm install

    # Build the project
    npm run build

    # Move the new build to the web root
    sudo cp -r dist/* /var/www/hobunror/deepsky/

    # Navigate to the backend directory
    cd ../backend

    # Activate the virtual environment
    source venv/bin/activate

    # Install backend dependencies
    pip install -r requirements.txt

    # Apply database migrations if needed
    flask db upgrade

    # Restart the backend server
    sudo systemctl restart deepsky

    # Restart Apache to apply changes
    sudo systemctl restart apache2

    # Log the completion
    echo "Deployment completed at $(date)" >> /var/log/deploy.log
    ```

4. Make the deployment script executable:

    ```bash
    chmod +x ~/github/deepsky/deploy.sh
    ```

5. Set up the webhook in your GitHub repository:
    - **Payload URL**: `http://your-server-ip:5001/webhook`
    - **Content type**: `application/json`
    - **Secret**: Leave blank unless you want to add additional security.
    - **Which events would you like to trigger this webhook?**: Select "Just the push event".
    - Click "Add webhook".

By following these steps, you will have a fully functional web application displaying the Messier Catalog with automated deployment triggered by GitHub webhooks.
```

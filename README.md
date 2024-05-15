# messier-catalog

# Installation
## Install npm packages
`npm install`
## Add .env variables
Create and fill in .env keys using example.env for:
- SESSION_KEY: Create Web session key:
  `python -c 'import os; print(os.urandom(24).hex())'`
## Activate virtual env for Python (venv)
- Create a new virtual environment
`python3 -m venv venv`
- Activate the new environment
`source venv/bin/activate`
- Install pip
`wget https://bootstrap.pypa.io/get-pip.py`
`python get-pip.py `
- Reinstall all your packages
`pip install -r requirements.txt`
- Update requirements after installing new packages
`pipreqs`
- Deactivate the current environment
`deactivate`
- Remove the current virtual environment folder
`rm -r venv`

## Interact with database
`sqlite3 AstroCaps.db`
`.tables`
`SELECT * FROM MessierObjects LIMIT 10;`

## Define services
Vue server:
`cd astro-caps-frontend`
`npm run serve`
or create a production build:
`npm run build`

Flask server:
- app.py - runs flask website
- control.py - 

Create:
1. Create service: `sudo nano /etc/systemd/system/app.service`
2. Reload systemd: `sudo systemctl daemon-reload`
3. Enable the service: `sudo systemctl enable app.service`
4. Start the service: `sudo systemctl start app.service`
5. Check status: `sudo systemctl status app.service`

```
[Unit]
Description=Skymonitor Control Service
After=network.target
[Service]
Type=simple
User=robert
WorkingDirectory=/home/user/skymonitor
ExecStart=/home/user/skymonitor/venv/bin/python /home/user/skymonitor/control.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=inherit
[Install]
WantedBy=multi-user.target
```
# Operation
## Code update procedure
On RPi:
1. `git commit -a` & `git push` "settings.json" from RPi

On development laptop:
2. Update and test code
3. `git commit -a` & `git push` the updates 

On RPi:
4. `git pull `
5. `sudo systemctl restart app`
6. `sudo systemctl restart control`
## Testing and bug fixing
### On development laptop: 
- Use `python3 serial_test_data.py` to generate serial data and follow port setting instruction
### On RPi (remote session):
Activate venv with 
- `source ~/github/skymonitor/venv/bin/activate`

Configure Geany to Use the Virtual Environment’s Interpreter:
- Open Geany, Navigate to Build → Set Build Commands
- Under the Execute commands, you need to modify the command line to use the Python interpreter from your virtual environment.
Replace the default Python command (usually something like python "%f") with the path to the Python interpreter in your virtual environment:
`~/github/skymonitor/venv/bin/python "%f"`

Check log files using `cat control.log` in ~\github\skymonitor
- control.log 
- app.log 
- fetch_data.log 
- store_data.log
- database_operations.log
- rain.log

check journal:
- sudo journalctl -u control.service
- sudo journalctl -u app.service 

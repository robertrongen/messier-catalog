# webhook.py
from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Trigger the deployment script
        subprocess.call(['bash', '~/github/deepsky/deploy.sh'])
        return 'Webhook received and deployment script triggered', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

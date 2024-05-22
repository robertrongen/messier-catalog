# webhook.py
from flask import Flask, request
import os
import subprocess
import hmac
import hashlib
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv(dotenv_path='/home/robert/github/deepsky/backend/.env')
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')

def verify_signature(request):
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        abort(400, 'Signature header missing')

    sha_name, signature = signature.split('=')
    if sha_name != 'sha256':
        abort(400, 'Invalid signature format')

    mac = hmac.new(WEBHOOK_SECRET.encode(), msg=request.data, digestmod=hashlib.sha256)
    if not hmac.compare_digest(mac.hexdigest(), signature):
        abort(400, 'Invalid signature')

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        verify_signature(request)

        payload = request.get_json()
        commits = payload.get('commits', [])
        skip_build = any('[skip ci]' in commit.get('message', '').lower() for commit in commits)

        if skip_build:
            return 'Build skipped due to commit message', 200

        # Trigger the deployment script
        subprocess.call(['bash', '~/github/deepsky/deploy.sh'])
        return 'Webhook received and deployment script triggered', 200
    else:
        abort(405)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

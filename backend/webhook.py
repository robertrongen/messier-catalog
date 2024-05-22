# webhook.py
from flask import Flask, request
import os
import subprocess
import hmac
import hashlib
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Verify the request signature
        signature = request.headers.get('X-Hub-Signature-256')
        if not signature:
            abort(400, 'Signature header missing')

        sha_name, signature = signature.split('=')
        if sha_name != 'sha256':
            abort(400, 'Invalid signature format')

        mac = hmac.new(WEBHOOK_SECRET.encode(), msg=request.data, digestmod=hashlib.sha256)
        if not hmac.compare_digest(mac.hexdigest(), signature):
            abort(400, 'Invalid signature')

        # Trigger the deployment script
        subprocess.call(['bash', '~/github/deepsky/deploy.sh'])
        return 'Webhook received and deployment script triggered', 200
    else:
        abort(405)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

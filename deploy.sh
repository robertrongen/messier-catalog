#!/bin/bash

# Stop script on error
set -e

# Source NVM to add Node.js and npm to PATH
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Navigate to the project directory
cd /home/robert/github/deepsky

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
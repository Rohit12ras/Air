#!/bin/bash

# Corporate Travel Platform - Setup Script
# This script sets up the development environment

set -e  # Exit on error

echo "=========================================="
echo "Corporate Travel Platform - Setup"
echo "=========================================="
echo ""

# Check prerequisites
echo "Checking prerequisites..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 20+ from https://nodejs.org/"
    exit 1
fi
echo "✅ Node.js $(node --version) found"

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm"
    exit 1
fi
echo "✅ npm $(npm --version) found"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.11+"
    exit 1
fi
echo "✅ Python $(python3 --version) found"

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker not found. Docker is recommended but optional."
else
    echo "✅ Docker $(docker --version) found"
fi

echo ""
echo "=========================================="
echo "Setting up project directories..."
echo "=========================================="

# Create necessary directories
mkdir -p src/frontend/src
mkdir -p src/backend/src
mkdir -p src/mobile/src
mkdir -p src/ai-services/app
mkdir -p models
mkdir -p logs
mkdir -p uploads

echo "✅ Directories created"

echo ""
echo "=========================================="
echo "Installing dependencies..."
echo "=========================================="

# Install root dependencies
echo "Installing root dependencies..."
npm install

# Frontend setup
echo ""
echo "Setting up frontend..."
cd src/frontend
if [ ! -f "package.json" ]; then
    echo "Creating frontend package.json..."
    npx create-react-app . --template typescript || echo "Using existing React setup"
fi
npm install
cd ../..

# Backend setup
echo ""
echo "Setting up backend..."
cd src/backend
if [ ! -f "package.json" ]; then
    cat > package.json << 'EOF'
{
  "name": "corporate-travel-backend",
  "version": "1.0.0",
  "description": "Backend API for Corporate Travel Platform",
  "main": "src/index.ts",
  "scripts": {
    "dev": "ts-node-dev --respawn --transpile-only src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "jest"
  },
  "dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.0",
    "redis": "^4.6.0",
    "jsonwebtoken": "^9.0.2",
    "bcrypt": "^5.1.1",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "helmet": "^7.1.0",
    "morgan": "^1.10.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.0",
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.3.0"
  }
}
EOF
fi
npm install
cd ../..

# AI Services setup
echo ""
echo "Setting up AI services..."
cd src/ai-services
if [ ! -f "requirements.txt" ]; then
    cat > requirements.txt << 'EOF'
fastapi==0.104.1
uvicorn[standard]==0.24.0
openai==1.3.0
python-multipart==0.0.6
python-dotenv==1.0.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
redis==5.0.1
pydantic==2.5.0
pytesseract==0.3.10
Pillow==10.1.0
pandas==2.1.3
numpy==1.26.2
tensorflow==2.15.0
scikit-learn==1.3.2
EOF
fi
python3 -m pip install -r requirements.txt
cd ../..

echo ""
echo "=========================================="
echo "Creating environment files..."
echo "=========================================="

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    cat > .env << 'EOF'
# Database
DATABASE_URL=postgresql://admin:changeme@localhost:5432/corporate_travel
REDIS_URL=redis://localhost:6379

# API Keys
OPENAI_API_KEY=your-openai-api-key-here
GOOGLE_MAPS_API_KEY=your-google-maps-key-here

# Authentication
JWT_SECRET=your-jwt-secret-change-in-production
JWT_EXPIRY=7d

# Environment
NODE_ENV=development
PORT=8000

# Frontend
REACT_APP_API_URL=http://localhost:8000
REACT_APP_AI_URL=http://localhost:8001
EOF
    echo "✅ .env file created (please update with your API keys)"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Update .env file with your API keys:"
echo "   - OPENAI_API_KEY (get from https://platform.openai.com/)"
echo "   - GOOGLE_MAPS_API_KEY (get from https://console.cloud.google.com/)"
echo ""
echo "2. Start the development environment:"
echo "   Option A (Docker - Recommended):"
echo "     docker-compose up -d"
echo ""
echo "   Option B (Manual):"
echo "     npm run dev:backend    # Terminal 1"
echo "     npm run dev:ai         # Terminal 2"
echo "     npm run dev:frontend   # Terminal 3"
echo ""
echo "3. Access the application:"
echo "   - Frontend:  http://localhost:3000"
echo "   - Backend:   http://localhost:8000"
echo "   - AI API:    http://localhost:8001"
echo ""
echo "4. Read the documentation:"
echo "   - README.md"
echo "   - CORPORATE_TRAVEL_PLAN.md"
echo "   - PROJECT_STRUCTURE.md"
echo ""
echo "Happy coding! 🚀"

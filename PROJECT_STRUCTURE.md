# Corporate Travel Platform - Project Structure

```
air-project/
├── README.md                          # Project overview and getting started
├── SUMMARY.md                         # LinkedIn article analysis
├── CORPORATE_TRAVEL_PLAN.md          # Detailed project plan
│
├── src/                              # Source code
│   ├── frontend/                     # Web application
│   │   ├── components/              # React components
│   │   ├── pages/                   # Page components
│   │   ├── hooks/                   # Custom React hooks
│   │   ├── services/                # API services
│   │   ├── store/                   # Redux store
│   │   └── utils/                   # Utility functions
│   │
│   ├── backend/                      # API server
│   │   ├── controllers/             # Request handlers
│   │   ├── models/                  # Data models
│   │   ├── routes/                  # API routes
│   │   ├── middleware/              # Express middleware
│   │   ├── services/                # Business logic
│   │   └── utils/                   # Helper functions
│   │
│   ├── mobile/                       # React Native app
│   │   ├── screens/                 # Mobile screens
│   │   ├── components/              # Mobile components
│   │   ├── navigation/              # Navigation config
│   │   └── services/                # API integration
│   │
│   └── ai-services/                  # AI/ML services
│       ├── assistant/               # AI travel assistant (AVA)
│       ├── expense-ocr/             # Receipt OCR
│       ├── analytics/               # Predictive analytics
│       ├── policy-engine/           # Smart policy enforcement
│       └── models/                  # ML model files
│
├── docs/                             # Documentation
│   ├── architecture/                # System architecture
│   │   ├── system-design.md
│   │   ├── database-schema.md
│   │   ├── api-design.md
│   │   └── security.md
│   │
│   ├── api/                         # API documentation
│   │   ├── travel-api.md
│   │   ├── expense-api.md
│   │   └── payments-api.md
│   │
│   └── user-guides/                 # User documentation
│       ├── employee-guide.md
│       ├── admin-guide.md
│       └── finance-guide.md
│
├── tests/                            # Testing
│   ├── unit/                        # Unit tests
│   ├── integration/                 # Integration tests
│   └── e2e/                         # End-to-end tests
│
├── config/                           # Configuration files
│   ├── development.json
│   ├── staging.json
│   └── production.json
│
├── scripts/                          # Utility scripts
│   ├── setup.sh                     # Initial setup
│   ├── deploy.sh                    # Deployment
│   └── seed-data.js                 # Sample data
│
├── docker/                           # Docker configuration
│   ├── Dockerfile.frontend
│   ├── Dockerfile.backend
│   ├── Dockerfile.ai
│   └── docker-compose.yml
│
└── infrastructure/                   # Infrastructure as Code
    ├── terraform/                    # Terraform configs
    ├── kubernetes/                   # K8s manifests
    └── ci-cd/                        # CI/CD pipelines
```

## Quick Start

```bash
# Clone or navigate to project
cd /Users/I325666/Downloads/personal/air-project

# Install dependencies (after setup)
npm install

# Start development servers
npm run dev:frontend    # Frontend on http://localhost:3000
npm run dev:backend     # Backend on http://localhost:8000
npm run dev:ai          # AI services on http://localhost:8001

# Run tests
npm test

# Build for production
npm run build

# Deploy
npm run deploy
```

## Key Technologies

### Frontend Stack
- React 18 + TypeScript
- Redux Toolkit for state management
- Material-UI for components
- React Query for data fetching
- Axios for API calls

### Backend Stack
- Node.js 20 + Express
- PostgreSQL for database
- Redis for caching
- JWT for authentication
- Elasticsearch for search

### AI/ML Stack
- Python 3.11 + FastAPI
- OpenAI GPT-4 for assistant
- TensorFlow for ML models
- Tesseract OCR for receipts
- Pandas for data analysis

### DevOps
- Docker + Docker Compose
- Kubernetes for orchestration
- GitHub Actions for CI/CD
- AWS/GCP for cloud hosting
- Terraform for infrastructure

## Development Workflow

1. **Feature Branch**: Create from `main`
2. **Development**: Write code + tests
3. **Pull Request**: Code review required
4. **CI Pipeline**: Automated tests + linting
5. **Staging Deploy**: Test in staging environment
6. **Production Deploy**: After approval

## Environment Variables

```env
# Backend
DATABASE_URL=postgresql://user:pass@localhost:5432/corporate_travel
REDIS_URL=redis://localhost:6379
JWT_SECRET=your-secret-key
OPENAI_API_KEY=sk-...

# Frontend
REACT_APP_API_URL=http://localhost:8000
REACT_APP_GOOGLE_MAPS_KEY=...

# AI Services
OPENAI_API_KEY=sk-...
OCR_ENGINE=tesseract
MODEL_PATH=/models
```

## Getting Help

- **Documentation**: See `/docs` folder
- **API Reference**: http://localhost:8000/api-docs
- **Issue Tracker**: Create issues in project repo
- **Team Chat**: #corporate-travel-dev

---

**Last Updated**: 2026-02-26
**Maintained By**: Development Team

# Corporate Travel Platform

**An AI-powered corporate travel and expense management system inspired by Navan**

## 🚀 Quick Start

```bash
# Navigate to project
cd /Users/I325666/Downloads/personal/air-project

# Install dependencies
npm install

# Start with Docker (Recommended)
docker-compose up -d

# Or start services individually
npm run dev:backend    # API server on http://localhost:8000
npm run dev:ai         # AI services on http://localhost:8001
npm run dev:frontend   # Web app on http://localhost:3000
```

## 📋 What This Project Does

This platform combines three core capabilities with sustainability at its heart:

1. **Travel Booking** - Book flights, hotels, and car rentals with AI recommendations
2. **Expense Management** - Automated expense tracking with receipt OCR
3. **Payment Solutions** - Corporate cards and expense reimbursements
4. **🌱 Sustainability** - CO2 tracking, carbon offsets, and green travel optimization

### Key Features

- ⚡ **7-minute booking** (vs 45-minute industry average)
- 🤖 **50% AI automation** of support interactions
- 💰 **15-25% cost savings** through AI optimization
- 🌱 **20-35% carbon reduction** with smart routing
- 🎁 **Green rewards** for eco-friendly choices
- 📊 **Real-time visibility** into spending & emissions
- 🧠 **AI suggestions** for cheaper & greener alternatives

## 🏗️ Project Structure

```
air-project/
├── src/
│   ├── frontend/      # React web application
│   ├── backend/       # Node.js API server
│   ├── mobile/        # React Native mobile app
│   └── ai-services/   # Python AI/ML services
├── docs/              # Documentation
├── tests/             # Testing suites
└── docker/            # Docker configuration
```

See [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) for detailed structure.

## 📚 Documentation

- 🎯 [Project Overview](./PROJECT_OVERVIEW.md) - **START HERE** - Visual summary
- 📋 [Corporate Travel Plan](./CORPORATE_TRAVEL_PLAN.md) - Complete 18-month roadmap
- 🌱 [Sustainability Features](./SUSTAINABILITY_FEATURES.md) - **NEW** CO2 tracking & AI optimization
- 🏗️ [Project Structure](./PROJECT_STRUCTURE.md) - Technical architecture
- 📊 [Navan Analysis](./SUMMARY.md) - LinkedIn article insights

## 🛠️ Technology Stack

### Frontend
- React 18 + TypeScript
- Redux Toolkit
- Material-UI
- React Query

### Backend
- Node.js + Express
- PostgreSQL + Redis
- Elasticsearch
- JWT Authentication

### AI/ML
- Python + FastAPI
- OpenAI GPT-4
- TensorFlow
- Tesseract OCR

### Infrastructure
- Docker + Kubernetes
- AWS/GCP
- GitHub Actions CI/CD

## 🎯 Development Roadmap

### Phase 1: MVP (Months 1-4)
- [x] Project structure created
- [x] CO2 calculation engine built
- [x] AI optimization engine built
- [ ] Basic travel search and booking
- [ ] Simple expense management
- [ ] User authentication
- [ ] Admin dashboard
- [ ] CO2 display in search results

### Phase 2: Core Features (Months 5-8)
- [ ] AI-powered cost recommendations
- [ ] Train vs flight suggestions
- [ ] Carbon offset program
- [ ] Green discount tiers
- [ ] Receipt OCR
- [ ] Policy engine
- [ ] ERP integrations
- [ ] Mobile apps

### Phase 3: AI Enhancement (Months 9-12)
- [ ] AI travel assistant (AVA-like)
- [ ] Multi-city route optimization
- [ ] Predictive pricing
- [ ] Carbon gamification & badges
- [ ] Anomaly detection
- [ ] Advanced cost + carbon optimization

### Phase 4: Advanced Features (Months 13-18)
- [ ] Corporate card issuance
- [ ] Advanced reporting
- [ ] Duty of care features
- [ ] Group travel booking

## 🧪 Testing

```bash
# Run all tests
npm test

# Unit tests
npm run test:unit

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e
```

## 🚢 Deployment

```bash
# Build for production
npm run build

# Deploy to staging
npm run deploy:staging

# Deploy to production
npm run deploy:production
```

## 📊 Target Metrics

### Business Goals
- **Booking Time**: <10 minutes average
- **Cost Savings**: 15%+ for customers
- **Customer Satisfaction**: 4.7+ / 5.0
- **Gross Margin**: 70%+ (Year 3)

### Technical Goals
- **API Response**: <200ms (p95)
- **Uptime**: 99.9%
- **AI Automation**: 50%+ support tickets
- **Mobile Rating**: 4.5+ stars

## 🔐 Security

- SOC 2 Type II compliance
- PCI-DSS for payment processing
- End-to-end encryption
- Regular security audits
- GDPR/CCPA compliant

## 🤝 Contributing

1. Create feature branch from `main`
2. Write code + tests
3. Submit pull request
4. Pass CI/CD checks
5. Get code review approval

## 📄 License

MIT License - See LICENSE file for details

## 📞 Support

- **Documentation**: See `/docs` folder
- **API Docs**: http://localhost:8000/api-docs
- **Issues**: Create GitHub issues
- **Email**: support@corporate-travel.com

## 🌟 Inspiration

This project is inspired by [Navan](https://www.navan.com), which successfully transformed from a traditional travel platform to an AI-native enterprise SaaS company, achieving:
- 62% → 73% gross margin improvement
- 7-minute average booking time
- 50%+ AI-powered support automation

Read the full analysis in [SUMMARY.md](./SUMMARY.md)

---

**Created**: 2026-02-26
**Status**: In Development
**Target MVP**: 2026-06-26

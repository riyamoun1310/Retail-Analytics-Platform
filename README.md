# AI-Powered Retail Analytics Platform

A comprehensive full-stack application for retail businesses to analyze sales data, predict trends, and generate AI-powered insights.

## 🚀 Features

### Backend (FastAPI)
- **Scalable API**: Built with FastAPI for high performance
- **Database Management**: PostgreSQL with SQLAlchemy ORM
- **Machine Learning**: Sales prediction using scikit-learn
- **GenAI Integration**: Natural language report generation with OpenAI
- **Real-time Analytics**: Comprehensive business intelligence

### Frontend (React + TypeScript)
- **Modern Dashboard**: Interactive analytics dashboard
- **Data Visualization**: Charts and graphs with Recharts
- **Responsive Design**: TailwindCSS for beautiful UI
- **Real-time Updates**: React Query for efficient data fetching

### Key Capabilities
- 📊 **Sales Analytics**: Comprehensive sales performance tracking
- 🔮 **Predictive Modeling**: AI-powered sales forecasting
- 📦 **Inventory Management**: Smart stock optimization
- 👥 **Customer Insights**: Detailed customer behavior analysis
- 🤖 **AI Reports**: Natural language business reports
- 📈 **Performance Metrics**: Real-time KPI monitoring

## 🛠️ Technology Stack

**Backend:**
- FastAPI (Python web framework)
- PostgreSQL (Database)
- SQLAlchemy (ORM)
- Scikit-learn (Machine Learning)
- OpenAI API (Natural Language Generation)
- Pandas & NumPy (Data processing)

**Frontend:**
- React 18 with TypeScript
- Vite (Build tool)
- TailwindCSS (Styling)
- React Query (Data fetching)
- React Router (Navigation)
- Recharts (Data visualization)
- Lucide React (Icons)

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- OpenAI API Key (optional, for AI features)

## 🚀 Quick Start

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file with your configuration:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/retail_analytics
   SECRET_KEY=your-secret-key-here
   OPENAI_API_KEY=your-openai-api-key-here
   ```

5. **Set up database:**
   ```bash
   # Create database
   createdb retail_analytics
   
   # Run migrations (tables will be created automatically)
   ```

6. **Start the backend server:**
   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Access the application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 📊 Database Schema

### Core Tables
- **Products**: Product catalog with inventory tracking
- **Customers**: Customer information and segmentation
- **Sales**: Transaction records with detailed metrics
- **Inventory**: Real-time stock levels by location
- **Sales Predictions**: ML model predictions and confidence scores

## 🤖 Machine Learning Features

### Sales Prediction Model
- **Algorithm**: Random Forest Regression
- **Features**: Historical sales, seasonality, product attributes, customer segments
- **Prediction Horizon**: 1-365 days ahead
- **Automatic Retraining**: Configurable intervals

### Feature Engineering
- Time-based features (day of week, month, quarter)
- Rolling averages (7-day, 30-day)
- Product category encoding
- Customer segment analysis

## 🔍 API Endpoints

### Products
- `GET /api/v1/products` - List products
- `POST /api/v1/products` - Create product
- `GET /api/v1/products/{id}` - Get product details
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product

### Sales
- `GET /api/v1/sales` - List sales
- `POST /api/v1/sales` - Record sale
- `GET /api/v1/sales/daily/summary` - Daily sales summary
- `GET /api/v1/sales/weekly/summary` - Weekly sales summary

### Analytics
- `GET /api/v1/analytics/sales-overview` - Sales analytics
- `GET /api/v1/analytics/inventory-status` - Inventory metrics
- `GET /api/v1/analytics/customer-insights` - Customer analytics

### Machine Learning
- `POST /api/v1/ml/predict-sales` - Sales prediction
- `POST /api/v1/ml/retrain-model` - Retrain ML model
- `GET /api/v1/ml/model-performance` - Model metrics

### AI Reports
- `POST /api/v1/reports/generate` - Generate AI report
- `POST /api/v1/reports/ask` - Ask business questions

## 🎯 Business Use Cases

1. **Sales Performance Analysis**
   - Track revenue trends and growth patterns
   - Identify top-performing products and categories
   - Monitor sales team performance

2. **Inventory Optimization**
   - Predict stock requirements
   - Identify slow-moving inventory
   - Automate reorder alerts

3. **Customer Intelligence**
   - Segment customers by behavior
   - Track customer lifetime value
   - Identify retention opportunities

4. **Demand Forecasting**
   - Predict future sales volumes
   - Plan seasonal inventory
   - Optimize pricing strategies

## 🔧 Configuration

### Environment Variables

**Backend (.env):**
```env
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/retail_analytics

# Security
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# AI Features
OPENAI_API_KEY=your-openai-api-key

# Environment
ENVIRONMENT=development
DEBUG=True

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:5173"]

# ML
MODEL_PATH=./models/
RETRAIN_INTERVAL_HOURS=24
```

**Frontend (.env):**
```env
VITE_API_BASE_URL=http://localhost:8000
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📈 Performance Optimization

### Backend
- Database indexing on frequently queried columns
- Async endpoints for I/O operations
- Connection pooling for database
- Caching for ML predictions

### Frontend
- Code splitting with React.lazy
- Memoization for expensive calculations
- Virtualization for large data sets
- Image optimization

## 🔒 Security Features

- JWT authentication
- Password hashing with bcrypt
- Input validation with Pydantic
- CORS configuration
- Rate limiting
- SQL injection prevention

## 📦 Deployment

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d
```

### Production Considerations
- Use production database (PostgreSQL)
- Configure reverse proxy (Nginx)
- Set up SSL certificates
- Enable logging and monitoring
- Configure backup strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**Database Connection Error:**
- Verify PostgreSQL is running
- Check database credentials in .env
- Ensure database exists

**Frontend Build Errors:**
- Clear node_modules and reinstall
- Check Node.js version compatibility
- Verify all dependencies are installed

**ML Model Training Fails:**
- Ensure sufficient data (minimum 50 samples)
- Check data quality and completeness
- Verify scikit-learn installation

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the API docs at `/docs`

---

Built with ❤️ for retail businesses looking to leverage AI for growth.

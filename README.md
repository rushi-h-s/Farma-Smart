# 🐛 Farma-Smart: AI-Powered Farm Management System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL%2FSQLite-336791)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/rushi-h-s/Farma-Smart)

**Farma-Smart** is a comprehensive **AI-powered farm management system** designed to help farmers optimize their operations, manage inventory, track sales, and make data-driven decisions. The application combines traditional database management with intelligent analytics to improve agricultural productivity.

---

## ✨ Key Features

- 🐾 **Employee Management** - Manage farm staff, roles, and salaries
- 📈 **Inventory Tracking** - Real-time stock management for crops, supplies, and equipment
- 💳 **Sales & Billing** - Generate invoices, track revenue, and manage transactions
- 🚶 **Supplier Management** - Maintain supplier contact and order information
- 🐎 **Livestock Management** - Track animal health, breeding, and productivity
- 🌟 **Crop Management** - Monitor crop rotation, yield, and growth stages
- 📄 **Financial Dashboard** - Analyze revenue, expenses, and profitability
- 🎉 **User-Friendly Interface** - Desktop application with intuitive design
- 🔐 **Secure Database** - Protected access to sensitive farm data

---

## 🏗️ Tech Stack

- **Backend:** Python 3.8+
- **Database:** PostgreSQL / SQLite
- **Frontend:** Desktop GUI (Tkinter/PyQt)
- **Architecture:** MVC (Model-View-Controller)
- **Additional Libraries:**
  - Flask/Django (optional for web interface)
  - SQLAlchemy (ORM)
  - Pandas (data analysis)
  - Matplotlib/Seaborn (visualization)

---

## 📁 Project Structure

```
Farma-Smart/
├── Admin.py                # Administrator dashboard
├── AdminPage.py            # Admin interface components
├── AdminPages.py           # Additional admin pages
├── BackgroundPage.py       # Background services
├── Billing.py              # Billing module
├── Billing1.py             # Extended billing features
├── Cart.py                 # Shopping cart functionality
├── ContactUs.py            # Customer contact form
├── Empdash.py              # Employee dashboard
├── Login.py                # User authentication
├── main.py                 # Main application entry point
├── Return.py               # Return/refund management
├── SetImage.py             # Image configuration
├── Supplier.py             # Supplier management module
├── UpdateEmp.py            # Employee update functionality
├── UpdateStock.py          # Inventory update system
├── UpdateSup.py            # Supplier update system
├── Stock.py                # Stock management
├── Sales.py                # Sales tracking
├── bills/                  # Generated invoices and bills
├── connector/              # Database connection modules
├── pharmacyStore/          # Store management (optional pharmacy module)
├── Image/                  # Product and UI images
├── C/                      # Configuration files
├── .DS_Store               # macOS system files
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

### Core Modules:

| Module | Purpose |
|--------|----------|
| `Login.py` | User authentication and access control |
| `Admin.py` | Administrative operations and reporting |
| `Empdash.py` | Employee interface and dashboard |
| `Billing.py` | Invoice generation and payment processing |
| `Stock.py` | Inventory management and tracking |
| `Sales.py` | Sales records and revenue tracking |
| `Supplier.py` | Supplier relationship management |
| `Cart.py` | Shopping cart for purchases |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- PostgreSQL or SQLite
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rushi-h-s/Farma-Smart.git
   cd Farma-Smart
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
   - Edit database connection strings in `connector/` modules
   - Create database: `createdb farma_smart` (PostgreSQL)
   - Run migrations if available

5. **Run the application:**
   ```bash
   python main.py
   ```

The application will launch with a login screen.

---

## 👤 User Roles

### Admin
- Full system access
- User management
- Financial reporting
- System configuration
- Inventory oversight

### Employee
- Dashboard access
- Inventory updates
- Sales recording
- Personal profile management

### Supplier
- Order tracking
- Delivery management
- Invoice viewing

---

## 📊 Key Functionality

### Employee Management
- Add/update/delete employees
- Track salary and payments
- Assign roles and responsibilities
- Monitor attendance

### Inventory Control
- Add new products
- Update stock levels
- Track expiry dates
- Generate low-stock alerts
- Categorize products

### Sales & Billing
- Create invoices
- Process payments
- Generate receipts
- Track sales trends
- Return management

### Financial Dashboard
- Revenue analysis
- Expense tracking
- Profit/loss reports
- Quarterly summaries

---

## 🔐 Database Schema

Key tables include:
- `users` - User accounts and authentication
- `employees` - Staff information
- `products` - Farm produce and supplies
- `inventory` - Stock levels and locations
- `sales` - Transaction records
- `suppliers` - Supplier details
- `bills` - Invoice data
- `payments` - Payment history

---

## 🛠️ Configuration

Edit the following files for configuration:

```python
# Database configuration (connector/config.py)
DATABASE_URL = "postgresql://user:password@localhost/farma_smart"
DB_TYPE = "postgresql"  # or "sqlite"

# Admin credentials (stored securely)
DEFAULT_ADMIN_USER = "admin"
DEFAULT_ADMIN_PASS = "change_me"  # Change on first login
```

---

## 🐛 Farm Management Features

### Crop Tracking
- Planting dates and schedules
- Growth stage monitoring
- Yield predictions
- Harvest scheduling

### Livestock Management
- Animal health records
- Breeding information
- Feed consumption tracking
- Productivity metrics

### Equipment Management
- Asset tracking
- Maintenance schedules
- Usage logs
- Depreciation tracking

---

## 👥 Contributors

- **Rushi Harshavardhan** - Lead Developer
- **Divesh Patil** - Co-Contributor

---

## 👋 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guide
- Write meaningful commit messages
- Test changes thoroughly
- Document new features

---

## 📄 Usage Examples

### Creating a New Product
```python
from models import Product

new_product = Product(
    name="Wheat",
    category="Crops",
    quantity=1000,
    price=50.00,
    supplier_id=1
)
db.session.add(new_product)
db.session.commit()
```

### Recording a Sale
```python
from models import Sale

sale = Sale(
    product_id=1,
    quantity=10,
    price=500.00,
    employee_id=1,
    date=datetime.now()
)
db.session.add(sale)
db.session.commit()
```

---

## 🛧️ Troubleshooting

### Database Connection Error
- Verify PostgreSQL is running
- Check connection credentials
- Ensure database exists

### Application Won't Start
- Verify Python version (3.8+)
- Check all dependencies installed: `pip install -r requirements.txt`
- Review error logs

### Login Issues
- Reset admin password via database
- Clear session cache
- Check user permissions in database

---

## 📁 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Rushi Harshavardhan**
- GitHub: [@rushi-h-s](https://github.com/rushi-h-s)
- Location: Dhule, Maharashtra, India
- Interests: AI/ML, Web Development, Agriculture Technology

---

## 🙋 Acknowledgments

- Flask/Django community
- SQLAlchemy ORM framework
- Data visualization libraries (Matplotlib, Seaborn)
- All contributors and testers

---

## 📄 Version History

- **v2.0** (Current) - Enhanced UI, database optimization
- **v1.5** - Added financial dashboard
- **v1.0** - Initial release with core features

---

## 📀 API Documentation

For detailed API documentation, see [API_DOCS.md](API_DOCS.md) (when available)

---

## 👎 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/rushi-h-s/Farma-Smart/issues)
- Email: Contact via GitHub
- Discuss in [Discussions](https://github.com/rushi-h-s/Farma-Smart/discussions)

---

**Last Updated:** January 11, 2026  
**Project Status:** Actively Maintained  
**Version:** 2.0.0

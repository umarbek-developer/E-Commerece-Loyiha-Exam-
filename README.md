# E-Commerce REST API

A fully-featured e-commerce backend built with **Django REST Framework** and **JWT authentication**. Covers user management, product catalog, shopping cart, orders, and payments — all accessible via a clean REST API.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6.0.5 + Django REST Framework 3.17.1 |
| Authentication | JWT via `djangorestframework-simplejwt` |
| Database | SQLite3 (development) |
| Image Processing | Pillow |
| Filtering | `django-filter` |
| Code Quality | Black, Flake8 |

---

## Features

- **User accounts** — registration, JWT login, profile & address management
- **Product catalog** — categories, products with images, discounts, stock tracking
- **Reviews & ratings** — per-product reviews with 1–5 star ratings and average aggregation
- **Wishlist** — save products for later (unique per user/product pair)
- **Shopping cart** — one cart per user, manage items and quantities
- **Orders** — create orders, track status (Pending → Processing → Shipped → Delivered / Cancelled)
- **Payments** — payment record per order with status tracking (Pending / Paid / Failed / Refunded)
- **Admin panel** — all models registered at `/admin/`

---

## Project Structure

```
E-Commerece-Loyiha-Exam-/
├── src/
│   ├── .env                    # Environment variables
│   ├── .env.example
│   └── backend/
│       ├── manage.py
│       ├── db.sqlite3
│       ├── config/             # Django settings, urls, wsgi, asgi
│       ├── api/
│       │   ├── urls.py         # All API route definitions
│       │   ├── views/          # ViewSets for each resource
│       │   └── serializers/    # DRF serializers
│       └── apps/
│           ├── users/          # Custom user model + addresses
│           ├── products/       # Categories, products, reviews, wishlists
│           ├── cart/           # Cart + cart items
│           ├── orders/         # Orders + order items
│           └── payments/       # Payments
└── requirements.txt
```

---

## Installation

**Prerequisites:** Python 3.8+

```bash
# 1. Clone the repository
git clone https://github.com/umarbek-developer/E-Commerece-Loyiha-Exam-.git
cd E-Commerece-Loyiha-Exam-

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cd src
cp .env.example .env
# Edit .env if needed (SECRET_KEY, ALLOWED_HOSTS, etc.)

# 5. Apply migrations
cd backend
python manage.py migrate

# 6. (Optional) Create a superuser for the admin panel
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

Server runs at `http://127.0.0.1:8000/`

---

## Environment Variables

| Variable | Example | Purpose |
|---|---|---|
| `SECRET_KEY` | `your-secret-key` | Django secret key |
| `DEBUG` | `True` | Debug mode (set `False` in production) |
| `ALLOWED_HOSTS` | `127.0.0.1,localhost` | Allowed hostnames |
| `CORS_ALLOWED_ORIGINS` | `http://localhost:3000` | Frontend origins for CORS |
| `CSRF_TRUSTED_ORIGINS` | `https://localhost:3000` | CSRF trusted origins |

---

## Authentication

All write endpoints require a valid **JWT Bearer token**. Public (read-only) endpoints are open without a token.

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","email":"john@example.com","password":"strongpass123","first_name":"John","last_name":"Doe"}'

# Obtain token
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"strongpass123"}'

# Use token in subsequent requests
curl http://127.0.0.1:8000/api/orders/ \
  -H "Authorization: Bearer <access_token>"

# Refresh token
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<refresh_token>"}'
```

**Token lifetimes:** Access = 10 days, Refresh = 30 days

---

## API Endpoints

### Auth
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/register/` | Public | Register new user |
| POST | `/api/token/` | Public | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Public | Refresh access token |

### Users & Addresses
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/users/` | Required | Current user profile |
| GET/PUT/DELETE | `/api/users/{id}/` | Required | User detail |
| GET/POST | `/api/addresses/` | Required | List / create addresses |
| GET/PUT/DELETE | `/api/addresses/{id}/` | Required | Address detail |

### Products & Catalog
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/categories/` | Public | List categories |
| POST | `/api/categories/` | Required | Create category |
| GET/PUT/DELETE | `/api/categories/{id}/` | Required | Category detail |
| GET | `/api/products/` | Public | List products (filterable) |
| POST | `/api/products/` | Admin | Create product |
| GET | `/api/products/{id}/` | Public | Product detail |
| PUT/DELETE | `/api/products/{id}/` | Admin | Update / delete product |

**Product query parameters:**

| Param | Type | Example | Description |
|---|---|---|---|
| `search` | string | `?search=shirt` | Search by name or description |
| `category` | int | `?category=2` | Filter by category ID |
| `min_price` | decimal | `?min_price=10.00` | Minimum price filter |
| `max_price` | decimal | `?max_price=100.00` | Maximum price filter |
| `min_rating` | int | `?min_rating=4` | Minimum average rating |
| `ordering` | string | `?ordering=price` | Sort by field (prefix `-` for desc) |

### Reviews & Wishlist
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET/POST | `/api/reviews/` | Required | List / create reviews |
| GET/PUT/DELETE | `/api/reviews/{id}/` | Required | Review detail |
| GET/POST | `/api/wishlists/` | Required | List / add to wishlist |
| GET/DELETE | `/api/wishlists/{id}/` | Required | Wishlist item detail |

### Cart
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET/POST | `/api/carts/` | Required | List / create cart |
| GET/PUT/DELETE | `/api/carts/{id}/` | Required | Cart detail |
| GET/POST | `/api/cart-items/` | Required | List / add cart items |
| GET/PUT/DELETE | `/api/cart-items/{id}/` | Required | Cart item detail |

### Orders
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET/POST | `/api/orders/` | Required | List / create orders |
| GET/PUT/DELETE | `/api/orders/{id}/` | Required | Order detail |
| GET/POST | `/api/order-items/` | Required | List / create order items |
| GET/PUT/DELETE | `/api/order-items/{id}/` | Required | Order item detail |

**Order statuses:** `PENDING` → `PROCESSING` → `SHIPPED` → `DELIVERED` / `CANCELLED`

### Payments
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET/POST | `/api/payments/` | Required | List / create payments |
| GET/PUT/DELETE | `/api/payments/{id}/` | Required | Payment detail |

**Payment statuses:** `PENDING` → `PAID` / `FAILED` / `REFUNDED`

---

## Data Models

```
User ──< Address
User ──< Review >── Product ──< Category
User ──< Wishlist >── Product
User ── Cart ──< CartItem >── Product
User ──< Order ──< OrderItem >── Product
             Order ── Payment
```

### Key model notes

- **Product** — stores `price` and `discount` (0–100%). `discounted_price` and `average_rating` are computed properties.
- **Cart** — one-to-one with User; `CartItem.quantity` minimum is 1.
- **OrderItem** — captures `price` at the time of order (snapshot), not live product price.
- **Payment** — one-to-one with Order; `amount` must be > 0.
- **Wishlist** — unique constraint on `(user, product)` prevents duplicates.

---

## Running Tests

```bash
cd src/backend
python manage.py test
```

---

## Admin Panel

Access the Django admin interface at `http://127.0.0.1:8000/admin/` using superuser credentials. All models (users, products, orders, payments, etc.) are registered and manageable from the admin.

---

## API Root

Visit `http://127.0.0.1:8000/api/` for a browsable list of all available endpoints (Django REST Framework browsable API).

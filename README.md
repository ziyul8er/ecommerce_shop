## **Project Overview**
This document provides a comprehensive guide to the e-commerce site built using **Next.js** for the front-end and **Django** for the back-end. The site allows users to browse products, add them to a cart, and complete purchases. It also includes admin functionality for managing products, orders, and user accounts.


---

## **Project Structure**

```
ecommerce-site/
├── api/                    # Django Ninja API app
├── core/                   # Django back-end
│   ├── manage.py           # Django management script
├── frontend/               # Next.js front-end
│   ├── components/         # Reusable components
│   ├── pages/              # Next.js pages
│   ├── styles/             # CSS or SCSS files
│   ├── public/             # Static assets
│   └── ...                 # Other Next.js files
├── items/                  # Store items app
│   │   ├── models/         # Database models
│   │   ├── views/          # API views
│   │   ├── urls/           # API views
│   │   └── ...            
│   └── ...
├── carts/                  # Carts app
├── users/                  # Users app
└── ...                     # Other project files
```

---

## **Technologies Used**

- **Front-End**: Next.js, React
- **Back-End**: Django, Django Ninja
- **Database**: SQLite
- **Authentication**: %% JWT (JSON Web Tokens) or Django Allauth %%
- **Deployment**: %% Vercel (for Next.js) and Heroku/AWS/DigitalOcean (for Django) %%
- **Version Control**: Git, GitHub

---

## **Front-End (Next.js)**
### Key Features
- **Product Listing**: Display products with pagination and filters.
- **Product Details**: Show detailed information about a product.
- **Shopping Cart**: Allow users to add/remove products and update quantities.
- **Checkout**: Handle payment processing (e.g., Stripe integration).
- **User Authentication**: Login, registration, and profile management.

### Pages

- `/` - Homepage with featured products.
- `/products` - Product listing page.
- `/products/[id]` - Product details page.
- `/cart` - Shopping cart page.
- `/checkout` - Checkout page.
- `/login` - User login page.
- `/register` - User registration page.
- `/profile` - User profile page.

### Components

- `Navbar` - Navigation bar with links to key pages.
- `ProductCard` - Reusable component for displaying product information.
- `CartItem` - Component for displaying items in the cart.
- `Footer` - Footer with links and contact information.

---

## **Back-End (Django)**
### Key Features
- **Product Management**: CRUD operations for products.
- **Order Management**: Handle order creation, updates, and status tracking.
- **User Management**: Handle user registration, login, and profile updates.
- **API Endpoints**: RESTful APIs for front-end integration.

### Models
- `User` - Custom user model (if needed).
- `Product` - Fields: `name`, `description`, `price`, `image`, `stock`, etc.
- `Order` - Fields: `user`, `total_price`, `status`, `created_at`, etc.
- `OrderItem` - Fields: `order`, `product`, `quantity`, `price`, etc.

### Views
- `ProductListView` - List all products.
- `ProductDetailView` - Retrieve a single product.
- `CartView` - Manage the shopping cart.
- `CheckoutView` - Handle the checkout process.
- `UserView` - Manage user profiles.

---

## **API Endpoints**
### Products
- `GET /api/products/` - List all products.
- `GET /api/products/{id}/` - Retrieve a single product.
- `POST /api/products/` - Create a new product (admin only).
- `PUT /api/products/{id}/` - Update a product (admin only).
- `DELETE /api/products/{id}/` - Delete a product (admin only).

### Cart
- `GET /api/cart/` - Retrieve the user's cart.
- `POST /api/cart/` - Add a product to the cart.
- `DELETE /api/cart/{id}/` - Remove a product from the cart.

### Orders
- `GET /api/orders/` - List all orders for the user.
- `POST /api/orders/` - Create a new order.

### Users
- `POST /api/register/` - Register a new user.
- `POST /api/login/` - Log in a user.
- `GET /api/profile/` - Retrieve the user's profile.
- `PUT /api/profile/` - Update the user's profile.

---

## **Database Schema**
```plaintext
User
- id
- username
- email
- password

Product
- id
- name
- description
- price
- image
- stock

Order
- id
- user (ForeignKey to User)
- total_price
- status
- created_at

OrderItem
- id
- order (ForeignKey to Order)
- product (ForeignKey to Product)
- quantity
- price
```

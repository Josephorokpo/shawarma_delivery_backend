## Shawarma Delivery Backend API

## Description
The Shawarma Delivery Backend API is a robust and scalable RESTful API service designed to manage the ordering and delivery of shawarma. Developed using Django and Django REST framework, this API provides comprehensive functionality for user authentication, order management, and admin operations. It serves as the backbone for a shawarma delivery service, ensuring efficient and seamless interactions between customers, delivery personnel, and administrators.

## Features

# User Authentication and Management

- Secure user registration and login using JWT tokens.
- Password reset and token refresh capabilities.

# Order Management

- Place new orders for shawarma.
- Retrieve and list all orders.
- Update and delete orders by their ID.
- Update the status of orders, restricted to admin users.
- List and retrieve orders specific to a user.

# Admin Functionality

- Admin access to manage and monitor all orders.
- Order status updates to manage the delivery process.

# API Documentation

- Comprehensive API documentation using Swagger UI for easy integration and testing.

# Security

- Secure endpoints with permissions for authenticated users and admins.
- JWT-based authentication for enhanced security.

## Routes to Implement

| METHOD |              ROUTE             |            FUNCTIONALITY        | ACCESS    |
|--------|--------------------------------|---------------------------------|-----------|
|                               User Authentication                                     | 
| POST   | /auth/signup/                  | Signup a new user               | All users |
| POST   | /auth/jwt/create/              | Login user                      | All users |
| POST   | /auth/jwt/refresh/             | Refresh the access token        | All users |
|                               Order Management                                        |
| POST   | /orders/                       | Place an order                  | All users |
| GET    | /orders/                       | Get all orders                  | All users |
| GET    | /orders/{order_id}/            | Retrieve an order               | Superuser |
| PUT    | /orders/{order_id}/            | Update an order                 | Superuser |
| PUT    | /orders/{order_id}/status/     | Update order status             | Superuser |
| DELETE | /orders/{order_id}/            | Delete an order                 | Superuser |
|                               User-Specific Orders                                    |
| GET    | /user/{user_id}/orders/        | Get user's Orders               | All users |
| GET    | /user/{user_id}/orders/{order_id}/ | Get a user's specific order | All users |
|                               API Documentation                                       |
| GET    | /docs/                         | View API documentation          | All users |

## Installation
1. Step 1
2. Step 2
3. Step 3

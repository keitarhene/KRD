# E-commerce platform 
# Plot 13 Restaurant E-Commerce Platform

Welcome to Plot 13 Restaurant E-Commerce Platform! This project aims to provide a seamless online ordering experience for our restaurant customers.

## Installation

1. Clone the repository: `git clone https://github.com/keitarhene/KRD.git`
2. Navigate to the project directory: `cd KRD`
3. Create and activate a virtual environment: `python3 -m venv venv` and `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4. the virtual environment `env` was created in the project file during project testing
5. Install dependencies: `pip install -r requirements.txt`
6. Set up the database: `python manage.py migrate`
7. Create a superuser account: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`

## Usage

1. Access the admin panel to manage restaurant products, orders, and customers: `http://127.0.0.1:8000/admin/`
2. Users can view the restaurant menu, add items to their cart, and place orders.
3. To process orders, admin staff can mark orders as 'completed' in the admin panel.

## Features

- Browse the restaurant menu and filter items by category.
- Add items to the cart, update quantities, and proceed to checkout.
- Secure user registration and login system.
- Responsive and user-friendly interface for both customers and staff.
- Customized admin panel for efficient order management.

## Apps and Models

- `menu`: Defines restaurant products and categories.
- `cart`: Manages user cart items and order processing.
- `accounts`: Handles user registration, login, and authentication.

## Custom Admin Classes

- Customized admin views for easy product and order management.

## Forms

- `AddToCartForm`: Allows users to add items to their cart.
- `CheckoutForm`: Collects user information for order processing.

## User Registration and Authentication

- Users can register with a valid email and password.
- User authentication is handled securely using Django's built-in authentication system.

## Custom Templating and Styling

- Custom HTML and CSS styling for an appealing and cohesive user experience.

## Data Validation and Error Handling

- Form validation ensures accurate and complete order information.
- User-friendly error messages guide users through any issues.

## Contributing

We welcome contributions from the community! Feel free to submit issues or pull requests.

## Credits

- This project utilizes Django, Bootstrap, and other open-source libraries.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact us at contact@plot13restaurant.com

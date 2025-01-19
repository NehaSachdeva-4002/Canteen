# 🥗 Canteen Management System

A web-based application designed to streamline the management of canteen operations, including inventory tracking, order management, and real-time updates. Built using Django, this project provides a user-friendly interface for canteen administrators and a seamless experience for users to place orders and view menu details.

## 🚀 Features

- **Inventory Management**: Add, update, and track item quantities in the canteen.
- **Order Management**: Place, view, and manage customer orders.
- **User Roles**: Admins can manage the menu, inventory, and user orders.
- **Dynamic Updates**: Real-time tracking of available items.
- **Merge Migration Handling**: Efficiently resolves migration conflicts for database changes.

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite (or any Django-supported database)
- **Frontend**: HTML, CSS, JavaScript (extendable to modern frameworks)

## 📸 Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/b190face-66ae-42a9-9811-26e7ed457e60)

### Admin Panel
![Admin Panel](https://github.com/user-attachments/assets/c9c40241-cc40-4979-944c-92e67a733399)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/canteen-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd canteen-management-system
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements or fixes.


# Chat App

## Overview

ChiChat is a real-time chat application built with Django Channels and WebSockets. This project provides a modern and responsive chat interface using Tailwind CSS for styling. The app also leverages Hyperscript and HTMX for enhanced interactivity, and features the Jazzmin Django admin panel for an improved admin experience.

## Features

- Real-Time Messaging: Utilize Django Channels and WebSockets for instant message delivery and real-time updates.
- Modern UI: Styled with Tailwind CSS for a clean and responsive design.
- Interactive Components: Enhanced frontend interactions with Hyperscript and HTMX.
- Admin Interface: Manage application data with the Jazzmin Django admin panel.

## Prerequisites

- Python 3.x
- Django
- Django Channels
- Tailwind CSS cdn
- daphne

## Installation

1. Clone the Repository:

   ~~~bash
   git clone https://github.com/AisDisappeared/chat.git
   ~~~

   ~~~bash
   cd chat
   ~~~

2. Create and Activate a Virtual Environment:

   ~~~bash
   python -m venv venv
   ~~~

   source venv/bin/activate  ---- On Windows use `venv\Scripts\activate`

3. Install Dependencies:

   ~~~bash
   pip install -r requirements.txt
   ~~~

4. Apply Migrations:

   ~~~bash
   python manage.py migrate
   ~~~

5. Run the Development Server:

   ~~~bash
   python manage.py runserver
   ~~~

6. Visit the App:

   Open your web browser and go to <http://127.0.0.1:8000> to view the chat application.

## Configuration

- Settings: Update the settings.py file for any necessary configuration changes, including Django Channels layers.

- Tailwind CSS: Tailwind is configured via cdn.

- HTMX and Hyperscript: Ensure proper inclusion in your HTML templates for interactive features.

## Usage

- Chat Interface: Use the chat interface to send and receive messages in real-time.
- Admin Panel: Access the Jazzmin admin panel at <http://127.0.0.1:8000/admin> to manage application data.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Aliseyfi0841@gmail.com](mailto:Aliseyfi0841@gmail.com).

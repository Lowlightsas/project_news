
News Project
Overview
This project is a News Platform built using the Django framework, designed to allow users to browse news articles and share them across different platforms. The platform includes the following key features:

User Authentication: Powered by Django's authentication framework, providing secure login and user management.
View Tracking: Tracks unique views per news article using Redis as the data storage for efficient and scalable user action tracking.
Responsive Design: Built with Bootstrap for a polished and mobile-friendly front-end.
Social Sharing: Generates shareable links using JavaScript for platforms like Telegram and WhatsApp, allowing users to share articles easily.
Features
1. User Authentication
User authentication is implemented using Django’s built-in authentication framework.
Authenticated and anonymous users are supported.
Secure session management ensures user data integrity.
2. View Tracking with Redis
Unique views are counted for each news article.
Redis is used as a fast and scalable data store to track unique users based on their IDs or session keys.
Prevents duplicate counting by ensuring each user contributes to the view count only once.
3. Responsive Front-End
The interface is styled using Bootstrap for a professional, responsive design.
News articles are presented in an organized layout, making navigation intuitive for users.
4. Social Sharing
Users can share news articles on Telegram, WhatsApp, and other platforms.
JavaScript dynamically generates links for sharing and enables link copying for convenience.
Includes styled buttons for a seamless sharing experience.
Technology Stack
Back-End
Django: Web framework for back-end logic and user authentication.
Redis: Used for tracking unique views efficiently.
Front-End
Bootstrap: Responsive design framework for styling and layout.
JavaScript: Handles dynamic interactions, including shareable link generation.
Database
  SQLite: Stores news data and user information.
  Redis: Tracks unique user views for each article.

![Снимок экрана 2024-11-26 080921](https://github.com/user-attachments/assets/1e658284-c837-477a-b5e6-bbb104a53eb5)
![Снимок экрана 2024-11-26 081101](https://github.com/user-attachments/assets/e8af8ff4-fd85-457d-a016-b49d1fc18e7c)
![Снимок экрана 2024-11-26 081133](https://github.com/user-attachments/assets/8f579d27-3512-4f8f-9a06-5d1075b02811)
![Снимок экрана 2024-11-26 081146](https://github.com/user-attachments/assets/14b7af18-bea0-4b5f-abca-5cf95374db44)
![Снимок экрана 2024-11-26 081200](https://github.com/user-attachments/assets/f904d5e3-f26f-4b0f-a5f2-d9cec5abc3c2)
![Снимок экрана 2024-11-26 081209](https://github.com/user-attachments/assets/74540c0b-4b04-477a-a41c-e1a86b84565f)
![Снимок экрана 2024-11-26 081222](https://github.com/user-attachments/assets/dc67b31b-b2dc-4e5a-bc30-908f3c07f2fb)






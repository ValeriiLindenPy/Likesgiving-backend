# Likesgiving Project API Documentation

<b> Likesgiving project is designed to capture the essence of your daily life, allowing you to celebrate the things that bring you joy and commiserate over the things that
frustrate you. Whether it's a new song that captivated your senses or an
annoying traffic jam that tested your patience, the project is your go-to destination for sharing these moments and connecting with others who resonate with your experiences.</b>

## Backend

This is backend part of likesgiving project.

## Authentication

### Create User
- **Endpoint:** `/auth/create/`
- **Method:** `POST`
- **Description:** Registers a new user.

### Login
- **Endpoint:** `/auth/login/`
- **Method:** `POST`
- **Description:** Logs in a user and provides an authentication token.

### Logout
- **Endpoint:** `/auth/logout/`
- **Method:** `POST`
- **Description:** Logs out a user and invalidates their authentication token.

### Show Profile Data
- **Endpoint:** `/auth/profile/`
- **Method:** `GET`
- **Description:** Retrieves the profile data of the authenticated user.

### Edit Profile
- **Endpoint:** `/auth/edit-profile/`
- **Method:** `PUT`
- **Description:** Allows the authenticated user to update their profile information.

### Change Password
- **Endpoint:** `/auth/change_password/`
- **Method:** `PUT`
- **Description:** Allows the authenticated user to change their password.

### Reset Password
- **Endpoint:** `/auth/password_reset/`
- **Method:** `POST`
- **Description:** Sends a password reset email to the provided email address.

### Confirm Password Reset
- **Endpoint:** `/auth/password_reset_confirm/`
- **Method:** `PUT`
- **Description:** Confirms password reset and updates the user's password.

## Posts

### Create Post
- **Endpoint:** `/posts/`
- **Method:** `POST`
- **Description:** Allows users to create new posts.

### Get Posts
- **Endpoint:** `/posts/`
- **Method:** `GET`
- **Description:** Retrieves a list of posts.

### Get Post
- **Endpoint:** `/posts/{post_id}/`
- **Method:** `GET`
- **Description:** Retrieves a specific post by ID.

### Update Post
- **Endpoint:** `/posts/{post_id}/`
- **Method:** `PUT`
- **Description:** Allows users to update their own posts.

### Delete Post
- **Endpoint:** `/posts/{post_id}/`
- **Method:** `DELETE`
- **Description:** Allows users to delete their own posts.

### Add Comment
- **Endpoint:** `/posts/add_comment/{post_id}/`
- **Method:** `POST`
- **Description:** Allows users to add comments to a post.

### Add Like
- **Endpoint:** `/posts/add-like/{post_id}/`
- **Method:** `PUT`
- **Description:** Allows users to like or unlike a post.

### Get Today's Statistics
- **Endpoint:** `/posts/get_statistics/`
- **Method:** `GET`
- **Description:** Retrieves statistics for today's posts, including the number of likes and dislikes, and the top post based on likes.

### Show All Post Comments
- **Endpoint:** `/posts/get_comments/{post_id}/`
- **Method:** `GET`
- **Description:** Retrieves all comments for a specific post.

### Remaining Posts Today
- **Endpoint:** `/posts/get_remaining_posts_today/`
- **Method:** `GET`
- **Description:** Retrieves the remaining number of posts a user can create today.

## Technologies Used

- Django
- Django REST Framework
- Knox Authentication
- AWS S3 for media storage
- Heroku hosting


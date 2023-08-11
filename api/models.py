from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class ProfileManager(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            **other_fields,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Spueruser must be stuff")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Spueruser must be True")

        return self.create_user(email, user_name, password, **other_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=200, unique=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = ProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    def __str__(self) -> str:
        return self.user_name


class Post(models.Model):
    POST_TYPE_CHOICES = [
        ("hate", "Hate"),
        ("love", "Love"),
    ]
    post_type = models.CharField(max_length=4, choices=POST_TYPE_CHOICES)
    text = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile, blank=True, related_name="liked_posts")
    comments = models.ManyToManyField(
        Profile, through="Comment", blank=True, related_name="commented_posts"
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Post by {self.author.user_name} - {self.pk}"

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments"
    )
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment to {self.post}"

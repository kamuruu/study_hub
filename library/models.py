from django.db import models

# Create your models here.
from django.db import models
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    # 1:N Relationship - A book has one author, an author has many books
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    # M:M Relationship - A book can have many genres, a genre has many books
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    # Unique ID for this specific physical copy
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 1:N Relationship - One book can have multiple physical copies
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    def __str__(self):
        return f"{self.id} ({self.book.title})"
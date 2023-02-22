from django.db import models


class Category(models.Model):
    CATEGORIES = {
    ('Other', 'Other'),
    ('Fashion', 'Fashion'),
    ('Beauty', 'Beauty'),
    ('Home & Garden', 'Home & Garden'),
    ('Toys & Game', 'Toys & Garden'),
    ('Sport & Outdoor', 'Sport & Outdoor'),
    ('Pet Supply', 'Pet Supply'),
    ('Books', 'Books'),
    ('Electronics', 'Electronics'),
    ('Car & Motorbike', 'Car & Motorbike')
    }

    name = models.CharField(max_length=50, choices=CATEGORIES, default='Other')
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name
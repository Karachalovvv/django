from django.db import models

" CREATE TABLE posts (id not null primary key autoincrement, title text, body text, rate int); "

"SELECT * FROM posts; --» Post.objects.all()"

"SELECT * FROM posts WHERE title ILIKE('%post%'); --» Post.objects.filter(title__icontains = 'post')"

"SELECT 1 FROM posts WHERE id; = 1 --» Post.objects.get(id = 1)"

"INSERT INTO posts (title, content, rate, category_id) VALUES('new post', 'new content', 0, 1); --> Post.objects.create(title = 'new post', content = 'new content', rate = 0, category_id = 1)"

class Category(models.Model):
    name = models.CharField(max_length = 256)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null = True, blank = True)
    title = models.CharField(max_length = 256)
    content = models.CharField(max_length = 456)
    rate = models.IntegerField(default = 0, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)


    def __str__(self):
        return f"{self.title} - {self.content}"
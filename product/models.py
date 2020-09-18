from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name
  

class Brand(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Product(models.Model):
  title = models.CharField(max_length=100)
  desc = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet quisquam, doloremque necessitatibus ullam temporibus quas quam corrupti ipsa maxime laboriosam laborum cum ducimus nam, distinctio facilis aliquam suscipit perferendis tempore quo labore! Doloremque perspiciatis sapiente veritatis est beatae magnam numquam accusamus, mollitia asperiores vitae fuga nostrum? Veniam molestias illo eveniet dolore corrupti quia facere magnam qui, provident quo pariatur eaque nobis cumque, quas nostrum accusantium, ipsum dignissimos quis doloribus in? Pariatur, eveniet. Eaque commodi aspernatur cumque illum culpa laborum fugiat, ab illo voluptatibus deserunt. Tenetur, alias ratione vitae asperiores officiis temporibus non autem deleniti rerum quae quis minus soluta dolore!')
  price = models.IntegerField()
  image = models.ImageField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None)

  def __str__(self):
      return self.title

# Generated by Django 3.0.7 on 2020-09-16 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet quisquam, doloremque necessitatibus ullam temporibus quas quam corrupti ipsa maxime laboriosam laborum cum ducimus nam, distinctio facilis aliquam suscipit perferendis tempore quo labore! Doloremque perspiciatis sapiente veritatis est beatae magnam numquam accusamus, mollitia asperiores vitae fuga nostrum? Veniam molestias illo eveniet dolore corrupti quia facere magnam qui, provident quo pariatur eaque nobis cumque, quas nostrum accusantium, ipsum dignissimos quis doloribus in? Pariatur, eveniet. Eaque commodi aspernatur cumque illum culpa laborum fugiat, ab illo voluptatibus deserunt. Tenetur, alias ratione vitae asperiores officiis temporibus non autem deleniti rerum quae quis minus soluta dolore!')),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.Brand')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
    ]
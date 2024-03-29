# Generated by Django 2.1.15 on 2024-02-07 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MediaStore',
            fields=[
                ('media_id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=20)),
                ('media_location', models.CharField(max_length=256)),
                ('upload_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_code', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.ItemCategory')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('menu_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.MenuItems')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField()),
                ('payment_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('order_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('payment_type', models.CharField(max_length=20)),
                ('payment_date', models.DateTimeField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('payment_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('restaurant_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comments', models.CharField(max_length=256)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Restaurants')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('adderss', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Users'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.PaymentStatus'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.OrderStatus'),
        ),
        migrations.AddField(
            model_name='orders',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Restaurants'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Users'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Orders'),
        ),
        migrations.AddField(
            model_name='menuitems',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Restaurants'),
        ),
        migrations.AddField(
            model_name='mediastore',
            name='menu_item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.MenuItems'),
        ),
        migrations.AddField(
            model_name='mediastore',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Restaurants'),
        ),
        migrations.AddField(
            model_name='itemcategory',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Restaurants'),
        ),
    ]

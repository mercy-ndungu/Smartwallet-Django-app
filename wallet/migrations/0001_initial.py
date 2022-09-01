# Generated by Django 4.0.6 on 2022-08-30 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=30)),
                ('balance', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('last_name', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('address', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('nationality', models.CharField(max_length=15, null=True)),
                ('id_number', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('proile_picture', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('marital_status', models.CharField(max_length=8, null=True)),
                ('employment_status', models.BooleanField(null=True)),
                ('signature', models.ImageField(default='default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=15)),
                ('transaction_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('status', models.CharField(max_length=6)),
                ('transaction_number', models.CharField(max_length=7)),
                ('date_time', models.DateTimeField()),
                ('transaction_description', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(null=True)),
                ('customer_id', models.IntegerField(null=True)),
                ('time', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=15, null=True)),
                ('history', models.DateTimeField(null=True)),
                ('pin', models.CharField(max_length=15, null=True)),
                ('active', models.BooleanField(null=True)),
                ('datecreated', models.DateTimeField(null=True)),
                ('type', models.CharField(max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Third_Party',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('id', models.CharField(max_length=8)),
                ('type', models.CharField(max_length=6)),
                ('transaction_account', models.IntegerField()),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Third_Party_account', serialize=False, to='wallet.account')),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=30)),
                ('transaction_type', models.CharField(max_length=30, null=True)),
                ('transaction_charge', models.IntegerField(null=True)),
                ('transaction_time', models.DateTimeField(null=True)),
                ('reciept', models.CharField(max_length=8, null=True)),
                ('destination_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='wallet.account')),
                ('origin_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_origin_account', to='wallet.account')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('customer_id', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('points', models.IntegerField()),
                ('date_of_reward', models.DateTimeField()),
                ('recipient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reward_recipient', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=15)),
                ('receipt_date', models.DateTimeField()),
                ('bill_number', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('receipt_file', models.FileField(upload_to='')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reciept_transaction', to='wallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.CharField(max_length=30)),
                ('card_name', models.CharField(max_length=30)),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(max_length=30)),
                ('expiry_date', models.DateTimeField()),
                ('card_status', models.CharField(max_length=30)),
                ('security_code', models.IntegerField()),
                ('issuer', models.CharField(max_length=30)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='wallet.account')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Card_wallet', to='wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.BigIntegerField()),
                ('loan_type', models.CharField(max_length=15)),
                ('amount', models.BigIntegerField()),
                ('datetime', models.DateTimeField()),
                ('intrest_rate', models.IntegerField()),
                ('payment_due_date', models.DateTimeField()),
                ('loan_balance', models.IntegerField()),
                ('Wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='wallet.wallet')),
                ('guaranter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guaranter', to='wallet.third_party')),
            ],
        ),
    ]

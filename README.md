# Terms of reference for the position of Python Developer Junior.
# Test task "Expense Accounting Manager":
**You need to implement an API to account for user expenses.**

**Technologies:**
- Язык программирования: Python 3.10+   
- DRF 3+   
- Соответствие исходного кода PEP 8

**Will be a plus:**
- Docker/Docker Compose
- Project deployment

**Minimum requirements:**
- User registration
- User authorization (by token)
- User transactions - CRUD
With the help of transactions, the user's balance is debited and accrued.
The transaction must contain: amount\*, time\*, category\*, organization\*, description.
The user should be able to sort, filter transactions by time, amount, date.

- User Categories - CRUD
Upon registration, the user receives a set of standard categories:
"Self care", "Salary", "Health and fitness", "Cafes and restaurants", 
"Car", "Education", "Recreation and entertainment", 
"Payments, commissions", "Shopping: clothes, appliances", "Products", "Directions".
The user can change/delete the standard categories as he wishes, as well as create his own.
- View user profile (information about the current balance)
- User statistics.
Implement sending statistics to the user's mail in the morning every day.
You can choose the amount of statistics you receive.

# SQL test job 
You are given a database of laptops that contains two tables. 
The notebooks\_brand table contains data about notebook brands. 
The notebooks\_notebook table contains data about the name of the laptop, its diagonal, width, depth and height,
and also has a link to the brand to which this model belongs.

**Technologies:**
- PostgreSQL
- DB dump - test\_db.dump

**Exercise:**
1. Write a query that will count how many laptops are represented in each brand. 
Sort the data in descending order.
2. You need to select groups of laptops by size. 
To do this, the sizes must first be rounded up to the nearest 0 or 5 and then grouped by the same sizes,
counting the number of laptops in each group. Sort the data by size.

# Run the project locally
1. **Fill in .env file, edit .env example**

2. **Build the containers**
```shell
docker-compose build
```
3. **Run the containers**
```shell
docker-compose up -d
```
4. **Track the logs**
```shell
docker-compose logs -f 
```
5. **Create superuser**
```shell
docker-compose exec app python manage.py createsuperuser --username admin
```
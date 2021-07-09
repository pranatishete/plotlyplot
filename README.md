# plotlyplot
Task


Database Tables

# Customer

ID	int AI PK
CustomerName	longtext
address	longtext
city	longtext
state	longtext
pincode	longtext
country	longtext
CustomerSegment	longtext
location	longtext
domain	varchar(45)
NumberOfWarehouses	int

# Products

ID	int AI PK
Product	text
NonConsumableParts	text
ConsumableParts	text

# Salesorder
ID	int AI PK
customer_id	double
seller_id	double
OrderDate	longtext
address	longtext
city	longtext
state	longtext
pincode	longtext
country	longtext
location	longtext
status	longtext
value	longtext
DeliveryDate	longtext
currency	longtext
DeliveryDays	longtext
DeliveryChallan	int
transporter_id	int
route	varchar(1000)

# Orderedunit
ID	int AI PK
ordertype	varchar(455)
order_id	int
unitType	varchar(100)
unit_id	int
No_of_units	int


# Approach 

There was no foreign key relationship between the tables. I have joined tables ordereunits and products assuming unit_id as product id and summed the no of units.
if there was any product id in sales order I could have been able to join and find the number of products ordered by customer.

# Run the file using

python run.py


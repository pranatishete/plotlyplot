import mysql.connector as sql
import plotly.express as px
import pandas as pd

db_connection = sql.connect(host='localhost', database='projectdf', user='root', password='')

db_cursor = db_connection.cursor()

db_cursor.execute("select products.ID,products.Product,SUM(orderedunits.No_of_units) as total from products JOIN orderedunits ON products.ID=orderedunits.unit_id GROUP BY products.ID HAVING (products.Product='Tyre' or products.Product='Electric Motor')")
columns = [col[0] for col in db_cursor.description]

table_rows = db_cursor.fetchall()

products = pd.DataFrame(table_rows,columns=columns)

print(products)
fig2 = px.bar(products,x="Product",y="total")
fig2.show()


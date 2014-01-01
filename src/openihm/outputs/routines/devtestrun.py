import data.mysql.connector
from data.config import Config

foodKcalQuery = '''SELECT  energyvalueperunit from setup_foods_crops WHERE name='maize' '''
db = data.mysql.connector.Connect(**self.config)
cursor = db.cursor()
cursor.execute(foodKcalQuery)
rows = cursor.fetchall()
print rows

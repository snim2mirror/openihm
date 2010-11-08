from data.database import Database

class FoodValuesStartup:
    def __init__(self):
        self.query =''
        #self.insertSartUpValues()

    def insertSartUpValues(self):
        database = Database()
        database.open()
        
        query = '''REPLACE INTO setup_foods_crops (name,category,energyvalueperunit) VALUES ('Sorghum - whole','crops',	%s) ,
                            ('Millet, whole',   'crops',    %s),
                            ('Sorghum flour',   'crops',    %s),
                            ('Wheat flour',     'crops',    %s),
                            ('Millet meal',     'crops',    %s),
                            ('Cassava fresh',   'crops',    %s),
                            ('Potato sweet',    'crops',    %s),
                            ('Cashew nut',      'crops',    %s),
                            ('Groundnut fresh', 'crops',    %s),
                            ('Leaves- dark green',   'wildfoods',        %s),
                            ('Leaves- medium',  'wildfoods',  %s),
                            ('Leaves - light green','wildfoods', %s)	,
                            ('Onion',           'crops',    %s)	,
                            ('Pumpkin',         'crops',    %s)	,
                            ('Tomato',	        'crops',       %s),
                            ('Banana',	        'crops',        %s),
                            ('Cashew apple',    'crops',   %s)	,
                            ('Mango',	        'wildfoods',      %s),
                            ('Papaya',          'crops',      %s)	,
                            ('Vegetable oils',  'crops',  %s)	,
                            ('Termites',        'wildfoods',      %s),
                            ('Milk, cow',       'livestock',     %s)	,
                            ('Milk, goat',      'livestock',     %s)	,
                            ('Milk, sheep',     'livestock',    %s)	,
                            ('Mice',	        'wildfoods',        %s),
                            ('Rice',            'crops',         %s)	,
                            ('Ground beans',    'crops',   %s)	,
                            ('Beef',            'livestock',         %s)	,
                            ('Eggs(Hens & ducks)','livestock',%s)	,
                            ('Meat, goat',      'livestock',    %s)	,
                            ('Meat, sheep',     'livestock',   %s)	,
                            ('Meat, poultry',   'livestock',	%s),
                            ('Meat, pig',       'livestock',   %s)	,
                            ('Soya',	        'crops',        %s),
                            ('Nzama(Bambara groundnut)','crops', %s)	,
                            ('Baobab fruit',    'wildfoods',   %s)	,
                            ('Fish',	        'wildfoods',        %s),
                            ('Tamarind',        'wildfoods',      %s)	,
                            ('Okra',	        'crops',        %s),
                            ('Sweet potatoes',	'crops',%s),
                            ('Brinjal',	        'crops',       %s),
                            ('Coconut(ripe nut)','wildfoods', %s)	,
                            ('Fish(freshwater)','wildfoods', %s)	,
                            ('Gourd',           'crops',        %s)	,
                            ('Guava',	        'wildfoods',     %s),
                            ('Lentils',	        'crops',        %s),
                            ('Mustard',	        'crops',       %s),
                            ('Potato',          'crops',      %s)	,
                            ('Radish',          'crops',    %s)	,
                            ('Red Amaranth(leaf)','wildfoods',  %s)	,
                            ('Sugar, white',    'crops',    %s)	,
                            ('Cabbage',         'crops',    %s)	,
                            ('Groundnut, dry',  'crops', %s)	,
                            ('Avocado, flesh',  'wildfoods',  %s)	,
                            ('Bambara groundnut',   'crops',%s)	,
                            ('Chillies, hot, dried',    'crops',%s)	,
                            ('coco-yam',        'crops',      %s)	,
                            ('Cowpea',          'crops',     %s)	,
                            ('Green maize, cob','crops',%s)	,
                            ('Millet, bullrush','crops',%s)	,
                            ('Pigeon peas',     'crops',   %s)	,
                            ('Pigeon pea, green',   'crops',%s)	,
                            ('sesame',          'crops',       %s)	,
                            ('Mango, medium',   'wildfoods',   %s)	,
                            ('Maize',   'crops',	%s)''' % (3550,3630,3530,3460,3650,1530,1140,5900,3320,480,280,330,480,360,200,1160,
                                                  560,630,390,9000,1480,640,710,1080,1340,3540,3670,2020,75,1450,1490,1390,3710,
                                                  3820,3670,560,500,3040,330,1140,280,400,950,480,630,3390,5440,1140,180,280,
                                                  4000,230,5790,1650,3670,2910,1000,3400,492,3630,3280,2110,5920,63,3420)
        database.execUpdateQuery(query)
        database.close()
                            
                            

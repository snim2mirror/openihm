from data.database import Database

class FoodValuesStartup:
    def __init__(self):
        self.query =''
        #self.insertSartUpValues()

    def insertSartUpValues(self):
        database = Database()
        database.open()
        
        query = '''INSERT INTO setup_crops (foodtype,energyvalueperunit) VALUES ('Sorghum - whole',	%s) ,
                            ('Millet, whole',   %s),
                            ('Sorghum flour',   %s),
                            ('Wheat flour',     %s),
                            ('Millet meal',     %s),
                            ('Cassava fresh',   %s),
                            ('Potato sweet',    %s),
                            ('Cashew nut',      %s),
                            ('Groundnut fresh', %s),
                            ('Leaves- dark green',%s),
                            ('Leaves- medium',  %s),
                            ('Leaves - light green',%s)	,
                            ('Onion',           %s)	,
                            ('Pumpkin',         %s)	,
                            ('Tomato',	        %s),
                            ('Banana',	        %s),
                            ('Cashew apple',    %s)	,
                            ('Mango',	        %s),
                            ('Papaya',          %s)	,
                            ('Vegetable oils',  %s)	,
                            ('Termites',        %s),
                            ('Milk, cow',       %s)	,
                            ('Milk, goat',      %s)	,
                            ('Milk, sheep',     %s)	,
                            ('Mice',	        %s),
                            ('Rice',            %s)	,
                            ('Ground beans',    %s)	,
                            ('Beef',            %s)	,
                            ('Eggs(Hens & ducks)',%s)	,
                            ('Meat, goat',      %s)	,
                            ('Meat, sheep',     %s)	,
                            ('Meat, poultry',	%s),
                            ('Meat, pig',       %s)	,
                            ('Soya',	        %s),
                            ('Nzama(Bambara groundnut)',%s)	,
                            ('Baobab fruit',    %s)	,
                            ('Fish',	        %s),
                            ('Tamarind',        %s)	,
                            ('Okra',	        %s),
                            ('Sweet potatoes',	%s),
                            ('Brinjal',	        %s),
                            ('Coconut(ripe nut)',%s)	,
                            ('Fish(freshwater)',%s)	,
                            ('Gourd',           %s)	,
                            ('Guava',	        %s),
                            ('Lentils',	        %s),
                            ('Mustard',	        %s),
                            ('Potato',          %s)	,
                            ('Radish',          %s)	,
                            ('Red Amaranth(leaf)',%s)	,
                            ('Sugar, white',    %s)	,
                            ('Cabbage',         %s)	,
                            ('Groundnut, dry',  %s)	,
                            ('Avocado, flesh',  %s)	,
                            ('Bambara groundnut',%s)	,
                            ('Chillies, hot, dried',%s)	,
                            ('coco-yam',        %s)	,
                            ('Cowpea',          %s)	,
                            ('Green maize, cob',%s)	,
                            ('Millet, bullrush',%s)	,
                            ('Pigeon peas',     %s)	,
                            ('Pigeon pea, green',%s)	,
                            ('sesame',          %s)	,
                            ('Mango, medium',   %s)	,
                            ('Maize',	%s)''' % (3550,3630,3530,3460,3650,1530,1140,5900,3320,480,280,330,480,360,200,1160,
                                                  560,630,390,9000,1480,640,710,1080,1340,3540,3670,2020,75,1450,1490,1390,3710,
                                                  3820,3670,560,500,3040,330,1140,280,400,950,480,630,3390,5440,1140,180,280,
                                                  4000,230,5790,1650,3670,2910,1000,3400,492,3630,3280,2110,5920,63,3420)
        database.execUpdateQuery(query)
        database.close()
                            
                            

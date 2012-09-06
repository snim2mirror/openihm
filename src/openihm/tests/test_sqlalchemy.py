import unittest
from database_helper import DatabaseHelper
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from model.schema import setup_foods_crops


class SetupFoodsCrops(object):

    def __init__(self, name, category, energyvalueperunit, unitofmeasure):
        self.name = name
        self.category = category
        self.energyvalueperunit = energyvalueperunit
        self.unitofmeasure = unitofmeasure

mapper(SetupFoodsCrops, setup_foods_crops)


class TestSQLAlchemy(unittest.TestCase):
    """
    In order to use these tests you need to have a config file named
    test_openihm.cfg in the directory you are running the tests from
    (i.e. the src directory).

        [database]
        superuser = root
        superuser_password = s00pers3cur3
        database = test_openihm
        user = openihm
        password = ihm2012

    This should contain database credentials for a database that exists
    in mysql for testing.  This database will be toyed around with a lot.
    Obviously avoid pointing it at a database you care about...

    """

    def setUp(self):
        self.helper = DatabaseHelper()
        self.config = self.helper.getConfig()
        self.helper.start_tests()

    def tearDown(self):
        # drop the database
        self.helper.end_tests()

    def test_connection_string(self):
        self.helper.setup_clean_db()
        cs = self.helper.real_config.sqlalchemy_connection_string()
        engine = create_engine(cs, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        self.assertEqual(session.query(SetupFoodsCrops).count(), 0)
        crop = SetupFoodsCrops('test', 'category', 10, 'kg')
        session.add(crop)
        self.assertEqual(session.query(SetupFoodsCrops).count(), 1)
        session.commit()

#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

class TestConsole(unittest.TestCase):
    """Tests for the HBNBCommand class"""
    def setUp(self):
        """ """
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_create_state(self):
        self.console.onecmd('create State name="California"')
        output = self.console.onecmd('all State')
        self.assertIn('California', output)
        # Assuming the output is stored in a variable or printed

    def test_create_place(self):
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        self.console.onecmd('all Place')
        self.assertIn('My_little_house', output)
        # Check that the output includes a place object

class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_base_model_creation(self):
        """Test creating a BaseModel object with parameters"""
        model = BaseModel(id="123", created_at="2022-01-01T00:00:00", updated_at="2022-01-01T00:00:00")
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, datetime.datetime(2022, 1, 1, 0, 0))
        self.assertEqual(model.updated_at, datetime.datetime(2022, 1, 1, 0, 0))


if __name__ == '__main__':
    unittest.main()

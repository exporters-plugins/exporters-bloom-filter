# -*- coding: utf-8 -*-
import unittest
from exporters.meta import ExportMeta
from exporters.records.base_record import BaseRecord
from exporters_bloom_filter.filter import DuplicatesBloomFilter


class DuplicatesBloomFilterTest(unittest.TestCase):

    def setUp(self):
        self.filter = DuplicatesBloomFilter({}, ExportMeta(None))

    def test_filter_empty_batch(self):
        self.assertTrue(list(self.filter.filter_batch([])) == [])

    def test_filter_no_duplicated_items(self):
        items = [{'name': 'item1', 'value': 'value1'}, {'name': 'item2', 'value': 'value2'}]
        batch = [BaseRecord(item) for item in items]
        self.assertEqual(list(self.filter.filter_batch(batch)), batch)

    def test_filter_duplicated_items(self):
        item = {'name': 'item1', 'value': 'value1'}
        items = [item, item]
        batch = [BaseRecord(i) for i in items]
        filtered_batch = list(self.filter.filter_batch(batch))
        self.assertEqual(len(filtered_batch), 1)
        self.assertEqual(filtered_batch, [item])

    def test_filter_with_field(self):
        config = {
            'options': {
                'field': 'name'
            }
        }
        field_filter = DuplicatesBloomFilter(config, ExportMeta(None))
        items = [{'name': 'item1', 'value': 'value1'}, {'name': 'item1', 'value': 'value2'}]
        batch = [BaseRecord(item) for item in items]
        filtered_batch = list(field_filter.filter_batch(batch))
        self.assertEqual(len(filtered_batch), 1)
        self.assertEqual(filtered_batch, [{'name': 'item1', 'value': 'value1'}])

    def test_filter_with_nested_field(self):
        config = {
            'options': {
                'field': 'value'
            }
        }
        field_filter = DuplicatesBloomFilter(config, ExportMeta(None))

        item1 = {
            'name': 'item1', 'value': [1, 2, 3]
        }

        item2 = {
            'name': 'item2', 'value': [1, 2, 3]
        }
        items = [item1, item2]
        batch = [BaseRecord(item) for item in items]
        filtered_batch = list(field_filter.filter_batch(batch))
        self.assertEqual(len(filtered_batch), 1)
        self.assertEqual(filtered_batch, [item1])

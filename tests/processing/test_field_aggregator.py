from models.processing.field_aggregator_parser import FieldAggregatorParserModel
from processing.field_aggregator import FieldAggregatorParser


class TestFieldAggregatorParser:
    def test_int_sum(self):
        model = FieldAggregatorParserModel(**{
            'type': 'field_aggregator',
            'model_applied': 'sales',
            'field_names': [
                'field1',
                'field2'
            ],
            'target_field_name': 'result',
            'method': 'sum'
        })

        parser = FieldAggregatorParser(model)

        input_entity = {
            'field1': 10,
            'field2': 20
        }

        expected_output = {
            'result': 30,
        }

        assert expected_output == parser.parse(input_entity)


    def test_float_sum(self):
        model = FieldAggregatorParserModel(**{
            'type': 'field_aggregator',
            'model_applied': 'sales',
            'field_names': [
                'field1',
                'field2'
            ],
            'target_field_name': 'result',
            'method': 'sum'
        })

        parser = FieldAggregatorParser(model)

        input_entity = {
            'field1': 1.5,
            'field2': 2.5
        }

        expected_output = {
            'result': 4,
        }

        assert expected_output == parser.parse(input_entity)

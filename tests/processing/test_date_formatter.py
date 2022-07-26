import datetime
from models.processing.date_formatter_parser import DateFormatterParserModel
from processing.date_formatter import DateFormatterParser


class TestDateFormatter:
    def test_parse_date_brazilian_format(self):
        model = DateFormatterParserModel(**{
            'type': 'date_formatter',
            'model_applied': 'sales',
            'field_name': 'date',
            'date_format': '%d/%m/%Y'
        })
        parser = DateFormatterParser(model)
        input_date = '25/11/1997'
        entity = {
            'date': input_date
        }
        expected_output = {
            'date': datetime.date(1997, 11, 25)
        }
        assert expected_output == parser.parse(entity)

    def test_parse_date_american_format(self):
        model = DateFormatterParserModel(**{
            'type': 'date_formatter',
            'model_applied': 'sales',
            'field_name': 'date',
            'date_format': '%m/%d/%Y'
        })
        parser = DateFormatterParser(model)
        input_date = '11/25/1997'
        entity = {
            'date': input_date
        }
        expected_output = {
            'date': datetime.date(1997, 11, 25)
        }
        assert expected_output == parser.parse(entity)

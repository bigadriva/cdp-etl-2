from pathlib import Path
from connector.ftp import FTPConnector
from file_handler.csv_factory import CSVFileHandlerFactory
from models.file.file_config import FileConfig
from models.mapping.salespeople import SalespeopleMapping


def main():
    ftp_connector = FTPConnector(
        'Catarinense Pharma',
        '201.55.119.243',
        21,
        FileConfig(type='csv', encoding='utf-8-sig', separator=';'),
        '/',
        'Driva',
        '@123driva#'
    )

    # paths = ftp_connector.download_data('data/catarinense')
    paths = [
        Path('./data/catarinense/DADOS_DRIVA.TXT'),
        Path('./data/catarinense/PROD_DRIVA.TXT'),
        Path('./data/catarinense/VEND_DRIVA.TXT'),
    ]
    for path in paths:
        columns = ftp_connector.extract_columns(path)
        print(columns)


if __name__ == '__main__':
    main()

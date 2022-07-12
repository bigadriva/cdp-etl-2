from connector.ftp import FTPConnector
from models.api.connector import APIConnector

class ConnectorFactory:
    @staticmethod
    def create_connector(api_connector: APIConnector):
        if api_connector.type == 'ftp':
            return FTPConnector(
                api_connector.company_name,
                api_connector.type,
                api_connector.host,
                api_connector.port,
                api_connector.directory,
                api_connector.user,
                api_connector.password,
                api_connector.file_config
            )

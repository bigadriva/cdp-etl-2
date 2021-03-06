from connector.base import Connector
from connector.ftp import FTPConnector
from models.connector.connector import ConnectorModel

class ConnectorFactory:
    @staticmethod
    def create_connector(api_connector: ConnectorModel) -> Connector:
        if api_connector.type == 'ftp':
            connector = FTPConnector(
                api_connector.company_name,
                api_connector.type,
                api_connector.host,
                api_connector.port,
                api_connector.directory,
                api_connector.user,
                api_connector.password,
                api_connector.file_config,
            )
            if api_connector.database_mapping is not None:
                connector.database_mapping = api_connector.database_mapping
            return connector

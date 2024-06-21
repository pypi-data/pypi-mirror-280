
import os


class ConfigOperation:
    """ ConfigOperation class is a singleton class that fetches the secrets from AWS Secrets Manager"""
    _instance = None
    secret_value = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigOperation, cls).__new__(cls)
            cls._instance._fetch_secrets()
        return cls._instance

    def _fetch_secrets(self):
        from dalatic_aws_toolkit import read_secret
        self.secret_name = os.environ["PBI"]
        try:
            self.secret_value = read_secret(secret_name=self.secret_name)
        except Exception as e:
            raise e

    @property
    def secrets(self):
        return self.secret_value

import configparser

from src.utils.FileUtils import FileUtils

config = configparser.RawConfigParser()
config.read(FileUtils.get_config_file())


class ConfigProperties:

    @staticmethod
    def get_input_file():
        return config.get("config_data", "input_file")

    @staticmethod
    def get_output_file():
        return config.get("config_data", "input_file")

    @staticmethod
    def get_base_url():
        return config.get("application", "base_url")

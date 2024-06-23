import configparser
import json
import os
import toml
import yaml

from configparser import MissingSectionHeaderError
from typing import Any
from warskald import utils

ENV_PROPS_DIR = os.environ.get('ENV_PROP_DIR')

class SimpleConfigParser(configparser.ConfigParser):
    def read(self, filenames, encoding=None):
        if isinstance(filenames, str):
            filenames = [filenames]
        for filename in filenames:
            with open(filename, 'r', encoding=encoding) as config_file:
                content = config_file.read()
                content = '[dummy_section]\n' + content
                self.read_string(content)
                
class ConfigReader:
    def __init__(self, config_path: str) -> None:
        self.config_data: dict = None
        self._parse_config(config_path)
    
    def _parse_config(self, config_path: str):
        
        config_data = self._read_config(config_path)
        self.config_data = {}
        
        if(isinstance(config_data, configparser.ConfigParser)):
            for section in config_data.sections():
                self.config_data[section] = {}
                for key, value in config_data.items(section):
                    self.config_data[section][key] = value
                    
        elif(isinstance(config_data, SimpleConfigParser)):
            for key, value in config_data.items('dummy_section'):
                self.config_data[key] = value
                
        elif(isinstance(config_data, dict)):
            self.config_data = config_data
    
    def _read_config(self, config_path: str):
        _, ext = os.path.splitext(config_path)
        
        if ext == '.json':
            with open(config_path, 'r') as file:
                return json.load(file)
            
        elif ext == '.ini':
            try:
                config = configparser.ConfigParser()
                config.read(config_path)
                return config
            except MissingSectionHeaderError:
                config = SimpleConfigParser()
                config.read(config_path)
                return config
            
        elif ext in ['.properties', '.conf']:
            config = configparser.ConfigParser()
            config.read(config_path)
            return config
        
        elif ext == '.yaml' or ext == '.yml':
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
            
        elif ext == '.toml':
            with open(config_path, 'r') as file:
                return toml.load(file)
            
        else:
            raise ValueError(f'Unsupported config file extension: {ext}')
                
class Config:
    def __init__(self, files: list[str] = ['environment.properties', 'application.properties']):
        self.config = {}
        self._parse_configs(files)
    
    def _parse_configs(self, file_paths: list[str]):
        
        for file_path in file_paths:
            config = ConfigReader(file_path).config_data
            if(isinstance(config, dict)):
                self.config.update(config)
            
    def get(self, path: str | list[str], default_val: Any = None) -> Any:
        return utils.get_nested(self.config, path, default_val)
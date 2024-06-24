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
        
        config_data, cfg_type = self._read_config(config_path)
        self.config_data = {}
        
        if(isinstance(config_data, configparser.ConfigParser)):
            for section in config_data.sections():
                if(section != 'dummy_section'):
                    self.config_data[section] = {}
                for key, value in config_data.items(section):
                    if(utils.not_empty(value)):
                        if(section == 'dummy_section'):
                            self.config_data[key] = value
                        else:
                            self.config_data[section][key] = value
                    
        
                
        elif(cfg_type == 'dict'):
            self.config_data = config_data
    
    def _read_config(self, config_path: str):
        _, ext = os.path.splitext(config_path)
        
        if ext == '.json':
            with open(config_path, 'r') as file:
                return json.load(file), 'dict'
            
        elif ext == '.ini':
            try:
                config = configparser.ConfigParser()
                config.read(config_path)
                return config, 'configparser'
            except MissingSectionHeaderError:
                config = SimpleConfigParser()
                config.read(config_path)
                return config, 'SimpleConfigParser'
            
        elif ext in ['.properties', '.conf']:
            config = SimpleConfigParser()
            config.read(config_path)
            
            return config, 'SimpleConfigParser'
        
        elif ext == '.yaml' or ext == '.yml':
            with open(config_path, 'r') as file:
                return yaml.safe_load(file), 'dict'
            
        elif ext == '.toml':
            with open(config_path, 'r') as file:
                return toml.load(file), 'dict'
            
        else:
            raise ValueError(f'Unsupported config file extension: {ext}')
                
class EnvPropsReader:
    def __init__(self):
        self.config = {}
        env_prop_files = os.listdir(ENV_PROPS_DIR)
        
        self._parse_configs([os.path.join(ENV_PROPS_DIR, file) for file in env_prop_files])
    
    def _parse_configs(self, file_paths: list[str]):
        
        for file_path in file_paths:
            config = ConfigReader(file_path).config_data
            #print(config)
            if(isinstance(config, dict)):
                for key, value in config.items():
                    #if(utils.not_empty(value)):
                    self.config[key] = value
            
    def get(self, path: str | list[str], default_val: Any = None) -> Any:
        return utils.get_nested(self.config, path, default_val)
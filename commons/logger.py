import os
import logging
import logging.config
import yaml

with open("config/logger.yml", 'rt') as f:
    LOGGER_CONFIG = yaml.safe_load(f.read())

class Logger:
  def __init__(self):
      '''
      Initialize logger
      :param config_file: str, yaml config file path
      '''
      Logger.setup_logger()

  @classmethod
  def setup_logger(cls):
      '''
      Read config file and setup logger
      :param config_file: yaml file
      :return:
      '''
      logging.config.dictConfig(LOGGER_CONFIG)

  @classmethod
  def get_logger(cls, logger_name):
      '''
      Fetch logger
      :param logger_name: str, logger name which is part of yaml file
      :return:
      '''
      return logging.getLogger(logger_name)
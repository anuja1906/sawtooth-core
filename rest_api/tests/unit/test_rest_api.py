import os
import unittest
import tempfile
import logging

from sawtooth_rest_api.rest_api import load_rest_api_config
from sawtooth_rest_api.config import RestApiConfig

LOGGER = logging.getLogger(__name__)
class Testparseargs(unittest.TestCase):
    def test_load_rest_api_config(self):
        """Tests function test_load_rest_api_config()
        to check if it returns a RestApiConfig created
        by loading a TOML file from the filesystem."""
        first_config = RestApiConfig(
            bind="test:1234",
            connect="tcp://test:4004",
            timeout=10,
            opentsdb_url="data_base",
            opentsdb_db="http://data_base:0000")
        os.environ.clear()
        directory = tempfile.mkdtemp(prefix="test-path-config-")
        os.environ['SAWTOOTH_HOME'] = directory
        config_dir = os.path.join(directory, 'etc')
        os.mkdir(config_dir)
        load_rest_api_config(first_config)
        
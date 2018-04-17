# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------
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

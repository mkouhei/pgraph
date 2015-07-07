# -*- coding: utf-8 -*-
"""pgraph.config module."""
import os
import sys
if sys.version_info < (3, 0):
    # pylint: disable=import-error
    import ConfigParser as configparser
else:
    import configparser


def load():
    """Load configuration file."""
    if os.environ.get('CONFIG_FILE') is None:
        sys.stderr.write("Missing env variable CONFIG_FILE\n\n")
        sys.exit(2)

    config_file = os.path.abspath(os.environ['CONFIG_FILE'])
    if not os.path.isfile(config_file):
        sys.stderr.write("Can't read file: {0}\n\n".format(config_file))
        sys.exit(2)

    config = configparser.SafeConfigParser()
    config.read(config_file)
    return config, config_file

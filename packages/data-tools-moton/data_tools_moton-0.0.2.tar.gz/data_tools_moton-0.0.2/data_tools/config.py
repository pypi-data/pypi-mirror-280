"""
### CODE OWNERS: Demerrick Moton
### OBJECTIVE:
    Class for dealing with collecting and managing configuration values
### DEVELOPER NOTES:
"""

import json
import logging
import os
import yaml
import importlib

from pathlib import Path

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=os.environ.get("LOGLEVEL", "INFO")
)
LOGGER = logging.getLogger(__name__)

# ===========================================================

def _read_config(config_file: Path) -> dict:
    """
    Read the json config

    Args:
        config_file (Path): Path of the configuration

    Returns:
        dict: Python dictionary of project configuration
    """
    assert config_file.exists(), "Provided configuration file does not exist"

    conf = None
    with open(str(config_file), "r") as js:
        conf = json.load(js)
    assert conf, "Configuration read from {} has returned empty result".format(
        config_file
    )
    return conf


def _write_config(config: dict, config_file: Path):
    """
    Modify and output json object

    Args:
        config (dict): Project configuration in the form of Python dictionary
        config_file (Path): Path to the configuration files
    """
    assert config_file.exists(), "Provided configuration file does not exist"

    with open(str(config_file), "w") as js:
        json.dump(config, js)


def load_config(header: str, config_file: Path, config_dict: dict = None) -> dict:
    """
    Load particular section from json configuration file

    Args:
        header (str): Name of section
        config_file (Path): Path to config file of interest
        config_dict (dict, optional): Dictionary of parameters to coalesce with config options

    Returns:
        dict: Dictionary of parameters derived from config file
    """
    if type(config_file) == str:
        config_file = Path(config_file)
    config = _read_config(config_file)

    if header not in config:
        LOGGER.warning("Section {} is not available".format(header))
        return

    if config_dict:
        config_from_file = {k: v for k, v in config[header].items() if v != ""}
        return {**config_dict, **config_from_file}
    else:
        return {**config[header]}


def update_config(
    header: str,
    option: str,
    value: str,
    config_file: Path,
):
    """
    Update particular section of json configuration file

    Args:
        header (str): Name of section
        option (str): Name of option to be modified
        value (str): Replacement value
        config_file (Path): Path to config file of interest
    """
    if type(config_file) == str:
        config_file = Path(config_file)
    config = _read_config(config_file)

    assert config[header], "Section {} is not available".format(header)

    if option not in config[header]:
        LOGGER.warning(f"Section {option} was found in the config file... Creating it")

    config[header][option] = value
    _write_config(config, config_file)


def remove_config_options(
    header: str,
    options: list,
    config_file: Path,
):
    """
    Remove particular section of json configuration file

    Args:
        header (str): Name of section
        option (list): List of options to be removed
        config_file (Path): Path to config file of interest
    """
    for option in options:
        update_config(header=header, option=option, value="", config_file=config_file)


def init_resource(resource, options) -> object:
    """
    Initialize a python object by setting its parameters dynamically

    Args:
        resource (object): Python object to be initialized
        options (dict): Parameter to be set

    Returns:
        object: Initialized resource
    """
    if not options:
        return
    # TODO: account for lists
    LOGGER.info("Initializing resource {}".format(type(resource).__name__))
    for k, v in options.items():
        try:
            getattr(resource, k)
        except Exception as error:
            LOGGER.error(error)
        else:
            setattr(resource, k, v)
    return resource


def init_resources(config_file: Path, resources: dict) -> dict:
    """
    Initialize a collection of python objects by setting their parameters dynamically

    Args:
        config_file (Path): Path to configuration file
        resources (dict): Dictionary of python objects to initialize

    Returns:
        dict: Dictionary of initialized resources
    """
    if type(config_file) == str:
        config_file = Path(config_file)
    if not resources:
        LOGGER.warn("No resources provided to be initialized")

    for name, resource in resources.items():
        options = load_config(header=name, config_file=config_file)
        resource = init_resource(resource=resource, options=options)
        resources[name] = resource
    return resources

def load_yaml_config(config_file: str) -> dict:
    """
    Load yaml file into a dictionary

    Args:
        config_file (str): Path to yaml config file of interest

    Returns:
        dict: Dictionary of parameters derived from config file
    """
    assert Path(config_file).suffix == ".yaml", "Provided configuration file is not a yaml file"
    assert Path(config_file).exists(), "Provided configuration file does not exist"

    return yaml.load(
        stream=open(config_file, "r"),
        Loader=yaml.FullLoader
    )

def import_modules(module_path: str) -> object:
    """
    Import module from path
    """
    module_name, class_name = module_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    callable_class = getattr(module, class_name)
    return callable_class
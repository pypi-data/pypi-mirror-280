import os
import importlib
def get_base_path():
    package_name = 'luganda_ocr'
    package = importlib.import_module(package_name)
    package_path = os.path.dirname(package.__file__)
    return package_path


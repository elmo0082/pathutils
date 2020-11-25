import os
from .get_dir_paths import get_home_dir, get_list_source_dirs
import sys
import setuptools

def create_pth_file(config_name='my_config.pth', create_in_site_package_dir=True):
    assert config_name.endswith('.pth')
    if create_in_site_package_dir:
        output_file = os.path.join(setuptools.__path__[0], "../", config_name)
    else:
        output_file = os.path.join(os.getcwd(), config_name)
    with open(output_file, "w") as f:
        for dir in get_list_source_dirs():
            f.write("{}\n".format(dir))


def change_paths_config_file(template_path):
    output_path = template_path.replace(".yml", "_temp.yml")
    path_placeholder = "$HCI_HOME\/"
    real_home_path = get_home_dir().replace("/", "\/")
    cmd_string = "sed 's/{}/{}/g' {} > {}".format(path_placeholder, real_home_path,
                                                  template_path,
                                                  output_path)
    os.system(cmd_string)
    return output_path


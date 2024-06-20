import os

import yaml


def get_data(module):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "../data_exporter/conf_info.yaml")
    with open(config_path, encoding='utf-8') as f:
        datas = yaml.safe_load(f).get(module)
        return datas


if __name__ == '__main__':
    d = get_data(module="mysql_info")
    print(d)
    print(type(d))

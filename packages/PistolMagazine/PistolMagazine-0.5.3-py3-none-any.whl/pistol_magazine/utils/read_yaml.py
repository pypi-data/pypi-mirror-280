import yaml


def get_data(module):
    with open("../data_exporter/conf_info.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f).get(module)
        return datas


if __name__ == '__main__':
    d = get_data(module="db_info")
    print(d)
    print(type(d))

import consul
import yaml

# def load_config() -> dict:
#     c = consul.Consul(host='192.168.1.102', port=8500)
#     index, data = c.kv.get('config/new_erp/setting')
#     config = yaml.load(data['Value'],Loader=yaml.SafeLoader)
#     return config


def load_config() -> dict:
    with open("config/setting.yml") as yaml_file:
        conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf

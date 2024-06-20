import yaml
from notebookutils import mssparkutils


class ConfigResolver:
    def __init__(self, config_str):
        self.config = yaml.safe_load(config_str)
        self.resolve_config(self.config)

    def get_secret(self, akv_name, secret_name):
        print(f"akv_name: {akv_name} secret_name: {secret_name}")
        return mssparkutils.credentials.getSecret(akv_name, secret_name)

    def resolve_config(self, node):
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, str):
                    node[key] = self.resolve_value(value)
                    if not node[key]:
                        raise ValueError(f"Configuration for {key} with value {value} not found")
                else:
                    self.resolve_config(value)
        elif isinstance(node, list):
            for i, item in enumerate(node):
                if isinstance(item, str):
                    node[i] = self.resolve_value(item)
                else:
                    self.resolve_config(item)

    def resolve_value(self, value):
        # Strip surrounding quotes if present
        if "secret:" in value:
            print(f"secret: {value}")

        while "{" in value and "}" in value:
            start = value.find("{") + 1
            end = value.find("}", start)
            placeholder = value[start:end]

            if "secret:" in placeholder:
                secret_name = placeholder.split("secret:")[1]
                akv_name = self.config.get("resources", {}).get("keyvault", "")
                if akv_name:
                    secret_value = self.get_secret(akv_name, secret_name)
                    print(f"secret_value: {secret_value}")
                    value = value.replace("{" + placeholder + "}", secret_value)
                else:
                    raise ValueError("Azure Key Vault name not found in configuration")
            else:
                path_parts = placeholder.split(".")
                replacement_value = self.config
                for part in path_parts:
                    if part in replacement_value:
                        replacement_value = replacement_value[part]
                    else:
                        raise ValueError(f"Configuration for {'.'.join(path_parts)} not found")
                value = value.replace("{" + placeholder + "}", str(replacement_value))

        return value

    def get(self, path=None):
        if path is None:
            return self.config
        else:
            keys = path.split(".")
            value = self.config
            for key in keys:
                if key in value:
                    value = value[key]
                else:
                    raise ValueError(f"Configuration for {path} not found")
            return value

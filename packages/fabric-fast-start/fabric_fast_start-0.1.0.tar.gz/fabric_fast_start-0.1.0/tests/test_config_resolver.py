from fabric_fast_start.config.config_resolver import ConfigResolver


def test_get_secret(mocker):
    # Mocking mssparkutils.credentials.getSecret
    mocker.patch(
        "fabric_fast_start.config.config_resolver.mssparkutils.credentials.getSecret", return_value="my_secret"
    )

    config_str = """
    resources:
        keyvault: my_keyvault
    """
    resolver = ConfigResolver(config_str)
    secret = resolver.get_secret("my_keyvault", "my_secret")
    assert secret == "my_secret"


def test_resolve_config():
    config_str = """
    resources:
        keyvault: my_keyvault
    """
    resolver = ConfigResolver(config_str)
    resolver.resolve_config(resolver.config)
    assert resolver.config == {"resources": {"keyvault": "my_keyvault"}}


def test_resolve_config_with_secret(mocker):
    # Mocking mssparkutils.credentials.getSecret
    mocker.patch(
        "fabric_fast_start.config.config_resolver.mssparkutils.credentials.getSecret", return_value="my_secret"
    )

    config_str = """
    resources:
        keyvault: my_keyvault
    data:
        secret: '{secret:my_secret}'
    """
    resolver = ConfigResolver(config_str)
    print(f"resolver.config: {resolver.config.get('data')}")
    secret = resolver.config["data"]["secret"]
    assert secret == "my_secret"


def test_resolve_value_with_secret(mocker):
    # Mocking mssparkutils.credentials.getSecret
    mocker.patch(
        "fabric_fast_start.config.config_resolver.mssparkutils.credentials.getSecret", return_value="secret_value"
    )

    config_str = """
    resources:
        keyvault: my_keyvault
    """
    resolver = ConfigResolver(config_str)
    value = resolver.resolve_value("{secret:my_secret}")
    assert value == "secret_value"


def test_resolve_value_with_config():
    config_str = """
    resources:
        keyvault: my_keyvault
        database:
            host: localhost
            port: 5432
    """
    resolver = ConfigResolver(config_str)
    value = resolver.resolve_value("{resources.database.host}")
    assert value == "localhost"


def test_get():
    config_str = """
    resources:
        keyvault: my_keyvault
        database:
            host: localhost
            port: 5432
    """
    resolver = ConfigResolver(config_str)
    value = resolver.get("resources.database.port")
    assert value == 5432

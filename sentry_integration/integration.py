import sentry_sdk

def init_sentry(
    dsn: str,
    environment: str,
    server_name: str
):
    sentry_sdk.init(
        dsn=dsn,
        add_full_stack=True,
        send_default_pii=True,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        environment=environment,
        server_name=server_name,
    )

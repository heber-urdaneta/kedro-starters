from kedro.framework.hooks import hook_impl
import snowflake.snowpark as sp


class SnowParkHooks:
    @hook_impl
    def after_context_created(self, context) -> None:
        """Initialises a Snowpark Session using the config
        defined in project's conf folder.
        """

        # Load the snowflake configuration in snowpark_credentials.yaml using the config loader
        parameters = context.config_loader.get("snowpark*", "snowpark*/**")
        _snowpark_session = sp.Session.builder.configs(parameters).create()

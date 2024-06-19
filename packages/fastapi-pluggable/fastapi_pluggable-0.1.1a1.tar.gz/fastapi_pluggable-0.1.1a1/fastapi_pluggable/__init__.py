import logging
from importlib.metadata import entry_points

from fastapi import FastAPI

log = logging.getLogger(__name__)


def merge_openapi_schemas(app: FastAPI, plugins: list[FastAPI]) -> None:
    """Attempts to merge mutliple OpenAPI specs to build a unified spec.

    Args:
        app:        FastAPI app.
        plugins:    List of FastAPI apps (plugins).
    """
    app.openapi()

    # Default schema is enough if no plugins
    if not plugins:
        return

    # Loop through plugins, ensure uniqueness of paths and other fields
    existing_schemas = []

    for plugin in plugins:
        paths = {}

        plugin.openapi()

        # Routes
        for k, v in plugin.openapi_schema["paths"].items():
            path = plugin.root_path + k
            paths[path] = v

        # Webhooks

        # Tags

        # Servers

        # Components / Schemas
        if schemas := plugin.openapi_schema.get("components", {}).get("schemas", {}):
            for schema, schema_impl in schemas.items():
                if schema in existing_schemas:
                    log.warning(
                        "Duplicate schema objects detected, renaming for uniqueness"
                    )
                else:
                    app.openapi_schema["components"]["schemas"][schema] = schema_impl

        # Merge
        app.openapi_schema["paths"] = dict(
            list(app.openapi_schema["paths"].items()) + list(paths.items())
        )


def load_plugins(
    app: FastAPI,
    entrypoint: str,
    path: str = "",
    merge_docs: bool = False,
    raise_exceptions: bool = True,
) -> None:
    """Attempts to load plugins based on an entry point.

    Args:
        app:                FastAPI app.
        entrypoint:         Entrypoint group to search for.
        path:               Plugin path.
        merge_docs:         Merge OpenAPI Schemas so /docs show all app endpoints.
        raise_exceptions:   Raise exceptions instead of warning/ignoring them.
    """
    plugins = []
    plugin_paths = []

    for plugin in entry_points(group=entrypoint):
        try:
            plugin_app: FastAPI = plugin.load()
        except Exception as err:
            log.warning(f"plugins failed to load: {plugin.name} (reason: '{err}')")
            continue

        # Validate if root_path exist and no plugin has a duplicate root_path
        if not plugin_app.root_path:
            log.warning("plugin must have root_path set in the FastAPI object")
            if raise_exceptions:
                raise ValueError(
                    f'plugin `{plugin.name}` root_path must not be empty, ensure you set like this for example: FastAPI(root_path="/plugin-abc")'
                )

            continue

        if plugin_app.root_path in plugin_paths:
            log.warning(
                f"plugin {plugin.name} root_path '{plugin_app.root_path}' is already used in another plugin"
            )
            continue

        plugin_paths.append(plugin_app.root_path)
        plugin_app.root_path = path + plugin_app.root_path

        app.mount(
            path=plugin_app.root_path,
            app=plugin_app,
        )
        plugins.append(plugin_app)

        log.info(f"plugin {plugin.name} successfully mounted to app ({app.title})")

    if merge_docs:
        merge_openapi_schemas(app=app, plugins=plugins)

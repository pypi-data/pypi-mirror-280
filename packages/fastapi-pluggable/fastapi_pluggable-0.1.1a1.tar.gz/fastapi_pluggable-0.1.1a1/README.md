# fastapi-pluggable

Make your FastAPI app pluggable with entrypoints.

This module is mainly aimed around monolithic applications where you would install your applications via a package registry, treating each plugin application as a separate repository that imports a core application to use the common functionality like HTML templates, dependencies and more!

Using entry points, we can treat each separate plugin as a separate installable module, here is an example using Poetry with the `pyproject.toml`, 

```
[tool.poetry.plugins."myapp.plugins"]
plugin_a = 'myapp_plugin_example.main:app'
```

```Contents of the myapp_plugin_example/main/app.py

from fastapi import FastAPI, Request
from pydantic import BaseModel

class Cool(BaseModel):
    yes: bool
    maybe: str

app = FastAPI(root_path="/plugin-a")


@app.get("/hello", response_model=Cool, tags=["Plugin-A"])
async def home(request: Request):
    return Cool(yes=True, maybe="No")
```

Now we need to ensure we load the plugins for our entrypoint defined in the toml file "myapp.plugins", we can also set a default path for all plugins to be loaded under, here is an example of the core application which will use these plugins.

```
from fastapi import FastAPI


app = FastAPI()

@app.get("/hello", tags=["Core-App"])
async def hello():
    return "this is the main application ok"


# Register plugins
from fastapi_pluggable import load_plugins

load_plugins(app=app, entrypoint="myapp.plugins", path="/plugins")
```

Now, `plugin-a` is reachable via the `/plugins/plugin-a` endpoint. If you also set `merge_docs` on the load_plugins function, fastapi_pluggable will attempt to merge the OpenAPI schemas between all the plugins so you can simply visit the `/docs` endpoint instead of multiple endpoints eg. `/docs` and `/plugins/plugin-a/docs`. This is set to False by default so you will have separate plugin openapi schemas unless your plugin disables them when initializing `app = FastAPI()`.

This module is still under heavy work to ensure the best user experience, so expect the logging, openschema merging and some of the other features to not fully work between versions and may even change without backwards compatibility if required. Documentation will also be reworked at some point...
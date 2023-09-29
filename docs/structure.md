Before you start to createing your own applications based on PyDeus, we strongly recommend to know about the package structure.

## Types
There consantrated all types, that PyDeus use (requests, responses, parsed and prepared models, and etc.) during work.

* `pydeus.types.app_config` <br/>
    Represents **app.config.json** from Modeus.
    We use it for API authentication, anyway you can request it by yourself and parse by AppConfigJSON, whith you can import from it package.

* `pydeus.types.requests` <br/>
    There consantrated all requests models that PyDeus use for making requests to Modeus's API.

* `pydeus.types.responses` <br/>
    Simillar to requests, but represent responses from Modeus's API.

* `pydeus.types.parsed` <br/>
    Contains models with parsed data to use it in applications.

## Client



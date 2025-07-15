# API Hit Counter Middleware

A middleware for FastAPI to track API hits.

## Installation

To install the middleware directly from GitHub, run the following command:

```bash
pip install git+https://github.com/TahsinTariq/HitCounter_Middleware.git
```

## Usage

To use the middleware, import it and add it to your FastAPI application.

```python
# Import the middleware
from api_hit_counter.middleware import HitCounterMiddleware

app = FastAPI()

# Add the middleware after instantiating FastAPI()
app.add_middleware(
    HitCounterMiddleware,
    project_name="My Awesome Project Name"
)
```

### Configuration

The `HitCounterMiddleware` accepts the following arguments:

-   `project_name` (str): **Required**. A unique name for your project to identify the hits.
-   `base_api_url` (str, optional): The base URL of the hit counter service.
    -   If not provided, the middleware will look for the `HITCOUNTER_URL` environment variable.
    -   If the environment variable is also not set, it will use the default value: `http://192.168.101.231:10101`, which is the aci gpuserver2x address.

# API Hit Counter Middleware

A middleware for FastAPI to track API hits.

## Installation

To install the middleware directly from GitHub, run the following command:

```bash
pip install git+https://github.com/TahsinTariq/HitCounter_Middleware.git
```

To include the optional dependencies for the dashboard, use:

```bash
pip install "git+https://github.com/TahsinTariq/HitCounter_Middleware.git#egg=api-hit-counter[dashboard]"
```

For development, to include testing libraries, use:

```bash
pip install "git+https://github.com/TahsinTariq/HitCounter_Middleware.git#egg=api-hit-counter[dev]"
```

## Usage

To use the middleware, import it and add it to your FastAPI application.

```python
from fastapi import FastAPI
from api_hit_counter.middleware import HitCounterMiddleware

app = FastAPI()

# Add the middleware
app.add_middleware(
    HitCounterMiddleware,
    project_name="My FastAPI Project",
    counting_api_url="https://your-counting-api.com/hit"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

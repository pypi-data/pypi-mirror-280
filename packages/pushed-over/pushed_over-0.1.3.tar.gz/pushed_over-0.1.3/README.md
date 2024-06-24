# Pushed Over

> Typed, async client for the Pushover API

```
pip install pushed-over
```

## Usage

```python
from pushed_over import notify

await notify(
    token="your-pushover-token",
    user="your-pushover-user",
    message="Hello, world!",
)
# Either[Err, Ok]
```

Or, with the `PUSHOVER_TOKEN` and `PUSHOVER_USER` environment variables set:

```python
await notify(message="Hello, world!")
```

For other parameters, just let auto-complete guide you ;)
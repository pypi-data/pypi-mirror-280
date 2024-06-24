from typing_extensions import TypedDict, Literal, NotRequired, TypeAlias
from dataclasses import dataclass
from pydantic import BaseModel, ValidationError as PyValidationError
import httpx

class Params(TypedDict):
  user: str
  message: str
  title: NotRequired[str]
  device: NotRequired[str]
  url: NotRequired[str]
  url_title: NotRequired[str]
  ttl: NotRequired[int]
  """Seconds after which the message will be deleted"""
  sound: NotRequired[str]

class HighPriorityParams(Params):
  priority: Literal[2]
  expire: int
  """Quoting the [docs](https://pushover.net/api): how many seconds your notification will continue to be retried for (every retry seconds). If the notification has not been acknowledged in expire seconds, it will be marked as expired and will stop being sent to the user. Note that the notification is still shown to the user after it is expired, but it will not prompt the user for acknowledgement. This parameter must have a maximum value of at most 10800 seconds (3 hours), though the total number of retries will be capped at 50 regardless of the expire parameter."""
  retry: int
  """Quoting the [docs](https://pushover.net/api): how often (in seconds) the Pushover servers will send the same notification to the user. In a situation where your user might be in a noisy environment or sleeping, retrying the notification (with sound and vibration) will help get his or her attention. This parameter must have a value of at least 30 seconds between retries."""

class LowPriorityParams(Params):
  priority: Literal[-2, -1, 0, 1]

class Ok(BaseModel):
  status: Literal[1]
  request: str

class PriorityOk(Ok):
  receipt: str

class PushoverError(BaseModel):
  status: int
  errors: list[str]
  request: str
  tag: Literal['pushover'] = 'pushover'

@dataclass
class NetworkError:
  err: httpx.HTTPError
  tag: Literal['network'] = 'network'

@dataclass
class ValidationError:
  err: PyValidationError
  tag: Literal['validation'] = 'validation'

Err = PushoverError | NetworkError | ValidationError
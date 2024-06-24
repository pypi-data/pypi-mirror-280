from typing_extensions import Unpack, overload
import os
import httpx
from haskellian import either as E, Left, Either
from ._types import HighPriorityParams, LowPriorityParams, Ok, PriorityOk, PushoverError, Err

@overload
async def notify(*, token: str | None = None, user: str | None = None, attachment: bytes | None = None, **params: Unpack[HighPriorityParams]) -> Either[Err, PriorityOk]:
  """Send a high-priority notification
  - `token`: can be `None` if the `PUSHOVER_TOKEN` env. variable is set
  - `user`: can be `None` if the `PUSHOVER_USER` env. variable is set
  - `attachment`: an image to send with the notification
  
  This function doesn't raise exceptions (except if you don't provide a token), but instead returns an appropriate `Left` value
  """
@overload
async def notify(*, token: str | None = None, user: str | None = None, attachment: bytes | None = None, **params: Unpack[LowPriorityParams]) -> Either[Err, Ok]:
  """Send a non-urgent notification
  - `token`: can be `None` if the `PUSHOVER_TOKEN` env. variable is set
  - `user`: can be `None` if the `PUSHOVER_USER` env. variable is set
  - `attachment`: an image to send with the notification
  
  This function doesn't raise exceptions (except if you don't provide a token), but instead returns an appropriate `Left` value
  """

async def notify(*, token: str | None = None, user: str | None = None, attachment: bytes | None = None, **params): # type: ignore
  token = token or os.getenv('PUSHOVER_TOKEN')
  user = user or os.getenv('PUSHOVER_USER')
  if not token:
    raise ValueError('Please provide a token or set the PUSHOVER_TOKEN env. variable')
  if not user:
    raise ValueError('Please provide a user or set the PUSHOVER_USER env. variable')
  
  params = { **params, 'token': token, 'user': user }
  files = {'attachment': attachment} if attachment else None
  
  try:
    async with httpx.AsyncClient() as client:
      response = await client.post('https://api.pushover.net/1/messages.json', data=params, files=files)
      if response.status_code == 200:
        model = PriorityOk if params.get('priority') == 2 else Ok
        return E.validate_json(response.text, model)
      else:
        return E.validate_json(response.text, PushoverError).bind(Left)
  except httpx.HTTPError as e:
    return Left(e)
from fastapi import FastAPI, Security, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from chess_pairings import GameId
from pushed_over import notify

def upload_message(tournId: str, group: str, round: str, board: str):
  return f'Game uploaded for {tournId}/{group}/{round}/{board}'

def authorize(token: str):
  def bound(auth: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    if auth.credentials != token:
      raise HTTPException(status_code=401, detail='Unauthorized')
  return bound

def api(token: str):
  app = FastAPI()

  @app.post('/game-upload')
  async def authed(gameId: GameId, auth = Depends(authorize(token))):
    title = f'Game Upload {gameId["tournId"]}'
    (await notify(title=title, message=upload_message(**gameId))).unsafe()

  return app

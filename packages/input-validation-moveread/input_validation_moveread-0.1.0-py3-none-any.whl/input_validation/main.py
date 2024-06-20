from dataclasses import dataclass
from q.api import ReadQueue, WriteQueue
from fastapi import FastAPI

@dataclass
class Input:
  gameId: str

@dataclass
class Output:
  gameId: str

def pipeline(Qin: ReadQueue[Input], Qout: WriteQueue[Output]):
  api = FastAPI()

  @api.get('/')
  def home():
    return 'Input Validation API'
  
  @api.get('/push')
  async def push():
    k, v = (await Qin.read()).unsafe()
    (await Qout.push(k, Output(v.gameId))).unsafe()
    (await Qin.pop(k)).unsafe()
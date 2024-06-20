from dataclasses import dataclass
import os
from q.api import ReadQueue, WriteQueue
from fastapi import FastAPI
from fullstack import fullstack

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

  dir = os.path.dirname(os.path.realpath(__file__))
  dist = os.path.join(dir, 'dist')
  
  def root_api(base: str):
    return fullstack(api, dist_path=dist, base_path=base)
  
  return root_api
import requests
from urllib.parse import urljoin

ENDPOINT = 'https://api.gostatit.com'


class coreAPI:
  '''A python API to interact with the api.gostatit.com core web API'''
    
  def __init__(self, username: str, apikey: str):
    self.username = username
    self.apikey = apikey

  def post(self, json):
    url = urljoin(ENDPOINT, 'core')
    r = requests.post(url,auth=(self.username, self.apikey), json=json)
    if r.status_code != 200 : raise ValueError(r.text)
    return r.json()

  def getSerie(self, id: str) -> dict[str, any]:
    json = {
      'action': 'getSerie', 'input': {
        'id': id,
      },
    }
    return self.post(json)

  def listSeries(self, parentid: str) -> list[dict[str, any]]:
    json = {
      'action': 'listSeries', 'input': {
        'id': parentid,
      },
    }
    return self.post(json)

  def deleteSerie(self, id: str):
    json = {
      'action': 'deleteSerie', 'input': {
        'id': id,
      },
    }
    return self.post(json)


  def getSerieJSON(self, input: dict[str, any]) -> dict[str, any]:
    json = {
      'action': 'getSerie', 'input': input,
    }
    return self.post(json)

  def batchGetSerieJSON(self, input: list[dict[str, any]]):
    json = {
      'action': 'batchGetSerie', 'input': input,
    }
    return self.post(json)

  def getAllSeriesJSON(self, input: list[dict[str, any]]):
    batch = []
    for serie in input:
      batch.append(serie)
      if len(batch) == 25:
        yield self.batchGetSerieJSON(batch)
        batch = []
    if batch != [] : yield self.batchGetSerieJSON(batch)

  def listSeriesJSON(self, input: dict[str, any]) -> list[dict[str, any]]:
    json = {
      'action': 'listSeries', 'input': input,
    }
    return self.post(json)
    
  def putSerieJSON(self, input: dict[str, any]):
    json = {
      'action': 'putSerie', 'input': input,
    }
    return self.post(json)

  def batchPutSerieJSON(self, input: list[dict[str, any]]):
    json = {
      'action': 'batchPutSerie', 'input': input,
    }
    return self.post(json)

  def putAllSeriesJSON(self, input: list[dict[str, any]]):
    batch = []
    for serie in input:
      batch.append(serie)
      if len(batch) == 25:
        yield self.batchPutSerieJSON(batch)
        batch = []
    if batch != [] : yield self.batchPutSerieJSON(batch)
    
  def updateSerieJSON(self, input: dict[str, any]):
    json = {
      'action': 'updateSerie', 'input': input,
    }
    return self.post(json)

  def deleteSerieJSON(self, input: dict[str, any]):
    json = {
      'action': 'deleteSerie', 'input': input,
    }
    return self.post(json)

  def batchDeleteSerieJSON(self, input: list[dict[str, any]]):
    json = {
      'action': 'batchDeleteSerie', 'input': input,
    }
    return self.post(json)

  def deleteAllSeriesJSON(self, input: list[dict[str, any]]):
    batch = []
    for serie in input:
      batch.append(serie)
      if len(batch) == 25:
        yield self.batchDeleteSerieJSON(batch)
        batch = []
    if batch != [] : yield self.batchDeleteSerieJSON(batch)

class functionsAPI:
  '''A python API to interact with the api.gostatit.com functions web API'''

  def __init__(self, username: str, apikey: str):
      self.username = username
      self.apikey = apikey

  def post(self, json):
    url = urljoin(ENDPOINT, 'functions')
    r = requests.post(url,auth=(self.username, self.apikey), json=json)
    if r.status_code != 200 : raise ValueError(r.text)
    return r.json()

  def getObs(self, id: str):
    json = {
      'action': 'getObs', 'input': {
        'id': id,
      },
    }
    return self.post(json)

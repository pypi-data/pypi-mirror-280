import requests
from urllib.parse import urljoin

ENDPOINT = 'https://api.gostatit.com'

class coreAPI:
  '''A python API to interact with the api.gostatit.com core web API'''
  
  def __init__(self, username: str, apikey: str):
    self.username = username
    self.apikey = apikey

  def post(self, action: str, inputDict: dict):
    url = urljoin(ENDPOINT, 'core')
    json = {'action': action, 'input': inputDict}
    r = requests.post(url, auth=(self.username, self.apikey), json=json)
    if r.status_code != 200:
      raise ValueError(r.text)
    return r.json()


  def getSerie(self, ID: str) -> dict:
    return self.post('getSerie', {'id': ID})

  def listSeries(self, parentID: str) -> list[dict]:
    return self.post('listSeries', {'id': parentID})

  def deleteSerie(self, ID: str):
    return self.post('deleteSerie', {'id': ID})


  def getSerieJSON(self, inputDict: dict) -> dict:
    return self.post('getSerie', inputDict)

  def batchGetSerieJSON(self, inputDict: list[dict]):
    return self.post('batchGetSerie', inputDict)

  def getAllSeriesJSON(self, inputDict: list[dict]):
    batch = []
    for serie in inputDict:
      batch.append(serie)
      if len(batch) == 25:
        yield self.batchGetSerieJSON(batch)
        batch = []
    if batch:
      yield self.batchGetSerieJSON(batch)

  def listSeriesJSON(self, inputDict: dict) -> list[dict]:
    return self.post('listSeries', inputDict)

  def putSerieJSON(self, inputDict: dict):
    return self.post('putSerie', inputDict)

  def batchPutSerieJSON(self, inputDict: list[dict]):
    return self.post('batchPutSerie', inputDict)

  def putAllSeriesJSON(self, inputDict: list[dict]):
    batch = []
    for serie in inputDict:
      batch.append(serie)
      if len(batch) == 25:
        yield self.batchPutSerieJSON(batch)
        batch = []
    if batch:
      yield self.batchPutSerieJSON(batch)

  def updateSerieJSON(self, inputDict: dict):
    return self.post('updateSerie', inputDict)

  def deleteSerieJSON(self, inputDict: dict):
    return self.post('deleteSerie', inputDict)

  def batchDeleteSerieJSON(self, inputDict: list[dict]):
    return self.post('batchDeleteSerie', inputDict)

  def deleteAllSeriesJSON(self, inputDict: list[dict]):
    batch = []
    for serie in inputDict:
      batch.append(serie)
      if len(batch) == 25:
        yield self.batchDeleteSerieJSON(batch)
        batch = []
    if batch:
      yield self.batchDeleteSerieJSON(batch)



class functionsAPI:
  '''A python API to interact with the api.gostatit.com functions web API'''

  def __init__(self, username: str, apikey: str):
    self.username = username
    self.apikey = apikey

  def post(self, action: str, inputDict: dict):
    url = urljoin(ENDPOINT, 'functions')
    json = {'action': action, 'input': inputDict}
    r = requests.post(url, auth=(self.username, self.apikey), json=json)
    if r.status_code != 200:
      raise ValueError(r.text)
    return r.json()


  def getObs(self, ID: str, end=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    return self.post('getObs', inputDict)

  def getObsSum(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getObsSum', inputDict)

  def getObsAverage(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getObsAverage', inputDict)

  def getObsChange(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getObsChange', inputDict)

  def getObsChangePercent(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getObsChangePercent', inputDict)

  def getObsDate(self, ID: str, end=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    return self.post('getObsDate', inputDict)

  def getPoint(self, ID: str, end=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    return self.post('getPoint', inputDict)

  def getPointSum(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getPointSum', inputDict)

  def getPointAverage(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getPointAverage', inputDict)

  def getPointChange(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getPointChange', inputDict)

  def getPointChangePercent(self, ID: str, end=None, periods=None):
    inputDict = {'id': ID}
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getPointChangePercent', inputDict)

  def getSerie(self, ID: str, start=None, end=None):
    inputDict = {'id': ID}
    if start is not None:
      inputDict['start'] = start
    if end is not None:
      inputDict['end'] = end
    return self.post('getSerie', inputDict)

  def getSerieSum(self, ID: str, start=None, end=None, periods=None):
    inputDict = {'id': ID}
    if start is not None:
      inputDict['start'] = start
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getSerieSum', inputDict)

  def getSerieAverage(self, ID: str, start=None, end=None, periods=None):
    inputDict = {'id': ID}
    if start is not None:
      inputDict['start'] = start
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getSerieAverage', inputDict)

  def getSerieChange(self, ID: str, start=None, end=None, periods=None):
    inputDict = {'id': ID}
    if start is not None:
      inputDict['start'] = start
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getSerieChange', inputDict)

  def getSerieChangePercent(self, ID: str, start=None, end=None, periods=None):
    inputDict = {'id': ID}
    if start is not None:
      inputDict['start'] = start
    if end is not None:
      inputDict['end'] = end
    if periods is not None:
      inputDict['periods'] = periods
    return self.post('getSerieChangePercent', inputDict)

  

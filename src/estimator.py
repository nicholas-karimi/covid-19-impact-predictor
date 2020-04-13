import math
def infectionsByTime(periodType, timeToElapse):
      # check the periodType
      if periodType == 'days':
            days = timeToElapse
            pair = (days / 3)
            return (math.pow(pair, 2))
      elif periodType == 'weeks':
            days = timeToElapse * 7
            pair = (days / 3)
            return (math.pow(pair, 2))
      elif periodType == 'months':
            days = timeToElapse * 30
            pair = (days / 3)
            return (math.pow(pair,2))



def impact(data, impactType):
      reportedCases = data['reportedCases']
      if impactType == 'normal':
            currentlyInfected = math.floor(reportedCases * 10)
      elif impactType == 'severe':
            currentlyInfected = math.floor(reportedCases * 50)
      
      timeToElapse = data['timeToElapse']
      periodType = data['periodType']

      time = infectionsByTime(periodType, timeToElapse)

      infectionsByRequestedTime = math.floor(currentlyInfected * time)

      return dict(currentlyInfected = currentlyInfected,
                        infectionsByRequestedTime = infectionsByRequestedTime)

def estimator(data):
      data = {
            'data': data ,
            
            'impact': impact(data, 'normal'),
            'severeImpact': impact(data, 'severe'),
      }
      return data







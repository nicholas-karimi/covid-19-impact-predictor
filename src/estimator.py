import math
def infectionsByTime(periodType, timeToElapse):
      # check the periodType
      if periodType == 'days':
            days = timeToElapse
            pair = (days / 3)
            return (int(2 ** pair))
      elif periodType == 'weeks':
            days = timeToElapse * 7
            pair = (days / 3)
            return (int(2** pair))
      elif periodType == 'months':
            days = timeToElapse * 30
            pair = (days / 3)
            return (int(2 **pair))



def bedCapacity(totalHospitalBeds, severeCasesByRequestedTime):
      occupiedBeds = int(totalHospitalBeds * 0.65)
      availableBeds = totalHospitalBeds - occupiedBeds
      availableForSevereCases = availableBeds - severeCasesByRequestedTime

      return int(availableForSevereCases)

def dollarFlight(infectionByTime, avgDailyIncomeInUSD, avgDailyIncomePopulation, periodType, time):
      days = infectionsByTime(periodType, time)
      return int((infectionByTime * avgDailyIncomeInUSD * avgDailyIncomePopulation)/days)

def impact(data, impactType):
      reportedCases = data['reportedCases']
      if impactType == 'normal':
            currentlyInfected = int(reportedCases * 10)
      elif impactType == 'severe':
            currentlyInfected = int(reportedCases * 50)
      
      timeToElapse = data['timeToElapse']
      periodType = data['periodType']

      time = infectionsByTime(periodType, timeToElapse)

      infectionsByRequestedTime = int(currentlyInfected * time)

      severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)

      totalBeds = data['totalHospitalBeds']

      hospitalBedsByRequestedTime = bedCapacity(totalBeds, severeCasesByRequestedTime)

      casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)

      casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)

      avgIncome = data['region']['avgDailyIncomeInUSD']
      avgIncomePopulation = data['region']['avgDailyIncomePopulation']

      dollarInFlight = dollarFlight(infectionsByRequestedTime, avgIncome, 
                                    avgIncomePopulation, periodType, timeToElapse)

      return dict(currentlyInfected = currentlyInfected,
                        infectionsByRequestedTime = infectionsByRequestedTime,
                        severeCasesByRequestedTime = severeCasesByRequestedTime,
                        hospitalBedsByRequestedTime = hospitalBedsByRequestedTime,
                        casesForICUByRequestedTime = casesForICUByRequestedTime,
                        casesForVentilatorsByRequestedTime = casesForVentilatorsByRequestedTime,
                        dollarInFlight = '{:.2f}'.format(dollarInFlight))

def estimator(data):
      data = {
            'data': data ,
            
            'impact': impact(data, 'normal'),
            'severeImpact': impact(data, 'severe'),
      }
      return data



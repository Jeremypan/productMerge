def make_json(csvFilePath):
    import csv
    # create a dictionary
    data = []
     
    # Open a csv reader called DictReader
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            data.append(rows)
    return data

output=make_json("./output/result_output.csv")
testResult=make_json("./testResult/result_output.csv")


def unitTest(output, testResult):
  try:
      for row in output:
        assert row in testResult
      for row in testResult:
        assert row in output
  except AssertionError:
      print("Unit Test Fail")
  else:
      print("Unit Test Pass")
      
    
    
unitTest(output,testResult)
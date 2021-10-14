import json
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
      #To check if there is duplicate result at output
      try:
        assert len(set([tuple(o.items()) for o in output]))==len(output)
      except AssertionError:
        print("Unit Test Fail, Output Has duplicates")
      #Initial check if the output has the same size as the correct results
      try:
        assert len(output)==len(testResult)
      except AssertionError:
        print("Unit Test Fail, the output size is different from the correct result")
      finally:
        try:
        #To check if output has correct result
            for row in output:
                assert row in testResult, "Unit Test Fail, Output "+json.dumps(row)+" is the incorrect result"
        #To check if output contain all of correct results
            for row in testResult:
                assert row in output, "Unit Test Fail, Output does not contain correct Result " + json.dumps(row)
        except AssertionError as msg:
            print(msg)
        else:
            print("Unit Test Pass")    
unitTest(output,testResult)


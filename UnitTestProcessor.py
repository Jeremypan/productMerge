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
        #To identify the missing result
        if(len(output)<len(testResult)):
            for row in testResult:
                if row not in output:
                    print("Unit Test Fail, Output does not contain correct Result " + json.dumps(row))
        else:
            for row in output:
                if row not in testResult:
                    print("Unit Test Fail, " + json.dumps(row) + " is the incorrect Result")
            
      else:
        try:
        #To check if output has correct result
            for row in output:
                assert row in testResult, "Unit Test Fail, Output "+json.dumps(row)+" is the incorrect result"
        except AssertionError as msg:
            print(msg)
        else:
            print("Unit Test Pass")
           
unitTest(output,testResult)


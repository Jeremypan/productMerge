import csv
def make_json(csvFilePath):
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


barcodesA=make_json("./input/barcodesA.csv")
barcodesB=make_json("./input/barcodesB.csv")
catalogA=make_json("./input/catalogA.csv")
catalogB=make_json("./input/catalogB.csv")

def make_matchingResult(barcodesA,barcodesB,catalogA,catalogB):
    result = []
    for A in catalogA:
        #Find Matching SKU in barcodesA
        barcodeAList = findBarCodeList(A['SKU'],barcodesA)
        #Put product from catalogA to result
        result.append({ "SKU":A['SKU'], "Description": A['Description'], "Source":"A"})
        #Process catalogB with barcodes with SKU from one of product in catalogA
        catalogB = catalogMatching(barcodeAList,barcodesB,catalogB)
    for B in catalogB:
        result.append({"SKU":B["SKU"], "Description":B['Description'], "Source":"B"})
    with open('./output/result_output.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SKU','Description','Source'])
        for res in result:
            writer.writerow([res['SKU'],res['Description'],res['Source']])
    return result


def findBarCodeList(sku,barcodes):
    return [obj['Barcode'] for obj in barcodes if obj['SKU']==sku]


def catalogMatching(barcodesList,barcodes,catalog):
    for barcodeObj in barcodes:
        if barcodeObj['Barcode'] in barcodesList:
           target=barcodeObj['SKU']
           for cataObj in catalog:
               if (cataObj['SKU']==target):
                   catalog.remove(cataObj)
    return catalog

print(make_matchingResult(barcodesA,barcodesB,catalogA,catalogB))

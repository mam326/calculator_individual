import csv

def getFileData(filepath):
    data = []
    with open(filepath, "r") as text_data:
        next(text_data)
        for row in text_data:
            numbers = row.split(",")
            data.append(numbers)
    text_data.close()
    return(data)


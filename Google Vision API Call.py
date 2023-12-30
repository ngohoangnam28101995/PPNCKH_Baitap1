import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types 
import pandas as pd
from os import listdir,path
from os.path import isfile, join
import numpy as np

#Need to provide "ServiceAccountToken.json" file to use
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'ServiceAccountToken.json'

#Call Google Vision API
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    result = []
    if len(texts) > 0:
        result = texts[0].description.encode('utf-8')
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message))
    return result

#Call API for all folder file
def mass_process_folder(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    col = []
    for i in onlyfiles:
        result = detect_text(f'{path}/{i}')
        if result == []:
            result = ''
        col.append(result)
    return col

folder = "Picture Data"
all_folder = [x for x in listdir('.') if path.isdir(x) is True]
all_folder.sort(reverse=True)

#Create label col dataframe:
onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
label_col = []
for i in onlyfiles:
    label_col.append(i.replace(".jpg","").encode("utf-8"))
df = pd.DataFrame({"label":label_col})

#Loop through other brightness
for f in all_folder:
    col = mass_process_folder(f)
    df[f] = col

#Save result data
df.to_excel("Result.xlsx",sheet_name="Sheet1",engine='xlsxwriter')





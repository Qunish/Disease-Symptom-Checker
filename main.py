from fastapi import FastAPI
import nest_asyncio
import uvicorn
from fuzzywuzzy import fuzz
from textblob import TextBlob

app = FastAPI()

info = {"stroke": "Sudden numbness or weakness in the face, arm, or leg, especially on one side of the body. Sudden confusion, trouble speaking, or difficulty understanding speech. Sudden trouble seeing in one or both eyes. Sudden trouble walking, dizziness, loss of balance, or lack of coordination.",
        "cancer": "Fatigue. Lump or area of thickening that can be felt under the skin. Weight changes, including unintended loss or gain. Skin changes, such as yellowing, darkening or redness of the skin, sores that won't heal, or changes to existing moles. Changes in bowel or bladder habits. Persistent cough or trouble breathing. Difficulty swallowing. Hoarseness. Persistent indigestion or discomfort after eating. Persistent, unexplained muscle or joint pain. Persistent, unexplained fevers or night sweats. Unexplained bleeding or bruising",
        "arthritis": "Pain. Stiffness. Swelling. Redness. Decreased range of motion",
        "pneumonia": "Chest pain when you breathe or cough. Confusion or changes in mental awareness (in adults age 65 and older). Cough, which may produce phlegm. Fatigue. Fever, sweating and shaking chills. Lower than normal body temperature (in adults older than age 65 and people with weak immune systems). Nausea, vomiting or diarrhea. Shortness of breath",
        "vertigo": "Problem focusing the eyes. Dizziness. Hearing loss in one or both ears. Loss of balance (may cause falls). Ringing in the ears. Nausea and vomiting, leading to loss of body fluids."}

def QDiseaseBotDriver(disease_name):
    q = TextBlob(disease_name)
    r = []
    for key, value in info.items():
        r.append(fuzz.token_set_ratio(q, key))
    for key, value in info.items():
        if fuzz.token_set_ratio(q, key) == max(r):
            return {"Symptoms of "+ key: value}
   
@app.get("/disease/{disease_name}")
async def getDiseaseSymptoms(disease_name: str):
    result = QDiseaseBotDriver(disease_name)
    return result

nest_asyncio.apply()
uvicorn.run(app, port=7000)
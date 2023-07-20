# Disease Symptoms Lookup API using FastAPI

This project is a Disease Symptoms Lookup API built using FastAPI, a modern web framework for building APIs with Python. The API allows users to input a disease name and retrieves the corresponding symptoms for that disease. The disease names and their symptoms are predefined in the code.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- FuzzyWuzzy
- TextBlob

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:

```bash
pip install fastapi uvicorn fuzzywuzzy textblob
```

## How to Use

1. Run the application by executing the following command:

```bash
python app.py
```

2. The application will start running at http://localhost:7000.

## Endpoint

### Get Disease Symptoms

- **Endpoint:** `/disease/{disease_name}`
- **Method:** GET
- **Input:** `disease_name` (string) - The name of the disease for which symptoms are to be retrieved.
- **Output:** JSON response containing the symptoms of the given disease.

## Sample Usage

Below is an example of how to use the API to get disease symptoms:

```python
import requests

response = requests.get("http://localhost:7000/disease/stroke")
print(response.json())  # Returns the symptoms of stroke
```

## Disease Information

The API contains predefined information about various diseases and their symptoms. The diseases and their symptoms are stored in the `info` dictionary within the code. Here are some sample disease entries:

- **Stroke:**
    - Sudden numbness or weakness in the face, arm, or leg, especially on one side of the body.
    - Sudden confusion, trouble speaking, or difficulty understanding speech.
    - Sudden trouble seeing in one or both eyes.
    - Sudden trouble walking, dizziness, loss of balance, or lack of coordination.

- **Cancer:**
    - Fatigue.
    - Lump or area of thickening that can be felt under the skin.
    - Weight changes, including unintended loss or gain.
    - Skin changes, such as yellowing, darkening or redness of the skin, sores that won't heal, or changes to existing moles.
    - Changes in bowel or bladder habits.
    - Persistent cough or trouble breathing.
    - Difficulty swallowing.
    - Hoarseness.
    - Persistent indigestion or discomfort after eating.
    - Persistent, unexplained muscle or joint pain.
    - Persistent, unexplained fevers or night sweats.
    - Unexplained bleeding or bruising.

- **Arthritis:**
    - Pain.
    - Stiffness.
    - Swelling.
    - Redness.
    - Decreased range of motion.

- **Pneumonia:**
    - Chest pain when you breathe or cough.
    - Confusion or changes in mental awareness (in adults age 65 and older).
    - Cough, which may produce phlegm.
    - Fatigue.
    - Fever, sweating and shaking chills.
    - Lower than normal body temperature (in adults older than age 65 and people with weak immune systems).
    - Nausea, vomiting or diarrhea.
    - Shortness of breath.

- **Vertigo:**
    - Problem focusing the eyes.
    - Dizziness.
    - Hearing loss in one or both ears.
    - Loss of balance (may cause falls).
    - Ringing in the ears.
    - Nausea and vomiting, leading to loss of body fluids.

## Acknowledgments

This project was inspired by the need to provide a simple API for retrieving disease symptoms based on user input. The FuzzyWuzzy and TextBlob libraries are used to handle fuzzy matching and text processing for better disease name matching.
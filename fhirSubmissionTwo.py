import matplotlib.pyplot as plt
import pandas as pd
import requests
from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()
url = "http://127.0.0.1:5002/api/fhirsubmission/"

data = requests.get(url)
data = data.json()
languages =  data["language"]
femaleData = data["female"]
maleData = data["male"]
r = []
raw_data = {}
raw_data["femaleBars"] = []
raw_data["maleBars"] = []

for x in range(len(languages)):
    r.append(x)
    raw_data["femaleBars"].append(femaleData[languages[x]])
    raw_data["maleBars"].append(maleData[languages[x]])


df = pd.DataFrame(raw_data)
totals = [i+j for i,j in zip(df['femaleBars'], df['maleBars'])]
pinkBars = [i / j * 100 for i,j in zip(df['femaleBars'], totals)]
darkBlueBars = [i / j * 100 for i,j in zip(df['maleBars'], totals)]


# plot
barWidth = 0.85



plt.bar(r, darkBlueBars, color='#4095F6', edgecolor='white', width=barWidth, label="Male")
# Create blue Bars
plt.bar(r, pinkBars, bottom=darkBlueBars, color='#F7C1FC', edgecolor='white', width=barWidth, label="Female")
# Custom x axis
plt.xticks(r, languages)
plt.xlabel("Languages (ISO 639-1 Language Codes)")
plt.ylabel("Percentage of People")
plt.title("Languages Spoken Separated by Gender")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Show graphic
plt.show()




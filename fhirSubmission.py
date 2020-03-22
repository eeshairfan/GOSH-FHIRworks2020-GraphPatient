import matplotlib.pyplot as plt
import pandas as pd
import requests
from fhir_parser import FHIR

fhir = FHIR()
patients = fhir.get_all_patients()

url = "http://127.0.0.1:5002/api/fhirsubmission/"

returnData = requests.get(url)
returnData = returnData.json()
data = returnData["data"]

r = [0,1]
raw_data = {'darkPinkBars': [data["USMarriedfemale"], data["UKMarriedfemale"]], 'darkBlueBars': [data["USMarriedmale"], data["UKMarriedmale"]],'pinkBars': [data["USNever Marriedfemale"], data["UKNever Marriedfemale"]], 'blueBars': [data["USNever Marriedmale"], data["UKNever Marriedmale"]]}
df = pd.DataFrame(raw_data)
totals = [i+j+k+l for i,j,k,l in zip(df['darkPinkBars'], df['darkBlueBars'], df['pinkBars'], df['blueBars'])]
darkPinkBars = [i / j * 100 for i,j in zip(df['darkPinkBars'], totals)]
darkBlueBars = [i / j * 100 for i,j in zip(df['darkBlueBars'], totals)]
pinkBars = [i / j * 100 for i,j in zip(df['pinkBars'], totals)]
blueBars = [i / j * 100 for i,j in zip(df['blueBars'], totals)]

# plot
barWidth = 0.5
names = ('US', 'UK')

# Create green Bars
plt.bar(r, darkPinkBars, color='#F866FF', edgecolor='white', width=barWidth, label="Married Female")
# Create orange Bars
plt.bar(r, darkBlueBars, bottom=darkPinkBars, color='#4095F6', edgecolor='white', width=barWidth, label="Married Male")
# Create blue Bars
plt.bar(r, pinkBars, bottom=[i + j for i, j in zip(darkPinkBars, darkBlueBars)], color='#F7C1FC', edgecolor='white', width=barWidth, label="Single Female")
plt.bar(r, blueBars, bottom=[i + j + k for i, j, k in zip(darkPinkBars, darkBlueBars, pinkBars)], color='#C3E7FC', edgecolor='white', width=barWidth, label="Single Male")

# Custom x axis
plt.xticks(r, names)
plt.xlabel("Location")
plt.ylabel("Percentage of People")
plt.title("Married/Single Male/Female in US and UK")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Show graphic
plt.show()




from flask import Flask
from flask_restful import Api, Resource
from fhir_parser.fhir import FHIR

app = Flask(__name__)
api = Api(app)
fhir = FHIR()
patients = fhir.get_all_patients()

languageConversion = {}
languageConversion['English'] = "en"
languageConversion["Spanish"] = "es"
languageConversion["French"] = "fr"
languageConversion["Italian"] = "it"
languageConversion["Greek"] = "el"
languageConversion["Hindi"] = "hi"
languageConversion["Portugese"] = "pt"
languageConversion["Chinese"] = "zh"
languageConversion["Russian (Russia)"] = "ru"
languageConversion["German (Germany)"] = "de"
languageConversion["Korean"] = "ko"
languageConversion["Vietnamese"] = "vi"
languageConversion["Japanese"] = "ja"
languageConversion["Portuguese"] = "pt"


class Data(Resource):
    def __init__(self):
        super(Data, self).__init__()

    def get(self):

        languages = []
        femaleData = {}
        maleData = {}
        data = {}
        data["USMarriedfemale"] = 0
        data["USMarriedmale"] = 0
        data["UKMarriedfemale"] = 0
        data["UKMarriedmale"] = 0
        data["UKNever Marriedfemale"] = 0
        data["UKNever Marriedmale"] = 0
        data["USNever Marriedmale"] = 0
        data["USNever Marriedfemale"] = 0

        for patient in patients:
            '''GRAPH 1'''
            country = patient.addresses[0].country
            maritalStatus = patient.marital_status
            gender = patient.gender
            details = str(country) + str(maritalStatus) + str(gender)
            data[details] += 1

            '''GRAPH 2'''
            language = str(patient.communications.languages)
            gender = str(patient.gender)
            length = len(language) - 2
            language = language[2:length]
            if language == "French (France)":
                language = "French"
            language = languageConversion[language]
            if language not in languages:
                languages.append(language)
                femaleData[language] = 0
                maleData[language] = 0

            if gender == "female":
                femaleData[language] += 1
            else:
                maleData[language] += 1
        returnData = {}
        returnData["female"] = femaleData
        returnData["male"] = maleData
        returnData["language"] = languages
        returnData["data"] = data
        return returnData


api.add_resource(Data, "/api/fhirsubmission/", endpoint="graph")

if __name__ == "__main__":
    app.run(debug=True, port=5002)

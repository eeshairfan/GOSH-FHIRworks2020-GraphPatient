# FHIR Submission


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the libraries and packages used in the code.

```bash
pip install -r requirements.txt
```

## How to Setup

The following github repo, [FHIRworks_2020](https://github.com/greenfrogs/FHIRworks_2020) was used to extract data from. Follow the README so that you have correctly installed Visual Studio Code and .NET Core 2.1 SDK 2.1.803 and to ensure that you have correctly setup the appsettings.json file with the relevant Azure FHIR API credentials. This is to setup the dotnet so that the command, ***dotnet run*** works.
<br />
You must also clone this repository.


## How to Run

cd into FHIRworks_2020\dotnet-azure-fhir-web-api. Then run the following commands in the terminal

```powershell
dotnet run
```

Then cd back to the folder where this repository was cloned. Then run apiDocuments.py in the bash terminal to start the server with the following command.

```bash
python apiDocuments.py
```

Then to display the graphs run any two of the following files.

```bash
python fhirSubmission.py
python fhirSubmissionTwo.py
```

## Graphs 
fhirSubmission.py and fhirSubmissionTwo.py are the python files that display the graphs. 

**Graph 1**
Displays a stacked bar chart that visually shows the proportional differences between the different combinations made by the attributes male/female, married/never married and US/UK. 

**Graph 2**
Displays a stacked bar chart that visually shows the differences in the ratio of male to female speakers of every language that is stored in the records. 

## Data Types
The code makes use of flask to create API that interfaces between the python files that displays graphs and the fhir records. When the python files access this URL"http://127.0.0.1:5002/api/fhirsubmission/", it requests data from the fhir records which is organised into dictionaries and arrays in the get function. 

The data returned from the API call is returnData which is a dictionary which is accessed as a JSON object.

Key/Value Pairs of returnData <br />
**data** : ***(Graph 1)*** Dictionary where the keys are the different combinations of US/UK, male/female and married/never married. The values are the count of those in the fhir records. <br />
**female** : ***(Graph 2)*** Dictionary where languages are the key and a count of the number of females who speak the language as the value <br />
**male** : ***(Graph 2)*** Dictionary where languages are the key and a count of the number of males who speak the language as the value. <br />
**language** : ***(Graph 2)*** Array of all the languages to be displayed on the graph. 

## Citations
In the code, I made use of Ethan Wood's [fhir-parser](https://github.com/greenfrogs/FHIR-Parser) to make it easier for me to extract and parse data from the tables given. I also used the github repo [FHIRworks_2020](https://github.com/greenfrogs/FHIRworks_2020).

## License
[MIT](https://choosealicense.com/licenses/mit/)

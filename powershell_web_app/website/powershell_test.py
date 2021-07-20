import subprocess
import os 
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
powershell_path = "%s\\powershell\\" % dir_path
script_path = "%s\\Test2.ps1" % powershell_path

def run_powershell_script(Name, Surname):
    
    firstname = Name
    lastname = Surname

    args2 = ['-FIRSTNAME', firstname, '-LASTNAME', lastname]

    result = subprocess.check_output([
        'powershell.exe',
        script_path,
        *args2,
    ])

    return result

# jsonValue = run_powershell_script("Patryk", "Golebiowski")
# jsonValue = json.loads(jsonValue)

# print(jsonValue["FirstName"])
# print(jsonValue["LastName"])
# print(jsonValue["FullName"])
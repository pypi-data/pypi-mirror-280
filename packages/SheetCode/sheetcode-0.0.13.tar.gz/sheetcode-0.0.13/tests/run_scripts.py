import os
import importlib
import sys
sys.path.append(".")

from SheetCode import Overview



# Set global constants
os.environ["TEST_SHEETS_PATH"] = "tests/sheets"
os.environ["TRACEABILITY_PATH"] = "tests/traceability"
os.environ["OVERVIEW_PATH"] = "tests/overview"
os.environ["RVT_FILEPATH"] = "../../../../DAA-000048 RVT/2A - Ongoing/DAA-000048_2A.xlsm"
os.environ["PARAMETERS_FILEPATH"] = "../Traceability/A-0000175109 1B App A_Traceability_RBC_9.4.0.xlsm"
os.environ["MODE"] = "Specification" # Specification or Execution

Overview.Clear()

# Set folder where .py scripts are located
scriptsDirectory = "scripts"

scriptNames = ["Example"] # Set to [] to run all scripts

if len(scriptNames) != 0:
    for scriptName in scriptNames:
        script = importlib.import_module(f"{scriptsDirectory}.{scriptName}")
        Overview.Store(script.sheet)
else:
    scriptFilePaths = os.listdir(scriptsDirectory)
    for scriptFilepath in scriptFilePaths:
        script = importlib.import_module(f"{scriptsDirectory}.{os.path(scriptFilepath).stem}")
        Overview.Store(script.sheet)

Overview.Save()

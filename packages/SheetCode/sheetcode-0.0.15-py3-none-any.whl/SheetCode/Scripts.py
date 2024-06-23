import os
import importlib
from . import Summary, Traceability
from enum import Enum
from termcolor import colored # need pip install termcolor

class Mode(Enum):
     Specification = 0
     Execution = 1

IsConfigured = False

def Configure(*,specId:str ,
                specVersion:str,
                scriptsPath:str = "scripts",
                sheetsPath:str = "sheets",
                traceabilityPath:str = "traceability",
                summaryPath:str = "summary", 
                rvtFilepath:str = "",
                parametersFilepath:str = "",
                mode: Mode):
    """ Configure SheetCode with:
    - specId : The MANDATORY prefix that will be added to each sheet name, identifying the test specification (e.g. BDV for Balise Data Verification)
    - specVersion : The MANDATORY version of the specification that will be added inside each sheet (e.g. 1A, 2A, A)
    - scriptsPath : Folder name where PY scripts are stored. Default is 'scripts'
    - sheetPath : Folder name where XLS test sheet will be created. Default is 'sheets'
    - traceabilityPath : Folder name where the incremental traceability will be stored. 
                        This can be use to populate the RVT.Default is 'traceability'
    - summaryPath : Folder name where XLS summary file will be created. 
                    This files stores the status of all sheets. Default is "summary". 
    - rvtFilePath : Defines the path to a RVT XLS file. SheetCode will search for any test allocated to a test sheet and will check the traceability.
                    If you don't want to check RVT traceability, do not set rvtFilePath (or leave it to default empty string).
    - parametersFilepath : Defines the path to a parameters XLS file. SheetCode will search for any test allocated to a parameter path and will check the traceability.
                    If you don't want to check parameters traceability, do not set parametersFilepath (or leave it to default empty string).
    - Mode : 
        - If set to Scripts.Mode.Specification, SheetCode will only execute Case, Action and ExpectedResult commands (not Result).
        - If set to Scripts.Mode.Execution, SheetCode will also execute Result command).
    """

    os.environ["TEST_SPEC_ID"] = specId
    os.environ["TEST_SPEC_VERSION"] = specVersion
    os.environ["TEST_SCRIPTS_PATH"] = scriptsPath
    os.environ["TEST_SHEETS_PATH"] = sheetsPath
    os.environ["TRACEABILITY_PATH"] = traceabilityPath
    os.environ["SUMMARY_PATH"] = summaryPath
    os.environ["RVT_FILEPATH"] =  rvtFilepath
    os.environ["PARAMETERS_FILEPATH"] = parametersFilepath
    os.environ["MODE"] = "Specification" if mode == Mode.Specification else "Execution"

    global IsConfigured
    IsConfigured = True

def Run(scriptNames):
    """ Run a specific script in scriptsPath, or a list of scripts.
    You can set scriptNames either to a single script name, or a [list of script names] """
    _CheckIsConfigured()
    scriptsPath = os.environ["TEST_SCRIPTS_PATH"]
    if type(scriptNames) is str: scriptNames = [scriptNames] # if string, make it a list of one string
    for scriptName in scriptNames:
            script = importlib.import_module(f"{scriptsPath}.{scriptName}")
            Summary.Store(script.sheet)
    Summary.Save()

def RunAll():
    """ Run all scripts in scriptsPath."""
    _CheckIsConfigured()
    Summary.Clear()
    Traceability.Clear()
    scriptsPath = os.environ["TEST_SCRIPTS_PATH"]
    scriptFilePaths = os.listdir(scriptsPath)
    for scriptFilepath in scriptFilePaths:
        script = importlib.import_module(f"{scriptsPath}.{os.path(scriptFilepath).stem}")
        Summary.Store(script.sheet)
    Summary.Save()

def _CheckIsConfigured():
    if not IsConfigured:
        raise Exception("Scripts must be configured preliminarily using Scripts.Configure() !")
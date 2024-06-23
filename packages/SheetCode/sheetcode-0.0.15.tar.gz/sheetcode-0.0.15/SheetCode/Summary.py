import os
from openpyxl.workbook import Workbook # need pip install openpyxl
import SheetCode as Sheet
import pandas as pd
from termcolor import colored # need pip install termcolor
from tabulate import tabulate

Sheets = pd.DataFrame(columns=['Reference',
                                       'Name',
                                       'Version',
                                       'Global Status',
                                       'Passed count',
                                       'Failed count',
                                       'Played at', 
                                       'Played by'])

Sheets['Passed count'] = Sheets['Passed count'].astype(int)
Sheets['Failed count'] = Sheets['Failed count'].astype(int)

def _GetSummaryFilepath():
    if not "SUMMARY_PATH" in os.environ:
        raise Exception("Environment variable SUMMARY_PATH is not set.\nUse os.environ['SUMMARY_PATH'] == '<Summary directory>' to set it.")
    
    return os.path.join(os.environ["SUMMARY_PATH"], "Summary.xlsx")

def Clear():
    Sheets = []

    summaryFilepath = _GetSummaryFilepath()

    if os.path.exists(summaryFilepath): os.remove(summaryFilepath)

def Store(sheet):
    print(colored(f"Storing sheet in summary", "green"))
    globalStatus = "No test done" if sheet.Statistics.GlobalStatus == None else "Passed" if sheet.Statistics.GlobalStatus else "FAILED"
    Sheets.loc[len(Sheets.index)] = [sheet.Reference, 
                                                     sheet.Name, 
                                                     sheet.Version, 
                                                     globalStatus, 
                                                     sheet.Statistics.PassedCount, 
                                                     sheet.Statistics.FailedCount, 
                                                     sheet.Statistics.PlayedAt,
                                                     sheet.Statistics.PlayedBy]

def Save():
    print(colored(f"Saving summary", "green"))
    print(tabulate(Sheets, headers='keys', tablefmt='simple_grid', showindex=False))

    summaryFilepath = _GetSummaryFilepath()
  
    # Create directory if not existing
    if not os.path.exists(os.environ["SUMMARY_PATH"]): os.mkdir(os.environ["SUMMARY_PATH"])

    # Load if existing
    if os.path.exists(summaryFilepath):
        existingSheets = pd.read_excel(summaryFilepath)

        joinedSheets = pd.concat([existingSheets, Sheets])
        joinedSheets = joinedSheets.sort_values('Played at').drop_duplicates('Reference', keep='last')
        joinedSheets = joinedSheets.sort_values('Reference')
        joinedSheets.to_excel(summaryFilepath, index=False)
    else:
        Sheets.to_excel(summaryFilepath, index=False)
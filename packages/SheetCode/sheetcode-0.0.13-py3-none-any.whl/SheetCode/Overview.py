import os
from openpyxl.workbook import Workbook # need pip install openpyxl
import SheetCode as Sheet
import pandas as pd
from termcolor import colored # need pip install termcolor
from tabulate import tabulate

SheetSummaries = pd.DataFrame(columns=['Reference','Name','Version','Global Status','Passed count','Failed count'])

def Clear():
    SheetSummaries = []

def Store(sheet):
    print(colored(f"Storing in overview", "green"))
    SheetSummaries.loc[len(SheetSummaries.index)] = [sheet.Reference, sheet.Name, sheet.Version, sheet.GlobalStatus, sheet.Statistics.PassedCount, sheet.Statistics.FailedCount]

def Save():
    print(colored(f"Saving overview", "green"))
    print(tabulate(SheetSummaries, headers='keys', tablefmt='simple_grid', showindex=False))
    
    if not os.path.exists(os.environ["OVERVIEW_PATH"]): os.mkdir(os.environ["OVERVIEW_PATH"])
    SheetSummaries.to_excel(os.path.join(os.environ["OVERVIEW_PATH"], "Overview.xlsx"), index=False)
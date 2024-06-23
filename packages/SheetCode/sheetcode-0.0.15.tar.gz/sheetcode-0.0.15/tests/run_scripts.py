import sys;sys.path.append(".")
from SheetCode import Scripts

Scripts.Configure(specId = "FCT",
                  specVersion = "1A",
                  scriptsPath = "scripts",
                  sheetsPath = "tests/sheets",
                  traceabilityPath = "tests/traceability",
                  summaryPath = "tests/summary",
                  rvtFilepath = "../../../../DAA-000048 RVT/2A - Ongoing/DAA-000048_2A.xlsm",
                  parametersFilepath = "../Traceability/A-0000175109 1B App A_Traceability_RBC_9.4.0.xlsm",
                  mode = Scripts.Mode.Execution)

Scripts.Run(["Example1", "Example2"])

#Scripts.RunAll()



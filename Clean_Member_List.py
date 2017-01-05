'''
Creator: Branden Connolly
Create Date: 1/5/2017
Purpose: drop header and footer from UHC Member list
'''

import pandas as pd
import os as os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

#select file to be cleaned
root.filename = filedialog.askopenfilename(initialdir = "I:/FMLH/Reporting/UHC_Member_Lists/",title = "Select file")
indataop = root.filename

#name the save file
root.filename = filedialog.asksaveasfilename(initialdir = "I:/FMLH/Reporting/UHC_Member_Lists/",title = "Name file")
outfileop = root.filename

#reads in pipe delimited file except header and footer 
df = pd.read_csv(indataop,engine = 'python', sep='|',skipfooter=1, header=1)

#outputs file as pipe delimited with out START and END tag
df.to_csv(outfileop,sep = '|',index = False)

#lets us know when the cleaning is finished
print('File Cleaning Finished')


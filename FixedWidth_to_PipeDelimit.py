
import Tkinter as tk,tkFileDialog, tkSimpleDialog

root = tk.Tk()
root.filename = tkFileDialog.askopenfilename(initialdir = "I:/FMLH/Reporting/Report Writers/Connolly_Branden",title = "Select file")
indataop = root.filename
print('Input pathway: ' + indataop)

root.filename = tkFileDialog.asksaveasfilename(initialdir = "I:/FMLH/Reporting/Report Writers/Connolly_Branden",title = "Select file")
outfileop = root.filename
print ('Output pathway: ' + outfileop)


width2 = tkSimpleDialog.askstring('List', 'Enter the fixed widths with commas seperating values: ')

list = [width2]
with open(outfileop, 'w') as outfile:
    with open(indataop, 'r') as infile:
        for line in infile:
            iter = 0
            prev_position = 0
            position = list[iter]
            temp = []
            while position < len(line) and iter + 1 < len(list):
                iter += 1
                temp.append(line[prev_position:position])
                prev_position = position
                position = list[iter]
            temp.append(line[prev_position:])

            temp_str = ''.join(x + "|" for x in temp)
            temp_str = temp_str[:-1]

            outfile.write(temp_str)

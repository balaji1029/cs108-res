from TexSoup import TexSoup
import os
import json
import tempfile
import time
import subprocess


overall = {
    "data": []
}

data = []

errors = [] # if marks deducted, push the reason as string in this list


msg = "Correct output."
total = 36
result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : total,
        "message": ""
    }
status = "success"
marks = 0

file = open("main.tex", 'r')
soup = TexSoup(file)

msg_list = []

## Checking sections
q = len(soup.find_all("section"))
if q == 3:
  marks += 3
else:
  marks += min(q, 3)
  msg_list.append(f"Number of sections != 3. Found {q}")

## Checking subsections
q = len(soup.find_all("subsection"))
if q == 3:
  marks += 3
else:
  marks += min(q, 3)
  msg_list.append(f"Number of subsections != 3. Found {q}")

## preamble
if soup.maketitle != None:
  marks += 1
else:
  msg_list.append("Preamble not found")

## table of contents
if soup.tableofcontents != None:
  marks += 1
else:
  msg_list.append("No table of contents")


## items in list
q = len(soup.find_all("item"))
if q == 2:
  marks += 2
else:
  marks += min(q, 2)
  msg_list.append(f"Number of items in list != 2. Found {q}")

## cross-references
q = len(soup.find_all("ref"))
if q == 2:
  marks += 2
else:
  marks += min(q, 2)
  msg_list.append(f"Number of ref tags != 2. Found {q}")

## Footnote
if soup.footnote != None:
  marks += 1
else:
  msg_list.append("Footnote not found")

## citations
q = len(soup.find_all("cite"))
if q == 3:
  marks += 3
else:
  marks += min(q, 3)
  msg_list.append(f"Number of citations != 3. Found {q}")

## diaplay math equations
if len(soup.find_all("\[")) == 3:
  marks += 3
else:
  tmp = len(soup.find_all("\["))
  marks += min(tmp, 3)
  msg_list.append(f"Number of display math equations in section 2 and section 3 not equal to 7. Found {tmp}")

# equation
if len(soup.find_all("equation")) == 2:
  marks += 4
else:
  tmp = len(soup.find_all("equation"))
  marks += min(2*tmp, 4)
  msg_list.append(f"Number of equation environments != 2. Found {tmp}")

# cases
if soup.equation != None and soup.equation.cases != None:
  marks += 1
else:
  msg_list.append("Cases not used in equation 1")

# figures
if soup.figure != None:
  marks += 1
else:
  msg_list.append("Figure not found")

# subfigures 
q = len(soup.find_all('subfigure'))
if q == 2:
  marks += 2
else:
  marks += min(q, 2)
  msg_list.append("Number of subfigures != 2")

## Table checking
if soup.tabular != None:
  marks += 1
else:
  msg_list.append("Table not found")

if soup.tabular != None and soup.tabular.multicolumn != None:
  marks += 1
else:
  msg_list.append("Multicolumn not present in table")


if soup.tabular != None:
  tabular_arg = soup.tabular.args[0].string
  vert_list = [i for i in range(len(tabular_arg)) if tabular_arg[i] == '|']
  if len(vert_list) == 5:
    marks += 1
  else:
    msg_list.append("5 Vertical lines in the table not found")
else:
  msg_list.append("5 Vertical lines in the table not found")

if len(soup.find_all("hline")) == 4:
  marks += 1
else:
  msg_list.append("Could not find 4 hline(s)")

if soup.fancyhf != None:
  marks += 1
else:
  msg_list.append("Use fancyhf for customizing headers and footer")

if soup.rhead != None:
  marks += 1
else:
  msg_list.append("Could not find rhead tag")

if soup.lhead != None:
  marks += 1
else:
  msg_list.append("Could not find lhead tag")

if soup.fancyfoot != None:
  marks += 1
else:
  msg_list.append("Could not find fancyfoot tag")

if soup.fancyfoot != None and soup.fancyfoot.args[0].string == 'C':
  marks += 1
else:
  msg_list.append("Page number not central aligned, use C arg in fancyfoot")

msg = ";  ".join([f"{i}) " + msg_list[i] for i in range(len(msg_list))])


completedProc = subprocess.run('/usr/local/texlive/2023/bin/x86_64-linux/pdflatex -interaction=nonstopmode main', shell=True)
if completedProc.returncode != 0:
  marks = 0 
  msg = "Compilation error after first command"
completedProc = subprocess.run('/usr/local/texlive/2023/bin/x86_64-linux/bibtex main', shell=True)
if completedProc.returncode != 0:
  marks = 0 
  msg = "Compilation error after second command"
completedProc = subprocess.run('/usr/local/texlive/2023/bin/x86_64-linux/pdflatex -interaction=nonstopmode main', shell=True)
if completedProc.returncode != 0:
  marks = 0 
  msg = "Compilation error after third command"

completedProc = subprocess.run('/usr/local/texlive/2023/bin/x86_64-linux/pdflatex -interaction=nonstopmode main', shell=True)
if completedProc.returncode != 0:
  marks = 0 
  msg = "Compilation error after third command"

result["score"] = marks
result["message"] = msg
data.append(result)

overall['data'] = data
print(json.dumps(overall, indent=4))

with open('../evaluate.json', 'w') as f:
  json.dump(overall,f,indent=4)

completedProc = subprocess.run('rm main*', shell=True)
completedProc = subprocess.run('rm references.bib', shell=True)


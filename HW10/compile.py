import os

os.system(r'cmd.exe /c taskkill /IM "Acrobat.exe"')
os.system(r"pdflatex template.tex")
os.system(r'cmd.exe /c start "template.pdf"')
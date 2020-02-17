import os

os.system(r'cmd.exe /c taskkill /IM "Acrobat.exe"')
os.system(r"pdflatex Template.tex")
os.system(r'cmd.exe /c start "Template.pdf"')
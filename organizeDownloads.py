import os
import shutil
import pathToPython

def organizeFiles(path: str):
    for filename in os.listdir(path):
        if(filename.endswith('.exe')):
            if(not(os.path.exists(path + '\\Applications'))):
                os.mkdir(path + '\\Applications')
            shutil.move(path + '\\' + filename, path + '\\Applications')
        elif(filename.endswith('jpg') or filename.endswith('.png') or filename.endswith('.JPG')):
            if(not(os.path.exists(path + '\\Images'))):
                os.mkdir(path + '\\Images')            
            shutil.move(path + '\\' + filename, path + '\\Images')
        elif(filename.endswith('.pdf')):
            if(not(os.path.exists(path + '\\PDFs'))):
                os.mkdir(path + '\\PDFs')
            shutil.move(path + '\\' + filename, path + '\\PDFs')
        elif(filename.endswith('.zip')):
            if(not(os.path.exists(path + '\\ZIPFiles'))):
                os.mkdir(path + '\\ZIPFiles')
            shutil.move(path + '\\' + filename, path + '\\ZIPFiles')
        elif(filename.endswith('.msi')):
            if(not(os.path.exists(path + '\\InstallationFiles'))):
                os.mkdir(path + '\\InstallationFiles')
            shutil.move(path + '\\' + filename, path + '\\InstallationFiles')
        elif(filename.endswith('.mp3') or filename.endswith('.wav')):
            if(not(os.path.exists(path + '\\MP3'))):
                os.mkdir(path + '\\MP3')
            shutil.move(path + '\\' + filename, path + '\\MP3')
        elif(filename.endswith('.txt')):
            if(not(os.path.exists(path + '\\TextFiles'))):
                os.mkdir(path + '\\TextFiles')
            shutil.move(path + '\\' + filename, path + '\\TextFiles')
        elif(filename.endswith('.xlsx') or filename.endswith('.xlsm')):
            if(not(os.path.exists(path + '\\ExcelFiles'))):
                os.mkdir(path + '\\ExcelFiles')
            shutil.move(path + '\\' + filename, path + '\\ExcelFiles')
        elif(filename.endswith('.docx')):
            if(not(os.path.exists(path + '\\WordFiles'))):
                os.mkdir(path + '\\WordFiles')
            shutil.move(path + '\\' + filename, path + '\\WordFiles')            


path = os.getcwd()
path = pathToPython.pythonPath(path)
organizeFiles(path)

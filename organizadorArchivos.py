import os
import shutil


documentos = "C:\\Users\\apuya\\Documents\\Documentos\\Documentos\\docs"
curent_dir = os.getcwd()

for f in os.listdir(documentos):
    filename,file_ext = os.path.splitext(f)
    try: 
        if not file_ext:
            pass
        elif file_ext in ('.docx'):
            shutil.move(
                os.path.join(documentos,f'{filename}{file_ext}'),
                os.path.join(documentos,'Word',f'{filename}{file_ext}'),
            )
        elif file_ext in ('.pptx'):
            shutil.move(
                os.path.join(documentos,f'{filename}{file_ext}'),
                os.path.join(documentos,'Powerpoint',f'{filename}{file_ext}'),
            )
        elif file_ext in ('.xlsx'):
            shutil.move(
                os.path.join(documentos,f'{filename}{file_ext}'),
                os.path.join(documentos,'Excel',f'{filename}{file_ext}'),
            )
            
        
    except (FileNotFoundError,PermissionError):
     pass

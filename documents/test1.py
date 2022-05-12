import subprocess

def doc2pdf_linux(doc):
    """
    convert a doc/docx document to pdf format (linux only, requires libreoffice)
    :param doc: path to document
    """
    cmd = 'libreoffice --convert-to pdf'.split() + [doc]
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=10)
    stdout, stderr = p.communicate()
    if stderr:
        raise subprocess.SubprocessError(stderr)
        


doc = "C:/Users/roysm/Documents/AlphaAI/linux_version/documents/AgencyAgreement.docx"
doc2pdf_linux(doc)
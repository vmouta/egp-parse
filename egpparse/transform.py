from os import rename, path
import zipfile
import time

def egptozip(egp):
    rename(egp, egp[:-4] + ".zip")


def egptocode(egp):
    """Extract the Project.xml file from an egp / zip file"""
    egptozip(egp)
    fp, egp_name = path.split(egp)
    fname = egp_name[:-4]
    zipped_egp = fp + '/' + fname + ".zip"

    if zipfile.is_zipfile(zipped_egp):
        # Yes it is a zip file
        zf = zipfile.ZipFile(zipped_egp)

        # Pull out the xml file containing the code
        zf.extract('project.xml', path=fp)

        # Check if file name already exists
        if path.isfile(fp + '/' + fname + ".xml"):
            xml_name = fname + str(int(round(time.time()))) + ".xml"
        else:
            xml_name = fname + ".xml"
        rename(fp + '/project.xml', fp + '/' + xml_name)

        zf.close()
        return xml_name
    else:
        return None
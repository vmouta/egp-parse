"""egpmove.py - Modify and Move EGPs"""
import zipfile
import os
import shutil
import time

def find_egps(cwd):
    """Find files with .EGP extension on network starting from cwd"""
    egp_list = []
    total_dir = os.walk(cwd)
    for (homedir, subdir, files) in total_dir:
        if len(files)>0:
            egp_list.extend([(homedir,file) for file in files if file[-4:]==".egp"])
    return egp_list

def move_zip_egp(egp_name, srcdir, dstdir):
    """Move EGP files to dstdir and give it a .zip extension"""
    shutil.copyfile(srcdir+'/'+egp_name,dstdir+'/'+egp_name[:-4]+'.zip')

def unpack_egp(homedir, egp_name, outdir):
    """Extract the Project.xml file from an egp / zip file"""
    print "Unpacking "+homedir+'/'+egp_name
    if zipfile.is_zipfile(homedir+'/'+egp_name):
        #IDed as a Zip File
        zf = zipfile.ZipFile(homedir+'/'+egp_name)
        try:
            zf.extract('project.xml',outdir)
            #Check if file name already exists
            new_name = egp_name[:-4]
            if os.path.isfile(outdir+'/'+new_name+'.xml'):
                new_name = new_name+str(int(round(time.time())))
            else:
                pass
            os.rename(outdir+'/project.xml',outdir+'/'+new_name+'.xml')
        except:
            print "Failed on %s" % egp_name
        zf.close()
    else:
        print "%20s is not a zip file" % egp_name


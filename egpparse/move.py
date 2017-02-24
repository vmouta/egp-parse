import shutil


def move_egp(idx, srcdir, egp_name, dstdir):
    """Move EGP files to dstdir and give it a .zip extension"""
    shutil.copyfile(srcdir + '/' + egp_name, dstdir + '/' + str(idx) + egp_name)
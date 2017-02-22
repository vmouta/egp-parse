import shutil


def move_egp(dir_egp_tuple, dstdir):
    """Move EGP files to dstdir and give it a .zip extension"""
    srcdir, egp_name = dir_egp_tuple
    shutil.copyfile(srcdir + '/' + egp_name, dstdir + '/' + egp_name)
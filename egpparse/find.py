import os


def find_egps(cwd):
    """Find files with .EGP extension on network starting from cwd"""
    egp_list = []
    total_dir = os.walk(cwd)
    for (homedir, subdir, files) in total_dir:
        if len(files) > 0:
            egp_list.extend([(homedir,file) for file in files if '.egp' == file[-4:]])

    return egp_list

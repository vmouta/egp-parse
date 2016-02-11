#!/usr/bin/env python

def write_program_list(file_list):
    with open('list_of_programs.txt','w') as fout:
        for (srcdir, egp) in file_list:
            mod_time = os.path.getmtime(srcdir+'/'+egp)
            mod_date = time.strftime('%Y-%m-%d', time.localtime(mod_time))
            fout.write('%s\t%s\t%s\n' % (srcdir, egp, mod_date))

def filter_dir_for(directory, ext):
    dir_contents = os.listdir(directory)
    return [afile for afile in dir_contents if afile[-len(ext):]==ext]

if __name__ == '__main__':
    import xmltodict
    import sys
    import re
    import os
    import shutil
    import time
    import egpmove
    import egpcols
    import operator
    
    startdir = sys.argv[1]
    outdir = sys.argv[2]

    file_list =  egpmove.find_egps(startdir)

    write_program_list(file_list)

    for (srcdir, egp) in file_list:
        egpmove.move_zip_egp(egp, srcdir, outdir)

    #Crawl the outdir to map new names of programs
    egps_as_zips = filter_dir_for(outdir, '.zip')

    #For every EGP, unzip it and extract project.xml file
    for egpzip in egps_as_zips:
        egpmove.unpack_egp(outdir,egpzip,outdir)

    #Identify list of XML documents
    xml_list = filter_dir_for(outdir, '.xml')

    #Loop through 
    for program in xml_list:
        with open(outdir+'/'+program,'r') as egp:
            xmldict = xmltodict.parse(egp.read())
            print '====='+program+'====='
            for query in egpcols.reach_task_code(xmldict):
                col_list = egpcols.list_columns(query)
                with open('column_list.txt','a') as coltxt:
                    for col in col_list:
                        coltxt.write('%s\t%s\n' % (program, col))

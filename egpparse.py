#!/usr/bin/env python
#f = open('query_test','r')
#qry = f.readlines()
#f.close()
#qry="".join(qry)

#from_line = re.compile('FROM(.+?)(?:WHERE|;)+?',flags=re.DOTALL).findall(qry)
#table_list = re.compile('\w+\.\w+\s\w+',flags=re.DOTALL).findall(''.join(from_line))
#select_line = re.compile('SELECT(.+?)FROM?',flags=re.DOTALL).findall(qry)
#column_list = re.compile('\w+\.(?:\'(?:\w|\s|#)+\'n|\w+)',flags = re.DOTALL).findall(select_line[0])

def write_program_list(file_list):
    with open('list_of_programs.txt','w') as fout:
        for (srcdir, egp) in file_list:
            mod_time = os.path.getmtime(srcdir+'/'+egp)
            mod_date = time.strftime('%Y-%m-%d', time.localtime(mod_time))
            fout.write('%s\t%s\t%s\n' % (srcdir, egp, mod_date))

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
    
    startdir = '/home/will/pyscripts'
    outdir = '/home/will/pyscripts/temp'
    file_list =  egpmove.find_egps(startdir)
    write_program_list(file_list)
    temp_zip_list = []
    for (srcdir, egp) in file_list:
        egpmove.move_zip_egp(egp, srcdir, outdir)
    #Crawl the outdir to map new names of programs
    new_zip_list = os.listdir(outdir)
    #For every EGP, unzip it and extract project.xml file
    for file in new_zip_list:
        if file[-4:]==".zip":
            egpmove.unpack_egp(outdir,file,outdir)
        else:
            pass
    #Identify list of XML documents
    xml_list_full = os.listdir(outdir)
    xml_list = [file for file in xml_list_full if file[-4:]==".xml"]
    for program in xml_list:
        with open(outdir+'/'+program,'r') as egp:
            xmldict = xmltodict.parse(egp.read())
            print program
            print "====================="
            for query in egpcols.reach_task_code(xmldict):
                col_list = egpcols.list_columns(query)
                with open('column_list.txt','a') as coltxt:
                    for col in col_list:
                        coltxt.write('%s\t%s\n' % (program, col))

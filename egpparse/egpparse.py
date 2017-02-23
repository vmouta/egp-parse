#!/usr/bin/env python
import sys
import os
import find
import output
import move
import transform
import parse

def filter_dir_for(directory, ext):
    dir_contents = os.listdir(directory)
    return [afile for afile in dir_contents if afile[-len(ext):]==ext]

if __name__ == '__main__':

    startdir = sys.argv[1]
    outdir = sys.argv[2]

    # Find all EGPs in throughout startdir
    file_list =  find.find_egps(startdir)

    # Write out all discovered EGPs to a text file
    output.write_program_list(file_list, outdir + '/' + 'egps.txt')

    for dir_egp_tuple in file_list:
        # Move all EGPs to outdir
        move.move_egp(dir_egp_tuple, outdir)

        # Extract XML file from inside EGP
        xml_file_name = transform.egptocode(outdir + '/' + dir_egp_tuple[1])

        # Parse the Task Code
        q = parse.get_tasks(outdir + '/' + xml_file_name)

        col_list = parse.list_columns(q)

        with open(outdir + '/column_list.txt', 'a') as coltxt:
            for col in col_list:
                coltxt.write('%s\t%s\n' % (dir_egp_tuple[1], col))


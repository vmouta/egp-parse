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
    # Enumerate to create idx (idx, (filepath, filename))
    file_list =  find.find_egps(startdir)

    # Write out all discovered EGPs to a text file
    output.write_program_list(enumerate(file_list), outdir + '/' + 'egps.txt')

    for (idx, (dir, egp)) in enumerate(file_list):

        # Move all EGPs to outdir
        move.move_egp(idx, dir, egp, outdir)

        # Extract XML file from inside EGP
        xml_file_name = transform.egptocode(outdir + '/' + str(idx) + egp)

        # Parse the Task Code
        q = parse.get_tasks(outdir + '/' + xml_file_name)

        # Write out the
        with open(outdir + '/column_list.txt', 'a') as coltxt:
            for task in q:
                try:
                    col_list = parse.list_columns(task)
                    for col in col_list:
                        coltxt.write('%s\t%s\t%s\n' % (str(idx), egp, col))
                except TypeError:
                    coltxt.write('%s\t%s\t%s\n' % (str(idx), egp, "Unable to parse"))


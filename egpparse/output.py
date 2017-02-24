import os
import time


def write_program_list(file_list, file_name = 'egps.txt'):
    with open(file_name,'w') as fout:
        for (idx, (srcdir, egp)) in file_list:
            mod_time = os.path.getmtime(srcdir+'/'+egp)
            mod_date = time.strftime('%Y-%m-%d', time.localtime(mod_time))
            fout.write('%s\t%s\t%s\t%s\n' % (str(idx), srcdir, egp, mod_date))
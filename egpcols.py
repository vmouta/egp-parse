"""egpcols.py - Extracts information out of the columns"""
import os
import re

def reach_task_code(xmldict):
    """Parses and XMLDICT object specifically for
       an EG.ProjectElements.Code object"""
    ###Assumes parsing an EGP project.xml
    xml_list = xmldict['ProjectCollection']['Elements']['Element']
    query_list = []
    for each in xml_list:
        if each['@Type'] == 'SAS.EG.ProjectElements.Code':
            query =  each['Code']['TaskCode']
            if query is not None:
                query_list.append(query)
            else: #Empty Query string
                pass
        else: #Not an EG.ProjectElements.Code block
            pass
    return query_list

def column_parse(query, pattern = r"\w+\.(?:\'(?:\w|\s|#)+\'n|\w+)"):
    """Extract Columns between a SELECT FROM statement
       Returns a list of column names or None"""
    try:
        select_line = re.compile('SELECT(.+?)FROM?',flags=re.DOTALL).findall(query)[0]
        column_list = re.compile(pattern,flags = re.DOTALL).findall(select_line)
    except:
        column_list = None
    return column_list

def column_parse2(query, pattern = r"\w+\.(?:\'(?:\w|\s|#)+\'n|\w+)"):
    """Extract Columns between a SELECT FROM statement
       Returns a list of column names or None"""
    #re.compile(r"ON \((.+)\)").findall(qry)
    #re.compile(r"WHERE\s(.+);?").findall(qry)
    try:
        all_lines = list()
        select_lines = re.compile('SELECT(.+?)FROM?',flags=re.DOTALL).findall(query)
        join_lines = re.compile(r"ON \((.+)\)").findall(query)
        where_lines = re.compile(r"WHERE\s(.+);?").findall(query)
        all_lines.extend(select_lines+join_lines+where_lines)
        all_lines_str = ' '.join(all_lines)
        column_list = re.compile(pattern,flags = re.DOTALL).findall(all_lines_str)
    except:
        column_list = None
    return column_list


def table_parse(query):
    """Extracts Tables between a FROM and (WHERE|;)
       and returns a list or None"""
    try:
        from_line = re.compile('FROM(.+?)(?:WHERE|;)+?',flags=re.DOTALL).findall(query)[0]
        table_list = re.compile('\w+\.\w+\s\w+',flags=re.DOTALL).findall(from_line)
    except:
        table_list = None
    return table_list

def list_columns(query):
    """Regular Expressions for Pulling out tables and columns
       from TASK CODE block (Specifically a PROC SQL query)"""
    table_list = table_parse(query)
    column_list = column_parse2(query)
    #print "There are %d columns across %d tables" %(len(column_list), len(table_list))
    if table_list is None or column_list is None:
        return None
    else:
        table_dict = {j[1]:j[0] for j in [i.split(' ') for i in table_list]}
        for col_idx in range(0,len(column_list)):
            col = column_list[col_idx]
            #For every column, loop through available tables
            #Will substitute the first match to a table alias
            for k in table_dict.keys():
                pattern = k+'\.'
                if re.match(pattern, col): #Does the table alias start the column?
                    column_list[col_idx] = re.sub(pattern,table_dict[k]+'.',col,1)
                    break
                else: #Pattern not found at beginning of column
                    pass
    return column_list

#
# SDB 1.0.7 (22.06.24)
# mady by DDavid701
#


import platform

if __name__ == '__main__':
    raise SystemExit("[!] Can't run as main")

def get_ids(database):
    with open(database, 'r') as db:
        cont = db.readlines()
    ids = {}
    for c in enumerate(cont):
        c_split = str(c[1]).split('|')
        id = c_split[0]
        ids[id] = c
    return ids

def get_specific_id(database, sid):
    with open(database, 'r') as db:
        cont  = db.readlines()
        count = 0
    for c in enumerate(cont):
        c_split = str(c[1]).split('|')
        id = c_split[0]
        full_c = c_split[0] + '|' + c_split[1] + '|' + str(count)
        count += 1
        if sid == id:
            return full_c
        else:
            pass

def init(output, file):
    ver = '1.0.7'  # Do not edit this!
    if output == True:
        print(f"SDB {ver} running using {platform.python_version()}")
    if not file:
        raise SystemExit("[!] No file given")
    try:
        with open(file, 'r') as db:
            cont = db.readlines()
            #print(get_ids(file))

    except Exception as e: raise SystemExit(f"[!] Couldn't open file '{file}'")
    return file

def get_parts(string):
    try:
        parts = string.split(';')
        return parts
    except Exception as e: print(f"Error: Couldn't get parts from '{string}'")

def read_row(database, row):

    if database == 'sdb': return "no database connected"
    with open(database, 'r') as db:
        CONTENT = db.readlines()

    tempsave = {}
    for line in enumerate(CONTENT):
        try:
            parts = str(line[1]).split('|')
            # dataid = parts[0]
            datacont = parts[1]
            tempsave[line[0]] = datacont
        except Exception as e: print(f"")

    try:
        if row == 0: row = 0
        else: row -= 1
        return tempsave[row]
    except Exception as e:
        print(f"[!] Row is corrupted or doesn't exist! {e}")
        return None

def read(database, id):

    if database == 'sdb': return "no database connected"
    with open(database, 'r') as db:
        CONTENT = db.readlines()

    tempsave = {}
    for line in enumerate(CONTENT):
        try:
            parts = str(line[1]).split('|')
            dataid = parts[0]
            datacont = parts[1]
            tempsave[dataid] = datacont
        except Exception as e: print(f"Error: id doesn't exist or is corrupted!")
    try:
        if id in tempsave:
            return tempsave[id]
        else: return None
    except Exception as e:
        print("[!] Id is corrupted or doesn't exist!")
        return None

def insert(database, data, id):
    if database == 'sdb': return "no database connected"
    ids = get_ids(database)
    if id in ids:
        print(f"Error: Couldn't insert data, id already exists! {id}")
        pass
    else:
        try:
            with open(database, 'a') as db:
                db.write(f'{id}|{data}\n')
        except Exception as e: print(f"Error: Couldn't insert data ({data}-{id})")

def remove_row(database, row):
    if database == 'sdb': return "no database connected"
    try:
        contdict    = {}
        lines       = []
        cache_start = []
        cache_end   = []
        with open(database, 'r') as db:
            CONTENT = db.readlines()

        for line in enumerate(CONTENT):
            contdict[line[0]] = line[1]
        for line in enumerate(CONTENT):
            lines.append(line[1])
        cur_line_count = 0
        try:
            row -= 1
            while row != cur_line_count:
                cache_start.append(lines[cur_line_count])
                cur_line_count += 1
        except Exception as e: print(e)

        cur_line_count += 1

        try:
            while cur_line_count != len(lines):
                cache_end.append(lines[cur_line_count])
                cur_line_count += 1
        except Exception as e: print(e)

        cache = cache_start + cache_end
        try:
            with open(database, 'w') as db:
                db.write('')
            with open(database, 'a') as db:
                cur_cell = 0
                for cell in cache:
                    db.write(cell)
        except Exception as e: print(e)
    except Exception as e: print(e)

def remove(database, id):
    curline = 0
    if database == 'sdb': return "no database connected"
    try:
        lines       = []
        cache_start = []
        cache_end   = []
        with open(database, 'r') as db:
            CONTENT = db.readlines()

        for line in enumerate(CONTENT):
            cur_line_count = line[0]
            lines.append(line[1])
        curline = 0
        try:
            specs = get_specific_id(database, id)
            specs = specs.split('|')
            while curline != int(specs[2]):
                cache_start.append(lines[curline])
                curline += 1
        except Exception as e: print("Error: id doesn't exist or is corrupted!")

        try:
            curline += 1
            while curline != len(lines):
                cache_end.append(lines[curline])
                curline += 1
        except Exception as e: print(e)

        cache = cache_start + cache_end

        try:
            with open(database, 'w') as db:
                db.write('')
            with open(database, 'a') as db:
                for cell in cache:
                    db.write(cell)
        except Exception as e: print(e)
    except Exception as e: print(e)

def clear(database):
    if database == 'sdb': return "no database connected"
    try:
        with open(database, 'w') as db:
            db.write('')
    except Exception as e: print(e)
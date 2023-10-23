import psycopg2
def prosmotr(id_app):
    con = psycopg2.connect(
        database="SovDB", user="postgres", 
        password="password", host="127.0.0.1", 
        port="5432")
    cur = con.cursor()
    cur.execute(
        f"""SELECT idae, idap, pr, mark from applel WHERE idap = {id_app}"""
            )
    element_apl = cur.fetchall()
    con.close()

    inf_req = dict()
    for i in element_apl:
        con = psycopg2.connect(
        database="SovDB", user="postgres", 
        password="password", host="127.0.0.1", 
        port="5432")
        cur = con.cursor()
        cur.execute(
            f"""SELECT id, idre, idpho from phreq WHERE id = {i[2]}"""
            )
        element_req = cur.fetchall()
        con.close()
        for j in element_req:
            if j[1] not in inf_req:
                inf_req[j[1]] = []
            inf_req[j[1]].append((j[0],j[2]))
    return inf_req
    
def mark(id_phreq):
    con = psycopg2.connect(
        database="SovDB", user="postgres", 
        password="password", host="127.0.0.1", 
        port="5432")
    cur = con.cursor()
    cur.execute(
        f"""SELECT idae, idap, pr, mark from applel WHERE pr = {id_phreq}"""
            )
    element_apl = cur.fetchall()
    con.close()
    return element_apl[0][0]

def photo(id_photo):
    con = psycopg2.connect(
        database="SovDB", user="postgres", 
        password="password", host="127.0.0.1", 
        port="5432")
    cur = con.cursor()
    cur.execute(
        f"""SELECT idph, photopath from photo WHERE idph = {id_photo}"""
            )
    phot = cur.fetchall()
    con.close()
    return phot[0][1]

def description(id_req):
    con = psycopg2.connect(
        database="SovDB", user="postgres", 
        password="password", host="127.0.0.1", 
        port="5432")
    cur = con.cursor()
    cur.execute(
        f"""SELECT idr, description from req WHERE idr = {id_req}"""
            )
    phot = cur.fetchall()
    con.close()
    return phot[0][1]
    
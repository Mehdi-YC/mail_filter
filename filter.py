import re
import sqlite3


conn = sqlite3.connect("mails.db")
cur = conn.cursor()




def change_type(cur,mail,type):
    cur.execute(f'alter mail set type="{type}" where mail="{mail}"')
    cur.commit()


def get(cur,type):
    cur.execute(f'select mail from mails where type="{type}" ')
    data = cur.fetchall()
    return data

    
def add(cur,name,domain,mail,type):
    cur.execute(f'insert into mails(mail,name,domain,type) values("{mail}","{name}","{domain}","{type}");')






def filter(cur,conn):
    pattern = re.compile('(?P<mail>(?P<name>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}))')
    conn.row_factory = lambda cursor, row: row[0]
    cur.execute('delete from mails')
    conn.commit()
    with open("mails.txt","r") as f:
        lines = f.readlines()
        for line in lines :
            search = pattern.search(line)
            try:
                mail = search.groupdict()

                if any(x in mail["mail"] for x in ["dz","algerie"] ):
                    add(cur,mail["name"],mail["domain"],mail["mail"],"DZ")



                elif any(x in mail["mail"] for x in ["sarl","eurl"] ):
                    add(cur,mail["name"],mail["domain"],mail["mail"],"PRO")


                else:
                    add(cur,mail["name"],mail["domain"],mail["mail"],"CASUAL")
            
            except :
                add(cur,"_","_",str(line),"ERROR")
    conn.commit()
    conn.close()
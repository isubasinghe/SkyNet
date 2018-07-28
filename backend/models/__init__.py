import atexit
from datetime import datetime
import rethinkdb as r

HOST = "192.168.99.100"
PORT = 32769

def load_model():
    #__rethinkdb = r.connect("192.168.99.100", 32769, db="test")
    #atexit.register(unload_models)
    pass

def add_fake_users():
    conn = r.connect("HOST", PORT, db="test")
    for i in range(10):
        r.table('users').insert([
            {
                "user": "user_" + str(i),
                "location": r.point(0,0),
                "time": r.expr(datetime.now(r.make_timezone('+11:00'))),
                "processed": True
            }
        ]).run(conn)
    conn.close()

def insert_coords(user, coords, processed):
    conn = r.connect("HOST", PORT)
    print(coords)
    user = r.table('users').filter({"user": user}).update({"location": r.point(coords[0], coords[1]), "time": r.expr(datetime.now(r.make_timezone('+11:00'))), "processed": processed}, return_changes=True).run(conn)
    # print(user)
    conn.close()

def set_true():
    conn = r.connect("HOST", PORT)
    r.table('users').filter({"processed": False}).update({"processed": True}, return_changes=True).run(conn)
    conn.close()

def add_fake_coords():
    conn = r.connect("HOST", PORT)
    coords = [[144.9738,-37.8110], [144.9671,-37.8183], [144.9561, -37.8117], [144.9676, -37.8118], [144.9764, -37.8101],[144.9463,-37.8112],[144.9717,-37.8033],[144.9568,-37.8076],[144.9583,-37.8206]]
    for i in range(len(coords)):
        r.table('users').filter({"user": "user_" + str(i+1)}).update({"location": r.point(coords[i][0], coords[i][1]), "time": r.expr(datetime.now(r.make_timezone("+11:00"))), "processed": False}, return_changes=True).run(conn)
    
    
    conn.close()


def get_user_coords(user):
    conn = r.connect("HOST", PORT)
    cursor = r.table('users').filter({"user": user}).run(conn)
    for document in cursor:

        retval =  document["location"]["coordinates"]
        retval.reverse()
        break
    conn.close()
    return retval    

def get_coords():
    conn = r.connect("HOST", PORT)
    # Obtain the unprocessed users
    cursor = r.table("users").filter({"processed": False}).run(conn)
    #cursor = r.table("users").run(conn)
    user_coords = []

    for document in cursor:
        coords = document['location']['coordinates']
        coords.reverse()
        user_coords.append(coords)
        #user_coords.append(document['location']['coordinates'])
        #print('coords={0}'.format(document['location']['coordinates']))
    #print(cursor)
    conn.close()
    return user_coords

def no_unprocessed_users():
    pass



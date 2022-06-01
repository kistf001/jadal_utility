from tokenize import String
import mariadb
import secreat
import sys

host, port, user, passwd, autocommit = secreat.out()

# Instantiate Connection 
try:
    conn = mariadb.connect(
        user=user, 
        host=host, 
        port=port, 
        password=passwd, 
        autocommit=autocommit
    )

except mariadb.Error as e: 
    print(f"Error connecting to MariaDB Platform: {e}") 
    sys.exit(1)

# Instantiate Cursor 
cur = conn.cursor()

def save_daily(key,data):

    query1 = (
        "INSERT INTO ranking.dayily "+
        "( `key_song_data`, `rank`, `date` ) "+
        "SELECT ?, ?, ? "+
        "FROM DUAL "+
        "WHERE NOT EXISTS "+
        "(SELECT * FROM `ranking`.`dayily` WHERE `key_song_data`=? AND `date`=? )"+
        "LIMIT 1 "
    )
    
    cur.execute(
        query1,
        (
            key,
            data["rank"],
            data["date"],
            key,
            data["date"],
        )
    )

    # fetch qeury result 
    #rows = cur.fetchall() 
    #print(rows,'\n') 

    conn.commit()

def song_data_insert(data):
    
    query1 = (
        "INSERT INTO `ranking`.`song_data` "+
        "( `title`, `composer`, `singer`, `published` ) "+
        "SELECT ?, ?, ?, ? "+
        "FROM DUAL "+
        "WHERE NOT EXISTS "+
        "(SELECT `title` FROM `ranking`.`song_data` WHERE `title`=? AND `published`=? )"+
        "LIMIT 1 "
    )
    
    query2 = (
        "SELECT `key` "+
        "FROM `ranking`.`song_data` "+
        "WHERE `title`=? AND `published`=? "+
        "LIMIT 1 "
    )
    
    cur.execute(
        query1,
        (
            data["title"],
            data["composer"],
            data["singer"],
            data["published"],
            # validation
            data["title"],
            data["published"],
        )
    )

    cur.execute(
        query2,
        (
            data["title"],
            data["published"],
        )
    )

    rows = cur.fetchall() 

    conn.commit()

    return rows[0][0]

def song_data_url(key,data):

    query1 = (
        "INSERT INTO `ranking`.`song_url` "+
        "( `key_song_data`, `url` ) "+
        "SELECT ?, ? "+
        "FROM DUAL "+
        "WHERE NOT EXISTS "+
        "(SELECT * FROM `ranking`.`song_url` WHERE `key_song_data`=? AND `url`=? )"+
        "LIMIT 1 "
    )

    cur.execute(
        query1,
        (
            key,
            data["url"],
            key,
            data["url"],
        )
    )

    conn.commit()

def media_not_downloaded_cheack():

    query1 = (
        "SELECT `key`, `url`, `site` "+
        "FROM ranking.song_url "+
        "WHERE media='empty' "
    )

    cur.execute(
        query1
    )

    # fetch qeury result 
    rows = cur.fetchall() 

    return rows
    #conn.commit()

# commit 
#song_data_insert()
#conn.commit()
#
#conn.close()
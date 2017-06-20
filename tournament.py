
import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception as e:
        print e
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    q = "DELETE FROM matches"
    c.execute(q)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    q = "TRUNCATE players CASCADE"
    c.execute(q)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players registered."""
    db, c = connect()
    q = 'SELECT COUNT(*) FROM players'
    c.execute(q)
    rows = c.fetchone()
    db.close()
    for row in rows:
        result = row[0]
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    q = "INSERT INTO players (player_name) VALUES (%s);"
    param = (name,)
    c.execute(q, param)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or
    a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    query = "SELECT * FROM standings"
    c.execute(query)
    results = cursor.fetchall()
    print results
    # If the top two results have more than 0 wins AND are equal then reorder
    # them by total wins divided by total games played
    if (results[0][2] != 0) and (results[0][2] == results[1][2]):
        query = "SELECT * FROM standings ORDER BY "
        query += "(cast(won AS DECIMAL)/played) DESC"
        c.execute(query)
        results = cursor.fetchall()
    db.close()

    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    q = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    param = (winner, loser,)
    c.execute(q, param)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, c = connect()
    query = 'SELECT * FROM standings'
    c.execute(query)
    results = cursor.fetchall()
    pairings = []
    count = len(results)

    for x in range(0, count - 1, 2):
        paired_list = (results[x][0], results[x][1], results[x + 1][0], results[x + 1][1])
        pairings.append(paired_list)

    db.close()
    return pairings

import sqlite3


def create_database():

    conn = sqlite3.connect(
        "realestate_history.db"
    )

    cursor = conn.cursor()


    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS reports
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        overview TEXT,
        pitch TEXT
    )
    """
    )


    conn.commit()

    conn.close()




def save_report(
    company,
    overview,
    pitch
):

    conn = sqlite3.connect(
        "realestate_history.db"
    )

    cursor = conn.cursor()


    cursor.execute(
    """
    INSERT INTO reports
    (
    company,
    overview,
    pitch
    )
    VALUES (?,?,?)
    """,
    (
    company,
    overview,
    pitch
    )
    )


    conn.commit()

    conn.close()




def get_reports():


    conn = sqlite3.connect(
        "realestate_history.db"
    )


    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM reports"
    )


    data = cursor.fetchall()


    conn.close()


    return data
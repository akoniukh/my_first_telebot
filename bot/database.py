import sqlite3


def server_start(file):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS core_fes(Id TEXT, '
                   'Set_lang TEXT)')
    cursor.execute("SELECT Id, Set_lang FROM core_fes ")
    results = cursor.fetchall()
    buffer_dict = {}
    for pair in results:
        buffer_dict.update({pair[0]: pair[1].split("-")})
    conn.close()
    return buffer_dict


def search_lang(users_dict, user_id, file):
    flag = users_dict.get(str(user_id))
    if flag is None:
        conn = sqlite3.connect(file)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS core_fes(Id TEXT, '
                       'Set_lang TEXT)')
        cursor.execute(
            'INSERT INTO core_fes VALUES( :1, "English-en");', {'1': str(user_id)})
        conn.commit()
        users_dict.update({str(user_id): ["English", "en"]})
        conn.close()
    return users_dict.get(str(user_id))


def update(user_id, lang, file):
    conn = sqlite3.connect(file)
    lang1 = '-'.join(lang.split())
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS core_fes(Id TEXT, '
                   'Set_lang TEXT)')
    cursor.execute('INSERT INTO core_fes VALUES( :1, :2);',
                   {'1': str(user_id), '2': lang1})
    conn.commit()

import json def populate_matches():
    with open("data/db.json") as in_:
        db = json.load(fp=in_)
    for user in db:
        user_data = db[user]

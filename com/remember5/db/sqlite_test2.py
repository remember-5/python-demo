from sqlite_utils import Database


"""
sqlite-utils 操作sqlite
https://sqlite-utils.datasette.io/en/stable/
"""
db = Database("chickens.db")
db["chickens"].insert_all([{
    "name": "Azi",
    "color": "blue",
}, {
    "name": "Lila",
    "color": "blue",
}, {
    "name": "Suna",
    "color": "gold",
}, {
    "name": "Cardi",
    "color": "black",
}])


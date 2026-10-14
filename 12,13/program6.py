def load_players(filename):
    players = {}
    f = open(filename, "r")
    entry = f.readline().rstrip('\n')
    while entry != "":
        entryAsList = entry.split(",")
        name = entryAsList[0]
        average = float(entryAsList[1])
        players.update({name: average})
        entry = f.readline().rstrip('\n')
    f.close()
    return players
def display_players(players):
    print(f"{'Player':12} {'Average':>8}")
    for name in players:
        print(f"{name:12} {players[name]:>8.3f}")
batting = load_players("program6.txt")
display_players(batting)
import csv


def exporter_csv(sejours, chemin):
    print("export de", len(sejours), "sejours vers", chemin)
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "service", "entree", "sortie", "age"])
        for s in sejours:
            w.writerow([s.id, s.service, s.entree, s.sortie, s.age])

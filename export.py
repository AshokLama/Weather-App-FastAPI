import csv

def export_to_csv(data):
    with open("weather.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Location", "Temp", "Description"])

        for d in data:
            writer.writerow([d.id, d.location, d.temperature, d.description])
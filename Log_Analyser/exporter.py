import csv


def export_to_csv(parsed_logs, report_csv):

    with open(report_csv, "w", newline="") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Date",
            "Time",
            "Level",
            "Service",
            "Message"
        ])

        for log in parsed_logs:

            writer.writerow([
                log["date"],
                log["time"],
                log["level"],
                log["service"],
                log["message"]
            ])

    print(f"\nCSV report saved as: {report_csv}")
from datetime import datetime

start_date_str = "2026-02-02"  # Internship start date
end_date_str = "2026-05-02"    # Internship end date


start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

total_days = (end_date - start_date).days + 1

print(f"Total days in the internship: {total_days}")
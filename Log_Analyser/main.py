from parser import parse_logs
from analyser import analyze_logs
from exporter import export_to_csv


# ===================================================
# PARSE LOGS
# ===================================================

parsed_logs = parse_logs("filee")


# ===================================================
# DISPLAY STRUCTURED LOGS
# ===================================================

print("\n========== STRUCTURED LOGS ==========\n")

for log in parsed_logs:
    print(log)


# ===================================================
# ANALYZE LOGS
# ===================================================

analysis = analyze_logs(parsed_logs)


# ===================================================
# DISPLAY SUMMARY
# ===================================================

print("\n========== LOG SUMMARY ==========\n")

print(f"Total Logs   : {analysis['total_logs']}")
print(f"INFO Logs    : {analysis['info_logs']}")
print(f"WARNING Logs : {analysis['warning_logs']}")
print(f"ERROR Logs   : {analysis['error_logs']}")


# ===================================================
# DISPLAY ERROR PATTERNS
# ===================================================

print("\n========== ERROR PATTERNS ==========\n")

for error, count in analysis["error_patterns"].items():
    print(f"{error} --> {count} occurrence(s)")


# ===================================================
# DISPLAY ERRORS BY SERVICE
# ===================================================

print("\n========== ERRORS BY SERVICE ==========\n")

for service, count in analysis["service_errors"].items():
    print(f"{service} --> {count} error(s)")


# ===================================================
# EXPORT CSV REPORT
# ===================================================

export_to_csv(
    parsed_logs,
    "log_analysis_report.csv"
)


print("\nMonitoring completed successfully.")
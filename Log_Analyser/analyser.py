from collections import Counter


def analyze_logs(parsed_logs):

    log_levels = [log["level"] for log in parsed_logs]

    level_counter = Counter(log_levels)

    error_logs = [
        log for log in parsed_logs
        if log["level"] == "ERROR"
    ]

    error_messages = [
        log["message"]
        for log in error_logs
    ]

    error_counter = Counter(error_messages)

    error_services = [
        log["service"]
        for log in error_logs
    ]

    service_counter = Counter(error_services)

    analysis = {
        "total_logs": len(parsed_logs),
        "info_logs": level_counter["INFO"],
        "warning_logs": level_counter["WARNING"],
        "error_logs": level_counter["ERROR"],
        "error_details": error_logs,
        "error_patterns": error_counter,
        "service_errors": service_counter
    }

    return analysis
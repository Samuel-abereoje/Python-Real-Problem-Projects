import re


def parse_logs(filee):

    pattern = re.compile(
        r"(\d{4}-\d{2}-\d{2}) "
        r"(\d{2}:\d{2}:\d{2}) "
        r"(INFO|ERROR|WARNING) "
        r"(\w+) "
        r"(.*)"
    )

    parsed_logs = []

    with open(filee, "r") as file:

        logs = file.readlines()

        for log in logs:

            match = pattern.match(log)

            if match:

                log_data = {
                    "date": match.group(1),
                    "time": match.group(2),
                    "level": match.group(3),
                    "service": match.group(4),
                    "message": match.group(5)
                }

                parsed_logs.append(log_data)

    return parsed_logs
  
  



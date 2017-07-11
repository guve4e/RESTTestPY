from src.process_requests import ProcessRequests
from src.parse_cmd_args import CmdArgumentsParser
import sys


if __name__ == "__main__":

    print("======================== RESTTestPY =============================")

    # process = ProcessRequests("crystalpure", "-v")

    cmd = CmdArgumentsParser(sys.argv)

    try:
        process = ProcessRequests(cmd.project_name, cmd.verbose, cmd.filter_keyword)
    except Exception as e:
        print(str(e))

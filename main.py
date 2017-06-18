from src.process_requests import ProcessRequests
import sys

if __name__ == "__main__":

    print("+++++++++ START ++++++++++")

    if len(sys.argv) > 1:
        project_name = sys.argv[1]

        try:
            process = ProcessRequests(project_name)
        except Exception as e:
            print(str(e))

    else:
        print("Specify A Project Name")
        exit()
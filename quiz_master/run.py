import os
import sys


# Check if port 3000 is in use
if os.system("netstat -an | findstr :3000") == 0:
    print("Detected FrontEnd Server is Running, Existing.")
    from app import create_app
    __app__ = create_app()
    if __name__ == '__main__':
        __app__.run(debug=True, port=7000)
        print("-------------------Backend Server Started-----------")
else:
    print("Front End Server Not Running,Hence Application Will exit")
    sys.exit(1)  





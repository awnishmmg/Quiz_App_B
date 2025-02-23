import os
import sys
import psutil
from app import create_app

def is_port_in_use(port):
    """Check if the given port is in use on localhost."""
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            return True  # Port is in use
    return False

# Exit if port 3000 is already occupied
if is_port_in_use(3000):
    print('---------Your Front End is Running ------------');
    __app__ = create_app()
    if __name__ == '__main__':
        __app__.run(debug=True, port=7000)
    print('---------Backend Also Started ------------');
else:
    print("Front End is not Running. Hence,Exiting application.")
    sys.exit(1)
    



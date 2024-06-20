import sys

from ascript.ios.developer import server
from ascript.ios.system import R

R.work_space = sys.argv[1]
dev_port = sys.argv[2]

server.run()

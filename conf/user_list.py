import sys, json
userlist=json.loads(sys.stdin.readlines()[0])["users"]
print "{0}".format("\n".join(i for i in userlist))

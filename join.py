import json
import pprint

pp = pprint.PrettyPrinter(indent=4)
hosts = json.load(open('hosts.json'))
newhosts = json.load(open('newhosts.json'))
pp.pprint(len(hosts["ah57_week2_8"]["hosts"]))
unique = set()
i =0
#while i < len(hosts):
for x in newhosts:
    unique.add(x)
    i+=1
print(unique)
for x in unique:
    hosts[x]["hosts"].extend(newhosts[x]["hosts"])
#hosts[].update(newhosts)
pp.pprint(len(hosts["ah57_week2_8"]["hosts"]))



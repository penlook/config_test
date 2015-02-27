import redis, os, yaml, json, sys

print "\n--------- TEST CONFIGURATION ----------\n"

redis = redis.StrictRedis(host='localhost', port=6379)

# Clear all key
for key in redis.keys():
	redis.delete(key)

root = os.path.dirname(os.path.realpath(sys.argv[0]))

def scan(module):

	base_path = root + "/" + module

	# Switch to module
	list_root = os.listdir(base_path)

	# Rebuild configuration
	for key in list_root:
		if key.endswith(".yml"):
			stream = open(base_path + "/" + key, 'r')
			value  = yaml.load(stream)
			redis.set(key, json.dumps(value))
			print 'Export ' + key + ' : ' + json.dumps(value)

scan('config')
print "\n-------------------------------------------\n"
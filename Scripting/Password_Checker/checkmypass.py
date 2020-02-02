'''
run scheme: python checkmypass.py pass1 pass2 ... passn
'''
import requests
import hashlib
import sys
import subprocess

# url = 'https://api.pwnedpasswords.com/range/' + 'password123' # returns [400], we have to give SHA1 hash string as pass
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97' # this is also not safe
# k anonimity, will look all pass hashes begins with these characters, so this API wouldnt know our password


def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char # only first 5 characters
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
  return res

def get_pwd_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    # if hash_to_check in h:
    #   print(h, count)
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  # Check password if it exists in API response
  # print(password.encode('utf-8')) # b'123
  # print(hashlib.sha1(password.encode('utf-8'))) #<sha1 HASH object @ 0x03E10560>
  # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper()) #40BD001563085FC35165329EA1FF5C5ECBDBBEEF
  # print(hashlib.sha1(password).hexdigest().upper()) #TypeError: Unicode-objects must be encoded before hashing
  
  sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1pwd[:5], sha1pwd[5:]
  response = request_api_data(first5_char)
  return get_pwd_leaks_count(response, tail)


# pwned_api_check('12345678')

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} found {count} times... you should probably change your password')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!' #this line runs when sys.exit used

if __name__ == '__main__':
  # main(sys.argv[1:])
  sys.exit(main(sys.argv[1:])) #to make sure to return back to command line

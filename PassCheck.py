import requests # Having a browser , request something
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char #123 is password->hash->first5
    res=requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching).{res.status_code} , check api')
    return res

def get_pass_leaks(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1pass = hashlib.sha1(str(password).encode('utf-8')).hexdigest().upper()
    #making own sha1 pass
    first_char,tail = sha1pass[:5],sha1pass[5:]
    response=request_api_data(first_char)
    return get_pass_leaks(response,tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times , you should CHANGE it')
        else:
            print(f'{password} was not found . Great!!')
    return print("done")

if __name__ == "__main__" :
    sys.exit(main(sys.argv[1:]))
## Input from text file



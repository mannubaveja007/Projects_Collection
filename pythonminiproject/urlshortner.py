import hashlib
data = {}
def display():
    display = """ URL shortner
    1. shorten a URL
    2.Retrive Original URL
    3.Exit
"""
    return display
def user_choice(intt):
        if intt == 1:
            shorten_url()
        elif intt == 2:
            retrive_url()
        elif intt == 3:
            print("exiting ... goodbye")
            return
        else:
            print("Invalid choice")     
def generate_url(long_url):
       hash_object = hashlib.md5(long_url.encode())
       short_code = hash_object.hexdigest()[:6]
       return f"https//short.lu/{short_code}"
def shorten_url():
        long_url = input("Enter the long url:- ").strip()
        if not long_url:
              print("invalid")
              return 
        for short,url in data.items():
                if url == long_url:
                    print(f"short Url already exit {short}")
                    return
        short_url = generate_url(long_url)     
        data[short_url] = long_url
        print(f"short url is {short_url}")
def retrive_url():
        short_url = input("Enter the short url:- ").strip()
        long_url = data.get(short_url)
        if long_url:
            print(f"original url is {long_url}")
        else:
            print("no url found")
def main():
        screen = display()
        print(screen)
        while True:
                intt = int(input("Choice an  option (1-3) :-  "))
                user_choice(intt)
                if intt == 3:
                      break

main()        
import pyshorteners
url=input("Enter your url")
n=pyshorteners.Shortener().tinyurl.short(url)
print("Your shorted url is -->",n)

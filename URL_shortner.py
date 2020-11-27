#CODE Created by IG@kamran_hccp

import pyshorteners
url = input("Enter your URL: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your Shorted is '" + s + "'")

#CODE Created by IG@kamran_hccp

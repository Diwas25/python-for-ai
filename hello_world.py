import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

name = "Diwas"
age = 34
occupation = "AI Engineer"

print("Name : "+name,age,occupation)
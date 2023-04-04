import requests

url = "https://stack_overflow_data1.p.rapidapi.com/xml_data"

headers = {
	"X-RapidAPI-Key": "40ab79f105msh29ef579383c5b76p121e00jsn02e3810dabb8",
	"X-RapidAPI-Host": "stack_overflow_data1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
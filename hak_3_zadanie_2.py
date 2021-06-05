import requests
new_student = {
	"name": "Namjoon",
	"age": 26,
	"group": "BTS",
	"phone": "+996777444333",
	"email": "rm@gmail.com",
	"created_by": "team3"
}

response = requests.post('http://206.189.44.36:8900/students/', data = new_student)

result = response.json()
print(result)

response = requests.get('http://206.189.44.36:8900/students/25/')
res = response.json()
res2 =(res["id"], res["name"], res["age"], res["group"])
print(res2)

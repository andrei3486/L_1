import json

json_string = '''{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false,
      "salary": 1500
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true,
      "salary": 1700
    },
    {
      "name": "Steven Cooke",
      "phone": null,
      "emails": "stevencooke@example.com",
      "has_licence": true,
      "salary": 2500
    }
  ]
}'''
# data = json.loads(json_string) # из json в словарь
#
# # print(data['people'][0]['emails'][1])
#
# for person in data['people']:
#     # print(person)
#
# # person = data['people'][1]
# # print(person['phone'], person['emails'])
#     del person['phone']
#     # print(data)
#
# new_json = json.dumps(data, indent=2) # indent сколько пробелов отпускать
# print(new_json)

import json

with open('people.json', 'r', encoding='utf8') as file:
    data = json.load(file)


for person in data['people']:
    if person ['has_licence'] == False:
        del person['has_licence']

with open ('people_edited.json', 'w', encoding='utf8') as wfile:
    json.dump(data, wfile, indent=2)
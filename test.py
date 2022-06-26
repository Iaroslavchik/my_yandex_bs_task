json = {
    "items": [
        {
            "type": "CATEGORY",
            "name": "Телевизоры",
            "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
            "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1"
        },
        {
            "type": "OFFER",
            "name": "Samson 70\" LED UHD Smart",
            "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
            "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
            "price": 32999
        },
        {
            "type": "OFFER",
            "name": "Phyllis 50\" LED UHD Smarter",
            "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
            "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
            "price": 49999
        }
    ],
    "updateDate": "2022-02-03T12:00:00.000Z"
}
for i in json["items"]:
    atribut = ''
    value = ''
    path = i['type']
    for j in i:
        atribut += str(j) + ', '
        if isinstance(i[j], str):
            value += "'" + str(i[j]) + "'" + ', '
        else:
            value += str(i[j]) + ', '
    atribut += 'date'
    value += "'" + str(json["updateDate"]) + "'"

    print(f'insert into {path}({atribut}) values ({value});')

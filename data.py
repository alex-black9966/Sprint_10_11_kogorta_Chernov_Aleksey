headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}



kit_body = {
       "name": "Мой набор",
   }


def get_kit_new_body(value):
    return get_kit_body("name", value)

def get_kit_body(key, value):
    new_body = kit_body.copy()
    new_body[key]=value

    return new_body
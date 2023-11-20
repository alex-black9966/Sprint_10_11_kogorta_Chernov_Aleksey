import sender_stand_request
import data


TOKEN = sender_stand_request.get_token()

# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):

    current_body = data.kit_body.copy()

    current_body["name"] = name

    return current_body

def positive_assert(name):
    # В переменную user_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert kit_response.json()["name"] == name

def negative_assert_code_400(name):
    # В переменную user_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)

    # В переменную response сохраняется результат
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400

    # Проверяется, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверяется текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")
# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd/"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                           "cdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы
def test_create_kit_eng_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_create_kit_rus_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert('"№%@",')

# Тест 8. Разрешены пробелы
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_create_kit_digit_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    negative_assert_code_400(name)

# Тест 11. Передан другой тип параметра (число)
def test_create_kit_number_letter_in_name_get_error_response():
    negative_assert_code_400(123)
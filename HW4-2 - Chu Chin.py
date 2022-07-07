# [2]

# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cilpio": 47.999, "a_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.ua": 38.324, "my-store": 37.166, "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
#
# Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "my-store", "main-service"

lower_limit = 35.9
upper_limit = 37.339

shop_dict = { "cilpio": 47.999, "a_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.ua": 38.324, "my-store": 37.166, "the_partner": 38.988, "sto": 37.720, "rozetka": 38.003}

# Вариант - вывожу из дикта все магазины и цены в диапазоне
for key, value in shop_dict.items():
    if lower_limit <= value >= upper_limit:
        print(key, '-->', value)

# Вариант - вывожу из дикта только магазины, цены которых в диапазоне
for key, value in shop_dict.items():
    if lower_limit <= value >= upper_limit:
        print(key)

# Вариант - в виде отдельного листа вывожу из дикта только магазины, цены которых в диапазоне
shop_match_list = list()

for key, value in shop_dict.items():
    if lower_limit <= value >= upper_limit:
        shop_match_list.append(key)

print(shop_match_list)


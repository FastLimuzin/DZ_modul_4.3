from utils import get_reg_data, reg_check


def main():
    users_list = []
    user_count = 0

    while user_count < 3:
        user_data = []
        patterns = get_reg_data()

        for i, pattern in enumerate(patterns):
            while True:
                if i < 2:  # Имя и фамилия
                    data_type = "Имя" if i == 0 else "Фамилия"
                    user_input = input(f"Введите ваше {data_type}: ")
                elif i == 2:  # Телефон
                    user_input = input("Введите ваш телефон (например, +79991234567): ")
                else:  # Email
                    user_input = input("Введите ваш Email: ")

                result = reg_check(user_input, pattern, users_list,
                                   [user[2] for user in users_list] if i == 2 else [user[3] for user in users_list])

                if result is not None:
                    user_data.append(result)
                    break

        users_list.append(user_data)
        user_count += 1
        print("Пользователь успешно зарегистрирован!")

    print("Все пользователи зарегистрированы!")
    print("Список зарегистрированных пользователей:", users_list)


if __name__ == "__main__":
    main()
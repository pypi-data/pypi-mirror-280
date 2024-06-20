#!/usr/bin/env python3
from __future__ import with_statement

import contextlib
import os
import platform
import sys

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def make_tiny(url):
    request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def prompt_language():
    while True:
        choice = input("Choose language / Выберите язык (E/R): ").strip().upper()
        if choice in ["E", "R"]:
            return choice
        else:
            print("Invalid choice. Please enter E or R / Неправильный выбор. Пожалуйста, введите E или R.")


def main():
    print("Made by Avinion")
    print("Telegram: @akrim")

    language = prompt_language()

    if language == "E":
        welcome_message = "Enter URL to shorten (or 'exit' to quit): "
        shortened_message = "Shortened URL: "
        continue_message = "Do you want to shorten another URL? (Y/N): "
        invalid_input_message = "Invalid input. Please enter Y or N."
    else:
        welcome_message = "Введите URL для сокращения (или 'exit' для выхода): "
        shortened_message = "Сокращенный URL: "
        continue_message = "Хотите сократить еще один URL? (Y/N): "
        invalid_input_message = "Неверный ввод. Пожалуйста, введите Y или N."

    while True:
        url = input(welcome_message).strip()
        if url.lower() == 'exit':
            break
        print(f"{shortened_message}{make_tiny(url)}")
        while True:
            continue_choice = input(continue_message).strip().upper()
            if continue_choice in ["Y", "N"]:
                break
            else:
                print(invalid_input_message)
        if continue_choice == "N":
            break
        clear_console()


if __name__ == '__main__':
    main()

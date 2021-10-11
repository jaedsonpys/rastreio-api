import requests
import os

endpoint = 'https://api.linketrack.com/track/json'

def get_package(code: str) -> None:
    email_user = os.environ.get("EMAIL_USER")
    token = os.getenv("TOKEN")

    params = f'?user={email_user}&token={token}&codigo={code}'

    req = requests.get(endpoint+params)
    result = req.json()

    info_package(result)

def info_package(info: dict) -> None:
    print('\033[47;30m Informações do pacote! \033[m\n')

    print(f'Código de rastreio: {info["codigo"]}')
    print(f'Última atualização: {info["ultimo"]}\n')

    print('\033[47;30m Trajetória do pacote \033[m')

    for event in info['eventos']:
        print('-'*15)
        print(f'\nData: {event["data"]}')
        print(f'Hora: {event["hora"]}')
        print(f'Cidade/País: {event["local"]}\n')
        print(f'\033[32mStatus: {event["status"]}\033[m')

        try:
            if 'http' not in event['subStatus'][0]:
                print(f'Local: {event["subStatus"][0]}\n')
        except (IndexError or KeyError):
            pass

        try:
            print(f'Destino: {event["subStatus"][1]}')
        except (KeyError, IndexError):
            pass

    print(info)

get_package(str(input('Digite seu codigo: ')))
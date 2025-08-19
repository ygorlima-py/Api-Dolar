import requests 



class Requisicao:
    
    def __init__(self):
        self.url = 'https://query2.finance.yahoo.com/v8/finance/chart/USDBRL=X'

    def requisicao_dolar(self):
    
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://finance.yahoo.com/"
            }
            resposta = requests.get(self.url, headers=headers)
            
            
            resposta_json = resposta.json()

            preco_atual = resposta_json['chart']['result'][0]['meta']['regularMarketPrice']
            
            return preco_atual



        except requests.RequestException as e:
            # trata erros de rede / HTTP / timeout
            status = getattr(locals().get('resposta', None), 'status_code', None)
            if status is not None:
                print(f'Erro de requisição. Status: {status} - {e}')
            else:
                print(f'Erro de requisição: {e}')
            return None

        except (ValueError, KeyError, IndexError) as e:
            # trata problemas ao interpretar o JSON ou acessar campos
            print(f'Erro ao processar resposta: {e}')
            return None

        



if __name__ == '__main__':
    requisicao = Requisicao()
    resposta = requisicao.requisicao_dolar()
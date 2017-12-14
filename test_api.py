import coinbase as cb
from coinbase.wallet.client import Client
import json

client = Client('tjSOJDfiJ5pX2xoD', 'hSaGcd5jvGrbi9O5RwCFIyxz2qt3EjLT')

user = client.get_current_user()
user_as_json_string = json.dumps(user)

def get_account_balance(client, ifUSD = True):
    all_accounts_dict = json.loads(json.dumps(client.get_accounts()))
    cleaned_accounts_json_string = json.dumps(all_accounts_dict['data'])
    cleaned_accounts_dict = json.loads(cleaned_accounts_json_string)
    num_of_accounts = len(cleaned_accounts_dict)
    res = {}
    if ifUSD:
        for a in range(num_of_accounts):
            res.update({cleaned_accounts_dict[a].get('balance').get('currency')+str(' in USD')
                        : cleaned_accounts_dict[a].get('native_balance').get('amount')})
    else:
        for a in range(num_of_accounts):
            res.update({cleaned_accounts_dict[a].get('balance').get('currency')
                       : cleaned_accounts_dict[a].get('balance').get('amount')})
    return res

get_account_balance(client, False)
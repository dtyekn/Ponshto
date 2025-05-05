BOT_TOKEN = '7694920024:AAHHN0bosivojMjX82rc69Wu1Uo25uupAVw'
DEPOSIT_ADDRESS = 'UQAEKS9SJGJF0qHNxRFsy3GQHxK4lRO8iERPYJ2jxeaqZGoV'
API_KEY = 'e9032c9e8a0168b02a6031963f88d31f832b1f16a1b8fd27e55f0f8e955bef4c'
RUN_IN_MAINNET = True  # Switch True/False to change mainnet to testnet

if RUN_IN_MAINNET:
    API_BASE_URL = 'https://toncenter.com'
else:
    API_BASE_URL = 'https://testnet.toncenter.com'

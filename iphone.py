import requests

cookies = {
    'as_dc': 'ucp1',
    'as_pcts': 'O_WYtGxBE6wHlPKJbUXRzECV0pTly-BxclVr94raog7cuAb8rbCoS4P45fjvnI19Ek',
    'dssf': '1',
    'dssid2': '61d6a301-cf08-475a-b0af-e325493722cf',
    'rtsid': '%7BHK%3D%7Bt%3Da%3Bi%3DR499%3B%7D%3B%7D',
    'as_cn': '~lQWovscziNORMsPOGNV-OKr-_7yNpM1q823aDOYonJA=',
    'as_disa': 'AAAjAAABJU3vTtoAuj__KGAYM2MpPj-GrFah1iHowbBvRn9lkY_W0jPgDJdNXXo2AbHVnqPLAAIB3rrsqq7Mtl2qyQreqKvLQ5TGVL4K5GQEHM95_iutwCg=',
    'as_rec': 'e7744089396fcfec958ae96d046abdc2a3bcda3f4ad86bc1e15379cef845117a2e8143d9f1151fb083cb3f559b65a3a85e20697df16b6871cf320d51b5b08eda0d64d51989f44de3238dd24990b614fc',
    'as_loc': 'a80c84bc76ee294b73a12beb6e0536498437df01ed3a7b1d6c6ab5a99aab6288477c6bf57661be81bcb4e97e5afe2369c4315cac3fd42061a5ec2fb02adb028cbdf20ad5ccd69612b9d2e56c23f8fc6f1f665267e8f0ce72dbc4b1981457f676',
    'as_ma-id': 'SD4CXTTUCCKHC7JXAXKJP9FDKH22YC7U7TACU2F9DAX9YXHFA',
    'ma-as': '5fd331f6e53a8f02e5899bd27ed504e4590b9d7e40aaf12c1ed0b760306f424e',
    'rdcStatus': '1',
    'xp_ci': '3znpLWBzDfvz4qozCRqzF3ZnuEYj',
}

headers = {
    'Host': 'mobileapp.apple.com',
    'xx-calleridentity': 'a=AppleStore;r=AD17C3A6-C12E-4EB0-8D91-9C8B0BD85B3B;run=ED1A8693-7D5B-4E8F-B701-29222BEC6C12;stm=1639185812299;vv=5.14;vb=514000;',
    'user-agent': 'ASA/5.14 (iPhone) ss/3.00',
    'x-ma-pcmh': 'REL-5.14.0',
    'x-mme-device-id': '00008110-000144A81E22801E',
    'x-malang': 'zh-HK',
    'x-mme-client-info': '<iPhone14,2> <iPhone OS;15.1.1;19B81> <com.apple.AuthKit/1 (com.apple.store.Jolly/5.14.0.761)>',
    'x-apple-i-timezone': 'GMT+8',
    'x-apple-i-client-time': '2021-12-11T01:23:32Z',
    'accept-language': 'en-us',
    'x-apple-i-md-rinfo': '84215040',
    'x-deviceconfiguration': 'ss=3.00;dim=1170x2532;m=iPhone;v=iPhone14,2;vv=5.14;sv=15.1.1',
    'accept': '*/*',
    'if-none-match': '"f428c69d29473245f40b490c260441c7.38-7876c26.VTLVNS.800"',
    'x-apple-i-locale': 'zh_HK',
    'x-apple-i-md-m': 'JpGej9LLUm2X+mmAuu9lbQT7xZUHQcba8a8m2XB95cogXCPZ1XoUSxgHkUoaSR8CZWiH9vhxDV5QF1GW',
    'x-apple-i-md': 'AAAABQAAABBY27r0fNvpbeuZIOHtCHztAAAAAw==',
}



def getstock(model_id,proxy):
    params = (
    ('pn', model_id),
    ('sc', 'UNLOCKED/WW'),
    ('stores', 'R485,R610,R499,R428,R409,R673'),
)
    response = requests.get('https://mobileapp.apple.com/merch/p/hk-zh/product-locator/quotes', headers=headers, params=params,proxies={'http' : proxy,'https':proxy},timeout=10, cookies=cookies,verify=True)
    return response.json()

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://mobileapp.apple.com/merch/p/hk-zh/product-locator/quotes?pn=MLT63ZA%2FA&sc=UNLOCKED%2FWW&stores=R485%2CR610%2CR499%2CR428%2CR409%2CR673%2CR484%2CR697%2CR672%2CR639%2CR577', headers=headers, cookies=cookies)
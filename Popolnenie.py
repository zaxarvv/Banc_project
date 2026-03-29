Accounts11 = {
    'user_1':{
        'user_id': '12345',
        'name': 'Zaxar',
        'card':[{'id_card': '294','balance':50000.0},
                {'id_card': '214', 'balance':1000.30}
                ]
    },
    'user_2':{
        'user_id': '12346',
        'name': 'Alex',
        'card':[{'id_card': '243','balance':50000.0},
                {'id_card': '135', 'balance':1000.30}
                ]
    }
}
def make_transfer(source_card, target_card, amount):
    if source_card['balance'] < amount:
        return 'ошибка недостаточно денег'
    if source_card['id_card'] == target_card['id_card']:
        return 'ошибка перевд самому себе'
    source_card['balance'] -= amount
    target_card['balance'] += amount
    return 'Перевод успешно выполнен'

card_from = Accounts['user_1']['card'][0]
card_to = Accounts['user_1']['card'][1]

result = make_transfer(card_from, card_to, 10000)

print(result)
print(f"Баланс карты  {card_from['id_card']}: {card_from['balance']}")
print(f"Баланс карты  {card_to['id_card']}: {card_to['balance']}")

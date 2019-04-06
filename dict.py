#dictionary 字典

words = {
	'ramen': '拉麵',
	'pasta': '義大利麵'
}

words['tea'] = '茶' #新增新的key

print(words['ramen'])
print(words['pasta'])

p0 = {
		'name': '麥香奶茶',
		'price': 10
}

p1 = {
	'name': '珍珠奶茶',
	'price': 60
}

drinks = [p0, p1]
print(drinks[0]['name']) # '麥香奶茶'
print(drinks[1]['price']) # 60

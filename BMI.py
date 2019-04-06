heigh = input('請輸入身高(公尺): ')
weight = input('請輸入體重(公斤): ')
BMI = float(weight)/(float(heigh)**2)
print('你的BMI: ',BMI)
if BMI < 18.5:
	print('體重過輕')
elif BMI >= 18 and BMI < 24:
	print('正常範圍')
elif BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
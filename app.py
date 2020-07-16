import func_module

nowdate = func_module.date_now()
year = nowdate.year
month = nowdate.month
day = nowdate.day
#print(year,'년',month,'월',day,'일') # 띄어쓰기 됨 비추
print('{}년 {}월 {}일'.format(year,month,day))

xmas = nowdate.replace(month=12,day=25)

print('{}년 {}월 {}일'.format(xmas.year,xmas.month,xmas.day))
# money = 1
# # money =0
# # seat = 1
# seat = 0
#
# if money == 1:
#     if seat >= 1:
#         print('请坐')
#     else:
#         print('站着等座')
# else:
#     print('没钱不能上车')

'''
money = int(input('请输入余额：'))
if money >= 1:
    print(f'剩余余额{money}，可以上车')
    seat = int(input('请输入剩余座位：'))
    if seat >= 1:
        print(f'剩余座位{seat}请坐')
    else:
        print(f'当前剩余座位{seat}站着等位')
else:
    print('没钱不能上车')
'''




'''
练习：
请输入密码查询卡内余额，低于一百需要充值，低于五百建议充值，五百以上可享受会员服务
'''

money = int(input('请输入密码查询卡内余额：'))
cardMoney = 500

if money < 100:
    print(f'卡内余额剩余为{money}低于一百，需要充值')
elif cardMoney > money >= 100 :
    print(f'卡内余额为{money}，超过一百，无须充值，但少于{cardMoney}元建议充值')
elif money >= cardMoney:
     print(f'余额为{money},大于{cardMoney}元，可享会员服务')

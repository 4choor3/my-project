user='admin'
password='1234'
print('欢迎登录系统')
print('用户名：', user)

num=0

while num<3:
    input_user=input('请输入密码：')
    if input_user==password:
        print('登录成功')
        break
    else:
        print('登录失败')
        num += 1

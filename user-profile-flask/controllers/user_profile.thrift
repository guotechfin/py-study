namespace java cn.jpush.user.profile

service UserProfileServiceV2 {

    list<string> queryUKeyByPhone(1:string phone),

    string queryUKeyByToken(1:string token),

    string queryUKeyByUid(1:string uid),

    map<string, map<string, string>> queryProfile(1:string type, 2:string key, 3:list<string> columns),
    
    map<string, string> queryTrace(1:string tag, 2:string type, 3:string key, 4:i64 start, 5:i64 stop),

    list<string> queryUidByToken(1:string token),

    list<string> queryUidByIMEI(1:string imei),

    list<string> queryUkeyByMac(1:string mac),
}
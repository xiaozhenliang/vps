namespace py saas 

typedef i64 Ip 


struct Vps {
   1 : i64 id                        ,
   2 : optional Ip ipv4              ,
   3 : optional Ip ipv4_netmask      ,
   4 : optional Ip ipv4_gateway      ,
   5 : string password               ,
   6 : i64 os                        ,                       //os的id会软连接到真实的os镜像
   7 : i16 hd                        ,                       //单位G
   8 : i64 ram                       ,                       //单位M
   9 : i16 cpu                       ,                       //几个core
  10 : i64 host_id                   ,                       //如pc1.42qu.us
}

enum Cmd{
  NONE    = 0,
  OPEN    = 1,
  CLOSE   = 2,
  RESTART = 3,
}


typedef i64 VpsId 
typedef i64 Id

service VPS {

   Id    todo            ( 1:i64  host_id , 2:Cmd cmd),
   void  done            ( 1:i64  host_id , 2:Cmd cmd, 3:Id id, 4:i32 state=0, 5:string message=''), 

   Vps   vps             ( 1:i64  vps_id   ),
   void  netflow_save    ( 1:map<VpsId, list<i64>> netflow),
}



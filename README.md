# chatroom
聊天室 

根據**socket模塊**提供的函式組合,採用傳輸層無連接協定**udp套接字**，進行資料的傳輸，並支援多個客戶端同時連接服務端進行資料的傳輸，且客戶端註冊
用戶名時，篩選用戶名是否重複以及是否與服務器管理員同名，透過**字典型態**儲存用戶名與連線資訊判斷，並使用**fork技術**進行多個客戶端於不同進程間的訪問，完成這次基於udp和fork多進程的代碼編寫。

-------------------------------------------------------
功能 ： 類似qq群聊
1. 進入聊天室需要輸入姓名，姓名不能重複
2. 有人進入聊天室會向其他人發送通知
   xxx 進入了聊天室
3. 一個人發消息，其他人會收到消息
   xxx 說 ： xxxxxxxx
4. 用戶輸入 "**" 及退出聊天室，其他人也會收到通知
   xxx 退出了聊天室
5. 管理員喊話 服務端發送消息所有的客戶端都就收到
   管理員說 ：xxxxxx
   
-------------------------------------------------------
![image](https://github.com/dian0624/chatroom/blob/master/image/1585108804570.jpg)
![image](https://github.com/dian0624/chatroom/blob/master/image/1585109258276.jpg)

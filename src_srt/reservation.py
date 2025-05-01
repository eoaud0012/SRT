import time
from random import randint 
from SRT import SRT
from SRT import SeatType
import telegram
import asyncio
from SRT.passenger import Adult, Disability4To6

TELEGRAM_TOKEN = "6041435620:AAH-C98ovxjuHmKOFbDM7z-Y8lI88YK1UT4"
TELEGRAM_CHATID = "6055095538"

srt = SRT("2287599141", "eoaoWkd1!") #
dep = '대전'
arr = '수서'
date = '20250302' # 날짜 (yyyymmdd)
tr_time = '213000' # 시간 (HHMMSS)

# 기차 검색
trains = srt.search_train(dep, arr, date, tr_time, available_only=False)
print(*trains, sep='\n')
# 결과 :  [[SRT] 11월 06일, 수서~부산(20:00~22:23) 특실 매진, 일반실 .....
train_num = input("몇 번째 기차를 예매하시겠어요?(0번부터 시작)")
train_num = int(train_num)


flag = False
i = 0

# 루프 시작
while flag == False:
    try:
        i += 1
        trains = srt.search_train(dep, arr, date, tr_time, available_only=False)
        time.sleep(randint(1, 5))
        print(f"{i}번째 시도")
        # reservation = srt.reserve(trains[train_num], passengers=[Disability4To6(), Adult()], special_seat=SeatType.GENERAL_ONLY)
        reservation = srt.reserve(trains[train_num], special_seat=SeatType.GENERAL_ONLY)
        # reservation = srt.reserve(trains[train_num], passengers=[Disability4To6()], special_seat=SeatType.GENERAL_ONLY)
        print(reservation)
        asyncio.run(telegram.bot.send_message(chat_id = TELEGRAM_CHATID, text=f"[SRT] 예약 완료!\n{reservation}"))
        flag = True
        
    except:
        pass
        
# 결과 : [SRT] 11월 06일, 수서~부산(22:40~01:07) 52400원(1석), 구입기한 11월 06일 22:36
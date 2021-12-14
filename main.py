import matplotlib.pyplot as plt
#Grouping.py 파일을 포함시킴
from Grouping import *
#bike_plus.py 파일을 포함시킴
from bike_plus import *


#경기도
figure = plt.figure()
ax1 = figure.add_subplot()
ax2 = ax1.twinx()
combine_Gyeonggi = combine_Gyeonggi[combine_Gyeonggi.연도 == 2020]
combine_Gyeonggi_del = combine_Gyeonggi['건수']
combine_Gyeonggi_def = combine_Gyeonggi['확진자']
combine_Gyeonggi_del.plot(kind = 'line', y ='건수',ax = ax1)
combine_Gyeonggi_def.plot(kind = 'line', y = '확진자',color = 'red',ax = ax2)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus=False)
plt.title("Gyeonggi")
plt.legend()
plt.show()

#경상남도
figure = plt.figure()
ax3 = figure.add_subplot()
ax4 = ax3.twinx()
combine_Gyeongnam = combine_Gyeongnam[combine_Gyeongnam.연도 == 2020]
combine_Gyeongnam_del = combine_Gyeongnam['건수']
combine_Gyeongnam_def = combine_Gyeongnam['확진자']
combine_Gyeongnam_del.plot(kind = 'line', y = '건수',ax = ax3)
combine_Gyeongnam_def.plot(kind = 'line', y ='확진자',color = 'red',ax = ax4)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("경상남도")
plt.legend()
plt.show()

#대구
figure = plt.figure()
ax5 = figure.add_subplot()
ax6 = ax5.twinx()
combine_Daegu = combine_Daegu[combine_Daegu.연도 == 2020]
combine_Daegu_del = combine_Daegu['건수']
combine_Daegu_def = combine_Daegu['확진자']
combine_Daegu_del.plot(kind = 'line', y = '건수',ax = ax5)
combine_Daegu_def.plot(kind = 'line', y = '확진자',color = 'red',ax = ax6)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("대구")
plt.legend()
plt.show()

#부산
figure = plt.figure()
ax7 = figure.add_subplot()
ax8 = ax7.twinx()
combine_Busan = combine_Busan[combine_Busan.연도 == 2020]
combine_Busan_del = combine_Busan['건수']
combine_Busan_def = combine_Busan['확진자']
combine_Busan_del.plot(kind = 'line', y = '건수',ax = ax7)
combine_Busan_def.plot(kind = 'line', y = '확진자',color = 'red',ax = ax8)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("부산")
plt.legend()
plt.show()

#서울
figure = plt.figure()
ax15 = figure.add_subplot()
ax16 = ax15.twinx()
combine_Seoul = combine_Seoul[combine_Seoul.연도 == 2020]
combine_Seoul_del = combine_Seoul['건수']
combine_Seoul_def = combine_Seoul['확진자']
combine_Seoul_del.plot(kind = 'line', y = '건수',ax = ax15)
combine_Seoul_def.plot(kind = 'line', y = '확진자',color = 'red',ax = ax16)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("서울")
plt.legend()
plt.show()

#충청남도
figure = plt.figure()
ax9 = figure.add_subplot()
ax10 = ax9.twinx()
combine_Chungnam = combine_Chungnam[combine_Chungnam.연도 == 2020]
combine_Chungnam_del = combine_Chungnam['건수']
combine_Chungnam_def = combine_Chungnam['확진자']
combine_Chungnam_del.plot(kind = 'line', y = '건수',ax = ax9)
combine_Chungnam_def.plot(kind = 'line', y = '확진자',color = 'red',ax = ax10)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("충청남도")
plt.legend()
plt.show()

#충청북도
figure = plt.figure()
ax11 = figure.add_subplot()
ax12 = ax11.twinx()
combine_Chungbuk = combine_Chungbuk[combine_Chungbuk.연도 == 2020]
combine_Chungbuk_del = combine_Chungbuk['건수']
combine_Chungbuk_def = combine_Chungbuk['확진자']
combine_Chungbuk_del.plot(kind = 'line', y = '건수',ax = ax11)
combine_Chungbuk_def.plot(kind = 'line', y = '확진자',color = 'red',ax = ax12)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("충청북도")
plt.legend()
plt.show()

#이륜차 대 수
figure = plt.figure()
ax13 = figure.add_subplot()
ax14 = ax13.twinx()
bike_sum = pd.concat([bike_01,bike_02,bike_03,bike_04,bike_05,bike_06,bike_07,bike_08,bike_09,bike_10,bike_11,bike_12])
bike_sum = bike_sum.reset_index(drop = True)
print(bike_sum["Unnamed: 1"].values)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
datas = bike_sum
print(datas)
datas_int = list(map(int,datas["Unnamed: 1"].values))
print(datas_int)
print(datas.index.values+1)
plt.plot(datas.index.values+1, datas_int)
plt.title("이륜차 대 수")
plt.show()


#이륜차 월별 사고 건수
data = accident_status.T
print(data[16].values)
data_int = list(map(int,data[16].values))
print(data_int)
print(data.index.values)
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
plt.title("이륜차 월별 사고 건수")
plt.plot(data.index.values, data_int)
plt.show()
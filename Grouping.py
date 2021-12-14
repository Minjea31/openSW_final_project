import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

#누적 확진자 해야됌.

#차 사고 현황
accident_status = pd.read_csv('C:/Users/user/PycharmProjects/openSW/openSW_final project_data/차 사고수 현황_원본.csv')
accident_status = accident_status.iloc[16:17, 16:28]

#차 사고 현황 - 오토바이 사고 현황
accident_Motorcycle = accident_status.iloc[16:22]

#코로나 확진자 수
Covid19 = pd.read_csv('openSW_final project_data/Covid_local_원본.csv')
list_month1 = ['01월','02월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
list_month2 = ['1','2','3','4','5','6','7','8','9','10','11','12']
list_month3 = [1,2,3,4,5,6,7,8,9,10,11,12]
list_year = ['2020', '2021']
list_year2 = [2020, 2021]
list_sido=['경기','서울','충청북도','충청남도','경상남도','대구','부산']

#경기도 코로나 확진자 수
Covid19_Gyeonggi = Covid19.loc[Covid19["gubun"] == "경기"]
Covid19_Gyeonggi = Covid19_Gyeonggi[['stdDay','incDec']]
Covid19_Gyeonggi_Filtered = pd.DataFrame(columns=['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Gyeonggi[Covid19_Gyeonggi['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]],'월':[list_month3[i]],'확진자':[temp['incDec'].sum()]})
        Covid19_Gyeonggi_Filtered = Covid19_Gyeonggi_Filtered.append(temporary,ignore_index = True)
Covid19_Gyeonggi_Filtered = Covid19_Gyeonggi_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Gyeonggi_Filtered)-1):
    temp2 = Covid19_Gyeonggi_Filtered.loc[i+1,'확진자']
    Covid19_Gyeonggi_Filtered.loc[i+1,'확진자'] += Covid19_Gyeonggi_Filtered.loc[i,'확진자']

#경상남도 코로나 확진자 수
Covid19_Gyeongnam = Covid19.loc[Covid19["gubun"] == "경남"]
Covid19_Gyeongnam = Covid19_Gyeongnam[['stdDay','incDec']]
Covid19_Gyeongnam_Filtered = pd.DataFrame(columns = ['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Gyeongnam[Covid19_Gyeongnam['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]], '월': [list_month3[i]], '확진자': [temp['incDec'].sum()]})
        Covid19_Gyeongnam_Filtered = Covid19_Gyeongnam_Filtered.append(temporary,ignore_index = True)
Covid19_Gyeongnam_Filtered = Covid19_Gyeongnam_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Gyeongnam_Filtered)-1):
    temp2 = Covid19_Gyeongnam_Filtered.loc[i+1,'확진자']
    Covid19_Gyeongnam_Filtered.loc[i+1,'확진자'] += Covid19_Gyeongnam_Filtered.loc[i,'확진자']



#대구 코로나 확진자 수
Covid19_Daegu = Covid19.loc[Covid19["gubun"] == "대구"]
Covid19_Daegu = Covid19_Daegu[['stdDay','incDec']]
Covid19_Daegu_Filtered = pd.DataFrame(columns = ['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Daegu[Covid19_Daegu['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]], '월': [list_month3[i]], '확진자': [temp['incDec'].sum()]})
        Covid19_Daegu_Filtered = Covid19_Daegu_Filtered.append(temporary,ignore_index = True)
Covid19_Daegu_Filtered = Covid19_Daegu_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Daegu_Filtered)-1):
    temp2 = Covid19_Daegu_Filtered.loc[i+1,'확진자']
    Covid19_Daegu_Filtered.loc[i+1,'확진자'] += Covid19_Daegu_Filtered.loc[i,'확진자']

#부산 코로나 확진자 수
Covid19_Busan = Covid19.loc[Covid19["gubun"] == "부산"]
Covid19_Busan = Covid19_Busan[['stdDay','incDec']]
Covid19_Busan_Filtered = pd.DataFrame(columns = ['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Busan[Covid19_Busan['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]], '월': [list_month3[i]], '확진자': [temp['incDec'].sum()]})
        Covid19_Busan_Filtered = Covid19_Busan_Filtered.append(temporary,ignore_index = True)
Covid19_Busan_Filtered = Covid19_Busan_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Busan_Filtered)-1):
    temp2 = Covid19_Busan_Filtered.loc[i+1,'확진자']
    Covid19_Busan_Filtered.loc[i+1,'확진자']+=Covid19_Busan_Filtered.loc[i,'확진자']

#서울 코로나 확진자 수
Covid19_Seoul = Covid19.loc[Covid19["gubun"] == "서울"]
Covid19_Seoul = Covid19_Seoul[['stdDay','incDec']]
Covid19_Seoul_Filtered = pd.DataFrame(columns = ['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Seoul[Covid19_Seoul['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]], '월': [list_month3[i]], '확진자': [temp['incDec'].sum()]})
        Covid19_Seoul_Filtered = Covid19_Seoul_Filtered.append(temporary,ignore_index = True)
Covid19_Seoul_Filtered = Covid19_Seoul_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Seoul_Filtered)-1):
    temp2=Covid19_Seoul_Filtered.loc[i+1,'확진자']
    Covid19_Seoul_Filtered.loc[i+1,'확진자']+=Covid19_Seoul_Filtered.loc[i,'확진자']

#충남 코로나 확진자 수
Covid19_Chungnam = Covid19.loc[Covid19["gubun"] == "충남"]
Covid19_Chungnam = Covid19_Chungnam[['stdDay','incDec']]
Covid19_Chungnam_Filtered = pd.DataFrame(columns = ['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Chungnam[Covid19_Chungnam['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]], '월': [list_month3[i]], '확진자': [temp['incDec'].sum()]})
        Covid19_Chungnam_Filtered = Covid19_Chungnam_Filtered.append(temporary,ignore_index = True)
Covid19_Chungnam_Filtered = Covid19_Chungnam_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Chungnam_Filtered)-1):
    temp2 = Covid19_Chungnam_Filtered.loc[i+1,'확진자']
    Covid19_Chungnam_Filtered.loc[i+1,'확진자'] += Covid19_Chungnam_Filtered.loc[i,'확진자']

#충북 코로나 확진자 수
Covid19_Chungbuk = Covid19.loc[Covid19["gubun"] == "충북"]
Covid19_Chungbuk = Covid19_Chungbuk[['stdDay','incDec']]
Covid19_Chungbuk_Filtered = pd.DataFrame(columns = ['stdDay','incDec'])

for j in range(2):
    for i in range(12):
        temp = Covid19_Chungbuk[Covid19_Chungbuk['stdDay'].str.contains(list_month1[i])]
        temp = temp[temp['stdDay'].str.contains(list_year[j])]
        temporary = pd.DataFrame({'연도':[list_year2[j]], '월': [list_month3[i]], '확진자': [temp['incDec'].sum()]})
        Covid19_Chungbuk_Filtered = Covid19_Chungbuk_Filtered.append(temporary,ignore_index = True)
Covid19_Chungbuk_Filtered = Covid19_Chungbuk_Filtered.drop(['stdDay','incDec'],axis = 1)

for i in range(len(Covid19_Chungbuk_Filtered)-1):
    temp2 = Covid19_Chungbuk_Filtered.loc[i+1,'확진자']
    Covid19_Chungbuk_Filtered.loc[i+1,'확진자'] += Covid19_Chungbuk_Filtered.loc[i,'확진자']

#2019_0106 배달 건 수
delivery_2019_0101 = pd.read_csv('openSW_final project_data/20190101_원본.csv')
delivery_2019_0712 = pd.read_csv('openSW_final project_data/20190701_원본.csv')
delivery_2020_0106 = pd.read_csv('openSW_final project_data/20200101_원본.csv')
delivery_2020_0712 = pd.read_csv('openSW_final project_data/20200701_원본.csv')
delivery_2021_0106 = pd.read_csv('openSW_final project_data/20210101_원본.csv')
delivery_2020_0112 = pd.concat([delivery_2019_0101, delivery_2019_0712, delivery_2020_0106,delivery_2020_0712, delivery_2021_0106])

delivery_2020_0112 = delivery_2020_0112.drop(["업종",'군구','거리'], axis = 1)

gyeonggi_data = delivery_2020_0112[delivery_2020_0112.시도 == '경기도']
gyeongnam_data = delivery_2020_0112[delivery_2020_0112.시도 == '경상남도']
Daegu_data = delivery_2020_0112[delivery_2020_0112.시도 == '대구광역시']
Busan_data = delivery_2020_0112[delivery_2020_0112.시도 == '부산광역시']
Seoul_data = delivery_2020_0112[delivery_2020_0112.시도 == '서울특별시']
Chungnam_data = delivery_2020_0112[delivery_2020_0112.시도 == '충청남도']
Chungbuk_data = delivery_2020_0112[delivery_2020_0112.시도 == '충청북도']

sido_del_data = pd.DataFrame(columns = ['시도','연도','월','건수'])

for sido in list_sido:
    for j in list_year2:
        for i in list_month3:
            sidotemp = delivery_2020_0112[delivery_2020_0112.월 == i]
            sidotemp = sidotemp[sidotemp.연도 == j]
            sidotemporary = pd.DataFrame({'시도':[sido],'연도': [j], '월': [i], '건수': [sidotemp['건수'].sum()]})
            sido_del_data = sido_del_data.append(sidotemporary,ignore_index = True)

combine_Gyeonggi = pd.merge(sido_del_data[sido_del_data.시도 == '경기'],Covid19_Gyeonggi_Filtered)
combine_Gyeongnam = pd.merge(sido_del_data[sido_del_data.시도 == '경상남도'],Covid19_Gyeongnam_Filtered)
combine_Daegu = pd.merge(sido_del_data[sido_del_data.시도 == '대구'],Covid19_Daegu_Filtered)
combine_Busan = pd.merge(sido_del_data[sido_del_data.시도 == '부산'],Covid19_Busan_Filtered)
combine_Seoul = pd.merge(sido_del_data[sido_del_data.시도 == '서울'],Covid19_Seoul_Filtered)
combine_Chungnam = pd.merge(sido_del_data[sido_del_data.시도 == '충청남도'],Covid19_Chungnam_Filtered)
combine_Chungbuk = pd.merge(sido_del_data[sido_del_data.시도 == '충청북도'],Covid19_Chungbuk_Filtered)
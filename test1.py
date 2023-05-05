import requests
import csv

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"

# 查询条件
bondType = '100001'
issueYear = '2023'
page = 1

up_data = f"?pageNo={page}&pageSize=15&isin=&bondCode=&issueEnty=&bondType={bondType}&couponType=&issueYear={issueYear}&rtngShrt=&bondSpclPrjctVrty="

# 提交get请求
res = requests.get(url=url+up_data, headers=headers)
# 获取数据
res_data = dict(res.json())['data']

# 解析
total = res_data['total']
resultList = res_data['resultList']

pageTotal = res_data['pageTotal']
# print(resultList)
# print(pageTotal)

titles = ['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']
data = []

for i in range(1, pageTotal):
    for eachData in resultList:
        this_data = [eachData['isin'], eachData['bondCode'], eachData['entyFullName'], eachData['bondType'], eachData['issueStartDate'], eachData['debtRtng']]
        data.append(this_data)
        # print(this_data)
    if (i+1) != pageTotal:
        up_data = f"?pageNo={i+1}&pageSize=15&isin=&bondCode=&issueEnty=&bondType={bondType}&couponType=&issueYear={issueYear}&rtngShrt=&bondSpclPrjctVrty="
        res = requests.get(url=url+up_data, headers=headers)
        resultList = dict(res.json())['data']['resultList']

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(titles)
    writer.writerows(data)

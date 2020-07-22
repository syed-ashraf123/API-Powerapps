from flask import Flask,render_template,request
import requests
import json
import re
from statistics import mean 
import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages
from bs4 import BeautifulSoup
headers={
    'accept':'*/*',
    'method': 'GET',
    'path': '/ajax/nav/UserNavAsync.htm?pageframe=true',

    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cookie': 'zguid=23|%247477d58d-26b4-48a4-874b-e4830bb00dee; _ga=GA1.2.1461655041.1593612751; zjs_user_id=null; zjs_anonymous_id=%227477d58d-26b4-48a4-874b-e4830bb00dee%22; _pxvid=e89dfed6-bba4-11ea-8b26-0242ac120009; _gcl_au=1.1.556517947.1593612752; _fbp=fb.1.1593612753197.31498831; _pin_unauth=dWlkPU9HVTFOVEEwT0RZdFl6RmpPQzAwTkdVMExXSmhNelF0WldZNFl6Rm1ObVEzTkdZMQ; G_ENABLED_IDPS=google; __gads=ID=9be2d6409f2ebf8b:T=1593616228:S=ALNI_MZIRCGndniilaken3iSWJNYe9H03g; ki_r=; ki_s=; ki_t=1593698015413%3B1593698015413%3B1593699560167%3B1%3B5; g_state={"i_p":1593842680487,"i_l":2}; zgsession=1|703dd965-b0af-48a4-b13f-ca15ab78468b; KruxPixel=true; DoubleClickSession=true; KruxAddition=true; _gid=GA1.2.664843069.1594030833; JSESSIONID=4897CD0C285049B023F8D4B9CCEB5E9E; GASession=true; _px3=f4134e9f51f364a544fd33e1c7bcf8319d4e1540db55d9fa5637aa19fb621590:kHDGu7NxblyQagsUeFyO8Sh9uow4Z7eA8PkL2JRzDasGO5q68kBlMEkGVs2UQ0JbklOj4N+uOxBZIh/Q8vSdLA==:1000:et0cqEPBqfv7n0FKxMrMRIVPO6DU5Fad8UgJ2f4rt8ZcVJa5DcQaBB+O6/KkRxiAgNyUjHHOnfIjh4EFa59JGCyl5gqytxawIE2GcIABcu3Q4tWWw3RTNNNEGFs8DyekL8UGuvEpOghMWWYPX5ebKldYheVi6/vgDlzn6mEiBrM=; _uetsid=d09a8cd5-2efa-ed86-ac0f-6e2e478fa11e; _uetvid=3603e5e3-1738-d84e-40b0-e7edb37453f4; _gat=1; AWSALB=MACKgbLQ4Xq5FoidFWOCBSYVe+thyj3rcW4SefyxG9zWSkDhOBnT3yRGVdUCHjGjLI6yyc9SHiNwRzvJCGQQ0TH1fQOAbi6rMRGUX6i8m5d3SkH6xeCh8OV2fqk5; AWSALBCORS=MACKgbLQ4Xq5FoidFWOCBSYVe+thyj3rcW4SefyxG9zWSkDhOBnT3yRGVdUCHjGjLI6yyc9SHiNwRzvJCGQQ0TH1fQOAbi6rMRGUX6i8m5d3SkH6xeCh8OV2fqk5; search=6|1596622908014%7Crect%3D38.96992552152501%252C-76.80287268359373%252C38.82831390105304%252C-77.22584631640623%26rid%3D41568%26disp%3Dmap%26mdm%3Dauto%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0941568%09%09%09%09%09%09',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
url="https://www.zillow.com/homes/"

app = Flask(__name__,template_folder='templates', static_folder='static')

@app.route('/<variable>')
def profile(variable):
    def scraper(address):
        df=0
        priceHistory=0
        tax=0
        transit=0
        walk=0
        scolrating=0
        address=url+address.replace(", ",".dash.").replace(" ",".dash.").replace("/",".dash.").replace("#",".num.").replace("-",".dash.")+'_rb'
        res=requests.get(address,headers=headers)
        a=0
        #try:
        soup=BeautifulSoup(res.text,'html.parser')
        price = soup.find("span", {"class": "ds-value"}).get_text()
        #estimated=soup.find("span", {"class": "sc-drMfKT hVItaR"}).get_text()
        beds=soup.find("h3", {"class": "ds-bed-bath-living-area-container"}).get_text()
        estimated=0
        median=soup.find_all("p", {"class": "Text-aiai24-0 StyledParagraph-sc-18ze78a-0 hxLFAq"})[-1].get_text()
        #dic={"Price":["".join(re.findall('\\d+', price ))],"Estimated":["".join(re.findall('\\d+', estimated ))],
        #     "Median":["".join(re.findall('\\d+', median ))],"Beds":[beds]}
        #df=pd.DataFrame(dic)
    #         fig, ax =plt.subplots(figsize=(12,4))
    #         ax.axis('tight')
    #         ax.axis('off')
    #         the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
    #         #https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
    #         pp = PdfPages("Price.pdf")
    #         pp.savefig(fig, bbox_inches='tight')
    #         pp.close()
        a=1
        #except:
        #    return "Either Address or something else is wrong please try checking the Address or try with different Address"  
        if a:
            priceHistory={'Event':[],'Time':[],'Price':[],'PriceChangeRate':[]}
            try:
                const=soup.select("[type='application/json']")
                firstValue = str(const[3]).index("{")
                lastValue = len(str(const[3])) - str(const[3])[::-1].index("}")
                jsonString = str(const[3])[firstValue:lastValue]
                l=json.loads(jsonString)
                x=json.loads(l['apiCache'])
                for c,i in enumerate(x):
                    if c==0:
                        continue
                    else:
                        for k in x[i]['property']['priceHistory']:
                            priceHistory['Event'].append(k['event'])
                            priceHistory['Time'].append(k['time'])
                            priceHistory['Price'].append(k['price'])
                            priceHistory['PriceChangeRate'].append(k['priceChangeRate'])
                    if not priceHistory['Event']:
                        priceHistory['Event']=[None]
                    if not priceHistory['Time']:
                        priceHistory['Time']=[None]
                    if not priceHistory['Price']:
                        priceHistory['Price']=[None]
                    if not priceHistory['PriceChangeRate']:
                        priceHistory['PriceChangeRate']=[None]                
                    priceHistory=pd.DataFrame(priceHistory)
            except:
                priceHistory['Event']=[None]
                priceHistory['Time']=[None]
                priceHistory['Price']=[None]
                priceHistory['PriceChangeRate']=[None]
                priceHistory=pd.DataFrame(priceHistory)
    #         fig, ax =plt.subplots(figsize=(12,4))
    #         ax.axis('tight')
    #         ax.axis('off')
    #         the_table = ax.table(cellText=priceHistory.values,colLabels=priceHistory.columns,loc='center')
    #         #https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
    #         pp = PdfPages("PriceHistory.pdf")
    #         pp.savefig(fig, bbox_inches='tight')
    #         pp.close()
        if a:
            tax={'Time':[],'TaxPaid':[],'TaxIncreaseRate':[],'Value':[],'ValueIncreaseRate':[]}
            try:
                const=soup.select("[type='application/json']")
                firstValue = str(const[3]).index("{")
                lastValue = len(str(const[3])) - str(const[3])[::-1].index("}")
                jsonString = str(const[3])[firstValue:lastValue]
                l=json.loads(jsonString)
                x=json.loads(l['apiCache'])
                
                for c,i in enumerate(x):
                    if c==0:
                        continue
                    else:
                        for k in x[i]['property']['taxHistory']:
                            tax['Time'].append(k['time'])
                            tax['TaxPaid'].append(k['taxPaid'])
                            tax['TaxIncreaseRate'].append(k['taxIncreaseRate'])
                            tax['Value'].append(k['value'])
                            tax['ValueIncreaseRate'].append(k['valueIncreaseRate'])
                    if not tax['Time']:
                        tax['Time']=[None]
                    if not tax['TaxPaid']:
                        tax['TaxPaid']=[None]
                    if not tax['TaxIncreaseRate']:
                        tax['TaxIncreaseRate']=[None]
                    if not tax['Value']:
                        tax['Value']=[None]
                    tax=pd.DataFrame(tax)
            except:
                tax['Time']=[None]
                tax['TaxPaid']=[None]
                tax['TaxIncreaseRate']=[None]
                tax['Value']=[None]
                tax['ValueIncreaseRate']=[None]
                tax=pd.DataFrame(tax)
    #         fig, ax =plt.subplots(figsize=(12,4))
    #         ax.axis('tight')
    #         ax.axis('off')
    #         the_table = ax.table(cellText=tax.values,colLabels=tax.columns,loc='center')
    #         #https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
    #         pp = PdfPages("PriceHistory.pdf")
    #         pp.savefig(fig, bbox_inches='tight')
    #         pp.close()
            const=soup.select("[type='application/json']")
            firstValue = str(const[3]).index("{")
            lastValue = len(str(const[3])) - str(const[3])[::-1].index("}")
            jsonString = str(const[3])[firstValue:lastValue]
            l=json.loads(jsonString)
            x=json.loads(l['apiCache'])
            for c,i in enumerate(x):
                if c==0:
                    continue
                j=x[i]['property']
            lat=j['latitude']
            long=j['longitude']
            address=f"https://www.walkscore.com/score/loc/lat={lat}/lng={long}/"
            res=requests.get(address)
            soup=BeautifulSoup(res.text,'html.parser')
            try:
                z=soup.find("span",{"id":"score-description-sentence"}).get_text()
                transit=soup.find_all('img')[4]['alt'][:3].strip()
                walk=re.search('\\d{2} out',z).group()[:3].strip()
                scolrating=[]
                for i in j['schools']:
                    scolrating.append(i['rating'])
            except:
                transit=0
                walk=0
                scolrating=[0]
            #df,priceHistory,tax,transit,walk,mean(scolrating)
            transit={"transit":transit,"walk":walk,"scolrating":mean(scolrating)}
        return transit

    scraped=scraper(variable)
    return scraped




if __name__ == "__main__":
    app.run(debug=True)

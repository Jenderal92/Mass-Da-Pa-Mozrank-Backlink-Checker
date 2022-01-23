#Youtube : Py
#Coded By Shin Code
#My Friend : Jenderal92 - h0d3_g4n - Moslem - Kiddenta - Naskleng45
# Mass Da/Pa ,Mozrank, Backlink Checker 
import requests,re,random,sys,time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''

               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  
=============
[ Mass Da/Pa ,Mozrank, Backlink Checker | Python Code ]
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)
Banner()

def Mozz(url):
	try:
		users = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Referer': 'https://www.checkmoz.com/',
		'Cookie': 'PHPSESSID=44abdbff391488753da06afcc1ab7829; _gid=GA1.2.482119999.1642210982; _ga_R1KTSPSL8T=GS1.1.1642210981.1.1.1642211108.0; _ga=GA1.2.804098276.1642210982; _gat_gtag_UA_184168411_1=1'}
		datas = {'getStatus': '1',
		'siteID': '1',
		'sitelink': url,
		'da': '1',
		'pa': '1',
		'moz': '1',
		'ml': '1',
		'alexa': '1',
		'ip': '1',
		'google': '1'
		}
		urll = requests.post("https://www.checkmoz.com/bulktool",data=datas, headers=users).text
		if '<td align="center">1</td><td id="link"><a href="' in urll:
			xx = re.findall('<td>(.*?)</td>', urll)
			print('Domain  : ' +Fore.GREEN+ url +Fore.WHITE)
			print('Domain Authority : ' +Fore.GREEN+ xx[0]+Fore.WHITE)
			print('Page Authority : ' +Fore.GREEN+ xx[1]+Fore.WHITE)
			print('MozRank : '+Fore.GREEN+ xx[2]+Fore.WHITE)
			print('BackLinks : '+Fore.GREEN+ xx[3]+Fore.WHITE)
			print('Alexa Rank : '+Fore.GREEN+ xx[4]+Fore.WHITE)
			print('IP Address : '+Fore.GREEN+ xx[5]+Fore.WHITE)
			print('Google Index : '+Fore.GREEN+ xx[6]+Fore.WHITE)
			print('--------------------------------------------------------------')
			open('results.txt', 'a').write('\n--------------- Da/Pa ,Mozrank, Backlink Checker -------------\n'+url+' : '+ xx[0] + '|' +xx[1] + '|' + xx[2] + '|' + xx[3] + '|' + xx[4] + '|' + xx[5] + '|' + xx[6] +'\n--------------- Coded By Shin Code -------------\n')
	except Exception as e:
		print('Coded By Shin Code'+str(e))

url_list = raw_input("URL LIST : ")
urr = open(url_list, 'r').readlines()
def main():
	for i in urr:
		try:
			site = i.strip()
			data=ssc(site)
		except:
			pass

pool = ThreadPool(15)
pool.map(Mozz, urr)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success")
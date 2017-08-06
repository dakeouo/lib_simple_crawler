#-*-coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import math

base_url = "http://millennium.lib.ntust.edu.tw/search~S1*cht?/"
msg_url = "http://millennium.lib.ntust.edu.tw/search~S2*cht/?" #To get the total Url

sType_dict = {"X":"關鍵字", "t":"書名", "a":"主題", "c":"索書號(美國國會)", "l":"索書號(中國圖書)", "i":"國際標準號碼", "v":"條碼"}
sScope_dict = {1:"全部館藏", 2:"圖書", 3:"期刊", 4:"視聽資料", 5:"學位論文", 6:"電子書", 7:"電子期刊"}

sSORT = "DZ"

def get_Total(sArg, sType="X", sScope=1):

    s_url = msg_url+"searchtype="+str(sType)+"&searcharg="+str(sArg)+"&searchscope="+str(sScope)+"&sortdropdown=-&SORT="+sSORT+"&extended=0&SUBMIT=查詢"+"&searchlimits="
    #print("sType="+str(sType)+",sScope="+str(sScope)+",sArg="+str(sArg))
    Search_res = requests.get(s_url + "browse")
    Search_res.status_code #200
    Search_soup = BeautifulSoup(Search_res.text, 'html.parser')
    searchMsg = Search_soup.find('div',{'class':'browseSearchtoolMessage'}) #get the total item
    searchMsg = searchMsg.text
    searchMsg = searchMsg.split(" ")

    return int(searchMsg[1])

def Search_book(sArg, sType="X", sScope=1):
    #print("sType="+str(sType)+",sScope="+str(sScope)+",sArg="+str(sArg))
    loc_i = 1
    sTot = get_Total(sArg,sType,sScope)

    while(loc_i <= sTot):
        save_file(loc_i,sTot,sArg,sType,sScope)
        print("已完成第%d頁的資料" %(math.floor(((loc_i+49)/51)+1)))
        loc_i = loc_i + 50

def save_file(start_item,tot_item,sArg,sType="X",sScope=1):

    end_item = start_item + 49
    if (tot_item < end_item):
        end_item = tot_item

    TASS = sType + sArg + "&searchscope=" + str(sScope) + "&SORT=" + sSORT
    url = base_url + TASS + "/" + TASS + "&SUBKEY" + sArg + "/" + str(start_item) + "%2C" + str(tot_item) + "%2C" + str(tot_item) + "%2CB/"
    NTUST_res = requests.get(url + "browse")
    NTUST_res.status_code #200
    NTUST_soup = BeautifulSoup(NTUST_res.text, 'html.parser')
    
    page = math.floor((end_item/51)+1)

    file_path = '[台科大圖書館]以{0}查詢{1}:{2}(Page{3}).txt'.format(str(sType_dict[sType]),str(sScope_dict[sScope]),str(sArg),str(page))
    bno = start_item #book number

    img_alt = [] #store book type
    img_find = NTUST_soup.findAll('div',{'class':'briefcitMedia'})
    for item in img_find:
        get_alt = item.find('img')
        img_alt.append(get_alt['alt'])

    x=0
    while(x<len(img_alt)):
        if img_alt[x] == "印刷型資料":
            img_alt[x] = "一般圖書"
        if img_alt[x] == "EBOOKS":
            img_alt[x] = "電子書"
        x=x+1

    with open(file_path, "w+", newline='') as txtfile:
        browseMsg_txt = "------{0}查詢結果：條目{1}-{2}，共{3}個結果查獲------".format(str(sArg),str(start_item),str(end_item),str(tot_item))
        txtfile.write(browseMsg_txt)

    i=0
    with open(file_path, "a", newline='') as txtfile:
        book_info = NTUST_soup.findAll('td',{'class':'briefcitDetail'})
        for item in book_info:
            #print(img_alt[i])
            b_info = item.text
            b_info = b_info.split("評級") #0:book info 1:NTUST library info
            n_info = b_info[0]
            n_info = n_info.strip() #del top/back '\n'
            n_info = n_info.split('\n') #0:book name 2:author 3:publish place/press/year
            if len(n_info) == 1:
                n_info.append("")
                n_info.append("(None)")
                n_info.append("(None)")
            elif len(n_info) == 3:
            	n_info.append("(None)")

            book_msg = '''
No.{b_no}[{b_alt}]
書名:{b_name}
作者:{b_auth}
出版地/出版社/出版年:{b_pub}
            '''.format(
                b_no = str(bno),
                b_alt = img_alt[i],
                b_name = n_info[0],
                b_auth = n_info[2],
                b_pub = n_info[3],
            )
            txtfile.write(book_msg)

            b_info = b_info[1]
            if img_alt[i] == "電子書":
                b_info = b_info.split("\n")
            else:
                #print((b_info))
                b_info = b_info.strip() #del top/back '\n'
                b_info = b_info.split("(說明)\n")
                if len(b_info) == 1:
                    b_info = ['','']

                b_info = b_info[1]
                b_info = b_info.strip("\n")
                b_info = b_info.split("\n")
                if len(b_info) == 1:
                    break

                #print(len(b_info))
                x=0 #count col times
                y=0 #count flag
                b_tail = []
                b_res = []
                while(len(b_info) >= 7*(x+1)):
                    b_res = []
                    while y < 8*x+7:
                        b_res.append(b_info[y])
                        y=y+1
                    b_tail.append(b_res)
                    x=x+1
                    y=y+1
                #print("x="+str(x))

                lib_title = '''
==========================================================
               [NTUST Library Information]
'''
                txtfile.write(lib_title)
                x=0
                while(x<len(b_tail)):
            	    detial_msg = '''
館藏地:{b_coll}
條碼:{b_code}
索書號:{b_claim}
冊次:{b_ty}
年代:{b_y}
狀態:{b_status}
-----------------
                    '''.format(
                        b_coll = b_tail[x][0].strip(),
                        b_code = b_tail[x][2].strip(),
                        b_claim = b_tail[x][3].strip(),
                        b_ty = b_tail[x][4].strip(),
                        b_y = b_tail[x][5].strip(),
                        b_status = b_tail[x][6].strip(),
                    )
            	    txtfile.write(detial_msg)
            	    x=x+1
                    
            bno = bno + 1
            i=i+1           


#print(Search_book("java"))
    
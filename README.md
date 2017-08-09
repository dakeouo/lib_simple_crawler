# lib_simple_crawler

The NTUST Library Simple Crawer 使用台科大圖書館網站來製作簡單的Python爬蟲

### 爬蟲執行步驟
1.如果是windows用戶，在執行[NTUST_lib](/NTUST_lib)之前，建議先新增requests、bs4函式庫：
```sh
$ pip install requests
$ pip install bs4
```
2.之後在shell打上`$ python NTUST_lib help`，會給你輸入說明
```sh
Python NTUST_lib search [-t type] [-s scope] [-c content]
-t    Search Book Type                      -s    Search Book Scope
----------------------------------------    ----------------------------------
X Keyword          t Book Name             1 All Result   5 Degree Thesis
a author           d topic                 2 Books        6 E-Books
c USA Claim number l China Claim number    3 Journals     7 Electronic Journal
i ISBN             v Barcode               4 Audiovisual info.
```
3.之後只要打上`$ python NTUST_lib search`，後面打上`-t`、`-s`、`-c`等變數，就會幫你把結果輸出成檔案(50筆為一個檔案)，儲存至當前的目錄
| 變數 | 說明 |
| ------ | ------ |
| -t type | 查詢內容的類型 |
| -s scope | 查詢館藏類型 |
| -c content | 要查詢的內容 |

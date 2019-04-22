# lib_simple_crawler

The NTUST Library Simple Crawer 使用台科大圖書館網站來製作簡單的Python爬蟲

### 爬蟲執行步驟
1.如果是windows用戶，在執行[NTUST_lib](/NTUST_lib)之前，請確認您的Python版本是否為第3版，並新增[requests](http://docs.python-requests.org/en/master/)、[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)函式庫：
```sh
$ pip install requests
$ pip install bs4
```
2.之後在shell打上`$ python3 NTUST_lib help`，會給你輸入說明
```sh
Python3 NTUST_lib search [-t type] [-s scope] [-c content]
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

4.檔案名稱命名規則：[台科大圖書館]以`type`查詢`scope`:`content`(Page`num`).txt

5.輸出檔案結果範例(以查詢關鍵字為例)

| 關鍵字 | 館藏類型 |結果|
| ------ | ------ |------|
| Django | 全部館藏 |[[台科大圖書館]以關鍵字查詢全部館藏:django(Page1).txt][result-django]
| Laravel | 全部館藏 |[[台科大圖書館]以關鍵字查詢全部館藏:laravel(Page1).txt][result-laravel]
| Public | 學位論文 |[[台科大圖書館]以關鍵字查詢學位論文:public(Page1).txt][result-public1]<br />[[台科大圖書館]以關鍵字查詢學位論文:public(Page2).txt][result-public2]<br />[[台科大圖書館]以關鍵字查詢學位論文:public(Page3).txt][result-public3]
| Java | 電子書 |[[台科大圖書館]以關鍵字查詢電子書:java(Page1).txt][result-java1]<br />[[台科大圖書館]以關鍵字查詢電子書:java(Page2).txt][result-java2]<br />[[台科大圖書館]以關鍵字查詢電子書:java(Page3).txt][result-java3]<br />[[台科大圖書館]以關鍵字查詢電子書:java(Page4).txt][result-java4]<br />[[台科大圖書館]以關鍵字查詢電子書:java(Page5).txt][result-java5]<br />[[台科大圖書館]以關鍵字查詢電子書:java(Page6).txt][result-java6]

   [result-django]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢全部館藏:django(Page1).txt>
   [result-laravel]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢全部館藏:laravel(Page1).txt>
   [result-public1]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢學位論文:public(Page1).txt>
   [result-public2]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢學位論文:public(Page2).txt>
   [result-public3]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢學位論文:public(Page3).txt>
   [result-java1]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢電子書:java(Page1).txt>
   [result-java2]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢電子書:java(Page2).txt>
   [result-java3]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢電子書:java(Page3).txt>
   [result-java4]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢電子書:java(Page4).txt>
   [result-java5]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢電子書:java(Page5).txt>
   [result-java6]: </NTUST_lib/sample/[台科大圖書館]以關鍵字查詢電子書:java(Page6).txt>

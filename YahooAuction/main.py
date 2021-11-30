import ListingData
import Const
import re
import os
import sys
import pandas as pd
import numpy as np
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options



# 写真チェック（1枚も設定されていない場合エラー処理）
def PictureCheck(picture):

    if (picture.product_img0 is np.NAN) and (picture.product_img1 is np.NAN) and (picture.product_img2 is np.NAN) and (picture.product_img3 is np.NAN and picture.product_img4 is np.NAN) \
        and (picture.product_img5 is np.NAN) and (picture.product_img6 is np.NAN) and (picture.product_img7 is np.NAN) and (picture.product_img8 is np.NAN) and (picture.product_img9 is np.NAN):
        return False

    else:
        return True


# データチェック（必要最低事項が未記入の場合エラー処理）
def DataCheck(data):

    if (data.title is np.NAN) or (data.description is np.NAN) or (data.location is np.NAN) or (data.price is np.NAN):
        return False

    else:
        return True


# csvファイルから出品情報を読み出し
def DataRead():
    
    # 商品リスト
    listing_data_list = []

    try:
        df = pd.read_csv('ProductList.csv', encoding='utf-8')                  # ToDo : ファイル名指定方法 （コマンドライン引数 or 固定ファイル名）  ※ユーザー決定
        global user
        user = df.iat[1, 1]         # ユーザー名：取得
        global password
        password = df.iat[2, 1]     # パスワード：取得

        if user is np.NAN or password is np.NAN:
            print("【 ユーザー名 / パスワード 】が、入力されていません。")
            print(" '.csv'内のデータを再度確認して下さい。")
            sys.exit()

        # 列挙型 Enum
        col = Const.Listing_Column
        s_num = Const.Shipping_Method_Num
    
        product_no = 1
        start_row = 6
        for row in range(start_row, len(df)):
            
            # クラスインスタンス生成
            listing_data = ListingData.Listing()
            
            # 商品画像
            listing_data.product_img0 = df.iat[row, col._img0.value] or np.NAN
            listing_data.product_img1 = df.iat[row, col._img1.value] or np.NAN
            listing_data.product_img2 = df.iat[row, col._img2.value] or np.NAN
            listing_data.product_img3 = df.iat[row, col._img3.value] or np.NAN
            listing_data.product_img4 = df.iat[row, col._img4.value] or np.NAN
            listing_data.product_img5 = df.iat[row, col._img5.value] or np.NAN
            listing_data.product_img6 = df.iat[row, col._img6.value] or np.NAN
            listing_data.product_img7 = df.iat[row, col._img7.value] or np.NAN
            listing_data.product_img8 = df.iat[row, col._img8.value] or np.NAN
            listing_data.product_img9 = df.iat[row, col._img9.value] or np.NAN

            if not PictureCheck(listing_data):
                continue

            # 商品詳細
            listing_data.no = product_no
            listing_data.title = df.iat[row, col._title.value] or np.NAN                                # ToDo：未記入エラー処理（落ち箇所通知）
            listing_data.category = df.iat[row, col._category.value] or const.OTHER
            listing_data.new_old = df.iat[row, col._new_old.value] or const.PRODUCT_STATUS_2
            listing_data.description = df.iat[row, col._description.value] or np.NAN                    # ToDo：未記入エラー処理（落ち箇所通知）

            # 商品（返品受付）
            product_return = int(df.iat[row, col._product_return.value]) or False
            if product_return == 1:
                listing_data.product_return = True

            elif product_return == 0:
                listing_data.product_return = False
            else:
                listing_data.product_return = False

            listing_data.location = df.iat[row, col._location.value] or np.NAN                          # ToDo：未記入エラー処理（落ち箇所通知）
            listing_data.shipping_charge = df.iat[row, col._shipping_charge.value] or const.SELLER

            # 配送方法
            shippinng_method_val = int(df.iat[row, col._shipping_method.value] or s_num._s_method2.value)
            if shippinng_method_val == s_num._s_method0.value:
                listing_data.shipping_method = const.YAHONEKO_POS

            elif shippinng_method_val == s_num._s_method1.value:
                listing_data.shipping_method = const.YAHONEKO_EXPRESS_COMPACT

            elif shippinng_method_val == s_num._s_method2.value:
                listing_data.shipping_method = const.YAHONEKO_EXPRESS
            
            elif shippinng_method_val == s_num._s_method3.value:
                listing_data.shipping_method = const.YU_PACKET

            elif shippinng_method_val == s_num._s_method4.value:
                listing_data.shipping_method = const.YU_PACK

            # 発送日数
            delivery_day_val = int(df.iat[row, col._deliverry_day.value] or const.THREESEVEN_DAY)
            if delivery_day_val == const.ONETWO_DAY:
                listing_data.deliverry_day = const.DELIBERY_ONEDAY

            elif delivery_day_val == const.TWOTHREE_DAY:
                listing_data.deliverry_day = const.DELIBERY_TWOTHREE

            elif delivery_day_val == const.THREESEVEN_DAY:
                listing_data.deliverry_day = const.DELIBERY_THREESEVEN


            listing_data.shipping_end = int(df.iat[row, col._shipping_end.value] or const.SEVEN_DAYS)
            listing_data.shipping_time = int(df.iat[row, col._shipping_time.value] or const.AM10_AM11)
            listing_data.price = int(df.iat[row, col._price.value] or np.NAN)                                # ToDo：未記入エラー処理（落ち箇所通知）

            if not DataCheck(listing_data):
                continue
                
            # 商品データクラス追加
            listing_data_list.append(listing_data)
            product_no += 1

    except Exception as e:
        print(e)
        print("ファイルが存在しない または ファイル名が異なります。")
        print("指定フォルダに 'csvファイル' が存在するか確認した後に再度実行して下さい。")
        print("詳細は 'ReadMe' を参照")
        sys.exit()


    return listing_data_list


# 商品投稿
def ProductUpload(data, driver):

    post_no = 1

    try:
        pic_up = driver.find_element_by_id('selectFile')

        # 商品画像
        if not data.product_img0 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img0))
            
        if not data.product_img1 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img1))

        if not data.product_img2 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img2))

        if not data.product_img3 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img3))

        if not data.product_img4 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img4))

        if not data.product_img5 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img5))

        if not data.product_img6 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img6))

        if not data.product_img7 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img7))

        if not data.product_img8 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img8))

        if not data.product_img9 is np.NAN:
            pic_up.send_keys(os.path.abspath(data.product_img9))


        # タイトル
        driver.find_element_by_id('fleaTitleForm').send_keys(data.title)

        # カテゴリー
        driver.execute_script(f'arguments[0].value = {data.category}', driver.find_element_by_name('category'))

        # 商品の状態
        Select(driver.find_element_by_name('istatus')).select_by_visible_text(data.new_old)

        # 返品
        if data.product_return:
            driver.find_element_by_xpath('/html/body/form/div/div[13]/label[not(contains(@class, "is-check"))]').click()
        # else:
        #     driver.find_element_by_xpath('/html/body/form/div/div[13]/label[(contains(@class, "is-check"))]').click()

        # 説明 iframeの rteEditorComposition0に切り替え
        iframe = driver.find_element_by_id('rteEditorComposition0')
        driver.switch_to.frame(iframe)
        driver.find_element_by_id('0').send_keys(data.description)
        driver.switch_to.default_content()

        # 発送元の地域　リストの中から文字列で都道府県選択
        Select(driver.find_element_by_name("loc_cd")).select_by_visible_text(data.location)

        # 送料負担
        if ListingData.Listing().shipping_charge == const.SELLER:
            driver.find_element_by_xpath('/html/body/form/div/section[2]/div[6]/label[(contains(@class, "is-check"))]').click()

        elif ListingData.Listing().shipping_charge == const.SUCCESSFUL_BIDDER:
            driver.find_element_by_xpath('/html/body/form/div/section[2]/div[6]/label[not(contains(@class, "is-check"))]').click()

        # 配送方法の選択
        driver.find_element_by_xpath(data.shipping_method).click()
        
        # 発送までの日数を選択
        driver.find_element_by_xpath(data.deliverry_day).click()

        # 終了日時
        Select(driver.find_element_by_id("ClosingYMD")).select_by_index(data.shipping_end)
        Select(driver.find_element_by_id("ClosingTime")).select_by_index(data.shipping_time)

        # 開始価格
        driver.find_element_by_id("auc_BidOrBuyPrice_buynow").clear()
        driver.find_element_by_id("auc_BidOrBuyPrice_buynow").send_keys(data.price)

        # 確認ボタン
        driver.find_element_by_xpath('/html/body/form/div/ul/li/input').click()

        # 出品
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr/td[2]/button').click()

        # ポップアップ削除
        # driver.find_element_by_xpath('/html/body/div/div[10]/div/div/div[3]/label/span[1][not(contains(@class, "is-check"))]').click()
        # driver.find_element_by_xpath('/html/body/div/div[10]/div/div/div[2]/a[2]').click()

        # 続けて出品
        driver.find_element_by_xpath('/html/body/div/div[7]/center/a[1]').click()

        sleep(3)
        print(post_no, "件目投稿完了")
        post_no += 1


    except Exception as e:
        print(e)
        pass    # ToDo：未記入エラー処理（落ち箇所通知）




url = 'https://login.yahoo.co.jp/config/login?auth_lv=pw&.lg=jp&.intl=jp&.src=auc&.done=https%3A%2F%2Fauctions.yahoo.co.jp%2F&sr_required=birthday%20gender%20postcode%20deliver'

# ログイン情報
user = np.NAN
password = np.NAN

# 定数クラス
const = Const._Const()


if __name__ == '__main__':

    product_list = DataRead()

    # オプション設定
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(1)

    try:
        # ログイン
        driver.find_element_by_id('username').send_keys(user)
        driver.find_element_by_id('btnNext').click()
        sleep(1)
        driver.find_element_by_id('passwd').send_keys(password)
        driver.find_element_by_id('btnSubmit').click()
        sleep(2)
        # ポップアップの削除(Chrome設定でポップアップ非表示設定)
        # driver.find_element_by_xpath('//*[@id="topPageArea"]/section/div/a[2]').click()
        sleep(1)
        # 出品ボタンクリック
        driver.find_element_by_xpath('//*[@id="topPageArea"]/div[1]/div[1]/div[5]/div[2]/ul/li[3]/a').click()
        sleep(2)
        
        if len(product_list) != 0:

            for product in product_list:
                
                ProductUpload(product, driver)

        else:
            print('商品リストが1つも作成されていません。')
            sys.exit()

            
    except Exception as e:
        print(e)
        # Chrome終了
        driver.close()
        driver.quit()


    print('全ての商品投稿が完了しました。')
    driver.close()
    driver.quit()
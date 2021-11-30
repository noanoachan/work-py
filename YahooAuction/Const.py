from enum import Enum


class Listing_Column(Enum):
    # 商品写真（最大10枚まで）
    _img0 = 1
    _img1 = 2
    _img2 = 3
    _img3 = 4
    _img4 = 5
    _img5 = 6
    _img6 = 7
    _img7 = 8
    _img8 = 9
    _img9 = 10

    # 出品情報
    _title = 11                 # タイトル
    _category = 12              # カテゴリ
    _new_old = 13               # 使用状況（例：未使用に近い）
    _description = 14           # 商品説明
    _product_return = 15        # 返品受付
    _location = 16              # 発送地域
    _shipping_charge = 17       # 出品者
    _shipping_method = 18       # 配送方法
    _deliverry_day = 19         # 発送日数
    _shipping_end = 20          # 終了日（設定値 +1日）
    _shipping_time = 21         # 終了時間（リストの index番号）
    _price = 22                 # 設定金額


class Shipping_Method_Num(Enum):
    # 配送方法（番号指定）
    _s_method0 = 0              # ヤフネコ！ネコポス
    _s_method1 = 1              # ヤフネコ！宅急便コンパクト
    _s_method2 = 2              # ヤフネコ！宅急便
    _s_method3 = 3              # ゆうパケット（おてがる版）
    _s_method4 = 4              # ゆうパック（おてがる版）


class _Const:

    # カテゴリー
    # COMPUTER = 23336                    # コンピューター
    # HOMEAPP_AV_CAMERA = 23632           # 家電、AV、カメラ
    # MUSIC = 22152                       # 音楽
    # BOOK_MAGAZINE = 21600               # 本、雑誌
    # MOVIES_VIDEO = 21964                # 映画、ビデオ
    # TOY_GAME = 25464                    # おもちゃ、ゲーム
    # HOBBY_CALTURE = 24242               # ホビー、カルチャー
    # ANTIQUE_COLLECTION = 20000          # アンティーク、コレクション
    # SPORTS_LEISURE = 24698              # スポーツ、レジャー
    # AUTOMOBILE_MOTORCYCLE = 26318       # 自動車、オートバイ
    # FASHION = 23000                     # ファッション
    # ACCESSORIES_CLOCK = 23140           # アクセサリー、時計
    # BEAUTY_HEALTHCARE = 42177           # ビューティー、ヘルスケア
    # FOOD_BEVERAGE = 23976               # 食品、飲料
    # HOUSE_INTERIOR = 24198              # 住まい、インテリア
    # PETS_CREATURES = 2084055844         # ペット、生き物
    # OFFICEWORK_STORESUPPLIES = 22896    # 事務、店舗用品
    # FLOWER_GARDENING = 26086            # 花、園芸
    # TICKETS_GOLDTICKET = 2084043920     # チケット、金券
    # HOTEL_RESERVATIONS = 2084043920     # 宿泊予約
    # BABY_PRODUCTS = 24202               # ベビー用品
    # TARENTGOODS = 2084032594            # タレントグッズ
    # COMIC_ANIMEGOODS = 20060            # コミック、アニメグッズ
    # REAL_ESTATE = 2084060731            # 不動産
    # CHARITY = 2084217893                # チャリティー
    # OTHER = 26084                       # その他
    OTHER = 26395                       # その他

    # 商品の状態
    PRODUCT_STATUS_0 = '未使用'
    PRODUCT_STATUS_1 = '未使用に近い'
    PRODUCT_STATUS_2 = '目立った傷や汚れなし'
    PRODUCT_STATUS_3 = 'やや傷や汚れあり'
    PRODUCT_STATUS_4 = '傷や汚れあり'
    PRODUCT_STATUS_5 = '全体的に状態が悪い'


    # 出品者 / 落札者（実装なし）
    SELLER = '出品者'
    SUCCESSFUL_BIDDER = '落札者'
    # 配送方法（full X_Path）
    YAHONEKO_POS = '/html/body/form/div/div[21]/div/section[1]/div[2]/ul/li[1]/label[(contains(@class, "is-check"))]'                # ヤフネコ！ネコポス
    YAHONEKO_EXPRESS_COMPACT = '/html/body/form/div/div[21]/div/section[1]/div[2]/ul/li[2]/label[(contains(@class, "is-check"))]'    # ヤフネコ！宅急便コンパクト
    YAHONEKO_EXPRESS = '/html/body/form/div/div[21]/div/section[1]/div[2]/ul/li[3]/label[(contains(@class, "is-check"))]'            # ヤフネコ！宅急便
    YU_PACKET = '/html/body/form/div/div[21]/div/section[2]/div[2]/ul/li[1]/label[(contains(@class, "is-check"))]'                   # ゆうパケット（おてがる版）
    YU_PACK = '/html/body/form/div/div[21]/div/section[2]/div[2]/ul/li[2]/label[(contains(@class, "is-check"))]'                     # ゆうパック（おてがる版）


    # 支払いから発送までの日数
    ONETWO_DAY = 12         # 1~2日
    TWOTHREE_DAY = 23       # 2~3日
    THREESEVEN_DAY = 37     # 3~7日
    # 発送日数（full X_Path）
    DELIBERY_ONEDAY = '/html/body/form/div/div[22]/div[2]/label[1][(contains(@class, "is-check"))]'
    DELIBERY_TWOTHREE = '/html/body/form/div/div[22]/div[2]/label[2][(contains(@class, "is-check"))]'
    DELIBERY_THREESEVEN = '/html/body/form/div/div[22]/div[2]/label[3][(contains(@class, "is-check"))]'


    # 現在の日付から ◯日後
    ONE_DAY = 1
    TWOD_AYS = 2
    THREE_DAYS = 3
    FOUR_DAYS = 4
    FIVE_DAYS = 5
    SIX_DAYS = 6
    SEVEN_DAYS = 7
    EIGHT_DAYS = 8


    # オークション終了時間
    AM10_AM11 = 10   # 10:00 ~ 11:00
    AM11_PM12 = 11   # 11:00 ~ 12:00
    PM12_PM13 = 12   # 12:00 ~ 13:00
    PM13_PM14 = 13   # 13:00 ~ 14:00
    PM14_PM15 = 14   # 14:00 ~ 15:00
    PM15_PM16 = 15   # 15:00 ~ 16:00
    PM16_PM17 = 16   # 16:00 ~ 17:00
    PM17_PM18 = 17   # 17:00 ~ 18:00
    PM18_PM19 = 18   # 18:00 ~ 19:00
    PM19_PM20 = 19   # 19:00 ~ 20:00
    PM20_PM21 = 20   # 20:00 ~ 21:00
    PM21_PM22 = 21   # 21:00 ~ 22:00
    PM22_PM23 = 22   # 22:00 ~ 23:00
    PM23_AM12 = 23   # 23:00 ~ 24:00
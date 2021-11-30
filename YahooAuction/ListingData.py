import Const


const = Const._Const()

class Listing():

    # 商品写真（最大10枚まで）
    product_img0 = None
    product_img1 = None
    product_img2 = None
    product_img3 = None
    product_img4 = None
    product_img5 = None
    product_img6 = None
    product_img7 = None
    product_img8 = None
    product_img9 = None

    # 出品情報
    no = None                                   # 商品番号
    title = None                                # タイトル
    category = const.OTHER                      # カテゴリ
    new_old = const.PRODUCT_STATUS_2            # 使用状況（例：未使用に近い）
    description = None                          # 商品説明
    product_return = False                      # 返品受付
    location = None                             # 発送地域
    shipping_charge = const.SELLER              # 出品者
    shipping_method = const.YAHONEKO_EXPRESS    # 配送方法
    deliverry_day = const.THREESEVEN_DAY        # 支払いから発送までの日数
    shipping_end = const.SEVEN_DAYS             # 終了日（設定値 +1日）
    shipping_time = const.AM10_AM11             # 終了時間（リストの index番号）
    price = None                                # 設定金額
    
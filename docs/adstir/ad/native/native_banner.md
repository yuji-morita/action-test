# ネイティブライクバナー

ネイティブライクバナー広告は、ネイティブ広告をバナーのように配置して掲載する広告形式です。

## 一般的な掲載方法

アプリ内でテンプレートに合ったサイズのWebViewを作成していただき、そこに管理画面で取得できるタグを記述したHTMLファイルを表示するのみです。なお、綺麗なサイズで表示するためには、marginやpaddingを初期化する必要があります。

```HTML
<style type="text/css">
html,body { margin:0; padding:0 } /* marginとpaddingを0に */
</style>
<script type="text/javascript">
var adstir_vars = {
  ver: "4.0",
  type: "native",
  app_id: "MEDIA-XXXXX",
  ad_spot: 1,
  async: false,
};
</script>
<script type="text/javascript" src="https://js.ad-stir.com/js/adstir_native.js"></script>
```

## バナーサイズのリサイズ

ネイティブライクバナーは、自由にリサイズをすることが可能です。下記の様に、幅とスケールを指定することで、基本サイズ(テンプレート選択画面に記載)からリサイズできます。

```HTML
<style type="text/css">
html,body { margin:0; padding:0 } /* marginとpaddingを0に */
#adstir_native_widget_wrapper {
    width: 150px;
    height: 100px;
}
#adstir_native_widget {
    transform: scale(0.5);
    -webkit-transform: scale(0.5); /* 古いバージョンのOSに対応させる場合に必須 */
}
</style>
<script type="text/javascript">
var adstir_vars = {
  ver: "4.0",
  type: "native",
  app_id: "MEDIA-XXXXX",
  ad_spot: 1,
  async: false,
};
</script>
<script type="text/javascript" src="https://js.ad-stir.com/js/adstir_native.js"></script>
```

## Android広告IDの使用

アプリに掲載する広告は、広告識別子を送信することでさらなる収益化が可能になる場合があります。

* [Android広告IDの使用](https://github.com/united-adstir/AdStir-Integration-Guide-Android/wiki/Android%E5%BA%83%E5%91%8AID%E3%81%AE%E9%80%81%E4%BF%A1)

## よくある質問

### User−Agentの変更について

User-Agentを標準のものから変更された場合、正常に広告は配信されません。

独自のUser-Agentをご利用になられる場合には、既存のUser-Agentの末尾に、文字列を追加して頂くようにお願い致します。

例：
Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 **AdStir-IOS com.ad-stir.appli/2.7.2** <- 太字部分を追加


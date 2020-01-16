# Amazon Publisher Services(APS)の初期設定

APSの広告は下記のものに対応しております。

* AdMobバナー
* AdMobインタースティシャル

## プロジェクトへAPSの導入

APSのSDKとアダプター、アドネットワークのSDKとアダプターをプロジェクトへ導入します。

### Android Studioで導入する場合
アプリケーションレベルのbuild.gradleにmavenリポジトリと依存関係を設定することで、adstirが利用するアドネットワークのSDKとアダプターを一括で導入することができます。

```groovy hl_lines="11 15"
repositories {
    maven { url 'http://cdnp.ad-stir.com/m2' }
    maven { url 'https://adcolony.bintray.com/AdColony' } // adcolony
    maven { url 'https://github.com/glossom-dev/GlossomAds-Android/raw/master' } // adcolsa
    maven { url 'https://imobile-maio.github.io/maven' } // maio
    maven { url 'http://fan-adn.github.io/nendSDK-Android-lib/library' } // nend
    maven { url 'https://s3.amazonaws.com/moat-sdk-builds' } // mopub
    maven { url 'https://imobile.github.io/adnw-sdk-android' } // imobile
}

dependencies {
    // 利用するadstirのSDKバージョンを設定します
    def adstir_version = "x.x.x" 
    implementation "com.ad-stir.mediationadapter:admob-package:${adstir_version}"
}
```

### 手動で導入する場合

営業担当にお問い合わせください。


## APSの初期化

営業担当がお知らせしたAPSのapp idを用いて、下記のように初期化を行います。

```java hl_lines="3 4 5 6 7 10 11"
import com.amazon.device.ads.AdRegistration;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        AdRegistration.getInstance("your_app_id", this);
    }
}
```

テスト時には下記を追加します。
アプリをリリースする前には下記のコードは削除してください。

```java
AdRegistration.enableTesting(true);
```

## 広告を実装する

* [バナー広告](banner.md)
* [インタースティシャル広告](interstitial.md)

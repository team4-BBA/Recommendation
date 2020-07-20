# Recommendation
設計はGoogle Colabで、実装はGCP Cloud FUnctionsで動いてます。
API定義：

##  リクエストラパメータ
- リクエストURL
`https://us-central1-arctic-conduit-280420.cloudfunctions.net/GetVector`

|GETパラメータ|データ|説明|
|:---|:---|:---|
|type|人:0<br>ホテル:1|ベクトル化対象のタイプ|
|value|type=0の場合string配列<br><br>type=1の場合int型ホテルid|ベクトル化のためのデータ|

例1

例2

## レスポンスデータ

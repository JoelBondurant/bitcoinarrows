# [bitcoinarrows.com](https://bitcoinarrows.com)

A system for monitoring Bitcoin.


## ScreenShot:
![ScreenShot](https://raw.github.com/JoelBondurant/bitcoinarrows/master/doc/img/bitcoin_arrows.png)

## Architecture (minus shortcuts):
![Architechure](https://raw.github.com/JoelBondurant/bitcoinarrows/master/doc/img/arch.jpg)

1. rt - Real Time data collector service. (polling ~10 seconds)
1. rtdb - rt overwrites keys in rocksdb (based on leveldb used by Bitcoin for fun)
1. ts - Time series builder service.
1. tsdb - Parquet files corresponding to rtdb over time.
1. arrows - Arrows on tsdb.
1. wsdb - /data/arrows/*.csv
1. wap - A Flask app Bitcoin dashboard made with vega-lite.
1. nginx - cache, proxy to deprivilege, ssl automation...

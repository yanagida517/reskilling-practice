関数1  名前: load_events  受け取るもの: path  返すもの: JSON から読み込んだ予定のリスト  役割: schedule.json を開いて予定を読み込む

関数2  名前: filter_by_date  受け取るもの: events, target  返すもの: 指定した日の予定だけを時刻順に並べたリスト  役割: 全体の予定から対象日だけを取り出して並べ替える

関数3  名前: format_event  受け取るもの: event  返すもの: 1件分の表示用文字列  役割: 予定1件を「時刻 タイトル @場所」の形に整える




HTTP
Request URL
https://github.com/
Request method
GET
Status code
200 OK
Remote address
20.27.177.113:443
Referrer policy
strict-origin-when-cross-origin


1ページ開いたときの往復の数（およそ）: 45 回
curl -I の1行目: HTTP/2 200
無いページの1行目: HTTP/2 404
API の full_name: yanagida517/reskilling-practice  pushed_at: 2026-10-02T08:36:39Z

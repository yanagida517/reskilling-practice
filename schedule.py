"""同じフォルダの schedule.json を読み、指定した日の予定を時刻順に表示する。

使い方:
    py schedule.py 2026-10-02    # 日付を指定
    py schedule.py               # 引数なしなら今日(日本時間)
"""

import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

JST = timezone(timedelta(hours=9))
SCHEDULE_PATH = Path(__file__).resolve().parent / "schedule.json"


def load_events(path):
    """schedule.json を読み込んで、予定のリストを返す(読むだけで書き換えない)。"""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"{path.name} が見つかりません。schedule.py と同じフォルダに置いてください。")
    except json.JSONDecodeError as e:
        sys.exit(f"{path.name} の形式が正しくありません({e.lineno} 行目付近)。")


def filter_by_date(events, target):
    """開始日が target(date)の予定だけを、開始時刻順に並べて返す。"""
    day = target.isoformat()
    picked = [e for e in events if e["start"].startswith(day)]
    return sorted(picked, key=lambda e: e["start"])


def format_event(event):
    """1件を「09:00-18:00 件名 @場所」の形の文字列にする。場所が無ければ @（場所なし) を付ける。"""
    start = datetime.fromisoformat(event["start"]).strftime("%H:%M")
    end = datetime.fromisoformat(event["end"]).strftime("%H:%M")
    line = f"{start}-{end} {event['title']}"
    if event.get("location"):
        line += f" @{event['location']}"
    else:
        line += " @（場所なし)"
    return line


def main():
    if len(sys.argv) >= 2:
        try:
            target = date.fromisoformat(sys.argv[1])
        except ValueError:
            sys.exit("日付は 2026-10-02 のような形式で指定してください。")
    else:
        target = datetime.now(JST).date()

    events = filter_by_date(load_events(SCHEDULE_PATH), target)
    print(f"{target.isoformat()} の予定 {len(events)} 件")
    for event in events:
        print(format_event(event))


if __name__ == "__main__":
    main()

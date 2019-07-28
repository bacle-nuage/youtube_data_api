#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import traceback
import sys

from services import api_request
from services import output

def get_args():
    #argparseを使ったコマンドライン引数の取得
    parser = argparse.ArgumentParser(description='YouTube Api')
    parser.add_argument('--api_key', dest='api_key', type=str, help='Youtube Data Api Key', required=True)
    parser.add_argument('-o', '--output', dest='output', type=str, help='OUT PUT')

    # function 使用する関数
    subparsers = parser.add_subparsers()

    # チャンネル情報取得
    get_channel_parser = subparsers.add_parser('channel', help='Get Youtube Channel Data')
    get_channel_parser.add_argument('channel_id', help='Channel Id') # チャンネルID
    get_channel_parser.set_defaults(func=api_request.channel) # 実行する関数設定

    return  parser.parse_args()


def main():
    # コマンドライン引数の取得
    args = get_args()

    #アプリケーション内部の実装
    try:
        res = args.func(args)

        if args.output is not None:
            output.file(res, args.output)
            print(args.output + 'に保存されました')

        #終了ステータスの定義
        print(res)

        #エラーの出力
    except :
        print('#' * 5 + 'エラーが発生して処理を中断しました' + '#' * 5)
        print(traceback.format_exc(sys.exc_info()[2]))

if __name__ == '__main__':
    main()

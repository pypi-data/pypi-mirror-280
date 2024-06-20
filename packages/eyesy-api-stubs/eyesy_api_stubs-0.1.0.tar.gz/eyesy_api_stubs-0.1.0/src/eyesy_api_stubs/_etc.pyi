from typing import List, Tuple

from pygame import Surface

class Etc:
    @property
    def audio_in(self) -> List[int]:
        """EYESY のオーディオ入力チャンネルによって登録された最新
        の 100 のオーディオレベルのリスト。

        左右の入力チャンネルは 1 つのモノチ
        ャンネルに統合されます。 100 個のオーディオ値は、最小-32,768 から最大
        +32,767 の範囲で、16 ビットの整数値で格納されます。トリガーボタンを押す
        と、このリストに正弦波が入力され、EYESY へのオーディオ入力がシミュレート
        されます。
        """
        ...

    @property
    def audio_trig(self) -> bool:
        """トリガーイベントを示すブール値（boolean value）。

        トリガーソースは、Shift + Trigger Select Knob で選択します。 オーディオがソース
        として選択されている場合、最後のフレームが draw（）関数を介して描画され
        てから、オーディオが固定のスレッショルドレベル（最大値の約 80％）を超える
        と、トリガーイベントが発生します。 さらに、Trigger ボタンを押すと、
        etc.audio_trig が true に設定されます。
        """
        ...

    @property
    def xres(self) -> float:
        """現在の出力解像度の水平。"""
        ...

    @property
    def yres(self) -> float:
        """現在の出力解像度の垂直。"""
        ...

    @property
    def knob1(self) -> float:
        """ノブ 1 の現在値を表すフロート。

        ノブが再び動かされるまで、現
        在選択されている MIDI チャンネルの番号 21 の着信 MIDI コントロールチェン
        ジメッセージがノブ 1 の値を置き換えます。
        """
        ...

    @property
    def knob2(self) -> float:
        """ノブ 2 の現在値を表すフロート。

        ノブが再び動かされるまで、現
        在選択されている MIDI チャンネルの番号 22 の着信 MIDI コントロールチェン
        ジメッセージがノブ 2 の値を置き換えます。
        """
        ...

    @property
    def knob3(self) -> float:
        """ノブ 3 の現在値を表すフロート。

        ノブが再び動かされるまで、現
        在選択されている MIDI チャンネルの番号 23 の着信 MIDI コントロールチェン
        ジメッセージがノブ 3 の値を置き換えます。
        """
        ...

    @property
    def knob4(self) -> float:
        """ノブ 4 の現在値を表すフロート。

        ノブが再び動かされるまで、現
        在選択されている MIDI チャンネルの番号 24 の着信 MIDI コントロールチェン
        ジメッセージがノブ 4 の値を置き換えます。
        """
        ...

    @property
    def knob5(self) -> float:
        """ノブ 5 の現在値を表すフロート。

        ノブが再び動かされるまで、現
        在選択されている MIDI チャンネルの番号 25 の着信 MIDI コントロールチェン
        ジメッセージがノブ 5 の値を置き換えます。
        """
        ...

    @property
    def lastgrab(self) -> Surface:
        """最後に撮影したスクリーンショットの画像を含む Pygame サ
        ーフェス（[Screenshot]ボタンを使用）。

        1280x720 で、スクリーンショットのフルサイズと一致します。
        """
        ...

    @property
    def lastgrab_thumb(self) -> Surface:
        """最後に撮影したスクリーンショットのサムネイル画像を含む Pygame サ
        ーフェス（[Screenshot]ボタンを使用）。

        このサーフェスのサイズは 128x72 です。
        """
        ...

    @property
    def midi_notes(self) -> List[int]:
        """128 のさまざまな MIDI ノートピッチを表すリスト。

        このリストの各値は、そのノートが現在オンであるかどうかを示します。

        たとえば“middle C”（MIDI ノート 60）が押されているときに実行される
        スレッショルド関数を次のように作成できます

        ```python
        if etc.midi_notes[60]:
            yourFunctionHere()
        """
        ...

    @property
    def midi_note_new(self) -> bool:
        """最後のフレームが描画されてから（draw（）関数を介して）、メッセージで少なくとも 1 つの新しい MIDI ノートが受信されたかどうかを示すブール値。"""
        ...

    @property
    def mode(self) -> str:
        """現在のモード名"""
        ...

    @property
    def mode_root(self) -> str:
        """現在のモードのフォルダへのファイルパスの文字列。

        これにより、`/sdcard/Modes/Python/CurrentModeFolder` などの文字列が返されます。
        これは、画像、フォント、またはその他のリソースをモードのフォルダからロードする必要がある場合に役立ちます。
        （setup() 関数はこれを行うのに適切な場所です。）
        """
        ...

    def color_picker_bg(self, knob: float) -> None:
        """背景色を設定します。

        通常は「etc.color_picker_bg(etc.knob5)」と指定されますが、任意のノブを使用して背景色をコントロールできます。
        この関数は、ノブの値（0-1 から）を取得して RGB 値に変換し、それを背景色に使用します。
        """
        ...

    def color_picker(self, knob: float) -> None:
        """この関数は、指定されたノブの値を色に変換します。
        通常は「etc.color_picker（etc.knob4）」と指定されますが、カラーピッカーには
        任意のノブを使用できます。 この関数が呼び出されると、この色の赤、緑、青
        のコンポーネントを表す 3 つの整数のタプルが返されます。 ファクトリモード
        では、この関数によってローカル変数（通常は色）が設定されていることがよく
        あります。
        """
        ...

    @property
    def bg_color(self) -> Tuple[int, int, int]:
        """背景色を表す RGB タプル。

        注意: このプロパティはドキュメントに正式には書かれていませんでしたが、雰囲気で追加しました。多分合ってるとは思いますが、間違っていたら教えてください。
        """
        ...

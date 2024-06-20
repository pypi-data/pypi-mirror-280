# eyesy-api-stub

[EYESY](https://umbrella-company.jp/products/eyesy/) の Python API のスタブです。

EYESY のコーディング支援を目的として作成されました。

コーディング時の補完機能やドキュメントの参照に利用してください（コーディングには VS Code & [Python 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python)の利用を推奨します）。

注意点: このパッケージ自体は機能を持っておらず、あくまで EYESY API の型定義とドキュメントを提供します。

このパッケージは EYESY のマニュアルを参考に作成しました。

<https://umbrella-company.jp/corporate/wp-content/uploads/2023/01/critter_and_guitari_eyesy_manual.pdf>

## 使い方

このパッケージが提供する型ヒントは1部、 Pygame に依存しているので Pygame と一緒にインストールしてください。

```bash
pip install pygame eyesy-api-stubs
```

コーディング時には、以下のように型ヒントとして利用してください。

```python
import pygame
from pygame import Surface
from eyesy_api_stubs import Etc

def setup(screen: Surface, etc: Etc):
    pass

def draw(screen: Surface, etc: Etc):
    size = 640
    position = (510, 500)
    color = (255, 0, 0)
    pygame.draw.circle(screen, color, position, size, 0)
```

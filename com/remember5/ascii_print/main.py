import time
from typing import List, Optional
from dataclasses import dataclass
from colorama import init, Fore, Style
import random

# 初始化颜色支持
init()

@dataclass
class AsciiBox:
    """精美的ASCII艺术盒子"""
    content: str
    style: str = 'classic'
    color: Optional[str] = None

class ArtisticPrinter:
    """艺术化的打印工具"""

    def __init__(self):
        self.frames = {
            'classic': {
                'top_left': '╭', 'top_right': '╮',
                'bottom_left': '╰', 'bottom_right': '╯',
                'horizontal': '─', 'vertical': '│'
            },
            'double': {
                'top_left': '╔', 'top_right': '╗',
                'bottom_left': '╚', 'bottom_right': '╝',
                'horizontal': '═', 'vertical': '║'
            }
        }
        self.colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'cyan': Fore.CYAN,
            'magenta': Fore.MAGENTA
        }

    def create_box(self, box: AsciiBox) -> str:
        """创造优雅的框架"""
        frame = self.frames[box.style]
        lines = box.content.split('\n')
        max_length = max(len(line) for line in lines)

        # 构建框架
        top = f"{frame['top_left']}{frame['horizontal'] * (max_length + 2)}{frame['top_right']}"
        bottom = f"{frame['bottom_left']}{frame['horizontal'] * (max_length + 2)}{frame['bottom_right']}"

        # 添加内容
        content = []
        for line in lines:
            padded = line.ljust(max_length)
            content.append(f"{frame['vertical']} {padded} {frame['vertical']}")

        # 组合
        result = '\n'.join([top] + content + [bottom])

        # 添加颜色
        if box.color:
            result = f"{self.colors[box.color]}{result}{Style.RESET_ALL}"

        return result

class AnimatedDisplay:
    """动态展示效果"""

    @staticmethod
    def typing_effect(text: str, delay: float = 0.05):
        """打字机效果"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

def main():
    """主函数展示"""
    printer = ArtisticPrinter()

    # 创建欢迎信息
    welcome_box = AsciiBox(
        content="欢迎来到Python艺术空间\n让我们开始这段奇妙旅程",
        style='classic',
        color='cyan'
    )

    # 动态展示
    AnimatedDisplay.typing_effect(printer.create_box(welcome_box))

    # 展示不同风格
    styles = ['classic', 'double']
    colors = ['red', 'green', 'blue', 'magenta']

    for style in styles:
        for color in colors:
            box = AsciiBox(
                content=f"风格: {style}\n颜色: {color}",
                style=style,
                color=color
            )
            print(printer.create_box(box))
            time.sleep(0.5)

if __name__ == "__main__":
    main()

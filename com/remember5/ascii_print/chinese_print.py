class ChineseArtBox:
    def __init__(self):
        self.frames = {
            'top_left': '╭', 'top_right': '╮',
            'bottom_left': '╰', 'bottom_right': '╯',
            'horizontal': '─', 'vertical': '│'
        }

    def calculate_visual_length(self, text: str) -> int:
        """计算字符串的视觉长度"""
        length = 0
        for char in text:
            # 东亚字符宽度判定
            if '\u4e00' <= char <= '\u9fff' or \
                    '\u3000' <= char <= '\u303f' or \
                    '\uff00' <= char <= '\uffef':
                length += 2
            else:
                length += 1
        return length

    def align_text(self, text: str, width: int) -> str:
        """对齐文本"""
        visual_length = self.calculate_visual_length(text)
        padding = width - visual_length
        if padding < 0:
            padding = 0
        return text + ' ' * padding

    def create_box(self, text: str, padding: int = 1) -> str:
        lines = text.split('\n')
        # 计算最大视觉宽度
        max_width = max(self.calculate_visual_length(line) for line in lines)

        # 构建框架
        box_width = max_width + (padding * 2)
        top = f"{self.frames['top_left']}{self.frames['horizontal'] * box_width}{self.frames['top_right']}"
        bottom = f"{self.frames['bottom_left']}{self.frames['horizontal'] * box_width}{self.frames['bottom_right']}"

        # 处理内容
        content = []
        for line in lines:
            aligned_line = self.align_text(line, max_width)
            padded_line = f"{self.frames['vertical']}{' ' * padding}{aligned_line}{' ' * padding}{self.frames['vertical']}"
            content.append(padded_line)

        return '\n'.join([top] + content + [bottom])

# 展示魔法
box = ChineseArtBox()
text = """
Test ASCII
Elegant Chinese Alignment
Test Data
AI Technology
"""

print(box.create_box(text.strip()))

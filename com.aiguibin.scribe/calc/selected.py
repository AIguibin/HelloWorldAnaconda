import pyautogui
import pyperclip


def calculate_selected_text():
    # 捕捉屏幕上的文本
    selected_text = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    selected_text.save("selected_text.png")

    # 使用OCR库（例如Tesseract）对图像进行文本识别
    # 这里使用pytesseract作为示例，需要安装pytesseract和tesseract-ocr
    try:
        import pytesseract
    except ImportError:
        print("请先安装pytesseract库和tesseract-ocr，并配置tesseract-ocr的路径")
        return

    # 识别文本
    extracted_text = pytesseract.image_to_string("selected_text.png", lang='eng')

    # 去除空格和换行符
    extracted_text = extracted_text.replace(" ", "").replace("\n", "")

    # 进行计算
    try:
        result = eval(extracted_text)
        pyperclip.copy(str(result))
        print("计算结果已复制到剪贴板：", result)
    except:
        print("无法计算选中的文本：", extracted_text)


if __name__ == "__main__":
    calculate_selected_text()

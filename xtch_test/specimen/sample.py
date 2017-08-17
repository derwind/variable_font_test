import os, sys, re
from drawBot.drawBotDrawingTools import _drawBotDrawingTool
import pagebot
from pagebot.style import A4Letter
from pagebot.elements import *
from pagebot.document import Document
from pagebot.fonttoolbox.variablefontbuilder import getVariableFont, Font

W, H = A4Letter # Vertical Letter size, horizontal A4.
PADDING = (24, 24, 40, 24) # General page padding.

# Get the root path of open source fonts, enclosed in PageBot.
ROOT_PATH = pagebot.getRootPath()

FONT_PATH = pagebot.getFontPath()
FONT_PATH = os.path.join(FONT_PATH, "xtch_test-Variable.ttf")
EXPORT_PATH = os.path.join("_export/sample.pdf")

def main():
    #print _drawBotDrawingTool._tempInstalledFonts
    template = Template(w=W, h=H, padding=PADDING)

    doc = Document(title="sample", w=W, h=H, autoPages=1, originTop=False,
        pageTemplate=template, startPage=1)
    view = doc.getView()
    view.padding = 40

    page1 = doc[0]

    for ypos, ytch in enumerate(range(200, 800+1, 200)):
        for xpos, xtch in enumerate(range(200, 800+1, 200)):
            f = getVariableFont(FONT_PATH, location=dict(xtch=xtch, ytch=ytch))
            newText("我H", point=(70*xpos, 750-40*ypos), parent=page1, name="", font=f.installedName, fontSize=40)
    doc.solve()
    doc.export(EXPORT_PATH)

if __name__ == "__main__":
    main()

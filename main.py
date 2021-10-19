# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#PyQt5: https://www.cnblogs.com/linuxAndMcu/p/14326801.html


import turtle
import math
import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from GeneCiruit import *
from PyQt5.QtGui import QFont


class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_Preview.clicked.connect(self.btn_Preview_event)  # 绑定函数
        self.btn_OpenFile.clicked.connect(self.open_file_event)  # 绑定函数
        self.btn_Save2File.clicked.connect(self.save_file_event)  # 绑定函数
        self.btn_PenColor.clicked.connect(self.btn_PenColor_event)
        self.btn_FillColor.clicked.connect(self.btn_FillColor_event)
        self.btn_AddElement.clicked.connect(self.btn_AddElement_event)
        self.btn_RemoveElement.clicked.connect(self.btn_RemoveElement_event)
        self.btn_RemoveAll.clicked.connect(self.btn_RemoveAll_event)
       # self.listType.clicked.connect(self.listType_event)
        self.listElements.clicked.connect(self.listElements_event)
        self.btn_Replace.clicked.connect(self.btn_Replace_event)

        self.btn_Exit.clicked.connect(self.close)
        self.listType.addItem('Promoter')
        self.listType.addItem('Ellipse')
        self.listType.addItem('Rectangle_Triangle')
        self.listType.addItem('Rectangle')
        self.listType.addItem('Circle')
        self.listType.addItem('Triangle')
        self.listType.addItem('PA')
        self.listType.addItem('Terminator')
        self.listType.addItem('Text')
        self.listType.addItem('Suppress')
        self.listType.addItem('Enhance')
        self.listType.addItem('Suppress bottom')
        self.listType.addItem('Enhance bottom')




        self.spinBoxHeight.setValue(20)
        self.spinBoxLength.setValue(20)
        self.spinBoxRepeat.setValue(1)
        self.spinBoxPosition.setValue(0)
        self.spinBoxFontsize.setValue(12)
        self.spinBoxPensize.setValue(2)

        self.txtPenColor.setStyleSheet("background-color:%s" % self.txtPenColor.text())
        self.txtFillColor.setStyleSheet("background-color:%s" % self.txtFillColor.text())


    def btn_Replace_event(self):
        listElementsIndex = self.listElements.currentIndex()
        if listElementsIndex.row() > -1:
             if self.listType.currentIndex().row() > -1:
                 if self.radioButton.isChecked():
                     direct = 'R'
                 else:
                     direct = 'L'
                 element = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
                 self.listType.currentItem().text(), direct, self.spinBoxPosition.value(), self.spinBoxPosition_Y.value(),
                 self.spinBoxLength.value(), self.spinBoxHeight.value(), self.txtPenColor.text(),
                 self.txtFillColor.text(), self.txtLabel.text(), self.spinBoxRepeat.value(),
                 self.spinBoxPensize.value(), self.spinBoxFontsize.value())

                 self.listElements.insertItem(listElementsIndex.row(),element)
                 self.listElements.takeItem(listElementsIndex.row()+1)
                 self.listElements.setCurrentRow(listElementsIndex.row())



    def listElements_event(self):
        partinfo=self.listElements.currentItem().text()
        p = partinfo.split(',')

        p0 = p[0].strip()
        p1 = p[1].strip()

        p2 = int(p[2].strip())
        p3 = int(p[3].strip())
        p4 = int(p[4].strip())
        p5 = int(p[5].strip())
        p6 = p[6].strip()
        p7 = p[7].strip()
        p8 = p[8].strip()
        p9= int(p[9].strip())
        p10 = int(p[10].strip())
        p11 = int(p[11].strip())

        # self.listType.currentItem().text()
        if p0=="Promoter":
            self.listType.setCurrentRow(0)
        if p0=="Ellipse":
            self.listType.setCurrentRow(1)
        if p0=="Rectangle_Triangle":
            self.listType.setCurrentRow(2)
        if p0=="Rectangle":
            self.listType.setCurrentRow(3)
        if p0=="Circle":
            self.listType.setCurrentRow(4)
        if p0 == "Triangle":
            self.listType.setCurrentRow(5)
        if p0=="PA":
            self.listType.setCurrentRow(6)
        if p0 == "Terminator":
            self.listType.setCurrentRow(7)
        if p0 == "Text":
            self.listType.setCurrentRow(8)
        if p0 == "Suppress":
            self.listType.setCurrentRow(9)
        if p0 == "Enhance":
            self.listType.setCurrentRow(10)
        if p0 == "Suppress bottom":
            self.listType.setCurrentRow(11)
        if p0 == "Enhance bottom":
            self.listType.setCurrentRow(12)


        #direct
        if p1 == "R":
            self.radioButton.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)
        #self.spinBoxPosition.value()
        self.spinBoxPosition.setValue(p2)
        #self.spinBoxPosition_Y.value()
        self.spinBoxPosition_Y.setValue(p3)
        # self.spinBoxLength.Value()
        self.spinBoxLength.setValue(p4)
        #self.spinBoxHeight.value()
        self.spinBoxHeight.setValue(p5)
        # self.txtPenColor.text()
        self.txtPenColor.setText(p6)
        self.txtPenColor.setStyleSheet("background-color:%s" % self.txtPenColor.text())
        # self.txtFillColor.text()
        self.txtFillColor.setText(p7)
        self.txtFillColor.setStyleSheet("background-color:%s" % self.txtFillColor.text())
        #self.txtLabel.text()
        self.txtLabel.setText(p8)
        #self.spinBoxRepeat.value()
        self.spinBoxRepeat.setValue(p9)
        # self.spinBoxPensize.value()
        self.spinBoxPensize.setValue(p10)
        #, self.spinBoxFontsize.value())
        self.spinBoxFontsize.setValue(p11)




    def listType_event(self):
        if self.listType.currentItem().text()=="Promoter":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(50)
            self.spinBoxRepeat.setValue(1)

        if self.listType.currentItem().text()=="Ellipse":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(20)
            self.spinBoxHeight.setValue(20)
            self.spinBoxRepeat.setValue(1)

        if self.listType.currentItem().text()=="Rectangle_Triangle":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)

        if self.listType.currentItem().text() == "Circle":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(15)
            self.spinBoxHeight.setValue(15)
            self.spinBoxRepeat.setValue(1)

        if self.listType.currentItem().text() == "Triangle":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(40)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)

        if self.listType.currentItem().text() == "PA":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(5)
            self.spinBoxHeight.setValue(30)
            self.spinBoxRepeat.setValue(5)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#FFFFFF')

        if self.listType.currentItem().text() == "Terminator":
            self.spinBoxPosition_Y.setValue(0)
            self.spinBoxLength.setValue(5)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#000000')

        if self.listType.currentItem().text() == "Text":
            self.spinBoxPosition_Y.setValue(-50)
            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#000000')

        if self.listType.currentItem().text() == "Suppress":
            self.spinBoxPosition_Y.setValue(20)
            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#000000')

        if self.listType.currentItem().text() == "Enhance":

            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#000000')

        if self.listType.currentItem().text() == "Suppress bottom":
            self.spinBoxPosition_Y.setValue(20)
            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#000000')

        if self.listType.currentItem().text() == "Enhance bottom":
            self.spinBoxPosition_Y.setValue(20)
            self.spinBoxLength.setValue(50)
            self.spinBoxHeight.setValue(40)
            self.spinBoxRepeat.setValue(1)
            self.txtPenColor.setText('#000000')
            self.txtFillColor.setText('#000000')

    def btn_RemoveAll_event(self):
        self.listElements.clear()


    def btn_RemoveElement_event(self):
        listElementsIndex = self.listElements.currentIndex()
        self.listElements.takeItem(listElementsIndex.row())


    def btn_AddElement_event(self):
        listTypeIndex = self.listType.currentIndex()

        if self.listType.currentIndex().row()  >-1  :
            if self.radioButton.isChecked():
                direct='R'
            else :
                direct='L'

            #type,l/r,position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize
            element='%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' %(self.listType.currentItem().text() , direct, self.spinBoxPosition.value(),self.spinBoxPosition_Y.value(),self.spinBoxLength.value(), self.spinBoxHeight.value(), self.txtPenColor.text(),self.txtFillColor.text(),self.txtLabel.text(),self.spinBoxRepeat.value(),self.spinBoxPensize.value(),self.spinBoxFontsize.value())
            self.listElements.addItem((element))
            self.spinBoxPosition.setValue(int(self.spinBoxPosition.text()))
            self.spinBoxLength.setValue(int(self.spinBoxLength.text()))
            self.spinBoxRepeat.setValue(int(self.spinBoxRepeat.text()))
            self.spinBoxPosition.setValue(int(self.spinBoxPosition.value())+int(self.spinBoxLength.value())*int(self.spinBoxRepeat.value())+10)
        else:
            QMessageBox.about(self, 'Error', 'Please select part type')



    def btn_PenColor_event(self):
        col = QColorDialog().getColor()
        if col.isValid():
            self.txtPenColor.setText(col.name())
            self.txtPenColor.setStyleSheet("background-color:%s" % col.name())


    def btn_FillColor_event(self):
        col = QColorDialog().getColor()
        if col.isValid():
            self.txtFillColor.setText(col.name())
            self.txtFillColor.setStyleSheet("background-color:%s" % col.name())



    def btn_Preview_event(self):
        a = self.spinBoxStart.value()
        b = self.spinBoxEnd.value()
        content = str(a) + "," + str(b)


        for i in range(0, self.listElements.count() , 1):
            item = self.listElements.item(i)
            content = content + "\n" + item.text()

        print(content);
        file = open('~temp', 'w')
        file.write(content)
        file.close()
        Draw('~temp')




    def open_file_event(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "Select Gene Circuit File", os.getcwd(),"Gene Circuit Files(*.gs)")
        self.FilenameBox.setText(fileName)

        filename = self.FilenameBox.text()
        if filename != "":
            #Draw(filename)
            f = open(filename, "r")
            datas = f.readlines()

            # 读取序列起始信息
            p = datas[0].split(',')

            self.spinBoxStart.setValue(int(p[0].strip()))
            self.spinBoxEnd.setValue(int(p[1].strip()))
            self.listElements.clear()

            for i in range(1, len(datas)):
                self.listElements.addItem(datas[i].strip())

        else:
            QMessageBox.about(self, 'Error', 'Please select a part File')

    def save_file_event(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name=self.FilenameBox.text()
        if file_name == "" :
            file_name="temp.gs"

        file_name, fileType = QFileDialog.getSaveFileName(None, "Save File", file_name, "part Files(*.gs)", options=options)
        self.FilenameBox.setText(file_name)

        if file_name == "":
           print(file_name)
        else:
            a = self.spinBoxStart.value()
            b = self.spinBoxEnd.value()
            content = str(a) + "," + str(b)

            for i in range(0, self.listElements.count() , 1):
                item = self.listElements.item(i)
                content = content + "\n" + item.text()

            save2File(file_name,content)


    def demo(self):

        if os.access('demo.gs', os.X_OK):
            path = os.getcwd()
            f = open("demo.gs", "r")
            datas = f.readlines()

            # 读取序列起始信息
            p = datas[0].split(',')

            self.spinBoxStart.setValue(int(p[0].strip()))
            self.spinBoxEnd.setValue(int(p[1].strip()))
            self.listElements.clear()

            for i in range(1, len(datas)):
                self.listElements.addItem(datas[i].strip())

            Draw("demo.gs")

def drawTriangleR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    #向上
    turtle.left(90)

    # 三角形
    turtle.begin_fill()

    turtle.fillcolor(fillcolor)

    turtle.forward(length/2)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.end_fill()

    DrawLabel(position, y - length / 2 - 20, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()


def drawTriangleL(position, y, length, height, pencolor, fillcolor, label, Repeatnumber, pensize, fontsize):
    turtle.pensize(pensize)
    turtle.penup()
    x = (position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    # 向上
    turtle.left(90)

    # 三角形
    turtle.begin_fill()

    turtle.fillcolor(fillcolor)

    turtle.forward(length / 2)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length )
    turtle.left(120)
    turtle.forward(length)
    turtle.end_fill()
    DrawLabel(position-length/2, y - length / 2 - 20, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()


def drawEnhanceR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)

    turtle.left(90)
    turtle.forward(height)

    turtle.right(90)
    turtle.forward(length)

    turtle.right(90)
    turtle.forward(height-10)

    # 三角形
    turtle.begin_fill()

    turtle.fillcolor(fillcolor)

    turtle.right(90)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()
    DrawLabel(position + length / 2 - 10, y + height + 10, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawEnhanceL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)

    turtle.left(90)
    turtle.forward(height)

    turtle.left(90)
    turtle.forward(length)

    turtle.left(90)
    turtle.forward(height-10)

    # 三角形
    turtle.begin_fill()

    turtle.fillcolor(fillcolor)

    turtle.right(90)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()
    DrawLabel(position - length / 2 - 10, y + height + 10, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawSuppressR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    #向上
    turtle.left(90)
    turtle.forward(height)
    #向右
    turtle.right(90)
    turtle.forward(length)

    turtle.right(90)
    turtle.forward(height-10)

    turtle.right(90)
    turtle.forward(10)

    turtle.right(180)
    turtle.forward(20)
    DrawLabel(position +length/2- 10, y +height+ 10, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawSuppressL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    #向上
    turtle.left(90)
    turtle.forward(height)
    #向左
    turtle.left(90)
    turtle.forward(length)

    turtle.left(90)
    turtle.forward(height-10)

    turtle.left(90)
    turtle.forward(10)

    turtle.left(180)
    turtle.forward(20)
    DrawLabel(position - length/2-10, y +height+ 10, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()



def drawEnhanceBottomR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    #向下
    turtle.right(90)
    turtle.forward(height)
    #向右
    turtle.left(90)
    turtle.forward(length)

    turtle.left(90)
    turtle.forward(height-10)

    # 三角形
    turtle.begin_fill()

    turtle.fillcolor(fillcolor)

    turtle.right(90)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()
    DrawLabel(position +length/2- 10, y -height- 25, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawEnhanceBottomL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)

    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)

    turtle.right(90)
    turtle.forward(height-10)

    # 三角形
    turtle.begin_fill()

    turtle.fillcolor(fillcolor)

    turtle.right(90)
    turtle.forward(5)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()
    DrawLabel(position - length/2-10, y -height- 25, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawSuppressBottomR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    #向上
    turtle.right(90)
    turtle.forward(height)
    #向右
    turtle.left(90)
    turtle.forward(length)

    turtle.left(90)
    turtle.forward(height-10)

    turtle.right(90)
    turtle.forward(10)

    turtle.right(180)
    turtle.forward(20)
    DrawLabel(position +length/2- 10, y -height- 25, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawSuppressBottomL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)

    turtle.right(90)
    turtle.forward(height)

    turtle.right(90)
    turtle.forward(length)

    turtle.right(90)
    turtle.forward(height-10)

    turtle.left(90)
    turtle.forward(10)

    turtle.left(180)
    turtle.forward(20)
    DrawLabel(position - length/2-10, y -height- 25, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

#绘制右向启动子
def drawStartOnR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()

    turtle.pencolor(pencolor)
    #向上
    turtle.left(90)
    turtle.forward(height)
    #向右
    turtle.right(90)
    turtle.forward(length)

    # 三角形
    turtle.begin_fill()


    turtle.fillcolor(fillcolor)
    turtle.penup()
    turtle.goto(x+length-10, y+height+5)
    turtle.pendown()

    turtle.right(90)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()
    DrawLabel(position-10, y-25, 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()


def drawStartOnL( position, y, length, height, pencolor, fillcolor, label, Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x=(position - startNum) * factor - 500

    turtle.goto(x, y)

    turtle.pendown()
    turtle.pencolor(pencolor)
    #向上
    turtle.left(90)
    turtle.forward(height)
    #向左
    turtle.left(90)
    turtle.forward(length)

    # 三角形
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    turtle.penup()
    turtle.goto(x-length, y+height-5)
    turtle.pendown()

    turtle.right(90)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(10)
    turtle.end_fill()
    DrawLabel(position-10, y-25 , 1, fontsize, '#000000', label)
    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()


def drawRectangleR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x = (position - startNum) * factor - 500

    turtle.goto(x,y-height/2)
    turtle.pendown()
    turtle.pencolor(pencolor)
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    #向上
    turtle.left(90)
    turtle.forward(height)
    #向右
    turtle.right(90)
    turtle.forward(length)
    # 向下
    turtle.right(90)
    turtle.forward(height)
    # 向左
    turtle.right(90)
    turtle.forward(length)

    turtle.end_fill()
    DrawLabel(position, y - height / 2 - 20, 1, fontsize, '#000000', label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawRectangleL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.penup()
    x = (position - startNum) * factor - 500

    turtle.goto(x,y-height/2)
    turtle.pendown()
    turtle.pencolor(pencolor)
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    #向上
    turtle.left(90)
    turtle.forward(height)
    #向左
    turtle.left(90)
    turtle.forward(length)
    # 向下
    turtle.left(90)
    turtle.forward(height)
    # 向右
    turtle.left(90)
    turtle.forward(length)

    turtle.end_fill()
    DrawLabel(position-length/2, y - height / 2 - 20, 1, fontsize, '#000000', label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def half_a(x):
  a = x
  b = 90
  while True:
    turtle.circle(a, 1)
    a = a - x / 100
    b = b - 1
    if b == 0:
      break

def half_b(x):
  a = x * 0.1
  b = 90
  while True:
    turtle.circle(a, 1)
    a = a + x / 100
    b = b - 1
    if b == 0:
      break


def DrawEllipse(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.penup()
    x = (position - startNum) * factor - 500
    turtle.goto(x, y - length / 2)
    turtle.pendown()
    turtle.speed(0)  # 设置画笔速度
    turtle.color(pencolor)      #设置画笔颜色
    turtle.pensize(pensize)       #设置画笔粗细
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)


    half_a(length)
    half_b(length)
    half_a(length)
    half_b(length)

    turtle.end_fill()

    turtle.speed(0)  # 设置画笔速度
    turtle.penup()
    turtle.goto(x, y )
    turtle.pendown()
    turtle.color(pencolor)  # 设置画笔颜色
    turtle.pensize(1)
    DrawLabel(position-length/2,y-length/2-20 ,1,fontsize,"#000000",label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def DrawLabel(position,y,pensize,fontsize,pencolor,label) :
    turtle.penup()
    x = (position - startNum) * factor - 500
    turtle.goto(x, y )
    turtle.pendown()
    turtle.speed(0)  # 设置画笔速度
    turtle.color(pencolor)  # 设置画笔颜色
    turtle.pensize(pensize)
    turtle.write(label, 0, font=("Arial", fontsize, "normal"))


def DrawText(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.penup()
    x = (position - startNum) * factor - 500
    turtle.goto(x, y )
    turtle.pendown()
    turtle.speed(0)  # 设置画笔速度
    turtle.color(pencolor)  # 设置画笔颜色
    turtle.pensize(pensize)
    turtle.write(label, 0, font=("Arial", fontsize, "normal"))

def drawPolyAR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :

    for i in range(0,Repeatnumber):
        drawRectangleR(position+length*i+2*i, y, length, height, pencolor, fillcolor, '',1,pensize,fontsize)

    DrawLabel(position, y-height/2-20, pensize, fontsize, '#000000', label)

def drawPolyAL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :


    for i in range(0,Repeatnumber):
        drawRectangleR(position-length*i-2*i, y, length, height, pencolor, fillcolor, '',1,pensize,fontsize)

    DrawLabel(position - length * Repeatnumber , y - height / 2 - 20, pensize, fontsize, pencolor, label)

def drawPartsR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.pencolor(pencolor)

    x = (position - startNum) * factor - 500
    turtle.penup()

    ww = length * factor

    turtle.goto(x, y+height/2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)


    turtle.forward(ww/2)

    a = math.atan((height/ww))
    aa = math.degrees(a)


    turtle.right(aa)


    z =math.sqrt(math.pow(height, 2) + math.pow(ww, 2))/2

    turtle.forward(z)
    turtle.right(180 - aa * 2)
    turtle.forward(z)
    turtle.right(aa)
    turtle.forward(ww/2)
    turtle.right(90)

    turtle.forward(height )
    turtle.goto(x, y+height/2 )
    turtle.right(180)
    turtle.forward(height/2)
    turtle.left(90)
    #turtle.forward(ww)

    turtle.end_fill()
    DrawLabel(position, y-height/2-20, pensize, fontsize, '#000000', label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawPartsL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.pencolor(pencolor)

    x = (position - startNum) * factor - 500
    turtle.penup()

    ww = length * factor

    turtle.goto(x, y+height/2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)

    turtle.left(180)
    turtle.forward(ww/2)

    a = math.atan((height/ww))
    aa = math.degrees(a)


    turtle.left(aa)


    z =math.sqrt(math.pow(height, 2) + math.pow(ww, 2))/2

    turtle.forward(z)
    turtle.left(180 - aa * 2)
    turtle.forward(z)
    turtle.left(aa)
    turtle.forward(ww/2)
    turtle.left(90)

    turtle.forward(height)
    turtle.goto(x, y+height/2 )
    turtle.right(180)
    turtle.forward(height)
    turtle.left(90)
    #turtle.forward(ww)

    turtle.end_fill()
    DrawLabel(position-ww/2, y-height/2-20, pensize, fontsize, '#000000', label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawCircleR(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.pencolor(pencolor)

    x = (position - startNum) * factor - 500
    turtle.penup()

    turtle.goto(x-length, y+length)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    turtle.circle(-length)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    DrawLabel(position-length*2, y - length  - 20, pensize, fontsize, '#000000', label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()

def drawCircleL(position,y,length,height,pencolor,fillcolor,label,Repeatnumber,pensize,fontsize) :
    turtle.pensize(pensize)
    turtle.pencolor(pencolor)

    x = (position - startNum) * factor - 500
    turtle.penup()

    turtle.goto(x-2*length, y-length)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    turtle.circle(length)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    DrawLabel(position-length*3, y - length  - 20, pensize, fontsize, '#000000', label)

    # 恢复海龟前进方向向右
    turtle.penup()
    turtle.home()
    turtle.pendown()



def Draw(filename):
    QMessageBox.about(None, 'Info', "Don't  close the window while drawing")
    turtle.Screen().setup(width=1200,height=600,startx=None,starty=None)
    turtle.title("Biopart Render - Create professional parts figures within minutes")
    #绘制水平线
    #turtle.setup(1200, 600, 0, 0)
    turtle.speed(0)  # 设置画笔速度
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-595, 280)
    turtle.pencolor("red")
    turtle.write("Don't close the window while drawing", 0, font=("Arial", 12, "normal"))
    turtle.pensize(5)

    turtle.home()
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.forward(1000)


    f=open(filename, "r")
    datas = f.readlines()

    #读取序列起始信息
    p=datas[0].split(',')

    startN=int(p[0])
    endN=int(p[1].strip())

    global  startNum
    startNum= int(startN)
    global endNum
    endNum = int(endN)
    global factor
    factor= 1000 / (endNum - startNum)

    for i in range(1, len(datas)):
        p = datas[i].split(',')

        p2 = int(p[2].strip())
        p3 = int(p[3].strip())
        p4 = int(p[4].strip())
        p5 = int(p[5].strip())

        p6 = p[6].strip()
        p7 = p[7].strip()
        p8 = p[8].strip()
        p9 = int(p[9].strip())
        p10 = int(p[10].strip())
        p11 = int(p[11].strip())
        if p[0] == "Promoter" and p[1] == "R":
            drawStartOnR(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Promoter" and p[1] == "L":
            drawStartOnL(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Ellipse":
            DrawEllipse(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Rectangle" and p[1] == "R":
            drawRectangleR(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Rectangle" and p[1] == "L":
            drawRectangleL(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Rectangle_Triangle" and p[1] == "R":
            drawPartsR(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Rectangle_Triangle" and p[1] == "L":
            drawPartsL(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Circle" and p[1] == "R":
            drawCircleR(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Circle" and p[1] == "L":
            drawCircleL(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Triangle" and p[1] == "R":
            drawTriangleR(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "Triangle" and p[1] == "L":
            drawTriangleL(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "PA" and p[1] == "R":
            drawPolyAR(p2,p3,p4,p5,p6,p7,p8,p9,p10,p11)

        if p[0] == "PA" and p[1] == "L":
            drawPolyAL(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Terminator" and p[1] == "R":
            drawRectangleR(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Terminator" and p[1] == "L":
            drawRectangleL(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Text":
            DrawText(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)

        if p[0] == "Suppress" and p[1] == "R":
            drawSuppressR(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Suppress" and p[1] == "L":
            drawSuppressL(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Enhance" and p[1] == "R":
            drawEnhanceR(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)

        if p[0] == "Enhance" and p[1] == "L":
            drawEnhanceL(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)


        if p[0] == "Suppress bottom" and p[1] == "R":
            drawSuppressBottomR(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Suppress bottom" and p[1] == "L":
            drawSuppressBottomL(p2, p3, p4, p5, p6, p7, p8, p9,p10,p11)

        if p[0] == "Enhance bottom" and p[1] == "R":
            drawEnhanceBottomR(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)

        if p[0] == "Enhance bottom" and p[1] == "L":
            drawEnhanceBottomL(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)




    f.close()
    turtle.penup()
    turtle.pencolor('white')
    turtle.home()
    turtle.goto(0, 300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('white')
    turtle.right((90))
    turtle.forward(20)
    turtle.right((90))
    turtle.forward(600)
    turtle.right((90))
    turtle.forward(20)
    turtle.right((90))
    turtle.forward(600)
    turtle.end_fill()

    turtle.done()
    turtle.TurtleScreen._RUNNING = True


def save2File(filename,content):
    file = open(filename, 'w')
    file.write(content)
    file.close()
    QMessageBox.about(None, 'Info', 'File Saved!')

def main():
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    font =QFont("Times New Roman")
    pointsize = font.pointSize()

    font.setPixelSize(pointsize * 90 / 72)

    app.setFont(font)
    myWin.show()
    myWin.demo()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()

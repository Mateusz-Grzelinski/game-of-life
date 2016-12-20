# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:36:13 2016

@author: ASRock
"""
import sys, random
from PyQt4 import QtOpenGL
from PyQt4 import QtGui, QtCore
from UIgame import Ui_MainWindow



class CellItem(QtGui.QGraphicsRectItem):
    _i= 0
    _j=0                #used for click event
    _status=False       
    _status_prev=False  #for counting next self.generation
    _plag=False
    backup_gen=False     #do guzika Back to begining
    backup_gen_plag=False #do guzika Back to begining
    
    def changeCell(self):
        global BOXES
        if self._status == True:
            BOXES[self._i][self._j]._status_prev = False
            BOXES[self._i][self._j]._status = False
            BOXES[self._i][self._j]._plag = False
        else:
            BOXES[self._i][self._j]._status_prev = True
            BOXES[self._i][self._j]._status = True
            BOXES[self._i][self._j]._plag = False
    def changeCellPlag(self):
        global BOXES
        if ( ui.PlagueCheckBox.isChecked()  ):
            if self._plag == True:
                BOXES[self._i][self._j]._plag = False
            else:
                BOXES[self._i][self._j]._plag = True
                BOXES[self._i][self._j]._status_prev = True
                BOXES[self._i][self._j]._status = True
    def mousePressEvent(self, event):
        global BOXES
        if event.button() == QtCore.Qt.LeftButton:
            self.changeCell()
        if event.button() == QtCore.Qt.RightButton:
            self.changeCellPlag()
        ui.DrawChange()
   
                   
class Ui_MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        global BOXES
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.generation = 0
        self.rows = 10
        self.columns = 10
        self.cel_size = 20
        self.graph()
        #self.setMouseTracking(True) niepotrzebne
        
    def graph(self):
        global BOXES
        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsScene.setSceneRect(0,0,400,300)
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsView.setViewport(QtOpenGL.QGLWidget()) #obliczenia na karcie graficznej
        #init cells:
        BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size) for i in range(self.rows)] for j in range(self.columns)]
        self.DrawGrid()
        
        self.RandomInfection.clicked.connect(self.RandomizePlag)
        self.RandomStart.clicked.connect(self.Randomize)
        self.ToBegin.clicked.connect(self.ToBeginning)
        self.Blank.clicked.connect( self.NewLife )
        self.PlagueCheckBox.stateChanged.connect(self.PlagRandomActivate)
        self.RowsColumsCheckBox.stateChanged.connect(self.SetSquare)
        self.RowsSpinBox.valueChanged.connect(self.UpdateValues)
        self.ColumnsSpinBox.valueChanged.connect(self.UpdateValues)
        self.Tick.clicked.connect(self.TickGen)
        self.graphicsView.setSceneRect(0,0,self.cel_size*self.rows,self.cel_size*self.columns)
        #self.graphicsView.setSceneRect(self.graphicsScene.itemsBoundingRect())

        self.ScaleIn.clicked.connect(self.scaleViewIn)
        self.ScaleOut.clicked.connect(self.scaleViewOut)
    
    def PlagRandomActivate(self):
        if ( self.PlagueCheckBox.isChecked() ):
            self.RandomInfection.setEnabled(True)
        else:
            self.RandomInfection.setEnabled(False)
    def Randomize(self):
        global BOXES
        for i in range(self.rows):
            for j in range(self.columns):
                if (random.randint(-50,30)<0): #ustawianie prawdopodobienstwa
                    BOXES[i][j]._status =False
                    BOXES[i][j]._status_prev =False
                else:
                    BOXES[i][j]._status = True
                    BOXES[i][j]._status_prev = True
        self.DrawChange()
        
    def RandomizePlag(self):
        global BOXES
        for i in range(self.rows):
            for j in range(self.columns):
                if (random.randint(-50,30)<0):
                    BOXES[i][j]._plag =False
                else:
                    BOXES[i][j]._plag = False
        self.DrawChange()
        
    def ToBeginning(self):
        global BOXES
        self.generation=0
        self.LGeneration.setText("Generacja: "+str(self.generation) )
        for i in range(self.rows):
            for j in range(self.columns):
                BOXES[i][j]._status =  BOXES[i][j].backup_gen
                BOXES[i][j]._status_prev = BOXES[i][j].backup_gen
                BOXES[i][j]._plag = BOXES[i][j].backup_gen_plag
        self.DrawChange()
        
    def UpdateValues(self):
        global BOXES
        self.rows = self.RowsSpinBox.value()
        if( self.RowsColumsCheckBox.isChecked() ):
            self.columns = self.rows
            self.ColumnsSpinBox.setValue(self.columns)
        else:
            self.columns = self.ColumnsSpinBox.value()
        BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size) for j in range(self.columns)] for i in range(self.rows)]
        self.DrawGrid()
        
    def getAmountOfNeighbs(self,x,y):
        neighbors = 0
        global BOXES
        for diffX in {-1,0,1}:
          for diffY in {-1,0,1}:
            nX = x + diffX
            nY = y + diffY
            if nX >= 0 and nY >= 0 and nX < self.rows and nY < self.columns:
                if (BOXES[nX][nY]._status_prev==True and not (diffX == diffY == 0)) :
                    neighbors += 1
        #if neighbors>0: 
        #    print (x,y,neighbors)
        return neighbors
        
    def TickGen(self):
        global BOXES
        if (self.generation==0): #ustawianie pkt powrotu Back to beginning 
            #backup_gen = [[False for j in range(self.columns)] for i in range(self.rows)]
            #BOXES[i][j].backup_gen_plag = [[False for j in range(self.columns)] for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.columns):
                    BOXES[i][j].backup_gen = BOXES[i][j]._status 
                    BOXES[i][j].backup_gen_plag = BOXES[i][j]._plag
                    
        self.generation+=1
        self.LGeneration.setText("Generation: "+str(self.generation) )
        for i in range(self.rows):
            for j in range(self.columns):
                neighbours=self.getAmountOfNeighbs(i,j)
                if ( not self.PlagueCheckBox.isChecked()  ):
                    if  BOXES[i][j]._status_prev == True and (neighbours < 2 or neighbours > 3):
                        BOXES[i][j]._status  = False
                    if BOXES[i][j]._status_prev == False and neighbours == 3:
                        BOXES[i][j]._status = True
                else: 
                    pass
                #miejsce na reguly z plaga
                
        for i in range(self.rows):     #potrzebne do generacji kolejnego pokolenia
            for j in range(self.columns):
                BOXES[i][j]._status_prev = BOXES[i][j]._status
        self.DrawChange()
        
    def NewLife(self):  #zresetuj wszystko oprocz wartosci BOXES._i, BOXES._j
        global BOXES
        self.generation=0
        self.LGeneration.setText("Generacja: "+str(self.generation) )
        for i in range(self.rows):
            for j  in range(self.columns):
                BOXES[i][j]._status = False
                BOXES[i][j]._status_prev = False
                BOXES[i][j]._plag = False
        self.DrawChange()
                
                
    def DrawGrid(self):     #wywolywane wtedu gdy zmienia sie rozmiar tablicy
        #todo zmienic definicje tablicy na append i del, dodać remove item i usunac scene.clear()
        global BOXES
        
        self.graphicsView.setSceneRect(0,0,self.cel_size*self.rows,self.cel_size*self.columns)
        self.graphicsScene.clear() #potrzebne gdy uswam elementy
        for i in range(self.rows):
            for j  in range(self.columns):
                #BOXES[i][j] = CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size)
                BOXES[i][j]._i = i
                BOXES[i][j]._j=j
                self.graphicsScene.addItem(BOXES[i][j])
        self.graphicsView.centerOn(BOXES[self.rows//2][self.columns//2])
        self.DrawChange()
    
    def DrawChange(self):   #rysuje wszystkie kolory
        global BOXES
        checked = QtGui.QBrush(QtGui.QColor(220,220,240))
        unchecked = QtGui.QBrush(QtGui.QColor(30,30,35))
        plague = QtGui.QBrush(QtGui.QColor(220,100,150))
        for i in range(self.rows):
            for j  in range(self.columns):
                if( BOXES[i][j]._status == True):
                    BOXES[i][j].setBrush(checked)
                else:
                    BOXES[i][j].setBrush(unchecked)
                if( BOXES[i][j]._plag == True ):
                    BOXES[i][j].setBrush(plague)

    def SetSquare(self):
        global BOXES
        if( self.RowsColumsCheckBox.isChecked() ):
            self.columns = self.rows
            self.LColums.setEnabled(False) 
            self.ColumnsSpinBox.setEnabled(False)
            BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size) for j in range(self.columns)] for i in range(self.rows)]
            self.DrawGrid()
        else:
            self.LColums.setEnabled(True) 
            self.ColumnsSpinBox.setEnabled(True)
            BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size) for j in range(self.columns)] for i in range(self.rows)]
            self.DrawGrid()
            
    def wheelEvent(self,event):
        if(event.delta() > 0):
            self.scaleViewIn()
        else:
            self.scaleViewOut()
    def scaleViewIn(self):
        self.graphicsView.scale(1.1,1.1)
        self.graphicsView.centerOn(BOXES[self.rows//2][self.columns//2])
    def scaleViewOut(self):
        self.graphicsView.scale(0.9,0.9)
        self.graphicsView.centerOn(BOXES[self.rows//2][self.columns//2])
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.show()
    sys.exit( app.exec_() )
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:36:13 2016

@author: ASRock
"""
import sys, random, time
#from PyQt4 import QtOpenGL
from PyQt4 import QtGui, QtCore
from GameUI20 import Ui_MainWindow
from WindowRules1 import Ui_RuleEditorWidget


class CellItem(QtGui.QGraphicsRectItem):
    def __init__(self, a,b,c,d,i=0,j=0 ):
        super().__init__(a,b,c,d)
        self._i= i
        self._j= j               #used for click event
        self._status=False
        self._status_prev=False  #for counting next self.generation
        self._plag=False
        self._backup_gen=False     #do guzika Back to begining
        self._backup_gen_plag=False #do guzika Back to begining
    
    def changeCell(self):
        if self._status == True:
            self._status_prev = False
            self._status = False
            self._plag = False
        else:
            self._status_prev = True
            self._status = True
            self._plag = False
    def changeCellPlag(self):
        if ( ui.PlagueCheckBox.isChecked()  ):
            if self._plag == True:
                self._plag=False
                self._plag = False
            else:
                self._plag=True
                self._plag = True
                self._status_prev = True
                self._status = True
    def mousePressEvent(self, event):
        global BOXES
        if event.button() == QtCore.Qt.LeftButton:
            self.changeCell()
        if event.button() == QtCore.Qt.RightButton:
            self.changeCellPlag()
        ui.DrawChangeSingle(self._i,self._j)
   
class MeasureTime():
    _time = 0.0
    _startTime = 0.0
    def start(self):
        self._startTime= time.clock()
    def stop(self):
        self._time = time.clock() - self._startTime
    def getTime(self):
        return self._time
                   
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        global BOXES
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
        self.RulesTabDies = "014567"   #ktore komorki umieraja
        self.RulesTabBorn = "3"        #ktore komorki rodza sie  
        self.generation = 0
        self.rows = 10
        self.columns = 10
        self.cel_size = 20
        self.checked = QtGui.QBrush(QtGui.QColor(220,220,240))
        self.unchecked = QtGui.QBrush(QtGui.QColor(30,30,35))
        self.plague = QtGui.QBrush(QtGui.QColor(220,100,150))
        self.fps = 1000/self.FPSSpinBox.value()
        self.watch = MeasureTime()
        self.timer = QtCore.QTimer()    #do autogeneracji
        self.timer.timeout.connect(self.TickGen)
        self.InitUI()
        #self.setMouseTracking(True) niepotrzebne
        
    def InitUI(self):    #wywolywana tylko raz, ustawia warunku poczatkowe
        global BOXES
        #self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsScene.setSceneRect(0,0,400,300)
        self.graphicsView.setScene(self.graphicsScene)
        #self.graphicsView.setViewport(QtOpenGL.QGLWidget()) #obliczenia na karcie graficznej
        #init cells:
        BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size) for i in range(self.rows)] for j in range(self.columns)]
        self.DrawGrid()
        
        self.EditRules.clicked.connect(self.EditRulesWindow)
        self.RemovePreset.clicked.connect(self.DeletePreset)
        self.FPSSpinBox.valueChanged.connect(self.UpdateFPS)
        self.StartStop.clicked.connect(self.ToogleAutoGen)
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

    def DeletePreset(self):
        choice = QtGui.QMessageBox.question(self, 'Delete preset: bla bla',
                                            "Are you sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Deleting current preset...")
            sys.exit()
        else:
            pass
    def UpdateFPS(self):    
        self.fps = 1000/self.FPSSpinBox.value()
        self.ToogleAutoGen()
        self.ToogleAutoGen()
    def ToogleAutoGen(self):
        if self.timer.isActive()==True:
            self.timer.stop()
        else:
            self.timer.start( self.fps )
    def PlagRandomActivate(self):
        if ( self.PlagueCheckBox.isChecked() ):
            self.RandomInfection.setEnabled(True)
        else:
            self.RandomInfection.setEnabled(False)
            global BOXES
            for i in range(self.rows): #wymaz wszyskie plagi
                for j in range(self.columns):
                        BOXES[i][j]._plag = False
    def Randomize(self):
        global BOXES
        for i in range(self.rows):
            for j in range(self.columns):
                if (random.randint(-50,30)>0): #ustawianie prawdopodobienstwa
                    BOXES[i][j]._status = True
                    BOXES[i][j]._status_prev = True
                else:
                    BOXES[i][j]._status =False
                    BOXES[i][j]._status_prev =False
        self.DrawChange()
    def RandomizePlag(self):
        global BOXES
        for i in range(self.rows):
            for j in range(self.columns):
                if (random.randint(-50,30)>0 and BOXES[i][j]._status==True):
                    BOXES[i][j]._plag =True
                else:
                    BOXES[i][j]._plag = False
        self.DrawChange()
        
    def ToBeginning(self):
        global BOXES
        self.timer.stop()
        self.generation=0
        self.LGeneration.setText("Generation: "+str(self.generation) )
        for i in range(self.rows):
            for j in range(self.columns):
                BOXES[i][j]._status =  BOXES[i][j]._backup_gen
                BOXES[i][j]._status_prev = BOXES[i][j]._backup_gen
                BOXES[i][j]._plag = BOXES[i][j]._backup_gen_plag
        self.DrawChange()
        
    def UpdateValues(self):
        global BOXES
        self.rows = self.RowsSpinBox.value()
        if( self.RowsColumsCheckBox.isChecked() ):
            self.columns = self.rows
            self.ColumnsSpinBox.setValue(self.columns)
        else:
            self.columns = self.ColumnsSpinBox.value()
        BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size, i, j) for i in range(self.rows)] for j in range(self.columns)]
        self.DrawGrid()
        
    def getAmountOfNeighbs(self,x,y):
        neighbors = 0
        global BOXES
        for diffX in {-1,0,1}:
          for diffY in {-1,0,1}:
            nX = x + diffX
            nY = y + diffY
            #czy jestem dalej w obszarze tablicy:
            if nX >= 0 and nY >= 0 and nX < self.rows and nY < self.columns: 
                if (BOXES[nX][nY]._status_prev==True and not (diffX == diffY == 0)) :
                    neighbors += 1
        if neighbors>0: 
            print ("sasiad: ",x,y,neighbors)
        return neighbors
        
    def TickGen(self):
        print("Born:", self.RulesTabBorn)
        print("Dies: ", self.RulesTabDies)
        global BOXES
        self.watch.start()
        if (self.generation==0): #ustawianie pkt powrotu Back to beginning 
            for i in range(self.rows):
                for j in range(self.columns):
                    BOXES[i][j]._backup_gen = BOXES[i][j]._status 
                    BOXES[i][j]._backup_gen_plag = BOXES[i][j]._plag
        self.generation+=1
        self.LGeneration.setText("Generation: "+str(self.generation) )
        
        for i in range(self.rows):      #dodac reguly dot plagi!!
            for j in range(self.columns):
                neighbours=self.getAmountOfNeighbs(i,j)
                if  BOXES[i][j]._status_prev == True and (str(neighbours) in self.RulesTabDies):
                    BOXES[i][j]._status  = False
                if BOXES[i][j]._status_prev == False and (str(neighbours) in self.RulesTabBorn):
                    BOXES[i][j]._status = True
                self.DrawChangeSingle(i,j)
                
        for i in range(self.rows):     #potrzebne do generacji kolejnego pokolenia
            for j in range(self.columns):
                BOXES[i][j]._status_prev = BOXES[i][j]._status
        #self.DrawChange()
        self.watch.stop()
        if (1/self.FPSSpinBox.value()<self.watch.getTime()):
            self.LDelay.setText("Last generation took:\n"+ "{0:.3f}".format(self.watch.getTime()) + " sec.to calculate"+"\nNOT reatlime")
        else:
            self.LDelay.setText("Last generation took:\n"+ "{0:.3f}".format(self.watch.getTime()) + " sec.to calculate")

        
    def NewLife(self):  #zresetuj wszystko oprocz wartosci 
        global BOXES
        self.timer.stop()
        self.generation=0
        self.LGeneration.setText("Generation: "+str(self.generation) )
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
        self.graphicsScene.clear() #potrzebne gdy usuwam elementy
        for i in range(self.rows):
            for j  in range(self.columns):
                #BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size, i, j) for i in range(self.rows)] for j in range(self.columns)]
                BOXES[i][j]._i= i 
                BOXES[i][j]._j=j
                self.graphicsScene.addItem(BOXES[i][j])
        self.graphicsView.centerOn(BOXES[self.rows//2][self.columns//2])
        self.DrawChange()
    
    def DrawChange(self):   #rysuje wszystkie kolory dla calej tablicy
        global BOXES
        for i in range(self.rows):
            for j  in range(self.columns):
                if( BOXES[i][j]._status == True):
                    BOXES[i][j].setBrush(self.checked)
                else:
                    BOXES[i][j].setBrush(self.unchecked)
                if( BOXES[i][j]._plag == True ):
                    BOXES[i][j].setBrush(self.plague)
                    
    def DrawChangeSingle(self, i, j):   #rysuje wszystkie kolory dla JEDNEJ komorki
        global BOXES
        if( BOXES[i][j]._status == True):
            BOXES[i][j].setBrush(self.checked)
        else:
            BOXES[i][j].setBrush(self.unchecked)
        if( BOXES[i][j]._plag == True ):
            BOXES[i][j].setBrush(self.plague)

    def SetSquare(self):
        global BOXES
        if( self.RowsColumsCheckBox.isChecked() ):
            self.columns = self.rows
            self.LColums.setEnabled(False) 
            self.ColumnsSpinBox.setEnabled(False)
            BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size, i, j) for i in range(self.rows)] for j in range(self.columns)]
            self.DrawGrid()
        else:
            self.LColums.setEnabled(True) 
            self.ColumnsSpinBox.setEnabled(True)
            BOXES = [ [CellItem(self.cel_size*i,self.cel_size*j,self.cel_size,self.cel_size, i, j) for i in range(self.rows)] for j in range(self.columns)]
            self.DrawGrid()
            
    def wheelEvent(self,event):
        if(event.delta() > 0):
            self.scaleViewIn()
        else:
            self.scaleViewOut()
    def scaleViewIn(self):
        self.graphicsView.scale(1.15,1.15)
    def scaleViewOut(self):
        self.graphicsView.scale(0.85,0.85)
    def closeEvent(self, event):
        self.WindowRulesEditor.close()
    def EditRulesWindow(self):
        self.WindowRulesEditor = RuleEditorWidget()
        #self.RulesTabDies
        #self.WindowRulesEditor.RulesTabBorn 
        #self.WindowRulesEditor.RulesTabDies 
        
class RuleEditorWidget(QtGui.QWidget, Ui_RuleEditorWidget): 
    #dziedziczy z qwidget aby postawic okno, Ui_RuleEditorWidget aby postawic UI,
    #z MainWindow aby miec dostep do RulesTabBorn, RulesTabDies
    def __init__(self):
        super(RuleEditorWidget,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.move(0,550)
        self.CellBornLineEdit.setText( self.CellBornLineEdit.text() )
        self.CellDiesLineEdit.setText( self.CellDiesLineEdit.text() )
        #self.CellBornLineEdit.textChanged.connect( self.UpdateBorn )
        #self.CellDiesLineEdit.textChanged.connect( self.UpdateDies )
        self.show()
    '''
    def UpdateBorn(self):
        #getattr(Ui_MainWindow, "UpdateRules")
        MainWindow.RulesTabBorn = self.CellBornLineEdit.text()
        print(self.RulesTabBorn)
        #return self.CellBornLineEdit.text()
    def UpdateDies(self):
        MainWindow.RulesTabDies = self.CellDiesLineEdit.text()
        print(MainWindow.RulesTabDies)
        #return self.CellDiesLineEdit.text()
        #self.WindowRulesEditor.RulesTabBorn zmienic warunek w klasie MainWindow
    '''

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    ui = MainWindow()
    #nowy = Ui_RuleEditorWidget()
    ui.show()
    sys.exit( app.exec_() )
#layout = QVBoxLayout(self)
#layout.add(everything)
#do skalowania na cały ekran   
    
    
    
    
    
    
    
    
    
    
    
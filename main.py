from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.car_brands = ['Audi', 'BMW', 'Mercedes-Benz','Acura','Honda', 'Alfa Romeo', 'Aston Martin', 'Bugatti', 'Buick','Cadillac', 'Chevrolet', 'Chrysler','Dodge','Ferrari','Fiat','Ford','Genesis','GMC']



        self.car_models = {
            
            
            'Mercedes-Benz': ['190 A-Class', 'AMG GT', 'B-Class', 'C-Class1', 'CL', 'CLA', 'CLK', 'CLS', 'E-Class', 'EQC', 'EQS', 'G-Class', 'GL', 'GLA', 'GLB', 'GLC', 'GLE', 'GLK', 'GLS', 'M-Class', 'Metris Van', 'Other', 'R-Class', 'S-Class', 'SL', 'SLC', 'SLK', 'SLR', 'SLS AMG', 'Sprinter Van', 'Sprinter Wagon'],
            'Acura': ['ILX', 'MDX', 'NSX', 'RDX', 'RLX', 'TLX'],
            'Alfa Romeo': ['4C', 'Giulia', 'Stelvio'],
            'Aston Martin': ['DB11', 'DBS Superleggera', 'Vantage'],
            'Audi': ['A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Q3', 'Q5', 'Q7', 'Q8', 'R8', 'RS Q8', 'RS3', 'RS5', 'RS6', 'RS7', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'SQ5', 'SQ7', 'TT'],
            'Bentley': ['Bentayga', 'Continental GT', 'Flying Spur', 'Mulsanne'],
            'BMW': ['1 Series','1 Series M','2 Series', '3 Series', '4 Series', '5 Series', '6 Series', '7 Series', '8 Series', 'M2', 'M3', 'M4', 'M5', 'M6', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'Z4'],
            'Bugatti': ['Chiron'],
            'Buick': ['Enclave', 'Encore', 'Envision', 'LaCrosse', 'Regal', 'Verano'],
            'Cadillac': ['ATS', 'CT4', 'CT5', 'CT6', 'CTS', 'Escalade', 'XT4', 'XT5', 'XT6', 'XTS'],
            'Chevrolet': ['Astro', 'Avalanche', 'Aveo', 'Bel Air / 150 / 210', 'Beretta', 'Blazer', 'Bolt', 'C/K 1500', 'C/K 2500', 'C/K 3500', 'C10', 'Camaro', 'Caprice', 'Cavalier', 'Chevelle', 'Chevy Van', 'Cheyenne', 'City Express', 'Cobalt', 'Colorado', 'Corsica', 'Corvair', 'Corvette', 'Cruze', 'Cutaway Van', 'El Camino', 'Epica', 'Equinox', 'Express', 'G Series Van', 'HHR', 'Impala', 'Lumina', 'Malibu', 'Metro', 'Monte Carlo', 'Nova', 'Optra', 'Orlando', 'Other', 'Other Pickups', 'S-10', 'Silverado 1500', 'Silverado 2500', 'Silverado 3500', 'Sonic', 'Spark', 'Sportvan', 'Sprint', 'SSR', 'Suburban', 'T100', 'Tahoe', 'Tracker', 'Trailblazer', 'Traverse', 'Trax', 'Uplander', 'Venture', 'Volt'],
            'Chrysler': ['300', 'Pacifica', 'Voyager'],
            'Dodge': ['Avenger', 'Caliber', 'Caravan', 'Challenger', 'Charger', 'Colt', 'Coronet', 'Dakota', 'Dart', 'Durango', 'Grand Caravan', 'Intrepid', 'Journey', 'Lancer', 'Magnum', 'Neon', 'Nitro', 'Other', 'Other Pickups', 'Power Wagon', 'Ram 1500', 'Ram 2500', 'Ram 3500', 'Ram Van', 'Shadow', 'Spirit', 'Sprinter', 'Stealth', 'Stratus', 'SX 2.0', 'Viper'],
            'Ferrari': ['488 GTB', '488 Pista', '812 Superfast', 'GTC4Lusso', 'Portofino', 'SF90 Stradale'],
            'Fiat': ['124 Spider', '500', '500L', '500X'],
            'Ford': ['Aerostar', 'Aspire', 'Bronco', 'Bronco II', 'Bronco Sport', 'C-Max', 'Club Wagon', 'Contour', 
             'Cougar', 'Crown Victoria', 'E 150', 'E 250', 'E 350', 'E 450', 'E-Series Van', 'EcoSport', 
             'Edge', 'Escape', 'Escort', 'Excursion', 'Expedition', 'Explorer', 'Explorer Sport', 
             'Explorer Sport Trac', 'F 100', 'F 150', 'F 150 Raptor', 'F 250', 'F 350', 'F 450', 'F 550', 
             'F 650', 'F 750', 'F 800', 'Fairlane', 'Fairmont', 'Falcon', 'Fiesta', 'Five Hundred', 
             'Flex', 'Focus', 'Freestar', 'FreeStyle / Taurus X', 'Fusion', 'Galaxie', 'Grand Marquis', 
             'Marauder', 'Maverick', 'Model A', 'Model T', 'Mustang', 'Mustang GT', 'Mustang Mach-E', 'Other', 
             'Other Pickups', 'Probe', 'Ranchero', 'Ranger', 'Taurus', 'Tempo', 'Thunderbird', 'Torino', 
             'Transit', 'Transit Cargo', 'Transit Connect', 'Transit Passenger', 'Windstar'],
            'Genesis': ['G70', 'G80', 'G90'],
            'Honda': ['Accord','Accord Crosstour','Civic','Clarity','CR-V','CR-Z','CRX','Del Sol','Element','Fit','HR-V','Insight','Odyssey','Other','Passport','Pilot','Prelude','Ridgeline','S2000'],
            'GMC': ['Acadia', 'C 5500', 'C/K 1500', 'C/K 2500', 'C/K 3500', 'C10', 'Canyon', 'Envoy', 'HUMMER EV', 'Jimmy', 'Other', 'Other Pickups', 'Rally Van', 'Safari', 'Savana', 'Sierra', 'Sierra 1500', 'Sierra 2500', 'Sierra 3500', 'Sonoma', 'Suburban', 'Terrain', 'Typhoon', 'Vandura', 'Yukon'],
        }


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 290, 111, 41))
        self.pushButton.setObjectName("pushButton")


        self.brand_combo = QtWidgets.QComboBox(self.centralwidget)
        self.brand_combo.setGeometry(QtCore.QRect(20, 70, 121, 22))
        self.brand_combo.addItems(self.car_brands)
        self.brand_combo.setObjectName("comboBox")
        self.brand_combo.currentIndexChanged.connect(self.update_models)


        self.model_combo = QtWidgets.QComboBox(self.centralwidget)
        self.model_combo.setGeometry(QtCore.QRect(168, 70, 121, 22))
        self.model_combo.setObjectName("comboBox_2")
    
        


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 50, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 50, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(22, 170, 361, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 311, 16))
        self.label_5.setObjectName("label_5")
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self.centralwidget)
        self.keySequenceEdit.setGeometry(QtCore.QRect(420, 170, 113, 20))
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 145, 141, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 290, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_models(self):
        # Очищаем список моделей
        self.model_combo.clear()
        
        # Получаем выбранную марку машины
        brand = self.brand_combo.currentText()
        
        # Получаем список моделей для выбранной марки
        models = self.car_models[brand]
        
        # Добавляем модели в выпадающий список
        self.model_combo.addItems(models)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Старт!"))
        self.label.setText(_translate("MainWindow", "Марка:"))
        self.label_2.setText(_translate("MainWindow", "Модель:"))
        self.label_3.setText(_translate("MainWindow", "Год выпуска:"))
        self.label_4.setText(_translate("MainWindow", "Пробег:"))
        self.label_5.setText(_translate("MainWindow", "Введите почту на которую будет отправлен результат:"))
        self.label_6.setText(_translate("MainWindow", "Повторный запуск через м:"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

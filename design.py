from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Создаем список марок машин
        self.car_brands = ['Audi', 'BMW', 'Mercedes']
        
        # Создаем словарь моделей машин для каждой марки
        self.car_models = {
            'Audi': ['A1', 'A3', 'A4', 'A5'],
            'BMW': ['1 Series', '2 Series', '3 Series', '4 Series'],
            'Mercedes': ['A Class', 'C Class', 'E Class', 'S Class']
        }
        
        # Создаем выпадающий список для марок машин
        self.brand_combo = QComboBox(self)
        self.brand_combo.setGeometry(10, 10, 150, 30)
        self.brand_combo.addItems(self.car_brands)
        self.brand_combo.currentIndexChanged.connect(self.update_models)
        
        # Создаем выпадающий список для моделей машин
        self.model_combo = QComboBox(self)
        self.model_combo.setGeometry(170, 10, 150, 30)
        
    def update_models(self):
        # Очищаем список моделей
        self.model_combo.clear()
        
        # Получаем выбранную марку машины
        brand = self.brand_combo.currentText()
        
        # Получаем список моделей для выбранной марки
        models = self.car_models[brand]
        
        # Добавляем модели в выпадающий список
        self.model_combo.addItems(models)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
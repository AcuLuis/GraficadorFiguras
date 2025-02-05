import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
centralWidget = None
panelConfiguracion = None
ancho = None
altura = None
eje_x = None
eje_y = None
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OPTIMIZACIÓN DE ESPACIOS")
        self.size_area = QLabel("")
        global altoArea
        global anchoArea
        escD = DialogEscala()
        escD.exec_()
        altoArea, anchoArea = escD.actualiza()
        menubar = self.menuBar()
        menuArchivo = menubar.addMenu("&Archivo")
        menuArchivo.addSeparator()
        menuForma = menubar.addMenu("&Forma")
        menuForma.addSeparator()
        Herramientas = menubar.addMenu("&Herramientas")
        Herramientas.addSeparator()
        status_bar = self.statusBar()
        status_bar.addWidget(self.size_area)
        nuevo = QAction('Nuevo', self)# Nuevo para Menu Archivo
        nuevo.triggered.connect(self.creaWorkSpace)
        menuArchivo.addAction(nuevo)
        configura = QAction('Configuraciones', self)# Configuraciones
        configura.triggered.connect(self.mostrar_configuraciones)
        Herramientas.addAction(configura)
        rectangulo = QAction('Rectángulo', self)# Rectángulo
        rectangulo.triggered.connect(lambda: centralWidget.cambia_forma('rectangulo'))
        menuForma.addAction(rectangulo)
        cuadrado = QAction('Cuadrado', self)# Cuadrado
        cuadrado.triggered.connect(lambda: centralWidget.cambia_forma('cuadrado'))
        menuForma.addAction(cuadrado)
        circulo = QAction('Círculo', self)# Círculo
        circulo.triggered.connect(lambda: centralWidget.cambia_forma('circulo'))
        menuForma.addAction(circulo)
        trapecio = QAction('Trapecio', self)# Trapecio
        trapecio.triggered.connect(lambda: centralWidget.cambia_forma('trapecio'))
        menuForma.addAction(trapecio)
        triangulo = QAction('Triángulo', self)# Triángulo
        triangulo.triggered.connect(lambda: centralWidget.cambia_forma('triangulo'))
        menuForma.addAction(triangulo)
        global centralWidget#CREAR AREA DE INICIO POR DEFECTO
        centralWidget = WorkSpace(anchoArea, altoArea)
        self.setCentralWidget(centralWidget)
        self.dock_widget = QDockWidget("Configuracion de Objeto", self)
        self.show_size_area()
        global panelConfiguracion#CREACION DEL PANEL DE CONFIGURACION
        panelConfiguracion = ConfigPanel()
        panelConfiguracion.setMinimumWidth(180)
        self.dock_widget.setWidget(panelConfiguracion)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget)
        self.dock_widget.setMaximumWidth(180)
        self.dock_widget.setStyleSheet("QDockWidget::title"
            "{"
            "background : lightblue;"
            "}")
        opciones = menubar.addMenu("&Opciones")#Opciones
        opciones.addSeparator()
        guardar = QAction('Guardar', self)
        guardar.triggered.connect(panelConfiguracion.Guardar)
        opciones.addAction(guardar)
        cargar = QAction('Cargar', self)# Añadir botón para cargar JSON
        cargar.triggered.connect(panelConfiguracion.Cargar)
        opciones.addAction(cargar)
    def mostrar_configuraciones(self):
        global panelConfiguracion
        if panelConfiguracion is None:
            panelConfiguracion = ConfigPanel()
            panelConfiguracion.setMinimumWidth(180)
        self.dock_widget.setWidget(panelConfiguracion)
        self.dock_widget.show()
    def show_size_area(self):
        global altoArea
        global anchoArea
        self.size_area.setText(f"Area: {altoArea/100} x {anchoArea/100} metros")
    def creaWorkSpace(self):
        panelConfiguracion.color.setEnabled(False)
        panelConfiguracion.spAltura.setEnabled(False)
        panelConfiguracion.spAncho.setEnabled(False)
        panelConfiguracion.spRotacion.setEnabled(False)
        alto, ok1 = QInputDialog.getInt(self, "Altura del área", "Introduce la altura:", min=100, max=1500)
        ancho, ok2 = QInputDialog.getInt(self, "Ancho del área", "Introduce el ancho:", min=100, max=1500)
        if ok1 and ok2:
            global centralWidget
            centralWidget = WorkSpace(ancho, alto)
            self.setCentralWidget(centralWidget)
            self.show_size_area()
class ConfigPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.widthSpin = 50
        lblEjeX = QLabel("Eje X")
        lblEjeY = QLabel("Eje Y")
        lblRotacion = QLabel("Rotacion")
        lblColor = QLabel("Color")
        lblAncho = QLabel("Ancho")
        lblAltura = QLabel("Altura")
        lblID = QLabel("ID")
        self.spEjeX = QDoubleSpinBox()
        self.spEjeX.setRange(0, 1500)
        self.spEjeX.setDecimals(2)
        self.spEjeX.setEnabled(False)
        self.spEjeY = QDoubleSpinBox()
        self.spEjeY.setRange(0, 1500)
        self.spEjeY.setDecimals(2)
        self.spEjeY.setEnabled(False)
        self.spRotacion = QSpinBox()
        self.spRotacion.setRange(0, 360)
        self.spRotacion.valueChanged.connect(self.on_rotation_change)
        self.spAltura = QDoubleSpinBox()
        self.spAltura.setRange(0, 1500)
        self.spAltura.setDecimals(2)
        self.spAltura.valueChanged.connect(self.on_size_change)
        self.spAncho = QDoubleSpinBox()
        self.spAncho.setRange(0, 1500)
        self.spAncho.setDecimals(2)
        self.spAncho.valueChanged.connect(self.on_size_change)
        self.color = QComboBox()
        self.color.addItem("")
        self.color.addItem("rojo")
        self.color.addItem("azul")
        self.color.addItem("amarillo")
        self.color.addItem("gris")
        self.color.currentTextChanged.connect(self.on_color_change)
        self.spID = QSpinBox()
        self.spID.setRange(0, 10000)
        self.spID.setEnabled(False)
        self.setFixedHeight(400)
        layout = QGridLayout()
        layout.addWidget(lblID, 0, 0)
        layout.addWidget(self.spID, 0, 1, 1, 2)
        layout.addWidget(lblEjeX, 1, 0)
        layout.addWidget(self.spEjeX, 1, 1, 1, 2)
        layout.addWidget(lblEjeY, 2, 0)
        layout.addWidget(self.spEjeY, 2, 1, 1, 2)
        layout.addWidget(lblRotacion, 3, 0)
        layout.addWidget(lblAltura, 4, 0)
        layout.addWidget(lblAncho, 5, 0)
        layout.addWidget(lblColor, 6, 0)
        layout.addWidget(self.spRotacion, 3, 1, 1, 2)
        layout.addWidget(self.spAltura, 4, 1, 1, 2)
        layout.addWidget(self.spAncho, 5, 1, 1, 2)
        layout.addWidget(self.color, 6, 1, 1, 2)
        self.setLayout(layout)
    def on_color_change(self, color):
        if centralWidget.selected_item:
            centralWidget.set_selected_color(color)
            new_brush = QBrush(centralWidget.get_selected_color(panelConfiguracion.color.currentText()))
            centralWidget.selected_item.setBrush(new_brush)
            centralWidget.update()
    def Guardar(self):
        dialog = QFileDialog()
        dialog.setOption(QFileDialog.ReadOnly, False)
        dialog.setOption(QFileDialog.HideNameFilterDetails, False)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilter("PNG Files (*.png);;JSON Files (*.json)")
        elecc, _ = dialog.getSaveFileName(self, 'Guardar como', '', 'PNG Files (*.png);;JSON Files (*.json)')
        if elecc:
            if elecc.endswith('.png'): self.Imagen(elecc)
            elif elecc.endswith('.json'): self.Json(elecc)
            QMessageBox.information(self, 'Éxito', 'Guardado exitosamente')
    def Imagen(self, ruta):
        image = QImage(centralWidget.vista.viewport().size(), QImage.Format_ARGB32)
        painter = QPainter(image)
        centralWidget.vista.viewport().render(painter)
        painter.end()
        image.save(ruta)
    def get_figura_forma(self, item):
        if isinstance(item, QGraphicsRectItem): return 'rectangulo'
        elif isinstance(item, QGraphicsEllipseItem): return 'circulo'
        elif isinstance(item, QGraphicsPathItem): return 'trapecio'
        elif isinstance(item, QGraphicsPolygonItem): return 'triangulo'
        return 'desconocida'
    def Json(self, ruta):
        data = {"lienzo": {
                "ancho": centralWidget.vista.sceneRect().width(),
                "alto": centralWidget.vista.sceneRect().height()},
            "figuras": []}
        for item in centralWidget.cuadro_grafica.items():
            figura = {"ID": centralWidget.figuras.get(item, 0),
                "forma": self.get_figura_forma(item),
                "color": item.brush().color().name(),
                "x": item.x(),
                "y": item.y(),
                "ancho": item.boundingRect().width(),
                "altura": item.boundingRect().height(),
                "rotacion": item.rotation()}
            data["figuras"].append(figura)
        try:
            with open(ruta, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            QMessageBox.information(self, 'Éxito', 'Guardado exitosamente')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al guardar el archivo: {str(e)}')
    def Cargar(self):
        dialog = QFileDialog()
        dialog.setOption(QFileDialog.ReadOnly, True)
        dialog.setNameFilter("JSON Files (*.json)")
        elecc, _ = dialog.getOpenFileName(self, 'Cargar archivo', '', 'JSON Files (*.json)')
        if elecc:
            try:
                with open(elecc, 'r') as json_file:
                    data = json.load(json_file)# Cargar dimensiones del lienzo
                    lienzo_ancho = data["lienzo"]["ancho"]
                    lienzo_alto = data["lienzo"]["alto"]
                    centralWidget.vista.setSceneRect(0, 0, lienzo_ancho, lienzo_alto)
                    centralWidget.cuadro_grafica.clear()# Cargar figuras
                    centralWidget.figuras.clear()  # Limpiar el diccionario de figuras
                    centralWidget.contador_figura = 0  # Reiniciar el contador de figuras
                    for figura in data["figuras"]:
                        self.recrear_figura(figura)
                QMessageBox.information(self, 'Éxito', 'Archivo cargado exitosamente')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al cargar el archivo: {str(e)}')
    def recrear_figura(self, figura):
        forma = figura["forma"]
        color = QColor(figura["color"])
        x, y = figura["x"], figura["y"]
        ancho, altura = figura["ancho"], figura["altura"]
        rotacion = figura["rotacion"]
        if forma == 'rectangulo': item = QGraphicsRectItem(x, y, ancho, altura)
        elif forma == 'circulo': item = QGraphicsEllipseItem(x, y, ancho, altura)
        elif forma == 'trapecio':
            trapecio_path = QPainterPath()
            trapecio_path.moveTo(x, y)
            trapecio_path.lineTo(x + 100, y)
            trapecio_path.lineTo(x + 75, y + 50)
            trapecio_path.lineTo(x + 25, y + 50)
            trapecio_path.closeSubpath()
            item = QGraphicsPathItem(trapecio_path)
        elif forma == "triangulo":
            triangle_path = QPolygonF()
            triangle_path.append(QPointF(x, y))
            triangle_path.append(QPointF(x + ancho, y))
            triangle_path.append(QPointF(x + ancho / 2, y + altura))
            item = QGraphicsPolygonItem(triangle_path)
        else:
            return # Configurar los flags para que la figura sea movible y seleccionable
        item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemSendsGeometryChanges)
        item.setBrush(QBrush(color))
        item.setPos(x, y)
        item.setRotation(rotacion)# Añadir la figura al diccionario de figuras
        centralWidget.contador_figura += 1
        centralWidget.figuras[item] = centralWidget.contador_figura
        centralWidget.cuadro_grafica.addItem(item)
    def on_rotation_change(self, value):
        if centralWidget.seleccion_forma and centralWidget.selected_item: centralWidget.rotate_figure(centralWidget.selected_item, value)
    def on_size_change(self, value):
        if centralWidget.seleccion_forma and centralWidget.selected_item: centralWidget.resize_figure(centralWidget.selected_item, self.spAncho.value(), self.spAltura.value())
class WorkSpace(QWidget):
    def __init__(self, escalaAncho, escalaAlto):
        super().__init__()
        self.figuras = {}
        self.info_lienzo = {}
        self.figura_copiada = None
        self.selected_item = None
        self.cont = 0
        self.contador_figura = 0  # Asegúrate de que este atributo esté inicializado
        self.selected_color = None
        self.seleccion_forma = None
        self.setMinimumSize(400, 400)
        self.vista = QGraphicsView(self)
        self.cuadro_grafica = QGraphicsScene(self)
        self.vista.setScene(self.cuadro_grafica)
        self.vista.setSceneRect(0, 0, escalaAncho, escalaAlto)
        self.cuadro_grafica.selectionChanged.connect(self.handle_selection_change)
    def copiar_figura(self, item):
        self.figura_copiada = item
        self.copiado_ancho = self.get_figure_size()[0]
        self.copiado_altura = self.get_figure_size()[1]
        self.copiado_color = self.selected_color
        self.copiado_rotacion = item.rotation()
    def pegar_figura(self):
        if self.figura_copiada is not None:
            x , y = 0, 0
            nueva_figura = None
            if isinstance(self.figura_copiada, QGraphicsRectItem): nueva_figura = QGraphicsRectItem(x, y, self.copiado_ancho, self.copiado_altura)
            elif isinstance(self.figura_copiada, QGraphicsEllipseItem): nueva_figura = QGraphicsEllipseItem(x, y, self.copiado_ancho, self.copiado_altura)
            elif isinstance(self.figura_copiada, QGraphicsPathItem): nueva_figura = QGraphicsPathItem(self.figura_copiada.path())
            elif isinstance(self.figura_copiada, QGraphicsPolygonItem): nueva_figura = QGraphicsPolygonItem(self.figura_copiada.polygon())
            if nueva_figura is not None:
                nuevo_id = max(self.figuras.values()) + 1
                self.figuras[nueva_figura] = nuevo_id
                nueva_figura.setPos(x, y)
                nueva_figura.setRotation(self.copiado_rotacion)
                pen = QPen(Qt.black)
                nueva_figura.setPen(pen)
                nueva_figura.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemSendsGeometryChanges)
                self.add_item(nueva_figura)
                colores = int(centralWidget.get_selected_color(self.copiado_color))
                if colores:
                    if colores == 7: nueva_figura.setBrush(Qt.red)
                    elif colores == 12: nueva_figura.setBrush(Qt.yellow)
                    elif colores == 2: nueva_figura.setBrush(Qt.black)
                    elif colores == 3: nueva_figura.setBrush(Qt.white)
                    elif colores == 5: nueva_figura.setBrush(Qt.gray)
                    elif colores == 9: nueva_figura.setBrush(Qt.blue)
                    else: nueva_figura.setBrush(Qt.NoBrush)
                nueva_figura.update()
    def cambia_forma(self, forma):
        self.seleccion_forma = forma
        self.cont = 0
        self.selected_item = None
        panelConfiguracion.spAltura.setValue(0)
        panelConfiguracion.spAncho.setValue(0)
        panelConfiguracion.spRotacion.setValue(0)
        panelConfiguracion.color.setCurrentText("")
        if forma == 'rectangulo': self.add_rectangle(0, 0)
        elif forma == 'cuadrado': self.add_square(0, 0)
        elif forma == 'circulo': self.add_circle(0, 0)
        elif forma == 'trapecio': self.add_trapecio(0, 0)
        elif forma == 'triangulo': self.add_triangle(0, 0)
    def set_selected_color(self, color):
        self.selected_color = color
    def get_figure_size(self):
        item = self.selected_item
        lista = []
        if isinstance(item, QGraphicsRectItem):
            rect = item.rect()
            lista.append(rect.width())
            lista.append(rect.height())
        elif isinstance(item, QGraphicsEllipseItem):
            rect = item.rect()
            lista.append(rect.width())
            lista.append(rect.height())
        elif isinstance(item, QGraphicsPathItem):
            path = item.path()
            points = path.toFillPolygon()
            x_values = [point.x() for point in points]
            y_values = [point.y() for point in points]
            width = max(x_values) - min(x_values)
            height = max(y_values) - min(y_values)
            lista.append(width)
            lista.append(height)
        elif isinstance(item, QGraphicsPolygonItem):
            bounding_rect = item.boundingRect()
            lista.append(bounding_rect.width())
            lista.append(bounding_rect.height())
        else:
            lista.append(0)
            lista.append(0)
        return lista
    def handle_selection_change(self):
        global eje_x
        global eje_y
        selected_items = self.cuadro_grafica.selectedItems()
        self.color_seleccion = self.selected_color
        if selected_items:
            panelConfiguracion.color.setEnabled(True)
            panelConfiguracion.spAltura.setEnabled(True)
            panelConfiguracion.spAncho.setEnabled(True)
            panelConfiguracion.spRotacion.setEnabled(True)
            for item in selected_items:
                self.selected_item = item
                eje_x = self.selected_item.pos().x()
                eje_y = self.selected_item.pos().y()
                panelConfiguracion.spEjeX.setValue(eje_x)
                panelConfiguracion.spEjeY.setValue(eje_y)
                talla = self.get_figure_size()
                panelConfiguracion.spAltura.setValue(talla[1])
                panelConfiguracion.spAncho.setValue(talla[0])
                panelConfiguracion.spRotacion.setValue(int(self.selected_item.rotation()))
                panelConfiguracion.spID.setValue(self.figuras[item])
                codColor=self.selected_item.brush().color()
                print(codColor.name())
                nomColor=self.getColorStr(codColor.name())
                panelConfiguracion.color.setCurrentText(nomColor)
        else:
            self.selected_item = None
            panelConfiguracion.spID.setValue(0)
            panelConfiguracion.spAltura.setValue(0)
            panelConfiguracion.spAncho.setValue(0)
            panelConfiguracion.spRotacion.setValue(0)
            panelConfiguracion.spEjeX.setValue(0)
            panelConfiguracion.spEjeY.setValue(0)
            panelConfiguracion.color.setCurrentIndex(0)
            panelConfiguracion.spID.setValue(0)
            panelConfiguracion.color.setEnabled(False)
            panelConfiguracion.spAltura.setEnabled(False)
            panelConfiguracion.spAncho.setEnabled(False)
            panelConfiguracion.spRotacion.setEnabled(False)
    def getColorStr(self,codigo):
        if(codigo=='#000000'): return ''
        elif (codigo == "#ff0000"): return 'rojo'
        elif (codigo == "#0000ff"): return 'azul'
        elif (codigo == "#ffff00"): return 'amarillo'
        elif (codigo == "#a0a0a4"): return 'gris'
    def add_rectangle(self, x, y):
        global ancho
        global altura
        ancho, altura = 100, 50
        item = QGraphicsRectItem(x, y, ancho, altura)
        self.add_item(item)
    def add_square(self, x, y):
        global ancho
        global altura
        ancho , altura = 100, 100
        item = QGraphicsRectItem(x, y, ancho, altura)
        self.add_item(item)
    def add_circle(self, x, y):
        global ancho
        global altura
        ancho , altura = 100, 100
        item = QGraphicsEllipseItem(x, y, ancho, altura)
        self.add_item(item)
    def add_trapecio(self, x, y):
        global ancho
        global altura
        ancho , altura = 100, 100
        trapecio_path = QPainterPath()
        trapecio_path.moveTo(x, y)
        trapecio_path.lineTo(x + 100, y)
        trapecio_path.lineTo(x + 75, y + 50)
        trapecio_path.lineTo(x + 25, y + 50)
        trapecio_path.closeSubpath()
        item = QGraphicsPathItem(trapecio_path)
        self.add_item(item)
    def add_triangle(self, x, y):
        global ancho
        global altura
        ancho , altura = 100, 100
        triangle_path = QPolygonF()
        triangle_path.append(QPointF(x, y))
        triangle_path.append(QPointF(x + ancho, y))
        triangle_path.append(QPointF(x + ancho / 2, y + altura))
        item = QGraphicsPolygonItem(triangle_path)
        self.add_item(item)
    def add_item(self, item):
        panelConfiguracion.spAltura.setValue(altura)
        panelConfiguracion.spAncho.setValue(ancho)
        panelConfiguracion.spRotacion.setValue(0)
        self.selected_color = None
        item.setBrush(QBrush(self.get_selected_color(panelConfiguracion.color.currentText())))
        pen = QPen(Qt.black)
        item.setPen(pen)
        item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemSendsGeometryChanges)
        self.cont += 1
        self.cuadro_grafica.addItem(item)
        self.contador_figura += 1
        self.figuras[item] = self.contador_figura
    def get_selected_color(self, color_text):
        if color_text:
            if color_text == 'rojo': return Qt.red
            elif color_text == 'azul': return Qt.blue
            elif color_text == 'amarillo': return Qt.yellow
            elif color_text == 'gris': return Qt.gray
            elif color_text == '': return Qt.white
        return Qt.NoBrush
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        for item, item_id in self.figuras.items():
            if item.isUnderMouse():
                eliminar_action = QAction(f'Eliminar figura {item_id}', self)
                eliminar_action.triggered.connect(lambda _, item=item: self.eliminar_figura(item))
                menu.addAction(eliminar_action)
                copiar = QAction(f'Copiar figura {item_id}', self)
                copiar.triggered.connect(lambda _, item=item: self.copiar_figura(item))
                menu.addAction(copiar)
        if self.figura_copiada is not None:
            pegar = QAction(f'Pegar figura', self)
            pegar.triggered.connect(self.pegar_figura)
            menu.addAction(pegar)
        menu.exec_(event.globalPos())
    def eliminar_figura(self, item):
        self.cuadro_grafica.removeItem(item)
        del self.figuras[item]
        self.selected_item = None
    def rotate_figure(self, item, rotation):
        if self.selected_item:
            bounds = item.boundingRect()
            item.setTransformOriginPoint(bounds.x(), bounds.y())
            items = self.cuadro_grafica.selectedItems()
            for item in items:
                item.setRotation(rotation)
    def resize_figure(self, item, width, height):
        if self.selected_item:
            if isinstance(item, QGraphicsRectItem): item.setRect(0, 0, width, height)
            elif isinstance(item, QGraphicsEllipseItem): item.setRect(0, 0, width, height)
            elif isinstance(item, QGraphicsPathItem):
                path = item.path()
                new_points = [QPointF(0, 0),QPointF(width, 0),QPointF(3 * width / 4, height),QPointF(width / 4, height)]
                new_path = QPainterPath()
                new_path.moveTo(new_points[0])
                new_path.lineTo(new_points[1])
                new_path.lineTo(new_points[2])
                new_path.lineTo(new_points[3])
                new_path.closeSubpath()
                item.setPath(new_path)
                self.update()
            elif isinstance(item, QGraphicsPolygonItem):
                new_polygon = QPolygonF()
                new_polygon.append(QPointF(0, 0))
                new_polygon.append(QPointF(width, 0))
                new_polygon.append(QPointF(width / 2, height))
                item.setPolygon(new_polygon)
class DialogEscala(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escala del área")
        self.layout = QVBoxLayout()
        self.ancho_input = QSpinBox()
        self.ancho_input.setRange(100, 1500)
        self.ancho_input.setValue(500)
        self.alto_input = QSpinBox()
        self.alto_input.setRange(100, 1500)
        self.alto_input.setValue(500)
        self.layout.addWidget(QLabel("Ancho:"))
        self.layout.addWidget(self.ancho_input)
        self.layout.addWidget(QLabel("Alto:"))
        self.layout.addWidget(self.alto_input)
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.accept)
        self.layout.addWidget(btn_ok)
        self.setLayout(self.layout)
    def aceptar(self):
        self.alturaEscala = 100 * float(self.caja_altura.text())
        self.anchoEscala = 100 * float(self.caja_ancho.text())
        self.accept()
    def actualiza(self): return self.alto_input.value(), self.ancho_input.value()
    def cancelar(self): self.reject()
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
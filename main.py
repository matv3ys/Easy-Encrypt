import sys
import random
import csv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QTableWidgetItem
from addalphabetdialogue import Ui_Dialog as AddAlphabetDialogue
from rotor_change import Ui_Dialog as RotorChangeDialogue
from reflector_change import Ui_Dialog as ReflectorChangeDialogue
from change_plug import Ui_Dialog as PlugChangeDialogue
from Help import Ui_Dialog as HelpDialogue
from main_window import Ui_MainWindow

# Алфавит по умолчанию

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Класс диалогового окна выбора алфавита

class DialogWindowAddAlphabet(QDialog, AddAlphabetDialogue):
    def __init__(self, mainwindow):
        QDialog.__init__(self)
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.buttonBox.accepted.connect(self.accept_alphabet)
        self.buttonBox.rejected.connect(self.reject_alphabet)

    # Добавление нового алфавита

    def accept_alphabet(self):
        name = self.lineEdit.text()
        alphabet = self.lineEdit_2.text()
        self.mainwindow.add_alphabet(name, alphabet)
        self.close()

    def reject_alphabet(self):
        self.close()


# Класс диалогового окна настройки ротора

class DialogWindowChangeRotor(QDialog, RotorChangeDialogue):
    def __init__(self, mainwindow, rotor, number):
        QDialog.__init__(self)
        self.setupUi(self)
        self.mainwindow = mainwindow
        a, b, c = rotor
        self.lineEdit_perms.setText(a)
        self.lineEdit_turnover.setText(b)
        self.lineEdit_ring_set.setText(c)
        self.number = number

        self.pshb_Random_rotor.clicked.connect(self.random)
        self.buttonBox.accepted.connect(self.accept_rotor)
        self.buttonBox.rejected.connect(self.reject_rotor)

    def random(self):
        a, b, c = random_rotor()
        self.lineEdit_perms.setText(a)
        self.lineEdit_turnover.setText(b)
        self.lineEdit_ring_set.setText(c)

    def accept_rotor(self):
        rotor = self.lineEdit_perms.text(), self.lineEdit_turnover.text(), self.lineEdit_ring_set.text()
        self.mainwindow.rotors[self.number] = rotor
        self.close()

    def reject_rotor(self):
        self.close()


# Класс диалогового окна настройки рефлектора

class DialogWindowChangeReflector(QDialog, ReflectorChangeDialogue):
    def __init__(self, mainwindow, reflector):
        QDialog.__init__(self)
        self.setupUi(self)
        self.mainwindow = mainwindow
        self.lineEdit_Reflector.setText(reflector)

        self.pshb_Random_reflector.clicked.connect(self.random)
        self.buttonBox.accepted.connect(self.accept_reflector)
        self.buttonBox.rejected.connect(self.reject_reflector)

    def random(self):
        self.lineEdit_Reflector.setText(create_reflector())

    def accept_reflector(self):
        self.mainwindow.reflector = self.lineEdit_Reflector.text()
        self.close()

    def reject_reflector(self):
        self.close()


# Класс диалогового окна настройки коммутационной панели

class DialogWindowChangePlug(QDialog, PlugChangeDialogue):
    def __init__(self, mainwindow, plug_board):
        QDialog.__init__(self)
        self.setupUi(self)
        self.mainwindow = mainwindow

        reader = plug_board
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(reader):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))

        self.pshb_Random.clicked.connect(self.random)
        self.buttonBox.accepted.connect(self.accept_reflector)
        self.buttonBox.rejected.connect(self.reject_reflector)

    def random(self):
        reader = create_plug_board(self.mainwindow.len_plug_board)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(reader):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))

    def accept_reflector(self):
        out = []
        for i in range(self.tableWidget.rowCount()):
            row = []
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                if item is not None:
                    row.append(item.text())
            out.append(tuple(row))
        self.mainwindow.plug_board = out
        self.close()

    def reject_reflector(self):
        self.close()


# Класс диалогового окна справки

class DialogWindowHelp(QDialog, HelpDialogue):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        self.close()


# Основное окно программы

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = 'untitled.txt'
        self.saved = False
        self.Open_Conf_Enable = True
        self.used_alphabets = ['Английский']
        self.alphabets = {
                          'Русский': 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                          'Английский': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                          }
        self.len_plug_board = 0
        self.create_elements()

        # Меню файл

        self.action_Create.triggered.connect(self.create_file)
        self.action_Open.triggered.connect(self.open_file)
        self.action_Save.triggered.connect(self.save_file)
        self.action_Save_as.triggered.connect(self.save_as_file)
        self.action_Exit.triggered.connect(self.exit_from_app)

        # Меню конфигурация

        self.action_Rotor1_change.triggered.connect(self.rotor1_change)
        self.action_Rotor2_change.triggered.connect(self.rotor2_change)
        self.action_Rotor3_change.triggered.connect(self.rotor3_change)
        self.action_Reflector_change.triggered.connect(self.reflector_change)
        self.action_Q_plug_board.triggered.connect(self.q_plug_change)
        self.action_Change_plug_board.triggered.connect(self.plug_change)
        self.action_Conf_open.triggered.connect(self.conf_open)
        self.action_Conf_save.triggered.connect(self.conf_save)

        # Меню алфавиты

        self.action_Choose_alphabet.triggered.connect(self.choose_alphabet)
        self.action_Add_alphabet.triggered.connect(self.add_alphabet_dial)

        # Вызов справки

        self.action_Help.triggered.connect(self.help)

        # Шифрование

        self.textEdit.textChanged.connect(self.encrypt)

    # Работа с файлами

    def create_file(self):
        self.saved = False
        self.fname = 'untitled.txt'
        self.textEdit.setText('')

    def open_file(self):
        self.saved = False
        self.fname = QFileDialog.getOpenFileName(self, 'Выберите текстовый документ (.txt)', '')[0]
        if self.fname == '':
            self.fname = 'untitled.txt'
            return
        try:
            with open(self.fname, 'rt') as f:
                text = f.read()
                self.textEdit.setText(text)
            self.label_Status.setText('')
        except:
            self.textEdit.setText('')
            self.label_Status.setText('Статус: Error encoding')

    def save_file(self):
        if self.saved:
            text = self.Encrypted.toPlainText()
            f = open(self.fname, 'w')
            f.write(text)
            f.close()
        else:
            self.save_as_file()

    def save_as_file(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'TXT (*.txt)')[0]
        if fname == '':
            return
        self.fname = fname
        self.saved = True
        text = self.Encrypted.toPlainText()
        f = open(self.fname, 'w')
        f.write(text)
        f.close()

    def exit_from_app(self):
        self.close()

    # Работа с конфигурацией машины

    def rotor1_change(self):
        rotor = self.rotors[0]
        DialogWindowChangeRotor_inst = DialogWindowChangeRotor(self, rotor, 0)
        DialogWindowChangeRotor_inst.show()
        DialogWindowChangeRotor_inst.exec()

    def rotor2_change(self):
        rotor = self.rotors[1]
        DialogWindowChangeRotor_inst = DialogWindowChangeRotor(self, rotor, 1)
        DialogWindowChangeRotor_inst.show()
        DialogWindowChangeRotor_inst.exec()

    def rotor3_change(self):
        rotor = self.rotors[2]
        DialogWindowChangeRotor_inst = DialogWindowChangeRotor(self, rotor, 2)
        DialogWindowChangeRotor_inst.show()
        DialogWindowChangeRotor_inst.exec()

    def reflector_change(self):
        reflector = self.reflector
        DialogWindowChangeReflector_inst = DialogWindowChangeReflector(self, reflector)
        DialogWindowChangeReflector_inst.show()
        DialogWindowChangeReflector_inst.exec()

    def q_plug_change(self):
        text = f'Текущее число подключений: {self.len_plug_board}'
        i, okBtnPressed = QInputDialog.getText(self, "Количество подключений",
                                               text)
        if okBtnPressed:
            try:
                i = int(i)
                if 1 <= i <= len(alphabet) // 2:
                    if i == self.len_plug_board:
                        return
                    else:
                        self.len_plug_board = i
                        self.plug_board = create_plug_board(self.len_plug_board)
                else:
                    return
            except:
                return

    def plug_change(self):
        plug_board = self.plug_board
        DialogWindowChangePlug_inst = DialogWindowChangePlug(self, plug_board)
        DialogWindowChangePlug_inst.show()
        DialogWindowChangePlug_inst.exec()

    def conf_open(self):
        global alphabet
        del self.plug_board
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл с конфигурацией', '', 'CSV (*.csv)')[0]
        if fname == '':
            return
        if self.Open_Conf_Enable:
            self.Open_Conf_Enable = False
            self.action_Conf_open.setEnabled(False)
        with open(fname, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            data = list(reader)
            self.rotors[0] = data[0][1], data[0][2], data[0][3]
            self.rotors[1] = data[1][1], data[1][2], data[1][3]
            self.rotors[2] = data[2][1], data[2][2], data[2][3]
            self.reflector = data[3][1]
            self.len_plug_board = data[4][1]
            try:
                board = data[4][2]
                board = [(board[i * 2], board[i * 2 + 1]) for i in range(0, len(board) // 2)]
                self.plug_board = board
            except:
                self.plug_board = []
            alphabet = data[5][0]

    def conf_save(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранить конфигурацию машины', '', 'CSV (*.csv)')[0]
        if fname == '':
            return
        with open(fname, "w", newline="") as file:
            zip = self.plug_board
            zip = [list(i) for i in zip]
            zip = ''.join(sum(zip, []))
            table = [['Rotor 1', self.rotors[0][0], self.rotors[0][1], self.rotors[0][2]],
                     ['Rotor 2', self.rotors[1][0], self.rotors[1][1], self.rotors[1][2]],
                     ['Rotor 3', self.rotors[2][0], self.rotors[2][1], self.rotors[2][2]],
                     ['Reflector', self.reflector],
                     ['PlugBoard', self.len_plug_board, zip],
                     [alphabet]]
            file.truncate()
            writer = csv.writer(file)
            for row in table:
                writer.writerow(row)

    # Работа с алфавитами (на стадии тестирования)

    def choose_alphabet(self):
        global alphabet
        alphabets = list(self.alphabets.keys())
        choice = tuple([item for item in alphabets if item not in self.used_alphabets])

        i, okBtnPressed = QInputDialog.getItem(self, "Выбор алфавита",
                                               "Выберите алфавит:",
                                               choice,
                                               1, False)
        if okBtnPressed:
            alphabet = self.alphabets[i]
            self.used_alphabets.append(i)
            self.create_elements()
        if len(alphabets) == len(self.used_alphabets):
            self.action_Choose_alphabet.setEnabled(False)

    def add_alphabet_dial(self):
        DialogWindowAddALphabet_inst = DialogWindowAddAlphabet(self)
        DialogWindowAddALphabet_inst.show()
        DialogWindowAddALphabet_inst.exec()

    def add_alphabet(self, name, alphabet):
        if len(alphabet) % 2 == 0 and len(alphabet) != 0:
            self.alphabets[name] = alphabet
            self.action_Choose_alphabet.setEnabled(True)
        else:
            return

    # Вызов справки

    def help(self):
        DialogWindowHelp_inst = DialogWindowHelp()
        DialogWindowHelp_inst.show()
        DialogWindowHelp_inst.exec()

    # Cочетания клавиш

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_S:
                self.save_as_file()
            if event.key() == Qt.Key_O:
                self.open_file()

    # Работа с машиной

    def create_elements(self):
        self.rotors = [random_rotor(), random_rotor(), random_rotor()]
        self.reflector = create_reflector()
        self.plug_board = create_plug_board(self.len_plug_board)

    def encrypt(self):
        if self.Open_Conf_Enable:
            self.Open_Conf_Enable = False
            self.action_Conf_open.setEnabled(False)
        self.machine = Machine(self.rotors, self.reflector, self.plug_board)
        text = self.textEdit.toPlainText()
        text = self.machine.encrypt(text)
        self.Encrypted.setText(text)
        del self.machine


# Класс ротора машины

class Rotor:
    perms = []
    turnover_position = ''

    def __init__(self, perms, turnover_position, ring_setting):
        self.position = alphabet[0]
        i = alphabet.index(ring_setting)
        perms = perms[i:] + perms[:i]
        self.perms = [c for c in perms]
        self.turnover_position = turnover_position

    def set_position(self, position):
        position_change = alphabet.index(position) - alphabet.index(self.position)
        self.position = position
        self.perms = self.perms[position_change:] + self.perms[:position_change]

    def turnover(self):
        return True if self.turnover_position == self.position else False

    def step(self):
        turnover = self.turnover()
        self.perms = self.perms[1:] + self.perms[:1]
        self.position = alphabet[(alphabet.index(self.position) + 1) % len(alphabet)]
        if turnover:
            return True
        else:
            return False

    def encrypt_forward(self, c):
        return self.perms[alphabet.index(c)]

    def encrypt_backward(self, c):
        return alphabet[self.perms.index(c)]


# Класс рефлектора машины

class Reflector:
    def __init__(self, pairs):
        self.pairs = {}
        for i, c in enumerate(alphabet):
            self.pairs[c] = pairs[i]

    def reflect(self, c):
        return self.pairs[c]


# Класс машины

class Machine:
    rotors = []
    reflector = None
    plug_board = {}
    double_step = False

    def __init__(self, rotors, reflector, plug_board):
        self.rotors = [Rotor(rotor[0], rotor[1], rotor[2]) for rotor in rotors]
        self.reflector = Reflector(reflector)
        for pair in plug_board:
            self.plug_board[pair[0]], self.plug_board[pair[1]] = pair[1], pair[0]

    def set_rotors(self, positions):
        if len(positions) != len(self.rotors):
            print('Error: rotor settings do not match with number of rotors')
        else:
            [rotor.set_position(positions[i]) for i, rotor in enumerate(self.rotors)]
        return

    def encrypt_char(self, c):
        c = self.plug_board[c] if c in self.plug_board else c
        for i, rotor in enumerate(self.rotors[::-1]):
            if i is 0:
                c = rotor.encrypt_forward(c)
            else:
                difference = (alphabet.index(self.rotors[::-1][i - 1].position) - alphabet.index(
                    self.rotors[::-1][i].position)) % len(alphabet)
                c = rotor.encrypt_forward(alphabet[alphabet.index(c) - difference])
        c = self.reflector.reflect(c)
        for i, rotor in enumerate(self.rotors):
            if i is 0:
                c = rotor.encrypt_backward(c)
            else:
                difference = (alphabet.index(self.rotors[i - 1].position) - alphabet.index(
                    self.rotors[i].position)) % len(alphabet)
                c = rotor.encrypt_backward(alphabet[alphabet.index(c) - difference])
        c = self.plug_board[c] if c in self.plug_board else c
        return c

    def status(self):
        return self.rotors[0].position + self.rotors[1].position + self.rotors[2].position

    def step(self):
        if self.double_step:
            self.rotors[1].step()
            self.rotors[0].step()
            self.double_step = False
        if self.rotors[2].step():
            self.rotors[1].step()
            if self.rotors[1].turnover():
                self.double_step = True

    def encrypt(self, s):
        global alphabet
        out = ''
        for c in s:
            if c.upper() in alphabet:
                self.step()
                if c.isupper():
                    out += self.encrypt_char(c)
                else:
                    c = c.upper()
                    out += self.encrypt_char(c).lower()
            else:
                out += c
        return out


# получить случайный ротор

def random_rotor():
    global alphabet
    rotor = list(alphabet)
    turnover_position = random.choice(rotor)
    ring_setting = random.choice(rotor)
    random.shuffle(rotor)
    rotor = ''.join(rotor)
    rotor = (rotor, turnover_position, ring_setting)
    return rotor


# получить случайный рефлектор

def create_reflector():
    global alphabet
    out = ['_'] * len(alphabet)

    for i in range(len(out)):
        if out[i] == '_':
            indexes = []
            for j in range(i + 1, len(out)):
                if out[j] == '_':
                    indexes.append(j)
            new_index = random.choice(indexes)
            out[i], out[new_index] = alphabet[new_index], alphabet[i]
        else:
            continue

    return ''.join(out)


# создать коммутационную панель

def create_plug_board(quantity):
    global alphabet
    try:
        quantity = int(quantity)
    except:
        return False
    if 0 <= quantity <= 13:
        letters = list(alphabet)
        random.shuffle(letters)
        letters = letters[:quantity * 2]
        plug_board = [(letters[i], letters[i + 1]) for i in range(0, quantity * 2, 2)]
        return plug_board
    else:
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QPushButton
)


class EditProfile(QWidget):
    def __init__(self, profile, manager):
        super().__init__()

        self.profile = profile
        self.manager = manager

        self.setWindowTitle(
            "Editar Perfil"
        )

        self.setGeometry(
            400,
            250,
            400,
            300
        )


        layout = QVBoxLayout()


        titulo = QLabel(
            "Editar Perfil"
        )


        self.nome = QLineEdit(
            profile["name"]
        )


        self.sensibilidade = QSpinBox()

        self.sensibilidade.setMinimum(1)
        self.sensibilidade.setMaximum(200)

        self.sensibilidade.setValue(
            profile["sensitivity"]
        )


        salvar = QPushButton(
            "Salvar"
        )


        salvar.clicked.connect(
            self.salvar
        )


        layout.addWidget(titulo)
        layout.addWidget(
            QLabel("Nome:")
        )
        layout.addWidget(
            self.nome
        )

        layout.addWidget(
            QLabel("Sensibilidade:")
        )

        layout.addWidget(
            self.sensibilidade
        )

        layout.addWidget(
            salvar
        )


        self.setLayout(
            layout
        )



    def salvar(self):

        self.profile["name"] = (
            self.nome.text()
        )

        self.profile["sensitivity"] = (
            self.sensibilidade.value()
        )


        self.manager.save()


        self.close()
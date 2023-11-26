from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilenames
from tkinter.simpledialog import askfloat, askstring
from tkinter import Tk, Button
from tkinter import filedialog
import os


class Proyecto:
    
    
    
    def __init__(self, master):
        
        self.frame = Frame(master)
        self.master.title("Mi Aplicación")

        self.archivo = 0
        self.cadena = ""
        self.posicion = 0
        self.word = ""

        self.palabraReservada = 0
        self.identificador = 0
        self.operadorRelacional = 0
        self.operadorLogico = 0
        self.operadorAritmetico = 0
        self.asignacion = 0
        self.entero = 0
        self.decimal = 0
        self.cadenaCaracteres = 0
        self.comentarioMulti = 0
        self.comentarioLinea = 0
        self.parentesis = 0
        self.llaves = 0
        self.error = 0
        
        
        
        master.configure(bg="lightgray")
        master.geometry("770x300")
        

        self.reservado = ["if","else","switch","case","default","for","while","break","int","String","double","char","print"]
        
        self.frame = Frame(self.master)
        self.frame.pack()
        self.texto = Text(master, wrap="none", undo=True)
        self.texto.pack(expand=YES, fill=BOTH)
        self.scrollX = Scrollbar(master, orient="horizontal", command=self.texto.xview)
        self.scrollX.pack(side=BOTTOM, fill=X)
        self.scrollY = Scrollbar(master, orient="vertical", command=self.texto.yview)
        self.scrollY.pack(side=RIGHT, fill=Y)
        self.texto.configure(xscrollcommand=self.scrollX.set, yscrollcommand=self.scrollY.set)

        # Añadir botón para guardar cambios en el archivo
        self.btnGuardar = Button(master, text="Guardar Cambios", command=self.guardarArchivo)
        self.btnGuardar.pack(side=TOP, fill=X)
        
        self.btnEvaluar = Button(text="Evaluar", command=self.evaluar)
        self.btnEvaluar.pack()
        self.btnEvaluar.place(x=60, y=50, width=130, height=60)
        self.btnEvaluar.config(font=("Arial", 11), fg="black", bg="green")
        # Configurando el widget de texto para mostrar y editar contenido
        self.text_widget = Text(master, wrap="none")
        self.scroll_x = Scrollbar(master, orient="horizontal", command=self.text_widget.xview)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(master, command=self.text_widget.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text_widget.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        
        self.texto = Text(root)
        self.texto.pack()
        self.texto.place(x=0, y=0, width=1, height=1)

        # Botón para cargar archivo de texto
        self.load_button = Button(master, text="Cargar Archivo", command=self.load_file)
        self.load_button.pack(side=TOP, fill=X)

        # Botón para guardar el texto modificado
        self.save_button = Button(master, text="Guardar", command=self.save_text)
        self.save_button.pack(side=TOP, fill=X)
        
        self.lblReservada = Label(text="Palabras Reservadas : 0")
        self.lblReservada.pack()
        self.lblReservada.place(x=220, y=50)
        self.lblReservada.config(font=("Arial", 14), fg="blue")

        
        self.lblIdentificador = Label(text="Identificadores : 0")
        self.lblIdentificador.pack()
        self.lblIdentificador.place(x=220, y=75)
        self.lblIdentificador.config(font=("Arial", 14), fg="blue")

       
        self.lblRelacional = Label(text="Operadores Relacionales : 0")
        self.lblRelacional.pack()
        self.lblRelacional.place(x=220, y=100)
        self.lblRelacional.config(font=("Arial", 14), fg="blue")

      
        self.lblLogico = Label(text="Operadores Logicos : 0")
        self.lblLogico.pack()
        self.lblLogico.place(x=220, y=125)
        self.lblLogico.config(font=("Arial", 14), fg="blue")

       
        self.lblAritmetico = Label(text="Operadores Aritmeticos : 0")
        self.lblAritmetico.pack()
        self.lblAritmetico.place(x=220, y=150)
        self.lblAritmetico.config(font=("Arial", 14), fg="blue")

       
        self.lblAsignacion = Label(text="Asignaciones : 0")
        self.lblAsignacion.pack()
        self.lblAsignacion.place(x=220, y=175)
        self.lblAsignacion.config(font=("Arial", 14), fg="blue")

        
        self.lblEntero = Label(text="Numeros Enteros : 0")
        self.lblEntero.pack()
        self.lblEntero.place(x=220, y=200)
        self.lblEntero.config(font=("Arial", 14), fg="blue")

        
        self.lblDecimal = Label(text="Numero Decimales : 0")
        self.lblDecimal.pack()
        self.lblDecimal.place(x=470, y=50)
        self.lblDecimal.config(font=("Arial", 14), fg="blue")

        
        self.lblCadena = Label(text="Cadena de Caracteres : 0")
        self.lblCadena.pack()
        self.lblCadena.place(x=470, y=75)
        self.lblCadena.config(font=("Arial", 14), fg="blue")

        
        self.lblMultilinea = Label(text="Comentario Multilinea : 0")
        self.lblMultilinea.pack()
        self.lblMultilinea.place(x=470, y=100)
        self.lblMultilinea.config(font=("Arial", 14), fg="blue")

       
        self.lblLinea = Label(text="Comentario de Linea : 0")
        self.lblLinea.pack()
        self.lblLinea.place(x=470, y=125)
        self.lblLinea.config(font=("Arial", 14), fg="blue")

        
        self.lblParentesis = Label(text="Parentesis : 0")
        self.lblParentesis.pack()
        self.lblParentesis.place(x=470, y=150)
        self.lblParentesis.config(font=("Arial", 14), fg="blue")

       
        self.lblLlave = Label(text="Llaves : 0")
        self.lblLlave.pack()
        self.lblLlave.place(x=470, y=175)
        self.lblLlave.config(font=("Arial", 14), fg="blue")

       
        self.lblError = Label(text="Errores : 0")
        self.lblError.pack()
        self.lblError.place(x=470, y=200)
        self.lblError.config(font=("Arial", 14), fg="blue")

        self.btnCargar = Button(text="Cargar Archivo de Texto", command=self.abrirArchivo)
        self.btnCargar.pack()
        self.btnCargar.place(x=30, y=120, width=180, height=60)
        self.btnCargar.config(font=("Arial", 11), fg="black", bg="green")
        
    
    def abrirArchivo(self):
        ruta_archivo = tkinter.filedialog.askopenfilename(title="Seleccione un archivo")
        if ruta_archivo:
            with open(ruta_archivo, "r") as file_object:
                contenido = file_object.read()
                self.texto.delete('1.0', END)  # Limpiar el widget de texto
                self.texto.insert('1.0', contenido)  # Insertar el contenido del archivo
                self.ruta_archivo_actual = ruta_archivo  # Guardar la ruta del archivo

    def guardarArchivo(self):
        contenido = self.texto.get('1.0', END)
        with open(self.ruta_archivo_actual, "w") as file_object:
            file_object.write(contenido)  # Guardar el contenido actual del widget de texto en el archivo
            


    
    self.frame.pack()
    #La función q1 es parte de un programa o una máquina de estados finitos (FSM) que procesa una cadena de caracteres.
    def q1(self):
        #print("q1")
        #Comprueba si la posi-(self.posicion) es igual a la longitud de la cadena (len(self.cadena)). Si es así, 
        # incrementa el contador de errores (self.error) en 1
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Si el carácter actual (self.cadena[self.posicion]) es un espacio, un salto de línea o una tabulación, incrementa la posición en 1 
        #(self.posicion += 1), incrementa el contador de errores en 1 (self.error += 1), y retorna el valor "q0", indicando que se debe pasar 
        #al estado q0.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si ninguna de las condiciones anteriores se cumple, incrementa la posición en 1 (self.posicion += 1) y retorna el valor "q1", 
        #indicando que se debe permanecer en el estado q1.
        else:
            self.posicion += 1
            return "q1"

    def load_file(self):
        file_path = askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_widget.delete(1.0, END)
                self.text_widget.insert(1.0, file.read())
            self.master.title(f"Editor de Texto Similar a JTextArea - {file_path}")

    def save_text(self):
        file_path = askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, END))
            self.master.title(f"Editor de Texto Similar a JTextArea - {file_path}")

    def qParentesis(self):
        #print("qParentesis")
        #Comprueba si la posición actual (self.posicion) es igual a la longitud de la cadena (len(self.cadena)). Si es así,
        #incrementa el contador de paréntesis (self.parentesis) en 1 
        if self.posicion == len(self.cadena):
            #self.posicion += 1
            self.parentesis += 1
            return "end"
        #Si el carácter actual (self.cadena[self.posicion]) es un espacio, un salto de línea o una tabulación, incrementa la posición en 1
        #(self.posicion += 1), incrementa el contador de paréntesis en 1 (self.parentesis += 1), y retorna el valor "q0", indicando que se debe pasar al estado q0.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.parentesis += 1
            return "q0"
        #Si ninguna de las condiciones anteriores se cumple, incrementa la posición en 1 (self.posicion += 1) y retorna el valor "q1", 
        #indicando que se debe permanecer en el estado q1.
        else:
            self.posicion += 1
            return "q1"
        
    def qLlave(self):
        #print("qLlave")
        #Comprueba si la posición actual (self.posicion) es igual a la longitud de la cadena (len(self.cadena)). Si es así, 
        #incrementa el contador de llaves y devuelve la cadena "end".
        if self.posicion == len(self.cadena):
            self.llaves += 1
            return "end"
        #Si el carácter en la posición actual de la cadena es un espacio, un salto de línea o una tabulación, incrementa self.posicion
        #y el contador de llaves, y devuelve la cadena "q0".
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.llaves += 1
            return "q0"
        #Si ninguno de los casos anteriores se cumple, incrementa self.posicion y devuelve la cadena "q1".
        else:
            self.posicion += 1
            return "q1"

    def qAritmetico2(self):
        #print("qAritmetico2")
        #Comprueba si la posición actual (self.posicion) es igual a la longitud de la cadena (len(self.cadena)). Si es así, incrementa el contador de operadorAritmetico y devuelve la cadena "end".
        if self.posicion == len(self.cadena):
            self.operadorAritmetico += 1
            return "end"
        #Si el carácter en la posición actual de la cadena es un espacio, un salto de línea o una tabulación, incrementa self.posicion y el contador de operadorAritmetico, y devuelve la cadena "q0".
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.operadorAritmetico += 1
            return "q0"
        #Si el carácter en la posición actual de la cadena es "/", incrementa self.posicion y devuelve la cadena "qComent".
        elif self.cadena[self.posicion] == "/":
            self.posicion += 1
            return "qComent"
        #Si el carácter en la posición actual de la cadena es "*", incrementa self.posicion y llama a la función qMulti(). El resultado de qMulti() se devuelve.
        elif self.cadena[self.posicion] == "*":
            self.posicion += 1
            return self.qMulti()
        #Si ninguno de los casos anteriores se cumple, incrementa self.posicion y devuelve la cadena "q1".
        else:
            self.posicion += 1
            return "q1"

    def qComent(self):
        #Comprueba si la posición actual (self.posicion) es igual a la longitud de la cadena (len(self.cadena)). Si es así, incrementa el contador de comentarioLinea y devuelve la cadena "end".
        if self.posicion == len(self.cadena):
            self.comentarioLinea += 1
            return "end"
        #Si el carácter en la posición actual de la cadena es un espacio, un salto de línea o una tabulación, incrementa self.posicion y el contador de comentarioLinea, y devuelve la cadena "q0".
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.comentarioLinea += 1
            return "q0"
        #Si ninguno de los casos anteriores se cumple, incrementa self.posicion y devuelve la cadena "qComent".
        else:
            self.posicion += 1
            return "qComent"

    def qMulti(self):
        #print("qMulti")
        #Si self.posicion (la posición actual en la cadena) es igual a la longitud de la cadena (len(self.cadena)), significa que se ha alcanzado el final de la cadena y no hay más caracteres para procesar. En este caso, se incrementa el contador de errores (self.error) y se devuelve el estado "end" para indicar que el análisis ha finalizado.
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Si el carácter actual es un espacio en blanco (" ") o una tabulación ("\t"), se incrementa self.error y se avanza a la siguiente posición (self.posicion += 1). Luego se devuelve el estado "q0", que parece ser otro estado del autómata.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si el carácter actual es un asterisco ("*"), se incrementa self.posicion y se llama a un método llamado qAsterisco. Es probable que qAsterisco represente otro estado del autómata relacionado con el procesamiento de un asterisco.
        elif self.cadena[self.posicion] == "*":
            self.posicion += 1
            return self.qAsterisco()
        #Si no se cumple ninguna de las condiciones anteriores, se incrementa self.posicion y se devuelve el estado actual "qMulti". Esto indica que se continúa en el mismo estado para procesar el siguiente carácter de la cadena.
        else:
            self.posicion += 1
            return "qMulti"
        
    def qAsterisco(self):
        #print("qAsterisco")
        #Si self.posicion es igual a la longitud de la cadena (len(self.cadena)), se ha alcanzado el final de la cadena. En este caso, se incrementa el contador de errores (self.error) y se devuelve el estado "end" para indicar que el análisis ha finalizado.
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Si el carácter actual es un espacio en blanco (" "), un salto de línea ("\n"), o una tabulación ("\t"), se incrementa self.posicion y self.error. Luego se devuelve el estado "q0", que parece ser otro estado del autómata
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si el carácter actual es un asterisco ("*"), se incrementa self.posicion y se devuelve el estado actual "qAsterisco". Esto indica que se continúa en el mismo estado para procesar el siguiente carácter de la cadena.
        elif self.cadena[self.posicion] == "*":
            self.posicion += 1
            return "qAsterisco"
        #Si el carácter actual es una barra diagonal ("/"), se incrementa self.posicion y se llama a un método llamado qFinCom.
        elif self.cadena[self.posicion] == "/":
            self.posicion += 1
            return self.qFinCom()
        #Si no se cumple ninguna de las condiciones anteriores, se incrementa self.posicion y se devuelve el estado "qMulti". Esto indica que se regresa al estado anterior "qMulti" para continuar procesando la cadena.
        else:
            self.posicion += 1
            return "qMulti"
    
    def qFinCom(self):
        #print("qFinCom")
        #i self.posicion es igual a la longitud de la cadena (len(self.cadena)), se ha alcanzado el final de la cadena. En este caso, se incrementa self.comentarioMulti
        if self.posicion == len(self.cadena):
            self.comentarioMulti += 1
            return "end"
        #Si el carácter actual es un espacio en blanco (" "), un salto de línea ("\n"), o una tabulación ("\t"), se incrementa self.posicion y self.comentarioMulti. Esto indica que se continúa en el estado "q0",
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.comentarioMulti += 1
            return "q0"
        #Si no se cumple ninguna de las condiciones anteriores, es decir, si el carácter actual no es un espacio en blanco, salto de línea o tabulación, se incrementa self.posicion y se devuelve el estado "q1". Esto indica que se pasa al estado "q1" para continuar procesando la cadena.
        else:
            self.posicion += 1
            return "q1"
        
    def qAritmetico(self):
        #print("qAritmetico")
        #Si self.posicion es igual a la longitud de la cadena (len(self.cadena)), se ha alcanzado el final de la cadena. En este caso, se incrementa self.operadorAritmetico
        if self.posicion == len(self.cadena):
            self.operadorAritmetico += 1
            return "end"
        #Si el carácter actual es un espacio en blanco (" "), un salto de línea ("\n"), o una tabulación ("\t"), se incrementa self.posicion y self.operadorAritmetico. Esto indica que se continúa en el estado "q0"
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.operadorAritmetico += 1
            return "q0"
        #i no se cumple ninguna de las condiciones anteriores, es decir, si el carácter actual no es un espacio en blanco, salto de línea o tabulación, se incrementa self.posicion y se devuelve el estado "q1". Esto indica que se pasa al estado "q1" para continuar procesando la cadena.
        else:
            self.posicion += 1
            return "q1"
        
    def qIdentificador(self):
        #print("qIdentificador")
        
        #Se agrega el último carácter de la cadena (self.cadena[self.posicion-1]) a self.word. Esto se hace para asegurarse de que se capture el último carácter de un identificador o palabra clave antes de finalizar el análisis.
        if self.posicion == len(self.cadena):
            self.word += self.cadena[self.posicion-1]
           #Se verifica si self.word está en la lista self.reservado. La lista self.reservado parece contener palabras reservadas del lenguaje. Si self.word está en la lista de palabras reservadas, se incrementa self.palabraReservada. Esto indica que se ha encontrado una palabra reservada.
            if self.word in self.reservado:
                self.palabraReservada += 1
           #Si self.word no está en la lista de palabras reservadas, se incrementa self.identificador. Esto indica que se ha encontrado un identificador.
            else:
                self.identificador += 1
            #Finalmente, se devuelve el estado "end". Esto indica que el análisis ha finalizado y se debe salir del autómata o proceso de análisis.          
            return "end"
        #Si el carácter actual es un espacio en blanco (" "), un salto de línea ("\n"), o una tabulación ("\t"), se incrementa self.posicion y self.operadorAritmetico. Esto indica que se continúa en el estado "q0", 
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
           #Se incrementa self.posicion en 1 para avanzar a la siguiente posición de la cadena.
            self.posicion += 1
            #Se verifica si self.word está en la lista self.reservado. Si self.word está en la lista de palabras reservadas, se incrementa self.palabraReservada en 1. Esto indica que se ha encontrado una palabra reservada en el código fuente.
            if self.word in self.reservado:
                self.palabraReservada += 1
            #Si self.word no está en la lista de palabras reservadas, se incrementa self.identificador en 1. Esto indica que se ha encontrado un identificador en el código fuente.
            else:
                self.identificador += 1
            #Se reinicia self.word a una cadena vacía para comenzar a construir un nuevo identificador.
            self.word = ""
            #Por último, se devuelve el estado "q0".
            return "q0"
        #Se concatena el carácter actual (self.cadena[self.posicion]) a self.word. Esto se realiza para construir el identificador actual, ya que se ha encontrado un carácter válido que forma parte del identificador.
        elif self.cadena[self.posicion].isalnum() or self.cadena[self.posicion] == "_":
            self.word += self.cadena[self.posicion]
            #Se incrementa self.posicion en 1 para avanzar a la siguiente posición de la cadena.
            self.posicion += 1
            #Se devuelve el estado "qIdentificador".
            return "qIdentificador"
        #En este bloque de código se maneja el caso en el que el carácter actual en la posición self.posicion de la cadena no cumple con las condiciones anteriores
        else:
            #Se incrementa self.posicion en 1 para avanzar a la siguiente posición de la cadena.
            self.posicion += 1
            #Se reinicia el contenido de self.word a una cadena vacía. Esto se hace porque el carácter actual no forma parte del identificador en construcción, por lo tanto, se reinicia 
            self.word = ""
            #Se devuelve el estado "q1
            return "q1"
        
    def qOrelacional(self):
        #print("qOrelacional")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, significa que se ha completado el análisis y se incrementa el contador self.operadorRelacional para contar el operador relacional encontrado
        if self.posicion == len(self.cadena):
            self.operadorRelacional += 1
            return "end"
        
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.posicion en 1 para avanzar a la siguiente posición y se incrementa self.operadorRelacional para contar el operador relacional encontrado. Luego, se devuelve el estado "q0" para continuar el análisis desde ese punto.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.operadorRelacional += 1
            return "q0"
        #Si el carácter actual es un signo igual ("="), se incrementa self.posicion en 1 y se devuelve el resultado de la función qOrelacional2(). Esto indica que se ha encontrado un operador relacional seguido de un igua
        elif self.cadena[self.posicion] == "=":
            self.posicion += 1
            return self.qOrelacional2()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve el estado "q1".
        else:
            self.posicion += 1
            return "q1"
        
    def qOrelacional2(self):
        #print("qOrelacional2")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.operadorRelacional para contar el operador relacional encontrado
        if self.posicion == len(self.cadena):
            self.operadorRelacional += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.operadorRelacional y se devuelve el estado "q0". Esto indica que se ha encontrado un operador relacional válido seguido de un espacio en blanco, una nueva línea o un tabulador, y se debe continuar el análisis desde ese punto.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.operadorRelacional += 1
            return "q0"
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve el estado "q1"
        else:
            self.posicion += 1
            return "q1"
        
    def qAdmiracion(self):
        #print("qAdmiracion")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.operadorLogico para contar el operador lógico encontrado y se devuelve el estado
        if self.posicion == len(self.cadena):
            self.operadorLogico += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.operadorLogico y se devuelve el estado "q0". Esto indica que se ha encontrado un operador lógico válido seguido de un espacio en blanco, una nueva línea o un tabulador, y se debe continuar el análisis desde ese punto.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.operadorLogico += 1
            return "q0"
        #Si el carácter actual en la posición self.posicion es "=", se incrementa self.posicion en 1 y se devuelve el resultado de la función qOrelacional2(). Esto indica que se ha encontrado el operador de negación lógica seguido de "=", y se debe continuar el análisis para reconocer un posible operador relacional.
        elif self.cadena[self.posicion] == "=":
            self.posicion += 1
            return self.qOrelacional2()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve el estado "q1". 
        else:
            self.posicion += 1
            return "q1"
        
    def qigual(self):
        #print("Asignacion")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.operadorLogico para contar el operador lógico encontrado y se devuelve el estado 
        if self.posicion == len(self.cadena):
            self.asignacion += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.operadorLogico y se devuelve el estado "q0". 
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.asignacion += 1
            return "q0"
        #Si el carácter actual en la posición self.posicion es "=", se incrementa self.posicion en 1 y se devuelve el resultado de la función qOrelacional2(). Esto indica que se ha encontrado el operador de negación lógica seguido de "=", y se debe continuar el análisis para reconocer un posible operador relacional.
        elif self.cadena[self.posicion] == "=":
            self.posicion += 1
            return self.qOrelacional2()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve el estado "q1"
        else:
            self.posicion += 1
            return "q1"
        
    def qAmperson(self):
        #print("qAmperson")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.operadorLogico para contar el operador lógico encontrado y se devuelve el estado
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.operadorLogico y se devuelve el estado "q0"
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si el carácter actual en la posición self.posicion es "&", se incrementa self.posicion en 1 y se devuelve el resultado de la función qOrelacional2(). Esto indica que se ha encontrado el operador de negación lógica seguido de "=", y se debe continuar el análisis para reconocer un posible operador relacional.
        elif self.cadena[self.posicion] == "&":
            self.posicion += 1
            return self.qlogico()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve el estado "q1".
        else:
            self.posicion += 1
            return "q1"
        
    def qlogico(self):
        #print("qOlogico")
        #e verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.operadorLogico para contar el operador lógico encontrado y se devuelve el estado
        if self.posicion == len(self.cadena):
            self.operadorLogico += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.operadorLogico y self.posicion en 1, y se devuelve el estado "q0". Esto indica que se ha encontrado un operador lógico seguido de un espacio en blanco, una nueva línea o un tabulador, y se debe continuar el análisis desde ese punto.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.operadorLogico += 1
            return "q0"
        #Si ninguna de las condiciones anteriores se cumple, se devuelve el estado "q1".
        else:
            return "q1"
        
    def qBarra(self):
        #print("qBarra")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.error para contar el error encontrado y se devuelve el estado
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.error y self.posicion en 1, y se devuelve el estado "q0". Esto indica que se ha encontrado una barra seguida de un espacio en blanco, una nueva línea o un tabulador, y se debe continuar el análisis desde ese punto.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si el carácter actual en la posición self.posicion es un carácter de barra vertical (|), se incrementa self.posicion en 1 y se devuelve el estado "qOlogico". Esto indica que se ha encontrado una barra seguida de una barra vertical, lo cual puede indicar un operador lógico específico. Se procede a analizar el siguiente carácter a partir de ese punto.
        elif self.cadena[self.posicion] == "|":
            self.posicion += 1
            return self.qlogico()
        #Si ninguna de las condiciones anteriores se cumple, se devuelve el estado "q1"
        else:
            self.posicion += 1
            return "q1"
        
    def qNum(self):
        #print("qNum")
        #Se verifica si se ha alcanzado el final de la cadena (self.posicion == len(self.cadena)). En caso afirmativo, se incrementa self.error para contar el error encontrado y se devuelve el estado
        if self.posicion == len(self.cadena):
            self.entero += 1
            return "end"
        #Se verifica si el carácter actual en la posición self.posicion es un espacio, una nueva línea o un tabulador (" ", "\n", "\t"). En caso afirmativo, se incrementa self.error y self.posicion en 1, y se devuelve el estado "q0". 
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.entero += 1
            return "q0"
        #Si el carácter actual en la posición self.posicion es un carácter de barra vertical (|), se incrementa self.posicion en 1 y se devuelve el estado "qOlogico". Esto indica que se ha encontrado una barra seguida de una barra vertical, lo cual puede indicar un operador lógico específico.
        elif self.cadena[self.posicion].isnumeric():
            self.posicion += 1
            return "qNum"
        #En la parte de código que has mostrado, cuando se encuentra un punto (.) en la cadena, se incrementa self.posicion en 1 y se llama a la función qPunto(). Esto indica que se ha identificado el inicio de una parte decimal en el número.
        elif self.cadena[self.posicion] == ".":
            self.posicion += 1
            return self.qPunto()
        #Si ninguna de las condiciones anteriores se cumple, se devuelve el estado "q1"
        else:
            self.posicion += 1
            return "q1"
        
    def qPunto(self):
        #print("qPunto")
        #En la función qPunto(), se verifica si la posición actual (self.posicion) en la cadena coincide con el final de la cadena. Si es así, se incrementa self.error en 1 y se devuelve "end
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Si el carácter en la posición actual es un espacio, un salto de línea o una tabulación, se incrementa self.posicion en 1 y self.error en 1. Luego, se devuelve "q0", lo que implica que se permanece en el mismo estado actual para continuar el análisis.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si el carácter en la posición actual es numérico, se incrementa self.posicion en 1 y se llama a la función qDecimal(). Esto sugiere que se ha reconocido un dígito después del punto decimal en el número y se procede al análisis de la parte decimal.
        elif self.cadena[self.posicion].isnumeric():
            self.posicion += 1
            return self.qDecimal()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve "q1", lo que generalmente indica un estado de error o un carácter no válido.
        else:
            self.posicion += 1
            return "q1"
        
    def qDecimal(self):
        #print("qDecimal")
        #Si la posición actual (self.posicion) coincide con el final de la cadena, se incrementa self.decimal en 1 para contar el número decimal analizado, y se devuelve "end" 
        if self.posicion == len(self.cadena):
            self.decimal += 1
            return "end"
        #Si el carácter en la posición actual es un espacio, un salto de línea o una tabulación, se incrementa self.posicion en 1 y self.decimal en 1. Luego, se devuelve "q0", lo que implica que se permanece en el mismo estado actual para continuar el análisis.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.decimal += 1
            return "q0"
        #Si el carácter en la posición actual es un dígito, se incrementa self.posicion en 1 y se llama a la función qDecimal(). Esto sugiere que se ha reconocido otro dígito en la parte decimal del número y se continúa el análisis de los dígitos decimales.
        elif self.cadena[self.posicion].isdecimal():
            self.posicion += 1
            return "qDecimal"
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve "q1"
        else:
            self.opsicion += 1
            return "q1"

    def qMenos(self):
        #print("qMenos")
        #Si la posición actual (self.posicion) coincide con el final de la cadena, se incrementa self.decimal en 1 para contar el número decimal analizado, y se devuelve "end"
        if self.posicion == len(self.cadena):
            self.operadorAritmetico += 1
            return "end"
        #Si el carácter en la posición actual es un espacio, un salto de línea o una tabulación, se incrementa self.posicion en 1 y self.decimal en 1. Luego, se devuelve "q0", lo que implica que se permanece en el mismo estado actual para continuar el análisis.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.operadorAritmetico += 1
            return "q0"
        #Si el carácter en la posición actual es un dígito, se incrementa self.posicion en 1 y se llama a la función qDecimal(). Esto sugiere que se ha reconocido otro dígito en la parte decimal del número y se continúa el análisis de los dígitos decimales.
        elif self.cadena[self.posicion].isnumeric():
            self.posicion += 1
            return self.qNum()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve "q1"
        else:
            self.posicion += 1
            return "q1"
        
    def qComillas(self):
        #print("qCad")
        #i la posición actual (self.posicion) coincide con el final de la cadena, se incrementa self.decimal en 1 para contar el número decimal analizado, y se devuelve "end
        if self.posicion == len(self.cadena):
            self.error += 1
            return "end"
        #Si el carácter en la posición actual es un espacio, un salto de línea o una tabulación, se incrementa self.posicion en 1 y self.decimal en 1. Luego, se devuelve "q0", lo que implica que se permanece en el mismo estado actual para continuar el análisis.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.error += 1
            return "q0"
        #Si el carácter en la posición actual es alfanumérico o un guion bajo (_), se incrementa self.posicion en 1 y se devuelve "qCad". Esto implica que se ha reconocido un carácter válido en la cadena y se continúa el análisis en busca de más caracteres de la cadena.
        elif self.cadena[self.posicion].isalnum() or self.cadena[self.posicion] == "_":
            self.posicion += 1
            return "qComillas"
        #Si el carácter en la posición actual es una comilla doble ("), se incrementa self.posicion en 1 y se llama a la función qCad2(). Esto indica que se ha encontrado el inicio de una cadena delimitada por comillas dobles y se procede a analizar el contenido de la cadena utilizando la función qCad2().
        elif self.cadena[self.posicion] == '"':
            self.posicion += 1
            return self.qComillas2()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve "q1"
        else:
            self.posicion += 1
            return "q1"
        
    def qComillas2(self):
        #Sprint("qCad2")
        #Si la posición actual es igual a la longitud de la cadena, significa que se ha llegado al final de la cadena. En este caso, se incrementa self.cadenaCaracteres en 1 para contar la cadena completa y se devuelve "end"
        if self.posicion == len(self.cadena):
            self.cadenaCaracteres += 1
            return "end"
        #Si el carácter en la posición actual es un espacio, un salto de línea o una tabulación, se incrementa self.posicion en 1 y self.cadenaCaracteres en 1. Esto implica que se ha encontrado un espacio en blanco después de la cadena y se incrementa el contador de caracteres de cadena. Luego, se devuelve "q0" para continuar analizando posibles espacios en blanco adicionales.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            self.cadenaCaracteres += 1
            return "q0"
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1. Esto indica que se ha encontrado un carácter válido dentro de la cadena delimitada por comillas dobles y se continúa el análisis en busca de más caracteres de la cadena. Se devuelve "q1" para indicar que se ha reconocido un carácter válido dentro de la cadena.
        else:
            self.posicion += 1
            return "q1"

    #este código dentro de la función q0() evalúa el carácter actual en la cadena y realiza transiciones a diferentes estados según el tipo de carácter encontrado. Cada condición determina la siguiente acción a tomar en función del carácter actual.
    def q0(self):
        #print("q0")
        comillas = '"'
        #Si la posición actual es igual a la longitud de la cadena, se devuelve "end" para indicar el final del análisis.
        if self.posicion == len(self.cadena):
            return "end"
        #Si el carácter en la posición actual es "(" o ")", se incrementa self.posicion en 1 y se realiza una transición al estado qParentesis().
        if self.cadena[self.posicion] == "(" or self.cadena[self.posicion] == ")":
            self.posicion += 1
            return self.qParentesis()
        #Si el carácter en la posición actual es un espacio, un salto de línea o una tabulación, se incrementa self.posicion en 1 y se devuelve "q0" para continuar analizando posibles espacios en blanco adicionales.
        if self.cadena[self.posicion] == " " or self.cadena[self.posicion] == "\n" or self.cadena[self.posicion] == "\t":
            self.posicion += 1
            return "q0"
        #Si el carácter en la posición actual es "{" o "}", se incrementa self.posicion en 1 y se realiza una transición al estado qLlave().
        elif self.cadena[self.posicion] == "{" or self.cadena[self.posicion] == "}":
            self.posicion += 1
            return self.qLlave()
        #Si el carácter en la posición actual es "/", se incrementa self.posicion en 1 y se realiza una transición al estado qAritmetico2().
        elif self.cadena[self.posicion] == "/":
            self.posicion += 1
            return self.qAritmetico2()
        #Si el carácter en la posición actual es "*", "%" o "+", se incrementa self.posicion en 1 y se realiza una transición al estado qAritmetico().
        elif self.cadena[self.posicion] == "*" or self.cadena[self.posicion] == "%" or self.cadena[self.posicion] == "+":
            self.posicion += 1
            return self.qAritmetico()
        #Si el carácter en la posición actual es alfabético o "_", se agrega el carácter a self.word, se incrementa self.posicion en 1 y se realiza una transición al estado qIdentificador().
        elif self.cadena[self.posicion].isalpha() or self.cadena[self.posicion] == "_":
            self.word += self.cadena[self.posicion]
            self.posicion += 1
            return self.qIdentificador()
        #Si el carácter en la posición actual es "<" o ">", se incrementa self.posicion en 1 y se realiza una transición al estado qOrelacional().
        elif self.cadena[self.posicion] == "<" or self.cadena[self.posicion] == ">":
            self.posicion += 1
            return self.qOrelacional()
        #Si el carácter en la posición actual es "!", se incrementa self.posicion en 1 y se realiza una transición al estado qAdmiracion().
        elif self.cadena[self.posicion] == "!":
            self.posicion += 1
            return self.qAdmiracion()
        #Si el carácter en la posición actual es "=", se incrementa self.posicion en 1 y se realiza una transición al estado qAsignacion().
        elif self.cadena[self.posicion] == "=":
            self.posicion += 1
            return self.qigual()
        #Si el carácter en la posición actual es "&", se incrementa self.posicion en 1 y se realiza una transición al estado qAmperson().
        elif self.cadena[self.posicion] == "&":
            self.posicion += 1
            return self.qAmperson()
        #Si el carácter en la posición actual es "|", se incrementa self.posicion en 1 y se realiza una transición al estado qBarra().
        elif self.cadena[self.posicion] == "|":
            self.posicion += 1
            return self.qBarra()
        #Si el carácter en la posición actual es numérico y no es "-" ni comillas dobles, se incrementa self.posicion en 1 y se realiza una transición al estado qNum().
        elif self.cadena[self.posicion].isnumeric and self.cadena[self.posicion] != "-" and self.cadena[self.posicion] != comillas:
            self.posicion += 1
            #print("a")
            return self.qNum()
        #Si el carácter en la posición actual es "-", se incrementa self.posicion en 1 y se realiza una transición al estado qMenos()
        elif self.cadena[self.posicion] == "-":
            self.posicion += 1
            return self.qMenos()
        #Si el carácter en la posición actual es comillas dobles, se incrementa self.posicion en 1 y se realiza una transición al estado qCad().
        elif self.cadena[self.posicion] == comillas:
            self.posicion += 1
            return self.qComillas()
        #Si ninguna de las condiciones anteriores se cumple, se incrementa self.posicion en 1 y se devuelve "q1" para indicar un estado genérico.
        else:
            self.posicion += 1
            return "q1"
        
    #la función evaluar() realiza la evaluación de la cadena almacenada en self.texto (asumiendo que self.texto es un widget de texto o similar) utilizando los diferentes estados y transiciones definidos en los métodos q0(), q1(), qComent(), qMulti(), qAsterisco(), qIdentificador(), qNum(), qDecimal() y qCad().
    #evaluar() coordina la evaluación de la cadena de texto mediante la llamada a diferentes métodos de transición de estado en función de los resultados obtenidos en cada etapa del análisis léxico.
    def evaluar(self):
        self.cadena = self.texto.get("1.0",END)

        if(self.archivo == 1):
            aux = self.q0()

            while aux != "end":
                if aux == "q0":
                    aux = self.q0()
                elif aux == "q1":
                    aux = self.q1()
                elif aux == "qComent":
                    aux = self.qComent()
                elif aux == "qMulti":
                    aux = self.qMulti()
                elif aux == "qAsterisco":
                    aux = self.qAsterisco()
                elif aux == "qIdentificador":
                    aux = self.qIdentificador()
                elif aux == "qNum":
                    aux = self.qNum()
                elif aux == "qDecimal":
                    aux = self.qDecimal()
                elif aux == "qComillas":
                    aux = self.qComillas()
                       
            #actualiza las etiquetas de texto en la interfaz gráfica con los resultados de la evaluación y reinicia las variables utilizadas en el proceso de evaluación para una nueva ejecución.
            self.lblReservada.configure(text=f"Palabras Reservadas : {self.palabraReservada}")
            self.lblIdentificador.configure(text=f"Identificadores : {self.identificador}")
            self.lblRelacional.configure(text=f"Operadores Relacionales : {self.operadorRelacional}")
            self.lblLogico.configure(text=f"Operadores Logicos : {self.operadorLogico}")
            self.lblAritmetico.configure(text=f"Operadores Aritmetico : {self.operadorAritmetico}")
            self.lblAsignacion.configure(text=f"Asignaciones : {self.asignacion}")
            self.lblEntero.configure(text=f"Numeros Enteros : {self.entero}")
            self.lblDecimal.configure(text=f"Numeros Decimales : {self.decimal}")
            self.lblCadena.configure(text=f"Cadena de Caracteres : {self.cadenaCaracteres}")
            self.lblMultilinea.configure(text=f"Comentario Multilinea : {self.comentarioMulti}")
            self.lblLinea.configure(text=f"Comentario de Linea : {self.comentarioLinea}")
            self.lblParentesis.configure(text=f"Parentesis : {self.parentesis}")
            self.lblLlave.configure(text=f"Llaves: {self.llaves}")
            self.lblError.configure(text=f"Errores: {self.error}")

            self.posicion = 0

            self.palabraReservada = 0
            self.identificador = 0
            self.operadorRelacional = 0
            self.operadorLogico = 0
            self.operadorAritmetico = 0
            self.asignacion = 0
            self.entero = 0
            self.decimal = 0
            self.cadenaCaracteres = 0
            self.comentarioMulti = 0
            self.comentarioLinea = 0
            self.parentesis = 0
            self.llaves = 0
            self.error = 0
            self.word = ""

    #este método permite establecer el valor de la variable self.cadena con una cadena específica que se pasa como argumento al llamar a este método. Esto proporciona una forma de actualizar la cadena de texto que será evaluada en el proceso posterior.
    def setCadena(self, cadena):
        self.cadena = cadena

    def abrirArchivo(self):
        #Se establece el valor de la variable de instancia self.archivo como 1, indicando que se está trabajando con un archivo.
         self.archivo = 1
    
    # Se muestra una ventana de diálogo para que el usuario seleccione el archivo que desea abrir.
         ruta_archivo = tkinter.filedialog.askopenfilename(title="Seleccione un archivo")
    
    # Verificar si el usuario seleccionó un archivo o canceló la selección.
         if ruta_archivo:
        # Se borra el contenido actual del widget de texto (self.texto) utilizando el método delete('1.0', END).
            self.texto.delete('1.0', END)

            self.palabraReservada = 0
            self.identificador = 0
            self.operadorRelacional = 0
            self.operadorLogico = 0
            self.operadorAritmetico = 0
            self.asignacion = 0
            self.entero = 0
            self.decimal = 0
            self.cadenaCaracteres = 0
            self.comentarioMulti = 0
            self.comentarioLinea = 0
            self.parentesis = 0
            self.llaves = 0
            self.error = 0
        #Se abre el archivo especificado por el usuario utilizando la función open() y se asigna el objeto de archivo resultante a file_object.
            with open(ruta_archivo) as file_object:
                self.cadena = ""
            # Se lee el contenido del archivo utilizando el método read() del objeto de archivo y se asigna a la variable de instancia self.cadena.
                self.cadena = file_object.read()
            # Se inserta el contenido del archivo en el widget de texto utilizando el método insert() del widget.
                self.texto.insert(tkinter.INSERT, self.cadena)
            # Se cierra el objeto de archivo utilizando el método close().
                file_object.close()

    def buscarReservadas(self):
        contador = 0   
        
if __name__ == "__main__":
    root = Tk()
    app = Proyecto(root)
    root.mainloop()
root = Tk()
root.title("Automata")
root.geometry("560x550")
aplicacion = Proyecto(root)
root.mainloop()
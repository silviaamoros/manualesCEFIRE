# Crea programa en python i tkinter que cree una cadena de text amb el següent text: "<script type='text/javascript'>window.onload = function () { var enumeracion = document.getElementsByClassName("enumeracion")[0];  enumeracion.innerHTML="<div style='font-size: 12px; margin: 10px;'>" després afegixca un text que traurà d'uan caixa de text anomenada text d'objectius, després afegirà el següent text: "\"; var objetivos = document.getElementsByClassName("perfil_elemento")[0]; var banner_div = document.createElement("div"); banner_div.innerHTML='<img id="banner_img" alt="Banner" border="0" width="640"><br><br>'; banner_div.style.cssText = 'text-align: center;'; objetivos.insertBefore(banner_div, objetivos.firstChild); var banner_img = document.getElementById("banner_img"); banner_img.src=\"" després el text d'una caixa de text que s'anmenarà banner i finalment el text: "\"; }; </script>" y ho traurà tot junt un una última caixa de text.

# Crea un botó per a afegir la cadena creat anteriorment a una pàgina web. El nom del botó ha d'apareixer com "Afegir contingut".

# Crea una finestra principal amb el següent disseny:

# - Una caixa de text anomenada "text_objectius" per introduïr el text de l'objectiu.
# - Una caixa de text anomenada "banner" per introduïr la URL del banner.
# - Un botó anomenat "Afegir contingut" que permet afegir la cadena creat anteriorment a una pàgina web.

from tkinter import *

class Aplicacio(Tk):
    def __init__(self):
        super().__init__()
        self.title("Creació de Contingut Gesform")  # noqa: E501
        self.geometry("500x300")

        Label(self, text="Text d'objectius:").grid(row=0, column=0, padx=10, pady=5)  # noqa: E501
        self.text_objectius = Text(self, width=50, height=5)
        self.text_objectius.grid(row=0, column=1, padx=10, pady=5)

        Label(self, text="URL del Banner:").grid(row=1, column=0, padx=10, pady=5)  # noqa: E501
        self.banner = Entry(self, width=50)
        self.banner.grid(row=1, column=1, padx=10, pady=5)

        Button(self, text="Afegir contingut", command=self.afegir_contingut).grid(row=2, columnspan=2, pady=10)  # noqa: E501

    def afegir_contingut(self):
        objectius = self.text_objectius.get("1.0", END).strip()
        banner_url = self.banner.get()

        # Agadfa la variable objectius i posa davant <ol></li> i en cada retorn de línia <li></li>  excepte al final que posese </ol>
        objectius = "<ol><li>" + objectius.replace("\n", "</li><li>") + "</li></ol>"



        script = f'<script type="text/javascript">window.onload = function () {{ var enumeracion = document.getElementsByClassName("enumeracion")[0]; enumeracion.innerHTML="<div style=\'font-size: 12px; margin: 10px;\'>{objectius}\"; var objetivos = document.getElementsByClassName("perfil_elemento")[0]; var banner_div = document.createElement("div"); banner_div.innerHTML=\'<img id="banner_img" alt="Banner" border="0" width="640"><br><br>\'; banner_div.style.cssText = \'text-align: center;\'; objetivos.insertBefore(banner_div, objetivos.firstChild); var banner_img = document.getElementById("banner_img"); banner_img.src="{banner_url}"\"; }}; </script>"'  # noqa: E501
        # self.text_objectius.delete("1.0", END)
        self.text_objectius.delete("1.0", END)
        self.banner.delete(0, END)

        # Aquí pots afegir el contingut a una pàgina web  # noqa: E501
        # Per exemple, es mostra en la una finestra nova amb un camp de text gran per a poder editar  # noqa: E501
        new_window = Toplevel(self)
        new_window.title("Script Generat")
        new_window.geometry("600x400")

        text_area = Text(new_window, wrap=WORD)
        text_area.pack(expand=True, fill=BOTH)
        text_area.insert(1.0, script)


if __name__ == "__main__":
    app = Aplicacio()
    app.mainloop()

import tkinter as tk
from tkinter import font

STRINGS = {
    "en": {
        "title": "Calculator",
        "error": "Error",
        "div0": "Can't divide by 0",
        "lang_label": "Language / Bahasa:",
    },
    "id": {
        "title": "Kalkulator",
        "error": "Kesalahan",
        "div0": "Tidak bisa dibagi 0",
        "lang_label": "Bahasa / Language:",
    },
}

# Reverse lookup so language switch can re-translate a visible error
ERROR_TEXTS = {v["error"] for v in STRINGS.values()} | {v["div0"] for v in STRINGS.values()}


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lang = tk.StringVar(value="en")
        self.geometry("320x490")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        self.expression = ""

        # --- Language switcher (bilingual EN / ID) ---
        lang_frame = tk.Frame(self, bg="#1e1e1e")
        lang_frame.pack(fill="x", padx=10, pady=(10, 0))

        self.lang_label = tk.Label(
            lang_frame, bg="#1e1e1e", fg="#cccccc",
            font=("Segoe UI", 10)
        )
        self.lang_label.pack(side="left")

        self.btn_en = tk.Button(
            lang_frame, text="EN", font=("Segoe UI", 10, "bold"),
            relief="flat", bd=0, padx=10,
            command=lambda: self.set_lang("en")
        )
        self.btn_en.pack(side="right", padx=(4, 0))

        self.btn_id = tk.Button(
            lang_frame, text="ID", font=("Segoe UI", 10, "bold"),
            relief="flat", bd=0, padx=10,
            command=lambda: self.set_lang("id")
        )
        self.btn_id.pack(side="right")

        # Display
        self.display_var = tk.StringVar(value="0")
        display_font = font.Font(family="Segoe UI", size=28, weight="bold")
        display = tk.Label(
            self, textvariable=self.display_var,
            anchor="e", bg="#1e1e1e", fg="white",
            font=display_font, padx=16, pady=20
        )
        display.pack(fill="x")

        # Buttons frame
        btn_frame = tk.Frame(self, bg="#1e1e1e")
        btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ("C", 0, 0, "#e81123"), ("%", 0, 1, "#333333"), ("⌫", 0, 2, "#333333"), ("÷", 0, 3, "#ff8c00"),
            ("7", 1, 0, "#2d2d2d"), ("8", 1, 1, "#2d2d2d"), ("9", 1, 2, "#2d2d2d"), ("×", 1, 3, "#ff8c00"),
            ("4", 2, 0, "#2d2d2d"), ("5", 2, 1, "#2d2d2d"), ("6", 2, 2, "#2d2d2d"), ("−", 2, 3, "#ff8c00"),
            ("1", 3, 0, "#2d2d2d"), ("2", 3, 1, "#2d2d2d"), ("3", 3, 2, "#2d2d2d"), ("+", 3, 3, "#ff8c00"),
            ("±", 4, 0, "#2d2d2d"), ("0", 4, 1, "#2d2d2d"), (".", 4, 2, "#2d2d2d"), ("=", 4, 3, "#0078d4"),
        ]

        for (text, r, c, color) in buttons:
            b = tk.Button(
                btn_frame, text=text, font=("Segoe UI", 16, "bold"),
                bg=color, fg="white", activebackground="#505050",
                activeforeground="white", relief="flat", bd=0,
                command=lambda t=text: self.on_press(t)
            )
            b.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

        for i in range(5):
            btn_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.grid_columnconfigure(i, weight=1)

        self.bind("<Key>", self.on_key)
        self.set_lang("en")

    def t(self, key):
        return STRINGS[self.lang.get()][key]

    def set_lang(self, lang):
        # Re-translate visible error message if one is showing
        current = self.display_var.get()
        self.lang.set(lang)
        self.title(self.t("title"))
        self.lang_label.config(text=self.t("lang_label"))
        if current in ERROR_TEXTS:
            if current in {v["div0"] for v in STRINGS.values()}:
                self.display_var.set(self.t("div0"))
            else:
                self.display_var.set(self.t("error"))
        # Highlight active language button
        active_bg, inactive_bg = "#0078d4", "#333333"
        self.btn_en.config(
            bg=active_bg if lang == "en" else inactive_bg, fg="white",
            activebackground=active_bg if lang == "en" else "#505050",
        )
        self.btn_id.config(
            bg=active_bg if lang == "id" else inactive_bg, fg="white",
            activebackground=active_bg if lang == "id" else "#505050",
        )

    def refresh(self):
        self.display_var.set(self.expression if self.expression else "0")

    def on_press(self, key):
        if key == "C":
            self.expression = ""
        elif key == "⌫":
            self.expression = self.expression[:-1]
        elif key == "=":
            self.calculate()
        elif key == "±":
            self.negate()
        else:
            # map display symbols to python ops
            mapping = {"×": "*", "÷": "/", "−": "-"}
            self.expression += mapping.get(key, key)
        self.refresh()

    def negate(self):
        try:
            if self.expression:
                val = eval(self.expression, {"__builtins__": {}})
                self.expression = str(-val)
        except Exception:
            self.display_var.set(self.t("error"))
            self.expression = ""

    def calculate(self):
        try:
            # safe eval: only allow numbers and operators
            allowed = set("0123456789+-*/.%() ")
            if not set(self.expression) <= allowed or not self.expression:
                return
            result = eval(self.expression, {"__builtins__": {}})
            # clean up float display
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set(self.t("div0"))
            self.expression = ""
            return
        except Exception:
            self.display_var.set(self.t("error"))
            self.expression = ""
            return

    def on_key(self, event):
        ch = event.char
        if ch in "0123456789+-*/.%()":
            self.expression += ch
            self.refresh()
        elif event.keysym in ("Return", "KP_Enter", "equal"):
            self.calculate()
            self.refresh()
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.refresh()
        elif event.keysym == "Escape":
            self.expression = ""
            self.refresh()

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

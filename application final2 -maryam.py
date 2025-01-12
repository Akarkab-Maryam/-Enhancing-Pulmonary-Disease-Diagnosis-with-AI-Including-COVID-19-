import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import customtkinter
from tkinter.ttk import Progressbar, Style

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Covid-19 Prediction")
        screen_width = int(self.winfo_screenwidth() * 0.99)
        screen_height = int(self.winfo_screenheight() * 0.90)
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.configure(bg='#ccffcc')  # Vert clair comme arrière-plan

        try:
            self.model = tf.keras.models.load_model("model_28-06-2024.h5")
            self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {e}")
            self.destroy()
            return

        def predict_covid(img_path):
            try:
                img = image.load_img(img_path, target_size=(224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array /= 255.0  # Normalize

                # Make prediction
                results = self.model.predict(img_array)
                return results
            except Exception as e:
                messagebox.showerror("Error", f"Prediction failed: {e}")
                return None

        def open_image():
            image_path = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                                    filetypes=(("All files", "*.*"), ("PNG files", "*.png")))
            if not image_path:
                return None

            img = Image.open(image_path)
            resized_img = img.resize((400, 400))
            img_tk = ImageTk.PhotoImage(resized_img)
            lung_img.configure(image=img_tk)
            lung_img.image = img_tk  # reference pour les image tkinter
            return image_path

        def perform_prediction():
            path = open_image()
            if path:
                # Réinitialiser la barre de progression
                progress_bar['value'] = 0
                style.configure("TProgressbar", foreground='blue', background='blue')
                self.update_idletasks()

                results = predict_covid(path)
                if results is not None:
                    if results[0][0] > 0.5:
                        result_label.configure(text='Covid-19')
                        style.configure("TProgressbar", foreground='red', background='red')
                    elif results[0][1] > 0.5:
                        result_label.configure(text='Normal')
                        style.configure("TProgressbar", foreground='green', background='green')
                    elif results[0][2] > 0.5:
                        result_label.configure(text='Virus Pulmonaire')
                        style.configure("TProgressbar", foreground='orange', background='orange')
                    else:
                        result_label.configure(text='Inconnu')
                        style.configure("TProgressbar", foreground='gray', background='gray')
                    
                    confidence = results[0][np.argmax(results)] * 100
                    confidence_label.configure(text=f'Confidence: {confidence:.2f}%')
                    progress_bar['value'] = confidence
                    progress_label.configure(text=f'{confidence:.2f}%')
                    self.update_idletasks()

        # Load logo image
        try:
            self.logo_image = Image.open("MSID.png").resize((240, 150))
            self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
            self.logo_image_label = tk.Label(self, image=self.logo_image_tk, bg='#ccffcc')
            self.logo_image_label.image = self.logo_image_tk  # reference img tkinter
            self.logo_image_label.pack(padx=20, pady=30)
        except Exception as e:
            messagebox.showerror("Error", f"Impossible de charger logo: {e}")

        title_label = tk.Label(self, text="Diagnostic des maladies pulmonaires", font=("Arial", 25, "bold"), bg='#ccffcc')
        title_label.pack(padx=20, pady=10)

        button1 = customtkinter.CTkButton(self, text="Importer Image", command=perform_prediction, width=200, height=80, font=("Arial", 20, "bold"))
        button1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button1.pack(padx=20, pady=20)

        lung_img = tk.Label(self, text="", bg='#ccffcc')
        lung_img.pack(padx=50, pady=25, side=tk.LEFT)

        result_label = tk.Label(self, text="", font=("Arial", 20, "bold"), bg='#ccffcc')
        result_label.pack(padx=50, pady=10, side=tk.LEFT)

        confidence_label = tk.Label(self, text="", font=("Arial", 16), bg='#ccffcc')
        confidence_label.pack(padx=50, pady=10, side=tk.LEFT)

        # Ajout de la barre de progression
        style = Style()
        style.theme_use('default')
        style.configure("TProgressbar", thickness=30)

        progress_bar = Progressbar(self, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
        progress_bar.pack(pady=20)

        # Ajout de l'étiquette de progression
        progress_label = tk.Label(self, text="0%", font=("Arial", 16), bg='#ccffcc')
        progress_label.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()

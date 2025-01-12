import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image , ImageDraw, ImageFont
import tensorflow as tf
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from tensorflow.keras.preprocessing import image
import customtkinter 
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Covid-19 Prediction")
        screen_width = int(self.winfo_screenwidth()*0.99)
        screen_height = int(self.winfo_screenheight()*0.90)
        self.geometry(f"{screen_width}x{screen_height}+0+0")
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
                results = predict_covid(path)
                if results is not None:
                    if results[0][0] > 0.5:
                        result_label.configure(text='Covid-19')
                    elif results[0][1] > 0.5:
                        result_label.configure(text='Normal')
                    elif results[0][2] > 0.5:
                        result_label.configure(text='Virus Pulmonaire')
                    else:result_label.configure(text='Inconnu')
                    confidence = results[0][np.argmax(results)] * 100
                    confidence_label.configure(text=f'Confidence: {confidence:.2f}%')
        try:
            self.logo_image = Image.open("MSID.png").resize((240, 150))
            self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
            self.logo_image_label = tk.Label(self, image=self.logo_image_tk)
            self.logo_image_label.image = self.logo_image_tk  # reference img tkinter
            self.logo_image_label.pack(padx=20, pady=30)
        except Exception as e:
            messagebox.showerror("Error", f"impossible de charger logo: {e}")
        title_label = tk.Label(self, text="Diagnostic des maladies pulmonaires",font=("Arial", 25, "bold"))
        title_label.pack(padx=20, pady=10)    
        button1 = customtkinter.CTkButton(self, text="Importer Image",command=perform_prediction,width=200,height=80,font=("Arial", 20, "bold"))
        button1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        button1.pack(padx=20, pady=20)      
        lung_img = tk.Label(self, text="")
        lung_img.pack(padx=50, pady=25, side=tk.LEFT)
        result_label = tk.Label(self, text="", font=("Arial", 20, "bold"))
        result_label.pack(padx=50, pady=10, side=tk.LEFT)
        confidence_label = tk.Label(self, text="", font=("Arial", 16))
        confidence_label.pack(padx=50, pady=10, side=tk.LEFT)
if __name__ == "__main__":
    app = App()
    app.mainloop()

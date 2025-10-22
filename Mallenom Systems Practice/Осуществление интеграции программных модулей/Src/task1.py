import tkinter as tk #Библиотека для создания графических интерфейсов
from tkinter import filedialog #Импорт модулей из библиотеки (предоставляет функции для открытия диалогового окна)
from PIL import Image, ImageTk #Библиотека Pillow для работы с изображениями (представляет изображение, преобразует изображение)

class ImageResizerApp: #Отвечает за создание интерфейса приложения для изменения размера изображений.
    def __init__(self, root): #Инициализирует графический интерфейс пользователя
        self.root = root #Сохранение ссылки на главное окно
        self.root.title("Редактор изображений") #Заголовок

        self.select_button = tk.Button(root, text="Выбрать изображение", command=self.load_image) #Создание кнопки для выбора изображений 
        self.select_button.pack(padx=10, pady=10) #Отступы 

        self.label_img = tk.Label(root) #Создание метки для отображение изображения в окне приложения
        self.label_img.pack(padx=10, pady=10) #Отступы

        self.size_buttons_frame = tk.Frame(root) #Создание Frame для размещения кнопок в окне приложений 
        self.size_buttons_frame.pack(padx=10, pady=10) #Отступы 

        sizes = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)] #Создаем размерную сетку 
        for width, height in sizes:
            button = tk.Button(self.size_buttons_frame, text=f"{width}x{height}", command=lambda w=width, h=height: self.resize_image(w, h))
            button.pack(side=tk.LEFT, padx=5)
            
        #Создаем кнопки поворота изображения влево и вправо, и делаем отсупы
        self.rotate_left_button = tk.Button(root, text="Повернуть влево", command=self.rotate_left).pack(padx=5, pady=5)
        self.rotate_right_button = tk.Button(root, text="Повернуть вправо", command=self.rotate_right).pack(padx=5, pady=5)
        
    #Выбор и загрузка изображения
    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        self.image = Image.open(self.image_path)  
        self.display_image()  
    
    #Открывает выбранное изображение
    def display_image(self):
        img_tk = ImageTk.PhotoImage(self.image)
        self.label_img.config(image=img_tk)
        self.label_img.image = img_tk  
            
    #Изменяет размер изображения
    def resize_image(self, new_width, new_height):
        resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)
        self.image = resized_image  
        self.display_image()

    #Поворачивает изображение влево
    def rotate_left(self):
        self.image = self.image.rotate(90, expand=True)  
        self.display_image()
      
    #Поворачивает изображение вправо
    def rotate_right(self):
        self.image = self.image.rotate(-90, expand=True)  
        self.display_image()
        
if __name__ == "__main__": #Проверяет запущен ли основной скрипт 
    root = tk.Tk() #Создает главный объект окна в приложении
    app = ImageResizerApp(root) #Инициализирует приложение с окном

    root.mainloop() #Запуск основного цикла

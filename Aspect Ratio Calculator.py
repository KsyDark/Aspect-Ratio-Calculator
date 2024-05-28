from tkinter import *

def perform_calculation():
    # Calculate width
    if height_entry.get() != '':
        try:
            height = float(height_entry.get())
            ratio_parts = ratio_entry.get().split(':')
            width = float(height * (float(ratio_parts[0]) / float(ratio_parts[1])))
            width_label.config(text=f"Ширина: {width}")
        except ValueError:
            width_label.config(text="Ошибка ввода!")
    
    # Calculate height
    if width_entry.get() != '':
        try:
            width = float(width_entry.get())
            ratio_parts = ratio_entry.get().split(':')
            height = float(width / (float(ratio_parts[0]) / float(ratio_parts[1])))
            height_label.config(text=f"Высота: {height}")
        except ValueError:
            height_label.config(text="Ошибка ввода!")

root = Tk()
root.title("Калькулятор соотношения сторон 1.0")
root.resizable(width=False, height=False)
root.geometry('370x250')

try:
    #Ставим иконку для заголовка приложения
    root.iconbitmap(r'calc.ico')
except:
    #Если иконки в каталоге нет, то ничего не делаем
    pass

# Height input
height_label = Label(root, text="Высота:", font="bold")
height_label.pack()
height_entry = Entry(root)
height_entry.pack()

# Calculate buttons
calculate_width_button = Button(root, text="Вычислить ширину", font=("Arial", 12, "bold"), command=perform_calculation)
calculate_width_button.pack()

#Пустота
height_label10 = Label(root, text="")
height_label10.pack()

# Width input
width_label = Label(root, text="Ширина:", font="bold")
width_label.pack()
width_entry = Entry(root)
width_entry.pack()

# Calculate buttons
calculate_height_button = Button(root, text="Вычислить высоту", font=("Arial", 12, "bold"), command=perform_calculation)
calculate_height_button.pack()

# Ratio input
ratio_label = Label(root, text="Соотношение (например, 16:9):", font="bold")
ratio_label.pack()
ratio_entry = Entry(root)
ratio_entry.insert(0, '16:9')
ratio_entry.pack()

def calculate(event):
    perform_calculation()

# Bind the Enter key event to the calculate function
root.bind('<Return>', calculate)

# Функция отчистки всех полей ввода
def clear(event):
    width_entry.delete(0, 1000) # Height input
    height_entry.delete(0, 1000) # Height input

#Привязываем кнопку Delete чтобы отчищать все строки
root.bind('<Delete>',clear)

#Закрыть главное окно
def exit_root(event):
    root.quit()
#Закрыть главное окно и все дочерние окна через ESC
root.bind('<Escape>', exit_root)

root.mainloop()
import tkinter as tt

root = tt.Tk()
root.geometry("500x200")
root.title("BMI Calculator")

def bmi_calculator():
    kg = int(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    if bmi <= 15.0:
            res = "\nBMI : " + str(bmi)+"\n\nYOU ARE SEVERELY UNDERWEIGHT!!"

    elif 16.0 < bmi < 18.5:
            res = "\nBMI : " + str(bmi)+"\n\nYOU ARE UNDERWEIGHT!"
            
    elif 18.5 <= bmi <= 25.0:
            res = "\nBMI : " + str(bmi)+"\n\nYOU ARE NORMAL"
            
    elif 25.0 < bmi <= 30:
            res = "\nBMI : " + str(bmi)+"\n\nYOU ARE OVERWEIGHT!"
            
    elif 30.0 < bmi <= 35.0:
            res = "\nBMI : " + str(bmi)+"\n\nYOU ARE MODERATELY OBESE!!"
           
    elif 35.0 < bmi <= 40.0:
            res = "\nBMI : " + str(bmi)+"\n\nYOU ARE SEVERELY OBESE!!!"
            
    else:
            res = "\nBMI is " + str(bmi)+"\n\nYOU ARE SUPER OBESE!!"

    label_result['text'] = f"{res}"

#Now let's create the GUI
label_kg = tt.Label(root,bg="red",font = ('forte',10,'bold'), 
                                 text="Weight(in kg): ")
label_kg.pack()

entry_kg = tt.Entry(root)
entry_kg.pack()

label_height = tt.Label(root,bg="red",font = ('forte',10,'bold'), 
                          text="Height(in metres): ")
label_height.pack()

entry_height = tt.Entry(root)
entry_height.pack()

button_calculate = tt.Button(root,bg="green",font = ('jokerman',10,'bold'),
                     text="Calculate", command=bmi_calculator)
button_calculate.pack()

label_result = tt.Label(root,font = ('showcard gothic',13,'bold'))
label_result.pack()

root.mainloop()

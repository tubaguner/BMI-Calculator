import tkinter as Tk
from tkinter import ttk

root = Tk.Tk()
root.title('BMI Calculator')
root.geometry("520x300")


def calculate_bmi_value(): 
    height = float(height_var.get())
    weight = float(weight_var.get())
    bmi = weight / (height ** 2)
    result_var.set(f"BMI: {bmi:.2f}")
    return_result()

#def calculate_button():
    #height = float(height_var.get())
    #weight = float(weight_var.get())
    #bmi = weight / (height ** 2)
    #result_var.set("BMI: {bmi:.2f}")

def return_result():
    msg = f'You entered result: {result_var.get()}'
    return_label.config(text=msg)
    





    
#def button3_clicked():
    """ callback when the login button3 clicked
    """
    #msg = f'You entered calculate: {calculate.get()}'
    #showinfo(
        #title='Information',
        #message=msg
    #)

calculate_bmi = ttk.Frame(root)
calculate_bmi.pack(padx=10, pady=10, fill='x', expand=True)

height_label = ttk.Label(calculate_bmi,text="Height:")
height_label.pack(fill='x', expand=True)

height_var = Tk.StringVar()
height_entry = ttk.Entry(calculate_bmi,textvariable=height_var,show='~')
height_entry.pack(fill='x', expand=True)
height_entry.focus()

# weight
weight_label = ttk.Label(calculate_bmi,text="Weight:")
weight_label.pack(fill='x', expand=True)

weight_var = Tk.StringVar()
weight_entry = ttk.Entry(calculate_bmi,textvariable=weight_var,show='~')
weight_entry.pack(fill='x', expand=True)

result_label = ttk.Label(calculate_bmi,text="Result:")
result_label.pack(fill='x', expand=True)

result_var = Tk.StringVar()
result_entry = ttk.Entry(calculate_bmi,textvariable=result_var)
result_entry.pack(fill='x', expand=True)

calculate_button = ttk.Button(calculate_bmi, text="Calculate",command=lambda:calculate_bmi_value)
calculate_button.pack(fill='y', expand=False, pady=10)


#button3 = Tk.Label(root, text="CALCULATE", bg="pink", fg="black")
#button3.pack(ipadx=15, ipady=10)


#def height(height):
    #return f"{Height}" 
#def weight(weight):
    #return f"{Weight}"
#def calculate(calculate):
    #return f"{Calculate}"
#def result(result):
    #return f"{Result}"

root.mainloop()

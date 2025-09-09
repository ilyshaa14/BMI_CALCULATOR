import tkinter
import tkinter.ttk
from PIL import Image, ImageTk


window = tkinter.Tk()
window.title('BMI CALCULATOR')
window.geometry('470x580+740+250')
window.resizable(False, False)
window.config(bg='#f0f1f5')



#icon
icon_image = tkinter.PhotoImage(file='bin/icon.png')
window.iconphoto(False, icon_image)
# top header
top_image_obj = tkinter.PhotoImage(file="bin/top.png")
top_image = tkinter.Label(master=window, image=top_image_obj)
top_image.place(x=-10, y=-10)

#bottom
bottom_bg = tkinter.Label(master=window, width=72, height=18, bg='Lightblue')
bottom_bg.pack(side=tkinter.BOTTOM)

#2  boxes
box_image_obj = tkinter.PhotoImage(file='bin/box.png')
tkinter.Label(master=window, image=box_image_obj).place(x=20, y=100)
tkinter.Label(master=window, image=box_image_obj).place(x=240, y=100)
# scale
scale_image_obj = tkinter.PhotoImage(file='bin/scale.png')
tkinter.Label(master=window, image=scale_image_obj, bg='peachpuff').place(x=20, y=310)
# Entry boxes
height_var = tkinter.StringVar()
height_var.set('0')

height_entry = tkinter.Entry(
     master=window,
     textvariable=height_var,
     width=5,
     font=('Arial', 50),
     bg='#fff',
     bd=0,
     justify=tkinter.CENTER
)
height_entry.place(x=35, y=160)




weight_var = tkinter.StringVar()
weight_var.set('0')
weight_entry = tkinter.Entry(
     master=window,
     textvariable=weight_var,
     width=5,
     font=('Arial', 50),
     bg='#fff',
     bd=0,
     justify=tkinter.CENTER
)
weight_entry.place(x=255, y=160)


#man image
man_image = tkinter.Label(master=window, bg='lightblue')
man_image.place(x=80, y=530)

## Slider 1

def get_current_h():
    return f'{current_h_val.get():.0f}'

def get_current_w():
    return f'{current_w_val.get():.0f}'


def slider_changed(value):
    h_value = get_current_h()
    height_var.set(h_value)
    w_value = get_current_w()
    weight_var.set(w_value)

    #print(h_value, type(h_value))


    # picture
    img_man = Image.open('bin/man.png')
    height = int(float(h_value))

    weight = int(float(w_value))
    
    img_man_resize = img_man.resize([10 + weight, 10 + height])
    
    temp = ImageTk.PhotoImage(img_man_resize)

    
    man_image.config(image=temp)
    man_image.place(x=80, y=550 - height)
    man_image.image=temp

    

current_h_val = tkinter.DoubleVar()
style = tkinter.ttk.Style()
style.configure('TScale', background='white',)
slider_h = tkinter.ttk.Scale(
    master=window,
    variable=current_h_val,
    command=slider_changed,
    from_=0,
    to=220
 )
slider_h.place(x=80, y=250)



current_w_val = tkinter.DoubleVar()
style = tkinter.ttk.Style()
style.configure('TScale', background='white',)
slider_w = tkinter.ttk.Scale(
    master=window,
    variable=current_w_val,
    command=slider_changed,
    from_=0,
    to=220
 )
slider_w.place(x=300, y=250)


# result button



def BMI_result():
    hm = float (height_var.get()) / 100
    w = float (weight_var.get())

    if hm > 0:
        bmi_value = round(w / hm**2)
        print(bmi_value)
        result_BMI['text'] = bmi_value

result_button = tkinter.Button(
    master=window,
    text="рузултат",
    command=BMI_result,
    bg='lightskyblue',
    fg='white',
    font=('arial', 15, 'italic')
    )
result_button.place(x=350, y=340)

result_BMI = tkinter.Label(
    master=window,
    text='0',
    font=('arial', 50, 'italic'),
    bg='lightblue',
    fg='white'
    )

result_BMI.place(x=365, y=440)



#peachpuff

window.mainloop()






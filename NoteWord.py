import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('NiteWord')


##############################    Main Menu   ################################
main_menu = tk.Menu()

new_icon = tk.PhotoImage(file= "C:/Users/janga/Downloads/icons2/new.png")
open_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/open.png")
save_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/save.png")
save_as_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/save_as.png")
exit_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/exit.png")

file = tk.Menu(main_menu,tearoff= False)

copy_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/copy.png")    
paste_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/paste.png")
cut_icon =tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/cut.png")
clear_all_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/clear_all.png")
find_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/find.png")

edit = tk.Menu(main_menu,tearoff= False)

edit.add_command(label = 'Copy',image=copy_icon,compound=tk.LEFT,accelerator= 'ctrl+C')
edit.add_command(label = 'Paste',image=paste_icon,compound=tk.LEFT,accelerator= 'ctrl+V')
edit.add_command(label = 'Cut',image=cut_icon,compound=tk.LEFT,accelerator= 'ctrl+X')
edit.add_command(label = 'Clear_All',image=clear_all_icon,compound=tk.LEFT,accelerator= 'ctrl+Alt+Alt+X')
edit.add_command(label = 'Find',image=find_icon,compound=tk.LEFT,accelerator= 'ctrl+F')

tool_bar_icon =tk.PhotoImage(file ="C:/Users/janga/Downloads/icons2/tool_bar.png" )
Status_bar_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/status_bar.png")
view = tk.Menu(main_menu,tearoff= False)

# Colour Theme
light_default_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/light_default.png")
light_plus_icon =tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/light_plus.png")
Dark_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/dark.png")
red_icon= tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/red.png")
monokai_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/monokai.png")
night_blue_icon=tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/night_blue.png")

theme_choice = tk.StringVar()
colour_icons = (light_default_icon,light_plus_icon,Dark_icon,red_icon,monokai_icon,night_blue_icon)
Color_Themes = tk.Menu(main_menu,tearoff= False)
colour_dict= {
    'light Default': ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark': ('#2d2d2d','#ffe8e8'),
    'Red': ('#d3b774','#474747'),
    'Monokai':('#d3b774','#6b9dc2'),
    'Night Blue': ('#ededed','#6b9dc2')
}


main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color_Themes',menu=Color_Themes)

############################# Tool Bar ############################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#### font Box ###

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state= 'readonly')
font_box['values']= font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)


###  Size Box #######
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

# # # # # # # # Bold Icon # # # # # # # #
bold_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/bold.png")
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

 # # # # # ## # # #  Italic Icon # # # # # # # # # # 
italic_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/italic.png")
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

## ##  ##   ## ##  # ### underline   # # # # # # # # # # # # 
underline_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/underline.png")
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

##   # # # # # # ##  font Color icon # # # # # ## # #  # # # # # # # #############
font_color_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/font_color.png")
font_color_btn = ttk.Button(tool_bar,image=font_color_icon,)
font_color_btn.grid(row=0,column=5,padx=5)

# # # # # # # Align Left # # # # # # # 
Align_left = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/align_left.png")
Align_icon = ttk.Button(tool_bar,image=Align_left)
Align_icon.grid(row=0,column=6,padx=5)

# # # # # # Align Center # # # # # # 
Align_center = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/align_center.png")
Align_btn = ttk.Button(tool_bar,image=Align_center)
Align_btn.grid(row=0,column=7,padx=5)

# #  ##  #  Align Right # # # # #
AlignRight_icon = tk.PhotoImage(file="C:/Users/janga/Downloads/icons2/align_right.png")
Align_right_btn = ttk.Button(tool_bar,image=AlignRight_icon)
Align_right_btn.grid(row=0,column=8,padx=5)

 # # # # # # # # Text Editer # # # # # # # # 
text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar =  tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font Family ####################################

current_font_family = 'Arial'
current_font_size = 12

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.config(font=(current_font_family,current_font_size))

def change_fontsize(main_application):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.config(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)

# # # # # # # ## # # # Bold Funtion # #  ## ## # # # ## 

def change_bold():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']== 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']== 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)

# ##################### Italic Button ###################

def change_italic():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']== 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']== 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
italic_btn.configure(command=change_italic)

###########  Underline ##############

def change_underline():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']== 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']== 1 :
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

####### Font Color ############
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command = change_font_color)

########### Align Funtion #################
# Left
def align(align_type):
    if align_type == "left":
        text_editor.tag_configure("left", justify='left')
        text_editor.tag_remove("center", '1.0', 'end')
        text_editor.tag_remove("right", '1.0', 'end')
        text_editor.tag_add("left", '1.0', 'end')
# Center
    elif align_type == "center":
        text_editor.tag_configure("center", justify='center')
        text_editor.tag_remove("left", '1.0', 'end')
        text_editor.tag_remove("right", '1.0', 'end')
        text_editor.tag_add("center", '1.0', 'end')
# Right
    elif align_type == "right":
        text_editor.tag_configure("right", justify='right')
        text_editor.tag_remove("left", '1.0', 'end')
        text_editor.tag_remove("center", '1.0', 'end')
        text_editor.tag_add("right", '1.0', 'end')

def align_left():
    align("left")

def align_center():
    align("center")

def align_right():
    align("right")

# Usage example
Align_icon.configure(command=align_left)  # Aligns text to the left
Align_btn.configure(command=align_center)  # Aligns text to the center
Align_right_btn.configure(command=align_right)  # Aligns text to the right


text_editor.config(font=('Arial',12))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> End text Editor <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#............................Status Bar..............................

Status_bar= ttk.Label(main_application,text = 'Status Bar')
Status_bar.pack(side=tk.BOTTOM)


text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(" ",''))
        Status_bar.config(text=f'Characters : {characters}Word :{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>', changed)


# ->->->->->>>>>>>>>>>> URL <<<<<<<<<<-<-<-<-<-<-<-
#__________________________  Variable __________________
url = ''
#((((((New File Functionlity))))))
def new_file (event=None): 
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

### Open file Command ###

file.add_command(label = 'New',image=new_icon,compound=tk.LEFT,accelerator= 'ctrl+N',command=new_file)
def open_file(even = None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All file','*.*')))
    try:
        with open (url,'r')as fr :
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError :
        return
    except:
        return
    main_application.title(os.path.basename(url))
file.add_command(label = 'Open',image=open_icon,compound=tk.LEFT,accelerator= 'ctrl+O',command=open_file)







###   ################       Save File Command           ##############      @######
def save_file (even=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open (url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
file.add_command(label = 'Save',image=save_icon,compound=tk.LEFT,accelerator= 'ctrl+S',command=save_file)

#>>>>>>>>>>>>>>>>>>>>>>>... Save As .. <<<<<<<<<<<<<<<<< 
def save_as(event=None):
    global url
    try :
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode ='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label = 'Save_as',image=save_as_icon,compound=tk.LEFT,accelerator= 'ctrl+Alt+S',command=save_as)

#================++++ Exit Funtions ++++================
 
def exit_func(event = None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Waring','Do You want To Save The File ? ')
            if mbox is True :
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open (url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else :
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
file.add_command(label = 'Exit',image=exit_icon,compound=tk.LEFT,accelerator= 'ctrl+Q',command= exit_func)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Find And Replace <<<<<<<<<<<<<<<<<<<<<

def find_func(event=None):
    
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find & Replace')
    find_dialogue.resizable(0,0)

    find_frame = ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame,text='Find :  ')
    text_replace_label = ttk.Label(find_frame,text='Replace')

    find_input = ttk.Entry(find_frame,width= 30)
    replace_input = ttk.Entry(find_frame,width=30)

    find_button = ttk.Button(find_frame,text='Find',command=find)
    replace_button = ttk.Button(find_frame,text='Replace',command=replace)

    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()




### Edit command ###

edit.add_command(label = 'Copy',image=copy_icon,compound=tk.LEFT,accelerator= 'ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label = 'Paste',image=paste_icon,compound=tk.LEFT,accelerator= 'ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label = 'Cut',image=cut_icon,compound=tk.LEFT,accelerator= 'ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label = 'Clear_All',image=clear_all_icon,compound=tk.LEFT,accelerator= 'ctrl+Alt+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label = 'Find',image=find_icon,compound=tk.LEFT,accelerator= 'ctrl+F',command=find_func)

######view Check Button ########

Show_statusbar =tk.BooleanVar()
Show_statusbar.set(True)
Show_toolbar= tk.BooleanVar()
Show_toolbar.set(True)

def hide_toolbar():
    global Show_toolbar
    if Show_toolbar:
        tool_bar.pack_forget()
        Show_toolbar = False
    else:
        text_editor.pack_forget()
        Status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        Status_bar.pack(side=tk.BOTTOM)
        Show_toolbar= True

def hide_statusbar():
    global Show_statusbar
    if Show_statusbar:
        Status_bar.pack.pack_forget()
        Show_statusbar = False
    else:
        Status_bar.pack(side=tk.BOTTOM)
        Show_statusbar= True





view.add_checkbutton(label = 'Tool bar',onvalue=True,variable=Show_toolbar, image = tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status bar',onvalue=False,variable=Show_statusbar, image=Status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

##### Colour Themes ######
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = colour_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg = fg_color)
count = 0
for i in colour_dict:
    Color_Themes.add_radiobutton(label=i,image=colour_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1



######### End Main menu ##################

main_application.config(menu=main_menu)

main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',save_as)
main_application.bind('<Control-q>',exit_func)
main_application.bind('<Control-f>',find_func)



main_application.mainloop()
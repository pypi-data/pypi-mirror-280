# Basic Import Functions
import tkinter as tk  # Importing tkinter library for GUI
import customtkinter as ctk  # Importing customtkinter library for custom UI elements
import PIL.Image  # Importing PIL library for image processing
import random  # Importing random module for random sampling
from pathlib import Path  # Importing Path class from pathlib module for working with file paths
import json  # Importing json module for working with JSON files
from os import path  # Importing path module from os for working with file paths


# Initialize a variable to store the ID of the scheduled update
timer_update_id = None #Boolean Variable to set whether the timer is meant to update or not


# Defining Commands - Making Main Frame, All Widgets in 2nd Window, Each widget placed here will be represened in the main window
def create_typing():
    global current_word_label, container, typing_container, text_container, current_text, typing_box, container, timer_label, test_time, len_time, wpm_label, Textspeech, check_var, Back, Restart_button, timer_label, is_on_main_window, is_on_typing_window, scale, modes, is_on_settings_window
    is_on_main_window = False #Boolean variable to show main window is not on, and now typing window keybinds wont work
    is_on_typing_window = True #Boolean variable to show that typing window is on, and now Main window keybinds wont work\
    is_on_settings_window = False
    
    # Clearing Frame
    for widget in main_window.winfo_children():  # Emptying out frame
        widget.place_forget()
    main_window.pack_forget()

    root.geometry("1400x700") #Creating Typing window frame
    container = ctk.CTkFrame(root)
    container.pack(expand=True, fill="both")
    
    typing_container = ctk.CTkFrame(container) #First container that holds everything else
    typing_container.place(
        relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="c"
    )
    main_image = PIL.Image.open(Path(__file__).resolve().parents[0] / path.join("Assets", "main_image.png")) #Image holder
    dummy_widget1 = ctk.CTkLabel(
        typing_container,
        text="",
        image=ctk.CTkImage(main_image, size=(1400, 700)),
    )
    dummy_widget1.pack() #Frame that holds the words to type, and time left
    text_container = ctk.CTkFrame(
        typing_container, border_width=5, border_color="#767272"
    )
    text_container.place(
        relx=0.5, rely=0.05, relwidth=0.9, relheight=0.45, anchor="n"
    )
    
    # Label for the WPM counter
    wpm_label = ctk.CTkLabel( #Label that displays the WPM of the user
        typing_container,
        text="WPM: ",
        corner_radius=100,
        fg_color="grey",
        text_color="black",
    )
    wpm_label.place(in_=typing_container, relx=0.1, rely=0.07)

    Back = ctk.CTkButton( #Button to go back to Main window from the typing window
        container,
        text="← Go Back (Esc)",
        command=go_back,
        corner_radius=100,
        fg_color="white",
        text_color="black",
    )
    Back.place(relx=0.1) #places back button

    current_word_label = ctk.CTkLabel( #Current word that the user has to type
        text_container,
        text=" ".join(sampled_words[0:3]),
        font=ctk.CTkFont(size=40),
    )
    current_word_label.place(relx=0.5, rely=0.5, anchor="c") #places current word onto text container

    timer_label = ctk.CTkLabel( #Timer label
        text_container, text=f"Time left: {timer_seconds} seconds"
    )
    timer_label.place(relx=0.5, rely=0.7, anchor="c")

    current_text = "" #This variable stores what the user has typed into the entrybox and then later on checks whether the word is spelt correctly
    typing_box = ctk.CTkEntry( #entrybox for the user to type in
        typing_container,
        placeholder_text="       Click Box To Begin",
        font=ctk.CTkFont(size=20)
    )
    typing_box.bind("<KeyRelease>", on_key_press)
    typing_box.place(
        relx=0.5, rely=0.6, anchor="c", relheigh=0.1, relwidth=0.3
    )
    #typing_box.focus() #Focus ensures that the entrybox is already highlighted, and that the user does not need to click it

    
  
    Restart_button = ctk.CTkButton( #To restart the test
        typing_container,
        text="Restart (Enter)",
        command=restart,
        fg_color="grey",
        text_color="black",
        hover_color= "red"
    )
    Restart_button.place(relx=0.5, rely=0.91, anchor="c")


def test_time(value): #Function that updates the time left in the timer label
    global timer_seconds
    timer_label.configure(text=f"Time left: {str(value)} seconds" )
    timer_seconds = int(value)


def scaling(value): #Function that sets the scale to what the user selects, Customtkinter function
    global current_scaling
    current_scaling = value
    ctk.set_widget_scaling(float(value))


# Function that commands the Go Back Button
def go_back():
    global is_on_main_window, is_on_typing_window, timer_update_id, timer_seconds, is_on_settings_window

    # If leaving the typing window, stop the timer
    if is_on_typing_window:
        if timer_update_id:
            root.after_cancel(timer_update_id)
            timer_seconds = int(len_time.get())
    
    # Set window flags accordingly
    is_on_main_window = True
    is_on_typing_window = False
    is_on_settings_window = False
    container.pack_forget()  # Forget the current window
    root.geometry("1400x700")  # Adjust window size
    make_main_window()  
    place_main_window_content()


# Function that commands when the first word is written right
def on_key_press(e):
    global score, sampled_words
    current_text = typing_box.get()
    if current_text.strip() == sampled_words[0]:
        sampled_words.pop(0)
        update_current_word()
        typing_box.configure(
            placeholder_text=" ".join(sampled_words[0:3])
        )  # More than 1 word on the screen
        typing_box.delete(0, ctk.END)
        score += 1
        if timer_seconds > 0:
            update_timer()


# Command for the restart button that occurs when time is up
def restart():
    global score, timer_seconds, timer_choice, len_time, root
    score = 0
    timer_seconds = int(len_time.get())
    timer_label.configure(text=f"Time left: {timer_seconds} seconds")
    typing_box.configure(state="normal")
    typing_box.delete(0, ctk.END)
    if timer_update_id:
        root.after_cancel(timer_update_id)


# Updated word as the word is spelt right
def update_current_word():
    current_word_label.configure(text=" ".join(sampled_words[0:3]))


# Receives word from JSON File "Words"
def get_words():
    global sampled_words
    with open(Path(__file__).resolve().parents[0] / "words.json") as file:
        words = json.load(file)
        sampled_words = random.sample(words, 100)


# Countdown Timer
def update_timer():
    global timer_seconds, timer_update_id, score, Restart_button
    if timer_seconds > 0:
        timer_seconds -= 1
        timer_label.configure(text=f"Time left: {timer_seconds} seconds")
        # Cancel the previous scheduled update
        if timer_update_id:
            root.after_cancel(timer_update_id)
        # Schedule the next update
        timer_update_id = root.after(1000, update_timer)
    else:
        timer_label.configure(text="Time's up!")
        value = int(len_time.get())
        if value == 10:
            wpm_label.configure(text=f"WPM: {score * 6} ") #formula depending on the length of the test the user wants to run. 

        elif value == 30:
            wpm_label.configure(text=f"WPM: {score * 2} ")
        else:
            wpm_label.configure(text=f"WPM: {score} ")
        typing_box.configure(state="disable")

def settings_back():
    container.pack_forget()  # Forget the current window
    root.geometry("1400x700")  # Adjust window size
    make_main_window()  
    place_main_window_content()
# Starts timer
def start_timer(duration):
    global timer_seconds
    timer_seconds = duration
    update_timer()

def opensettings():
    global dummy_widget3, opennsettings_frame, container, is_on_settings_window, is_on_typing_window, is_on_main_window, settings_backbutton, Back, len_time, timer_label
    for widget in main_window.winfo_children():  # Emptying out frame
        widget.place_forget()
    main_window.pack_forget()

    is_on_settings_window =True
    is_on_main_window = False
    is_on_typing_window = False

    root.geometry("1400x700") #Creating Typing window frame
    container = ctk.CTkFrame(root)
    container.pack(expand=True, fill="both")

    opennsettings_frame = ctk.CTkFrame(root, border_width=5, border_color="#767272", height=280, fg_color= "#767272")
    opennsettings_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="c")
    settings_image = PIL.Image.open(Path(__file__).resolve().parents[0] / path.join("Assets", "settingsbg.png")) #Image holder
    dummy_widget3 = ctk.CTkLabel(
        opennsettings_frame,
        text="",
        image=ctk.CTkImage(settings_image, size=(1400, 700)))
    dummy_widget3.pack()
    Back = ctk.CTkButton( #Button to go back to Main window from the typing window
        container,
        text="← Go Back (Esc)",
        command=settings_back,
        corner_radius=100,
        fg_color="white",
        text_color="black",
    )
    Back.place(relx=0.1) #places back button
    len_time = ctk.CTkOptionMenu( 
        opennsettings_frame,
        values=["10", "30", "60"],
        command=test_time,
        button_color="gray",
        fg_color="black",
    )
    len_time.configure(state="disable")
    len_time_label = ctk.CTkLabel(
        opennsettings_frame,
        text="Seconds",
        fg_color="#272626",
        text_color="white",
        font=("helvetica", 20) 
    )
    len_time.place(relx = 0.45, rely=0.4)
    len_time_label.place(relx = 0.475, rely = 0.3)
    modes = ctk.CTkOptionMenu( #Options for mode the user wants, system, dark or light
        opennsettings_frame,
        values=["dark", "light", "system"],
        command= ctk.set_appearance_mode,
        button_color="gray",
        fg_color="black",
    )
    modes_label = ctk.CTkLabel(
        opennsettings_frame,
        text="Themes",
        fg_color="#272626",
        text_color="white",
        font=("helvetica", 20) 
    )
    modes.set("system")
    modes.set(ctk.get_appearance_mode())
    modes_label.place(relx = 0.475, rely = 0.5)
    modes.place(relx = 0.45, rely = 0.6)
    scale = ctk.CTkOptionMenu( #Options for the scale the user wants to use
        opennsettings_frame,
        values=["0.75", "1.0", "1.25"],
        command=scaling,
        button_color="gray",
        fg_color="black",
    )
    scale_label = ctk.CTkLabel(
        opennsettings_frame,
        text="UI Scale",
        fg_color="#272626",
        text_color="white",
        font=("helvetica", 20) 
    )
    scale.set(current_scaling)
    scale_label.place(relx = 0.475, rely = 0.7)
    scale.place(relx = 0.45, rely =0.8)





    

   
    
    
# Command that remakes the main window content after the Back Button is pressed
def place_main_window_content():
    main_window.pack(expand=True, fill="both")
    dummy_widget.pack()
    Begin_TTH.place(relx=0.5, rely=0.4, anchor="c")
    EndProgram.place(relx=0.5, rely=0.7, anchor="c")
    Credits.place(relx=0.5, rely=0.6, anchor="c")
    Settings.place(relx=0.5, rely=0.5, anchor="c")

    
    


# Credits Function
def credits():
    tk.messagebox.showinfo("Credits", "Made by Gaurav 12SDD2")



# Main Window Content - Frame Buttons labels etc
def make_main_window():
    # Pop Up-Window - Begin Touch Type Helper
    global root, main_window, Welcome_TTH, Begin_TTH, Credits, dummy_widget, EndProgram, is_on_main_window, is_on_typing_window, Settings, is_on_settings_window
    is_on_main_window = True
    is_on_typing_window = False
    is_on_settings_window = False
    
    # main_window
    main_window = ctk.CTkFrame(
        root, width=400, height=500, border_width=10
    )  # border_color = "#13141F") )

    dummy_widget = ctk.CTkLabel( #holds main window's image 
        main_window,
        text="",
        image=ctk.CTkImage(
            PIL.Image.open(
                Path(__file__).resolve().parents[0] / path.join("Assets", "logo.png")
            ),
            size=(1400, 700),
        ),
    )

    
    

    # Buttons in main window
    Begin_TTH = ctk.CTkButton( #Begin button
        main_window,
        text="Begin (⇧ + ↵)",
        font=("Arial", 16),
        fg_color="#272626",
        command=create_typing,
    )

    EndProgram = ctk.CTkButton( #End program button
        main_window,
        text="End Program (⇧ + Esc)",
        font=("Arial", 16),
        fg_color="#272626",
        command=root.destroy,
    )

    Credits = ctk.CTkButton( #Credits buttton
        main_window,
        text="Credits",
        font=("Arial", 16),
        fg_color="#272626",
        command=credits,
    )
    
    Settings = ctk.CTkButton(main_window, text= "Settings", font=("Arial", 16), fg_color="#272626", command= opensettings)
    




def keybind(button, action): #Function to make sure that keybinds only work when the correct window is opened. 
    global is_on_main_window, is_on_typing_window
    if action in actions[0:2] and is_on_main_window: #if the user is on the main window only the begin and end program keybinds work
        button.invoke()
    elif action in actions[2:4] and is_on_typing_window: #If users is on the typing window only the back and restart button work
        button.invoke()
    elif action in actions[3:4] and is_on_settings_window: #If user is on the settings window only back button works
        button.invoke()

def start_app(): #Function to begin app when it is called through the temrinal
    try:
        global current_scaling, timer_seconds, score, root, timer_choice, is_on_main_window, is_on_typing_window, scale, actions, is_on_settings_window
        get_words()
        timer_seconds = 10
        score = 0  # Keeps score on how many words are right
        is_on_main_window = False #Sets variabel to false when program is intially run
        is_on_typing_window = False#Sets variabel to false when program is intially run
        is_on_settings_window = False#Sets variable to false when program is initially run
        actions = ["to_typing_window", "do_exit", "do_restart", "to_main_window"]
        current_scaling = "1.0"
#Basic UI 
        root = ctk.CTk()
        root.geometry("1400x700")
        root.title("Touch Typing Helper - Gaurav Surve")
        make_main_window()
        place_main_window_content()
        #Assigning values to keybinds to make sure that they only work when called
        root.bind("<Shift-Return>", lambda e: keybind(Begin_TTH, actions[0])) 
        root.bind("<Shift-Escape>", lambda e: keybind(EndProgram, actions[1]))
        root.bind("<Return>", lambda e: keybind(Restart_button, actions[2]))
        root.bind("<Escape>", lambda e: keybind(Back, actions[3]))
        root.bind("")
        
        root.mainloop()

    except Exception as ex:
        with open ("test.txt", "x") as f:
            f.write(f"{type(ex).__name__} {ex}") #pypi package

# Main variables for when program is started
if __name__ == "__main__":
    start_app()

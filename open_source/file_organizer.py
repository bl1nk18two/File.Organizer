import os 
from tkinter.filedialog import askdirectory
from tkinter import *

def interface():
    window = Tk()
    window.title("File Organizer")
    window.geometry("510x200")
    
    label = Label(window, text="Path: ", font=8)
    label.grid(column=0, row=0)

    path_var = StringVar()
    entry = Entry(window, textvariable=path_var, width=60)
    entry.grid(column=1, row=0)

    def explore():
        path = askdirectory(title="Select a Folder")
        path_var.set(path) 
    
    button = Button(window, text="Explore", command=explore, font=8, bg="lightgray", fg="black")
    button.grid(column=2, row=0)

    terminal_output = Text(window, height=2, width=60)
    terminal_output.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

    def run_command():
        organize(path_var.get())
        terminal_output.insert(END, "Completed Successfully!\n")
    
    button = Button(window, text="Organize", command=run_command, font=8, bg="lightgray", fg="black")
    button.grid(column=2, row=1)

    window.mainloop()

def organize(path):   
    file_list = os.listdir(path)
    file_extensions = {
        "images": [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".gif", ".webp", ".ico", ".cur", ".svg", ".ai", ".psd"],
        "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".csv", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".odp", ".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".json", ".xml", ".zip", ".rar", ".7z"],
        "audio": [".wav", ".flac", ".aiff", ".alac", ".mp3", ".aac", ".ogg", ".wma", ".m3u", ".pls", ".m4a"],
        "video": [".mov", ".avi", ".wmv", ".mp4", ".mkv", ".flv", ".webm", ".srt", ".vtt"],
        "system": [".exe", ".app", ".elf", ".sh", ".dll", ".so", ".dylib", ".ttf", ".otf", ".woff", ".woff2"]
    }
    for file in file_list:
        name, extension = os.path.splitext(f'{path}/{file}')
        for folder in file_extensions:
            if extension.lower() in file_extensions[folder]:
                if not os.path.exists(f"{path}/{folder}"):
                    os.mkdir(f"{path}/{folder}")
                os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")
                
if __name__ == '__main__':
    interface()



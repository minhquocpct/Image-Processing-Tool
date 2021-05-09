import PySimpleGUI as sg
import os.path
import io
import process as process
from PIL import Image
# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [
        sg.Button("Histogram", key="-HIS-"),
        sg.Button("Logarit", key="-LOGA-"),
        sg.Button("Gamma", key="-GAM-"),
        sg.Button("Archive", key="-ARC-")

    ],
    # [
    #     sg.Button("Export", key="-EXP-")
    # ]
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left", size=(40,1), key='-TITLEORIGINAL-')],
    [sg.Image(key="-IMAGE-")],

    [sg.Text(size=(40, 1), key='-TITLE-')],
    [sg.Image(key="-IMAGEPROCESS-")],
]




# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Process", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break


    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".tif", ".jpg",".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            image = Image.open(filename)
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-TITLEORIGINAL-"].update("Original Image")
            window["-IMAGE-"].update(data=bio.getvalue())
            window["-IMAGEPROCESS-"].update()
            window["-TITLE-"].update("")


        except:
            pass
    if event == "-HIS-":
        process.Histo()
        window["-TITLE-"].update("Histogram Processing Image")
    if event == "-LOGA-":
        process.Loga()
        window["-TITLE-"].update("Logarit Processing Image")
    if event == "-GAM-":
        process.Gamma()
        window["-TITLE-"].update("Gamma Processing Image")
    if event == "-ARC-":
        process.Archive()
        window["-TITLE-"].update("Archiving Image")

window.close()
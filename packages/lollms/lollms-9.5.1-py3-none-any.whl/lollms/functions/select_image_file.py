from lollms.utilities import PackageManager, find_first_available_file_index, discussion_path_to_url
from lollms.client_session import Client
if not PackageManager.check_package_installed("pyautogui"):
    PackageManager.install_package("pyautogui")
if not PackageManager.check_package_installed("PyQt5"):
    PackageManager.install_package("PyQt5")
import cv2
import time
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from functools import partial


def select_image_file(processor, client):
    app = QtWidgets.QApplication(sys.argv)
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.ReadOnly
    file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image File", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
    if file_name:
        frame = cv2.imread(file_name)

        if frame is None:
            return "Failed to read the image file."

        view_image = client.discussion.discussion_folder/"view_images"
        image = client.discussion.discussion_folder/"images"
        index = find_first_available_file_index(view_image,"selected_image_",".png")
        fn_view = view_image/f"selected_image_{index}.png"
        cv2.imwrite(str(fn_view), frame)
        fn = image/f"selected_image_{index}.png"
        cv2.imwrite(str(fn), frame)
        client.discussion.image_files.append(fn)
        return f'<img src="{discussion_path_to_url(fn_view)}" width="80%"></img>'
    else:
        return "No file selected."

def select_image_file_function(processor, client):
    return {
            "function_name": "select_image_file",
            "function": partial(select_image_file, processor=processor, client=client),
            "function_description": "Opens a file dialog to select an image file and displays it.",
            "function_parameters": []                
        }
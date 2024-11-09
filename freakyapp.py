import tkinter as tk

class FreakyBobApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FreakyBob App")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Welcome to FreakyBob App!")
        self.label.pack()

        self.button = tk.Button(root, text="Get Freaky!", command=self.get_freaky)
        self.button.pack()

    def get_freaky(self):
        print("You're getting freaky!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FreakyBobApp(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from supports import check_spoiler



class Feedback:

    def __init__(self, mainframe):
        self.commentsList=[]
        self.showSpoiler=False
        self.spoiledComment=""
        mainframe.title('Add Your Comment')
        mainframe.resizable(False, False)
        mainframe.configure(background='#f7f7f7')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f7f7f7')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#f7f7f7', font=('Arial', 12))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.header_frame = ttk.Frame(mainframe)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text='Comment App', style='Header.TLabel').grid(row=0, column=1)
        ttk.Label(self.header_frame, wraplength=300,
                  text=(
                      'Add your name, email, and comment, then click submit to add your comment.  Click clear if you make a mistake.')).grid(
            row=1, column=1)

        self.content_in_frame = ttk.Frame(mainframe)
        self.content_in_frame.pack()

        ttk.Label(self.content_in_frame, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.content_in_frame, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.content_in_frame, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.comment_name = ttk.Entry(self.content_in_frame, width=24, font=('Arial', 10))
        self.comment_email = ttk.Entry(self.content_in_frame, width=24, font=('Arial', 10))
        self.comments = Text(self.content_in_frame, width=50, height=10, font=('Arial', 10))

        self.comment_name.grid(row=1, column=0, padx=5)
        self.comment_email.grid(row=1, column=1, padx=5)
        self.comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.content_in_frame, text='Submit',
                   command=self.submit).grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(self.content_in_frame, text='Clear',
                   command=self.clear).grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(self.content_in_frame,text='Show spoiler',command=self.spoiler).grid(row=4, column=2, padx=5,pady=5)
        



    def submit(self):
        print('Submit')
        self.comment=self.comments.get(1.0, 'end')
        print(f'Name: {self.comment_name.get()}')
        print(f'Email: {self.comment_email.get()}')
        print(f'Comments: {self.comment}')
        self.commentsList.append(self.comment)
        if(check_spoiler('Endgame',self.comment)=='spoiler'):
            print('Spoiler',self.showSpoiler)
            self.spoiledComment=self.comment
            self.comment=self.comment if self.showSpoiler else 'spoiler'
            
        print(self.comment)
        ttk.Label(self.content_in_frame, text=self.comment).grid(row=5, column=0, columnspan=2, padx=5)
        self.clear()
        messagebox.showinfo(title='Comment info', message='Thanks for your comment!')

    def clear(self):
        self.comment_name.delete(0, 'end')
        self.comment_email.delete(0, 'end')
        self.comments.delete(1.0, 'end')
    def spoiler(self):
        self.showSpoiler=not self.showSpoiler
        print(self.showSpoiler)
        self.comment=self.spoiledComment if self.showSpoiler else self.comments.get(1.0, 'end')
        ttk.Label(self.content_in_frame, text=self.comment).grid(row=5, column=0, columnspan=2, padx=5)

def main():
    root = Tk()
    root.geometry('500x400')
    feedback = Feedback(root)
    root.mainloop()


if __name__ == '__main__': main()
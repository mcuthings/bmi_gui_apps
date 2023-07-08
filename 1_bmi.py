"""
- 設定項目：身長、性別
- 数値（体重）入力
- 計算項目：BMI

"""
import tkinter as tk
import tkinter.font as font

class Bmi_Calculator(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.geometry("700x300" )
        self.master.title("BMI計算アプリ")

        myFont1= tk.font.Font(family= "Arial", size=40)
        
        # タイトル用フレーム
        frame_top=tk.Frame(self.master,bg='#fffaf0', padx=5, pady=10)
        frame_top.pack(fill="x")
        label = tk.Label(frame_top, text="BMI計算機", font=('Arial', '30'), bg='#d3d3d3',width=20, height=1, anchor = tk.CENTER, pady=0)
        label.pack(anchor=tk.CENTER)
        
        # BMI表示用メインフレーム
        frame_main = tk.Frame(self.master, pady=10, padx=10, bg='#fffaf0')
        frame_main.pack(expand=True, fill='both' )
        
        label_bmi = tk.Label(frame_main,text="BMI値", font=myFont1,bg='#fffaf0')
        self.label_result = tk.Label(frame_main,text="xxx", font=myFont1,bg='#fffaf0')
        label_kg = tk.Label(frame_main, text="kg", font =('Arial', '20'),bg='#fffaf0')
        label_cm = tk.Label(frame_main, text="cm", font =('Arial', '20'), bg='#fffaf0')
        self.entry_weight = tk.Entry(frame_main, width=6,font=('Arial', '20'))
        self.entry_height = tk.Entry(frame_main, width=6, font=('Arial','20'))
        button_cal = tk.Button(frame_main, command =self.cal, text="計算", font=myFont1,bg='#ffa500')

        label_bmi.grid(row=0, column=0, padx=40, pady=5)
        self.label_result.grid(row=0, column=1, padx=40, pady=5)
        label_kg.grid(row=0, column=3, padx=40, pady=5)
        label_cm.grid(row=1, column=3, padx=40, pady=5)
        self.entry_weight.grid(row=0, column=2,sticky=tk.E, ipady=10)
        self.entry_height.grid(row=1, column=2,sticky=tk.E, ipady=10)
        button_cal.grid(row=2, columnspan=4, ipady=10)
    def cal(self):
        height = float(self.entry_height.get())/100
        weight = float(self.entry_weight.get())
        result = weight/(height*height)
        #result = 100
        self.label_result['text']=f'{result:2.1f}'
        return
if __name__ == "__main__":
    root = tk.Tk()
    app = Bmi_Calculator(master=root)
    app.mainloop()

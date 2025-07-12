import tkinter as tk

root = tk.Tk()  # Tkinter 윈도우 객체 생성
root.geometry("300x200")  # 윈도우 크기 설정

# Label 위젯을 사용하여 "Hello World" 텍스트를 생성
label = tk.Label(root, text="Hello World", font=("Arial", 16))
label.place(relx=0.5, rely=0.5, anchor="center")  # 화면 중앙에 배치

root.mainloop()  # 이벤트 루프 시작
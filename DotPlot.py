from tkinter import *
from tkinter import ttk
import pylab

def align_sequences():
    """Create a dot matrix of the two DNA sequences specified by the user"""
    window = 1
    seq_one = firstSeq.get()
    seq_two = secondSeq.get()
    data = [[(seq_one[i:i + window] != seq_two[j:j + window]) \
        for j in range(len(seq_one) - window + 1)] \
        for i in range(len(seq_two) - window + 1)]
    pylab.gray()
    pylab.imshow(data)
    pylab.xlabel("%s (length %i bp)" % ("First sequence", len(seq_one)))
    pylab.ylabel("%s (length %i bp)" % ("Second sequence", len(seq_two)))
    pylab.title("Dot matrix using window size %i" % window)
    pylab.show()

root = Tk()
root.title ('Bioinformatics Dot Matrix')
frame = ttk.Frame(root)

firstSeq = StringVar()
secondSeq = StringVar()

# Widgets in the control frame
label1 = ttk.Label(frame, text = 'Specify two DNA sequneces with bases A, T, G, and C')
label2 = ttk.Label(frame, text = 'First sequence')
label3 = ttk.Label(frame, text = 'Second sequence')
entry1 = ttk.Entry(frame, textvariable = firstSeq)
entry2 = ttk.Entry(frame, textvariable = secondSeq)
button = ttk.Button(frame, text = 'Dot matrix', command = align_sequences)

frame.grid(column = 0, row = 0)
label1.grid(column = 0, row = 0, columnspan = 2)
label2.grid(column = 0, row = 1)
label3.grid(column = 0, row = 2)
entry1.grid(column = 1, row = 1)
entry2.grid(column = 1, row = 2)
button.grid(column = 2, row = 2)

root.mainloop()
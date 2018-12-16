#!/usr/bin/python

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

try:
    from tkinter import filedialog as tkFileDialog
except ImportError:
    import tkFileDialog

import threading

from sierpinski_triangle import SierpinskiTriangle, credits, IsIterable


class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Sierpinski Triangle')

        # Define settings
        self.menuTearOff = False
        # self.title = 'Sierpinski Triangle'
        self.fileFormats = (
            ('SVG', '*.svg'),
        )

        # yellow on black like a zelda triforce
        self.foregroundCol = '#FFFF00'
        self.backgroundCol = '#000000'
        self.sideLength = 600

        self.grid()

        self.CreateMenu()
        self.CreateControls()

        self.KeyBindings()

        self.st = SierpinskiTriangle(sideLength=self.sideLength)
        self.Display()

    def KeyBindings(self):
        '''Set keybindings corresponding to the accelerator text of the
        menu items, requires the event placeholder in each of the
        methods called.
        '''
        # file
        self.master.bind('<Control-r>', self.Reset)
        self.master.bind('<Control-o>', self.OpenFile)
        self.master.bind('<Control-s>', self.SaveFile)
        self.master.bind('<KeyRelease-Escape>', self.Quit)
        # if the user keys to quit then holding shift while releasing it will
        # nullify the close of the program
        self.master.bind('<Shift-KeyRelease-Escape>', lambda e: None)

        # edit
        self.master.bind('<Control-z>', self.Undo)
        self.master.bind('<Control-x>', self.OpenFile)
        self.master.bind('<Control-c>', self.SaveFile)
        self.master.bind('<Control-v>', self.Paste)

        self.master.bind('<F1>', self.Help)
        self.master.bind('<F12>', self.About)

    def CreateMenu(self):
        '''Define mainmenu and menu element holder.
        '''
        self.menubar = tk.Menu(self)
        self.casmenu = tk.Menu(self.menubar)

        # define File branch
        self.casmenu.file = tk.Menu(self.casmenu, tearoff=self.menuTearOff)
        self.casmenu.file.add_command(
            label='Reset',
            command=self.Reset,
            accelerator='Ctrl+R')
        self.casmenu.file.add_command(
            label='Open',
            command=self.OpenFile,
            accelerator='Ctrl+O')
        self.casmenu.file.add_command(
            label='Save As',
            command=self.SaveFile,
            accelerator='Ctrl+S')
        self.casmenu.file.add_separator()
        self.casmenu.file.add_command(
            label='Exit',
            command=self.Quit,
            accelerator='Esc')

        # define Edit branch
        self.casmenu.edit = tk.Menu(self.casmenu, tearoff=self.menuTearOff)
        self.casmenu.edit.add_command(
            label='Undo',
            command=self.Undo,
            accelerator='Ctrl+Z')
        self.casmenu.edit.add_separator()
        self.casmenu.edit.add_command(
            label='Cut',
            command=self.Cut,
            accelerator='Ctrl+X')
        self.casmenu.edit.add_command(
            label='Copy',
            command=self.Copy,
            accelerator='Ctrl+C')
        self.casmenu.edit.add_command(
            label='Paste',
            command=self.Paste,
            accelerator='Ctrl+V')

        # define Help branch
        self.casmenu.help = tk.Menu(self.casmenu, tearoff=self.menuTearOff)
        self.casmenu.help.add_command(
            label='Help',
            command=self.Help,
            accelerator='F1')
        self.casmenu.help.add_separator()
        self.casmenu.help.add_command(
            label='About',
            command=self.About,
            accelerator='F12')

        # add all cascading branches to main menu
        self.menubar.add_cascade(label='File', menu=self.casmenu.file)
        self.menubar.add_cascade(label='Edit', menu=self.casmenu.edit)
        self.menubar.add_cascade(label='Help', menu=self.casmenu.help)

        # connect main menu to form
        self.master.config(menu=self.menubar)

    def CreateControls(self):
        fCont = tk.Frame(self)

        tk.Button(fCont, text='Reset', command=self.Reset).pack(side=tk.LEFT)
        tk.Button(fCont, text='Step', command=self.Step).pack(side=tk.LEFT)

        self.vStep = tk.StringVar()
        tk.Label(fCont, textvariable=self.vStep).pack(side=tk.LEFT)

        self.vTriangles = tk.StringVar()
        tk.Label(fCont, textvariable=self.vTriangles).pack(side=tk.LEFT)

        self.vPoints = tk.StringVar()
        tk.Label(fCont, textvariable=self.vPoints).pack(side=tk.LEFT)

        self.vValuesStored = tk.StringVar()
        tk.Label(fCont, textvariable=self.vValuesStored).pack(side=tk.LEFT)

        self.vAreaRatio = tk.StringVar()
        tk.Label(fCont, textvariable=self.vAreaRatio).pack(side=tk.LEFT)

        fCont.grid(sticky=tk.W)

        # column span must be one more than number of previous controls
        # (to allow the blank extra one to take precidence in
        # absorbing extra space)

        self.cnv_Image = tk.Canvas(
            bd=0,
            width=self.sideLength,
            height=self.sideLength,
            background=self.backgroundCol)
        self.cnv_Image.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(1, weight=1)

    def Flatten(self, lst):
        """Taken from http://www.daniweb.com/code/snippet649.html no need to
        reinvent the wheel with this, it should be built-in.
        Changed from generator.
        """
        output = []
        for elem in lst:
            if IsIterable(elem):
                output.extend((i for i in self.Flatten(elem)))
            else:
                output.append(elem)
        return tuple(output)

    def Reset(self, event=None):
        self.st.Reset()
        self.Display()

    def OpenFile(self, event=None):
        pass

    def SaveFile(self, event=None):
        filename = tkFileDialog.asksaveasfilename(
            filetypes=self.fileFormats,
            defaultextension='')
        print('filename:', filename)
        if len(filename) > 0:
            buffer = [
                '<?xml version="1.0" encoding="UTF-8" standalone="no"?>',
                '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' +
                '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
                '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" ' +
                'width="%dpx" height="%dpx">' % (
                    self.sideLength, self.sideLength),
                '\t<!-- %s, Number of Steps: %s -->' % (
                    credits, self.st.steps),
                '\t<rect width="%s" height="%s" fill="%s"/>' % (
                    self.sideLength, self.sideLength, self.backgroundCol)
            ]

            fill = ' fill="%s"/>' % (self.foregroundCol)

            bufferData = (
                '\t<polygon points="%s,%s %s,%s %s,%s"' % (
                    self.Flatten(tri) + fill)
                for tri in self.st.triangles
            )
            buffer.extend(bufferData)

            buffer.append('</svg>\n')

            inFile = open(filename, 'w')

            inFile.write('\n'.join(buffer))

            inFile.close()
            print('SaveFile')
        else:
            print('SaveFile failed or was cancelled')

    def Quit(self, event=None):
        self.master.destroy()

    def Step(self, event=None):
        stepThread = threading.Thread(target=self.st.Step)

        stepThread.start()
        newStep = self.st.steps + 1
        print('Starting step: %d' % (newStep))

        stepThread.join()
        print('Finished calc step: %d' % (newStep))

        self.Display()
        print('Displayed step: %d' % (newStep))

    def Display(self):
        self.vStep.set('Steps = %d' % (self.st.steps))
        self.vTriangles.set('Triangles = %d' % self.st.NumOfTriangles())
        self.vPoints.set('Points = %d' % (self.st.NumOfTriangles()*3))
        self.vValuesStored.set(
            'Values Stored = %d' % (self.st.NumOfTriangles()*3*2))
        self.vAreaRatio.set('Area Ratio = %.3f : 1' % self.st.AreaProportion())

        self.cnv_Image.delete(tk.ALL)

        for triangle in self.st.triangles:
            self.cnv_Image.create_polygon(fill=self.foregroundCol, *triangle)

    def Undo(self, event=None):
        print('Undo')

    def Cut(self, event=None):
        print('Cut')

    def Copy(self, event=None):
        print('Copy')

    def Paste(self, event=None):
        print('Paste')

    def Help(self, event=None):
        print('Help')

    def About(self, event=None):
        print('About: %s' % (credits))


if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()

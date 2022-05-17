#!/usr/bin/env python
import wx

class MiMarco(wx.Frame):

    def __init__(self, imagen, padre=None, id=-1,
            pos=wx.DefaultPosition, titulo='Hola solo programadores'):
        temp = imagen.ConvertToBitmap()
        tamano = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, padre, id, titulo, pos, tamano)
        self.bmp = wx.StaticBitmap(self, -1, temp)

class MiAplic(wx.App):

    def OnInit(self):
        wx.InitAllImageHandlers()
        imagen = wx.Image('1.jpg', wx.BITMAP_TYPE_JPG)
        self.miMarco = MiMarco(imagen)
        self.miMarco.Show()
        self.SetTopWindow(self.miMarco)
        return True

if __name__ == '__main__':
    miAplic = MiAplic()
    miAplic.MainLoop()

class LoginGUI(wx.Frame):
    def __init__(self, registro, parent=None, id=-1, title='Juego tres en raya: login'):
        wx.Frame.__init__(self, parent, id, title)
        self.SetBackgroundColour(wx.WHITE)
        self.registro = registro

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menu1.Append(101, "&Salir", "Haz clic para salir")
        menuBar.Append(menu1, "&TresEnRaya")
        self.SetMenuBar(menuBar)
        wx.EVT_MENU(self, 101, self.OnSalir)

        nombreUsuarioLabel = wx.StaticText(self, -1, "Nombre usuario:")
        self.nombreUsuarioTxtCtrl= wx.TextCtrl(self, -1, "", size=(125, -1))

        passwordLabel = wx.StaticText(self, -1, "Password:")
        self.passwordTxtCtrl = wx.TextCtrl(self, -1, "", size=(125, -1), style=wx.TE_PASSWORD)

        ventanaLogin = LoginGUI(registro)

        self.botonNuevoUsuario = wx.Button(self, -1, "Nuevo usuario")
        wx.EVT_BUTTON(self, self.botonNuevoUsuario.GetId(), self.OnNuevoUsuario)
        self.botonLogin = wx.Button(self, -1, "Login")
        self.botonLogin.Enable(False)
        wx.EVT_BUTTON(self, self.botonLogin.GetId(), self.OnLogin)
        self.botonSalir = wx.Button(self, -1, "Salir")
        wx.EVT_BUTTON(self, self.botonSalir.GetId(), self.OnSalir)

        bsizer = wx.BoxSizer(wx.VERTICAL)

        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        topSizer.Add(nombreUsuarioLabel, 0, wx.GROW | wx.ALL, 4)
        topSizer.Add(self.nombreUsuarioTxtCtrl, 0, wx.GROW | wx.ALL | wx.ALIGN_RIGHT, 4)

        bsizer.Add(topSizer, 0, wx.GROW | wx.ALL, 4)

        wx.EVT_MENU(self, 101, self.OnSalir)

        botonAccionSizer = wx.BoxSizer(wx.HORIZONTAL)
        botonAccionSizer.Add(self.botonNuevoUsuario, 0, wx.GROW | wx.ALL, 4)

        wx.EVT_TEXT(self, self.nombreUsuarioTxtCtrl.

        GetId(), self.EvtText)
        bsizer.Add(botonAccionSizer, 0, wx.GROW | wx.ALL, 4)

        bsizer.Fit(self)
        self.SetAutoLayout(True)
        self.SetSizer(bsizer)
        wx.EVT_CLOSE(self, self.OnSalir)
        wx.EVT_BUTTON(self, self.botonSalir.GetId(), self.OnSalir)

    def OnSalir(self, evt):
        self.__cerrarAplicacion()

    def OnLogin(self, evt):
        try:
            self.registro.login(self.nombreUsuarioTxtCtrl.GetValue(), self.passwordTxtCtrl.GetValue())
        except:
            mostrarDialogo(self, 'No hay ningun usuario registrado con el nombre de usuario y password especificados', 'Login incorrecto')
            return
        try:
            self.ventanaUsuario = LoggedInGUI(self.nombreUsuarioTxtCtrl.GetValue(), self.passwordTxtCtrl.GetValue(), parent=self)
            self.ventanaUsuario.Show()
            self.Hide()
        except Exception, e: mostrarDialogo(self, "Problemas haciendo login para usuario" + self.nombreUsuarioTxtCtrl.GetValue() + ": " + str(e.args), "Error al hacer login")

    def OnNuevoUsuario(self, evt):

        ventanaNuevoUsuario = NuevoUsuarioGUI(self)
        ventanaNuevoUsuario.Show()
        self.Hide()

    def __cerrarAplicacion(self):

        if self.__dict__.has_key('ventanaUsuario'):
            if self.ventanaUsuario: self.ventanaUsuario.Destroy()
            self.Destroy()

    def EvtText(self, event):

        if len(self.nombreUsuarioTxtCtrl.GetValue().strip()) > 0 and len(self.passwordTxtCtrl.GetValue().strip()) > 0:
            self.botonLogin.Enable(True)
        else:
            self.botonLogin.Enable(False)

    def __initTablero(self):

        self.gridsizer = wx.GridSizer(3,3,0,0)
        self.celdaTablero = []
        self.bitmaps = []

        for i in range(9):

            self.bitmaps.append(wx.Bitmap ("images/1.png", wx.BITMAP_TYPE_PNG))
            self.celdaTablero.append(wx.BitmapButton (self, i, self.bitmaps[i]))

            wx.EVT_BUTTON(self, i , self.OnClick)
            self.gridsizer.Add(self.celdaTableroa[i])

        self.gridsizer.Fit(self)
        self.SetAutoLayout(True)
        self.SetSizer(self.gridsizer)

    def mostrarDialogo(ventanaPadre, mensaje, titulo, modo=wx.OK):

        dialog = wx.MessageDialog(ventanaPadre, mensaje, titulo, modo);
        dialog.ShowModal()

class EstadisticasGUI(wx.Frame):

    def __init__(self, ventanaUsuario, nombreUsuario, resultadoEstadisticas):

        self.anchura = 640
        self.altura = 480
        self.SetSize((self.anchura, self.altura))
        self.SetBackgroundColour(wx.WHITE)
        wx.EVT_PAINT(self, self.OnPaint)

    def OnPaint(self, evt):

        dc = wx.PaintDC(self)
        dc.Clear()
        dc.BeginDrawing()
        dc.SetPen(wx.Pen("BLACK",1))
        dc.SetBrush(wx.Brush("RED"))

        partidasJugadas = self.resultadoEstadisticas[0] + self.resultadoEstadisticas[1] + self.resultadoEstadisticas[2] + 0.0

        if partidasJugadas > 0: alturaBarraGanadas = int(250*(self.resultadoEstadisticas[0]/partidasJugadas))
            alturaBarraEmpatadas = int(250*(self.resultadoEstadisticas[1]/partidasJugadas))
            alturaBarraPerdidas = int(250*(self.resultadoEstadisticas[2]/partidasJugadas))

            if alturaBarraGanadas < 1:
                alturaBarraGanadas = 1
            if alturaBarraEmpatadas < 1:
                alturaBarraEmpatadas = 1
            if alturaBarraPerdidas < 1:
                alturaBarraPerdidas = 1
        else:

            alturaBarraGanadas = 1
            alturaBarraEmpatadas = 1
            alturaBarraPerdidas = 1

        cabecera = "Total partidas jugadas: " + str(int(partidasJugadas))
        (w, h) = dc.GetTextExtent(cabecera)
        dc.DrawText(cabecera, 320-(w/2), 70-h)

        (w, h) = dc.GetTextExtent("Ganadas")
        dc.DrawText("Ganadas", 160-(w/2), 390-h)
        dc.DrawRectangle(100, 350, 120, -alturaBarraGanadas)

        (w, h) = dc.GetTextExtent('self.resultadoEstadisticas[0]')
        dc.DrawText('self.resultadoEstadisticas[0]', 160-(w/2), 350-alturaBarraGanadas-20)

        dc.SetBrush( wx.Brush("GREEN"))
        dc.SetBrush( wx.Brush("BLUE") )
        dc.EndDrawing()

class RegistroJugadoresPersistente(RegistroJugadores):

    def __init__(self):
        RegistroJugadores.__init__(self)
        self._RegistroJugadores__jugadores = shelve.open("jugadores")
        if not self._RegistroJugadores__jugadores.has_key('solop'):
            self._RegistroJugadores__jugadores['solop'] = 'solop'
        self._RegistroJugadores__estadisticas = shelve.open("estadisticas")
        if not self._RegistroJugadores__estadisticas.has_key('solop'):
            self._RegistroJugadores__estadisticas['solop'] = [0, 0, 0]

    def __del__(self):
        self._RegistroJugadores__jugadores.close()
        self._RegistroJugadores__estadisticas.close()
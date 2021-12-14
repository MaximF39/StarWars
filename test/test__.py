def Slave(self):
    # try:
    a = PackageDecoder()
    a.data = self.Client.recv(8)
    index = a.readInt()
    if (index < Packages.ServerRequest.MIN and index > Packages.ServerRequest.MAX):
        a.data = self.Client.recv(a.readInt(), socket.MSG_WAITALL)
    Packages.PackagesMenager.initializePackage(index, a.data, self.id)
# except:
# import VacuumClient; VacuumClient.ConsoleLog(Localization.ResourceString.BotError.replace(Localization.ResourceString.NameIndex, self.User.login).replace(Localization.ResourceString.ErrorIndex, "Питон не умеет показывать ошибки 🤷"))
# self.disconnect(True)

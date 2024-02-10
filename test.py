def CheckCurrentDate(self, dtvalue):
    if dtvalue != None and dtvalue.lower() != 'none' and dtvalue != '' :
            currentdt = str(datetime.datetime.now()).split(" ")[0].split("-")
            crrdtobj = datetime.date(int(currentdt[0]), int(currentdt[1]), int(currentdt[2]))
            inputdt = str(dtvalue)
            test = ''
            if ( inputdt.find("/") >= 0 ):
                inputdtsplit = inputdt.split("/")
                inputdtobj = datetime.date(int(inputdtsplit[2]), int(inputdtsplit[0]), int(inputdtsplit[1]))
                list1 = []
            else:
                inputdtobj = datetime.date(int(inputdt[:4]), int(inputdt[4:6]), int(inputdt[6:]))
            if ( crrdtobj < inputdtobj ):
                    return False
            else:
                    return True
    else:
            return False


def CheckDate(self, fromdt, todt):
    if len(fromdt) == 8 and len(todt) == 8 and fromdt.isdigit() and todt.isdigit():
            frmyear = int(fromdt[:4])
            toyear = int(todt[:4])
            frmnth = int(fromdt[4:6])
            tomnth = int(todt[4:6])
            frmday = int(fromdt[6:])
            today = int(todt[6:])

            if frmyear > toyear:
                    return "To Date should be greater than From Date"
            elif (frmnth > tomnth and ( not (frmyear < toyear))):
                    return "To Date should be greater than From Date"
            elif (frmday > today and (not (frmyear < toyear)) and (not (frmnth < tomnth))):
                    return "To Date should be greater than From Date"
            else:
                    return True
    else:
            return None



def CheckCurrentDate(self, dtvalue):
    if dtvalue != None and dtvalue.lower() != 'none' and dtvalue != '' :
            print('1')
            currentdt = str(datetime.datetime.now()).split(" ")[0].split("-")
            crrdtobj = datetime.date(int(currentdt[0]), int(currentdt[1]), int(currentdt[2]))
            inputdt = str(dtvalue)
            print('2')
            test = ''
            if ( inputdt.find("/") >= 0 ):
                inputdtsplit = inputdt.split("/")
                print('3')
                inputdtobj = datetime.date(int(inputdtsplit[2]), int(inputdtsplit[0]), int(inputdtsplit[1]))
                list1 = []
                print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            else:
                print("hellllllllllllo")
                inputdtobj = datetime.date(int(inputdt[:4]), int(inputdt[4:6]), int(inputdt[6:]))
                print('4')
            if ( crrdtobj < inputdtobj ):
                    print('5')
                    return False
            else:
                    return True
    else:
            return False


def CheckDate(self, fromdt, todt):
    if len(fromdt) == 8 and len(todt) == 8 and fromdt.isdigit() and todt.isdigit():
            print('600000000000000000')
            frmyear = int(fromdt[:4])
            toyear = int(todt[:4])
            frmnth = int(fromdt[4:6])
            print('7')
            tomnth = int(todt[4:6])
            frmday = int(fromdt[6:])
            today = int(todt[6:])

            if frmyear > toyear:
                    print('8')
                    return "To Date should be greater than From Date"
            elif (frmnth > tomnth and ( not (frmyear < toyear))):
                    return "To Date should be greater than From Date"
            elif (frmday > today and (not (frmyear < toyear)) and (not (frmnth < tomnth))):
                    print('9')
                    return "To Date should be greater than From Date"
            else:
                    return True
    else:
            return None
            print('10')


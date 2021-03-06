def carType(type, name):
    type = type.lower()
    name = name.lower()
    if name.find('прицеп') != -1 or name.find('автоприцеп') != -1:
        return 'Автоприцеп'
    elif type == 'автомобили легковые':
        return 'Автомобиль легковой'
    return type

def getRelative(owner, name):
    if owner == name:
        return "null"
    return owner

def getOwner(owner, curOwner):
    if owner is not None:
        return owner
    else:
        return curOwner


def getSquareFloat(squareStr):
    return float(squareStr.replace(',', '.').replace(' м', '').replace(' п.м.', ''))


def needSquareComment(squareStr):
    if squareStr is not None:
        if squareStr.find('+') != -1:
            return True
    return False


def fixSquare(squareStr):
    if squareStr.find('+') != -1:
        sqSplit = squareStr.split()
        return sqSplit[0]
    return squareStr

def getSquare(squareStr):
    if squareStr is None:
        return 0.02
    squareStr = fixSquare(squareStr)
    return getSquareFloat(squareStr)


def getIncomeSize(sizeStr):
    return round(float(sizeStr.replace(' ', '').replace(',', '.')), 2)


def getParty(name):
    if name.find("ЕДИНАЯ РОССИЯ") != -1:
        return "Единая Россия"
    elif name.find("ЛДПР") != -1:
        return "ЛДПР"
    elif name.find("КПРФ") != -1:
        return "КПРФ"
    elif name.find("СПРАВЕДЛИВАЯ РОССИЯ") != -1:
        return "Справедливая Россия"
    return name


def replaceNullQuotes(inStr):
    return inStr.replace('"null"', 'null')




def getEstateType(type):
    type = type.lower()
    if (type.find('земельный участок') != -1):
        return 'Земельный участок'
    elif (type.find('жилой дом') != -1):
        return 'Жилой дом'
    elif (type.find('квартира') != -1):
        return 'Квартира'
    elif (type.find('дача') != -1):
        return 'Дача'
    elif (type.find('гараж') != -1):
        return 'Гараж'
    elif (type.find('иное') != -1):
        return 'Иное'
    else:
        return 'null'


def getAmountShare(share):
    try:
        return share[share.find("(") + 1:share.find(")")].split(', ')[1].split('/')
    except:
        return None

def getOwnType(type, default):
    type = type.lower()
    if (type.find('наем') != -1 or type.find('наём') != -1 or type.find('аренда') != -1):
        return 'Наём (аренда)'
    elif (type.find('безвозмездное пользование на срок полномочий депутата гд') != -1):
        return 'Служебное жилье'
    elif (type.find('безвозмездное пользование') != -1):
        return 'Безвозмездное пользование'
    else:
        return default

def getRoundEstateSize(size):
    return size

def addComment(comment, msg):
    if comment != '':
        return comment + '. ' + msg
    else:
        return comment + msg

def getEstateComment(estatesTd):
    comment = ''
    for i in range(0, len(estatesTd)):
        if estatesTd[i] is not None:
            comment += estatesTd[i] + ' '
    if len(comment) != 0:
        return comment[0:len(comment) - 1]

def haveOwnEstate(paramSearch):
    for i in paramSearch:
        if i.text == "принадлежащие на праве собственности":
            return True
    return False


def haveUseEstate(paramSearch):
    for i in paramSearch:
        if i.text == "находящиеся в пользовании":
            return True
    return False


def getRole(role):
    if role is not None:
        return role
    else:
        return ""

def writeLog(lineArgs, log):
    for i in lineArgs:
        log.write(str(i) + " ")
    log.write("\n")
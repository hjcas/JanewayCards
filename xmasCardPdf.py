import io
import pandas
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Cour', 'cour.ttf'))
pdfmetrics.registerFont(TTFont('Arvo', 'Arvo-Bold.ttf'))
pdfmetrics.registerFont(TTFont('WSB', 'WorkSans-Bold.ttf')) 
pdfmetrics.registerFont(TTFont('WSR', 'WorkSans-Regular.ttf'))   
pdfmetrics.registerFont(TTFont('WSSB', 'WorkSans-SemiBold.ttf')) 

# Iterative Python program to count
# number of digits in a number
def countDigit(n):
	count = 0
	while n != 0:
		n //= 10
		count += 1
	return count

# Standardizes the number of digits in the ticketNumber to 6 
def standardizeDigits(digits, ticketNumber):
    if digits == 1 :
        result = f"00000{ticketNumber}"
    elif digits == 2 :
        result = f"0000{ticketNumber}"
    elif digits == 3 :
        result = f"000{ticketNumber}"
    elif digits == 4 :
        result = f"00{ticketNumber}"
    elif digits == 5 :
        result = f"0{ticketNumber}"
    else :
        result = f"{ticketNumber}"
    return result
    
def parseTicketNumber(ticketNum,index):
    parseOne = ticketNum.split(';')[2 + (9*index)]
    parseTwo = parseOne.split(':')[2]
    extractedTicketNumber = parseTwo.split('"')[1]

    digits = countDigit(int(extractedTicketNumber))
    ticketNumFinal = standardizeDigits(digits, extractedTicketNumber)
    return ticketNumFinal    

def insertVals(c, n, special):
    
    ticketNum = df.iloc[n,0]
    to = df.iloc[n,1]    
    fromX = df.iloc[n,2]
    
    parseNumberOfTickets = ticketNum.split(':')[1]

    #Left Xmas Card  
    c.setFont("WSSB",7)
    c.drawString(43, 283, f'Happy Holidays, {to}')
    c.drawString(43, 200, f"Best wishes, {fromX}")

    #Used to handle if there is no right card to print
    if (not special) :
        ticketNum_ = df.iloc[n+1,0]
        to_ = df.iloc[n+1,1]    
        fromX_ = df.iloc[n+1,2]

        parseNumberOfTickets_ = ticketNum_.split(':')[1]
        
        #Right Xmas Card
        c.drawString(528, 283, f"Happy Holidays, {to_}")
        c.drawString(528, 200, f"Best wishes, {fromX_}")

    # #Ticket Numbers
    # c.setFont("Cour",5)
    # l = 0
    # for j in range(5):
    #     for i in range(5):
    #         #Left Xmas Card
    #         ticketNumFinal = parseTicketNumber(ticketNum,l)
    #         c.drawString(49.5+(48*i), 168-(7*j), f"{ticketNumFinal}")

    #         #Used to handle if there is no right card to print
    #         if(not special):
    #             #Right Xmas Card
    #             ticketNumFinal_ = parseTicketNumber(ticketNum_,l)
    #             c.drawString(533+(48*i), 168-(7*j), f"{ticketNumFinal_}")
    #         l = l + 1

    if (parseNumberOfTickets == '3') :
        initialX = 97.5
        forLoopOne = 1
        forLoopTwo = 3
    elif (parseNumberOfTickets == '10') :
        initialX = 49.5
        forLoopOne = 2
        forLoopTwo = 5
    else:
        initialX = 49.5
        forLoopOne = 5
        forLoopTwo = 5
    
    #Ticket Numbers
    c.setFont("Cour",5)
    l = 0
    for j in range(forLoopOne):
        for i in range(forLoopTwo):
            #Left Xmas Card
            ticketNumFinal = parseTicketNumber(ticketNum,l)
            c.drawString(initialX+(48*i), 168-(7*j), f"{ticketNumFinal}")
            l = l + 1        

    if (parseNumberOfTickets_ == '3') :
        initialX_ = 581
        forLoopOne_ = 1
        forLoopTwo_ = 3
    elif (parseNumberOfTickets_ == '10') :
        initialX_ = 533
        forLoopOne_ = 2
        forLoopTwo_ = 5
    else:
        initialX_ = 533
        forLoopOne_ = 5
        forLoopTwo_ = 5

    #Ticket Numbers
    c.setFont("Cour",5)
    l = 0
    for j in range(forLoopOne_):
        for i in range(forLoopTwo_):
            #Used to handle if there is no right card to print
            if(not special):
                #Right Xmas Card
                ticketNumFinal_ = parseTicketNumber(ticketNum_,l)
                c.drawString(initialX_+(48*i), 168-(7*j), f"{ticketNumFinal_}")
            l = l + 1                        

df = pandas.read_csv('orders1.csv')

for x in range(0,len(df),2):
    special = False

    if(x == (len(df)-1)):
        special = True

    packet = io.BytesIO()
    # # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    insertVals(can, x, special)
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("Festive5050CardTemplate.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("order(%d).pdf" % (x/2) , "wb" )
    output.write(outputStream)
    outputStream.close()
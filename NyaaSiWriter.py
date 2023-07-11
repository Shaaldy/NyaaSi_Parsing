import xlsxwriter
from parsNyaaSi import array
def writer(parametr):
    book = xlsxwriter.Workbook("parsTest2.xlsx")
    page = book.add_worksheet("Anime")

    row = 1
    coloumn = 0
    page.write(0, coloumn, "Subers")
    
    page.write(0, coloumn + 1, "Name")
    
    page.write(0, coloumn + 2, "Episode")
    
    page.write(0, coloumn + 3, "Quality")
    
    page.write(0, coloumn + 4, "Torrent")

    page.write(0, coloumn + 5, "Date")


    page.set_column("A:A", 20)
    page.set_column("B:B", 40)
    page.set_column("C:C", 10)
    page.set_column("D:D", 10)
    page.set_column("E:E", 50)
    page.set_column("F:F", 18)

    for item in parametr():
        page.write(row, coloumn, item[0])
        page.write(row, coloumn+1, item[1])
        page.write(row, coloumn+2, item[2])
        page.write(row, coloumn+3, item[3])
        page.write(row, coloumn+4, item[4])
        page.write(row, coloumn+5, item[5])
        row+=1

    book.close()

writer(array)

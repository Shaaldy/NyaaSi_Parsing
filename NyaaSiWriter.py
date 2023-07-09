import xlsxwriter


def writer(parametr):
    book = xlsxwriter.Workbook("parsNyaaSi.xlsx")
    page = book.add_worksheet("Anime")

    row = 1
    coloumn = 0
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 10)
    page.set_column("E:E", 70)

    for item in parametr():
        page.write(row, coloumn, item[0])
        page.write(row, coloumn+1, item[1])
        page.write(row, coloumn+2, item[2])
        page.write(row, coloumn+3, item[3])
        page.write(row, coloumn+4, item[4])
        row+=1

    book.close()

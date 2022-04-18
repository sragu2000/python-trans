from googletrans import Translator
import xlsxwriter   
f1=open("products.txt","r")  
book = xlsxwriter.Workbook('result.xlsx')     
sheet = book.add_worksheet()
row = 0    
column = 0   
translator = Translator()
count=1
for i in f1:
    word=i.strip()
    print(word," ",count)
    sheet.write(row, column, word)  
    translation = translator.translate(word, dest='ta')#tamil
    sheet.write(row, column+1, translation.text) 
    translation = translator.translate(word, dest='pa')#punjabi
    sheet.write(row, column+2, translation.text) 
    translation = translator.translate(word, dest='hi')#hindi
    sheet.write(row, column+3, translation.text) 
    translation = translator.translate(word, dest='zh-cn')#chinese
    sheet.write(row, column+4, translation.text) 
    row+=1
    count+=1
book.close()    
print("Finished")
"""TXT UZANTILI DOSYAYA MAİLİ GÖNDERMEK İSTEDİĞİMİZ MAİL ADRESLERİNİ YAZIYORUZ VE BÖYLECE TOPLU MAİL GÖNDERME İŞLEMİ GERÇEKLEŞTİRMİŞ OLUYORUZ.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


with open("mail.txt","r",encoding="utf-8") as file:
    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        mesaj = MIMEMultipart()

        mesaj["From"] = "mailin_gonderildigi_mail_adresi"

        mesaj["To"] = satır_elemanları[1]

        mesaj["Subject"] = "Smtp Mail Gönderme"

        yazi ="""
         
         Smtp ile mail gönderiyorum..
                
         
         """





        mesaj_govdesi = MIMEText("Merhaba\n"+satır_elemanları[0]+yazi, "plain")

        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login("mail_adresi", "sifre")

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

            print("Mail Başarıyla Gönderildi....")

            mail.close()

        except:
            sys.stderr.write("Bir sorun oluştu!")
            sys.stderr.flush()




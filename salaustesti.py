# Hannu Mäkilampi 2021

from datetime import datetime
from os import system

# otetaan vastaan luku, luodaan aikaleima, kerrotaan se vastaanotetulla luvulla ja
# palautetaan tulosta 6 ensimmäistä numeroa stringinä
def authenticator(checkNum):
  timeNow = int(datetime.now().strftime("%S%M%H%d%m%Y"))
  authenticatorToken = str(timeNow * int(checkNum))[:6]
  return authenticatorToken

# kertoo annetun salasanan syntymäajalla, korvaa numerot salaKirja-dictionaryn
# mukaan ja palauttaa muutetun stringin
def hash(synty,salis):
  monimutkainen = int(synty) * int(salis)
  hashattu = ""
  for ch in str(monimutkainen):
    hashattu += str(salaKirja.get(ch))
  return hashattu

# ottaa vastaan käyttäjän ja tekee 2 tiedostoa: 
# käyttäjän nimen mukaisen txt-tiedoston, johon tallentaa salatun salasanan ja
# kayttajasynty.txt tiedoston, johon tallentaa syntymäajan
def luoKayttaja(name,synty,hashSalis):
  with open(f'{name}.txt','w') as userFile:
    userFile.write(hashSalis)
    userFile.close()
  with open(f'{name}synty.txt', 'w') as userSynty:
    userSynty.write(synty)
    userSynty.close()

# tarkoituksella epämääräinen ilmoitus väärästä salasanasta / tunnuksesta / tunnusluvusta
def vaarinMeni():
    print("")
    print("Wrong credentials!")
    print("")

# dictionary, jossa määritellään numeroita 1-9 vastaavat merkkijonot
salaKirja = {
  "1" : "fheopgheri 8y98glkrne9h9grh",
  "2" : "jdwiwei098hojnonoiniofnwe",
  "3" : "fwe   n89 9898 ehfhnlknklnk",
  "4" : "ln  wem,m,nnm,, jnnnoioidfv",
  "5" : "h8f9we h98h098hf90weh09c  jopasdasasdw",
  "6" : "mpqw  dqwnaew ",
  "7" : "fji ew 222 aa sda 9 dsadjl ",
  "8" : "knnen n,mn,dwqm233232nn,mnn,nm,",
  "9" : "nlkklnnklsdfnin ,n,nnjnnnon"
} 

### tällä koodilla voi luoda ylläpitäjän salasanan
'''
masterPass = input("Anna ylläpitäjän salasana: ")
checkNumber = input("Anna tarkistenumero: ")
hash(masterPass,checkNumber)

with open("masterpass.txt", "w") as mpass:
  mpass.write(hash(masterPass,checkNumber))
  mpass.close()
'''
###


# valitaan toiminto, joko luodaan uusi käyttäjä tai valitaan olemassaoleva
menuQuit = False
while True:
  while True:
    print("")
    print("Choose 1) for existing user, 2) for creating a user or 3) quit.")
    valinta = input("Your choice: ")
    if valinta == "2":

# kyselllään mastersalasana
        while True:
          try:
            masterPass = int(input("Give master password: "))
            break
          except:
            print("Not a number!")

# kysellään mastersalasanan yhteydessä määritelty tarkistenumero
        while True: 
          try:
            masterCheck = int(input("Give check number: "))
            break
          except:
            print("Not a number!")

# tarkistetaan, onko oikein ja jos on, luodaan kertakäyttötunniste
        with open("masterpass.txt", 'r') as mpass:
          savedMasterPass = mpass.read()
          mpass.close()
        if hash(masterPass,masterCheck) == savedMasterPass:
          masterToken = authenticator(masterPass)
          print(masterToken)
          givenMasterToken = input("Enter authenticator token: ")
          if givenMasterToken == masterToken:
            print("")
            name = input("anna nimi: ")
            synty = input("anna syntymäaika (ppkkvv): ")
            salis = input("anna uusi salasana (numeroita 1-9 peräkkäin:")
            hashSalis = hash(synty,salis)
            luoKayttaja(name,synty,hashSalis)
          else: 
            vaarinMeni()
        else: 
          vaarinMeni()

    elif valinta == "1":
      break

    elif valinta == "3":
      menuQuit = True
      break
  
  if menuQuit == True:
    print("Quitting program.")
    quit()

  # kysytään käyttäjänimi ja salasana, avataan käyttäjänimen mukainen tiedosto
  # salataan salasan kuten sitä luodessa ja verrataan salattua muotoa tiedostossa olevaan
  # jos ok, pääsee eteenpäin
  while True:
    userChoice = ""
    goodPass = ""
    try:
      userChoice = input("Username: ")
      with open(f'{userChoice}.txt', 'r') as chosenUser:
          goodPass = chosenUser.read()
          chosenUser.close()
          userNameOk = True
      break
    except:
      print("")
      print("No such username!")
      userNameOk = False
      break

  if userNameOk == True:

    while True:
      try: 
        passWord = int(input("Password: "))
        break
      except:
        print("Not a number!")

    with open(f'{userChoice}synty.txt', 'r') as chosenUserSynty:
        goodDate = chosenUserSynty.read()
        chosenUserSynty.close()

    givenPassword = hash(passWord,goodDate)
    if givenPassword == goodPass:
      token = authenticator(goodDate)
      print(token)
      givenAuthToken = input("Enter authenticator token: ")
      if givenAuthToken == token: 
          print("Correct password!")
          break
      else:
          vaarinMeni()

    else: 
        vaarinMeni()

print("Pääsit eteenpäin ohjelmassa")

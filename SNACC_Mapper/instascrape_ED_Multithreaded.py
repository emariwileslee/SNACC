# Generated by Selenium IDE
import pytest
import time
from time import sleep
from datetime import datetime
import json
from math import ceil
from math import floor
import requests as r
import pandas as pd
import threading
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

class InstaScrape():
  def __init__(self,URL):
    self.driver =  webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get(URL)
    self.allUserList = []
    self.allUnifiedList = []
    self.seed = URL
    #self.allCommentList = []
    self.currDate = datetime.now()
    #self.driver.maximize_window()
    
  def setup_method(self, method):
    #self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def login(self,USERNAME,PASSWORD):#This is used to sign into instagram with a user account to allow greater viewing privelege
   self.driver.get("https://www.instagram.com/accounts/login/")
   element_present = EC.presence_of_element_located((By.NAME,"username"))
   WebDriverWait(self.driver,10).until(element_present)
   if self.driver.find_element(By.NAME, "username"):
        sleep(1)#AFTER PROTOTYPING USE WEB WAIT FOR SLEEP
        self.driver.find_element(By.NAME, "username").click()
        # 7 | type | name=username |
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME) #USERNAME
        # 8 | click | name=password |  | 
        self.driver.find_element(By.NAME, "password").click()
        # 9 | type | name=password |
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD) #PASSWORD
        # 10 Click login button on the sign in page
        self.driver.find_element(By.CSS_SELECTOR, ".sqdOP > .Igw0E").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"))).click()
        except:
            print("Could not complete login")
   else:
        #Selects the login button at the root page
        element = self.driver.find_element(By.CSS_SELECTOR, "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > span > a:nth-child(1) > button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        #Selects the center login terminal
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions.move_to_element(element).perform()
        # 5 | click | css=.tdiEy > .sqdOP |  | 
        self.driver.find_element(By.CSS_SELECTOR, ".tdiEy > .sqdOP").click()
        # 6 | click | name=username |  | 
        sleep(1)#AFTER PROTOTYPING USE WEB WAIT FOR SLEEP
        self.driver.find_element(By.NAME, "username").click()
        # 7 | type | name=username |
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME) #USERNAME
        # 8 | click | name=password |  | 
        self.driver.find_element(By.NAME, "password").click()
        # 9 | type | name=password |
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD) #PASSWORD
        # 10 Click login button on the sign in page
        self.driver.find_element(By.CSS_SELECTOR, ".sqdOP > .Igw0E").click()
        # 13 Selects "Not Now" when prompted to save credentials
        #sleep(2)
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"))).click()
        except:
            print("Could not complete login")
    
  def logout(self):#This is used to log out of a user account
    #This clicks the profile menu
    self.driver.find_element(By.CSS_SELECTOR, ".qNELH > .\\_6q-tv").click()
    #This clicks the logout button
    self.driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/div/div/div/div/div").click()
    
  def page_nav(self,ROWS,COLUMNS,KEYWORD):# This is used to navigate to individual posts on the page
    X = 0 #Set to 0 by default, use for manual post selection control
    Y = 0 #Set to 0 by default, use for manual post selection control
    sleep(2)
    #self.driver.find_element(By.CSS_SELECTOR, "div.Nnq7C:nth-child({1}) > div:nth-child({0}) > a:nth-child(1)".format(X,Y)).click() #2D Grid(X,Y) - First "nth-child" = Y and Second "nth-child" = X. Third "nth-child" should not change
    #sleep(1)
    #InstaScrape.likes_grab(self)

    for k in range(1,2):#DONT CHANGE
        if(k>1):
            for c in range(0,2):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2.25)
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 600);") #335
            sleep(30)
        for i in range(1,(COLUMNS+1)): 
            Y = i
            #rowNumber+=1
            #print("Row: ",rowNumber)
            for j in range(1,(ROWS+1)): #CHANGE THIS TO REGULATE NUMBER OF COLUMNS TO SCAN !!!
                X = j
                #postNumber+=1
                #print("Post: ",postNumber)
                print("Coordinates(X,Y): {0}, {1}".format(X,Y))
                #try:
                bio = InstaScrape.bio_Grab(self)
                #print(bio)
                try:
                    self.driver.find_element(By.CSS_SELECTOR, "div.Nnq7C:nth-child({1}) > div:nth-child({0}) > a:nth-child(1)".format(X,Y)).click() #2D Grid(X,Y) - First "nth-child" = Y and Second "nth-child" = X. Third "nth-child" should not change
                except:
                    print("Grid Structure Not Found")
                    pass
                #except NoSuchElementException:
                    #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    #sleep(4)
                    #self.driver.find_element(By.CSS_SELECTOR, "div.Nnq7C:nth-child({1}) > div:nth-child({0}) > a:nth-child(1)".format(X,Y)).click()
                                         
                sleep(1)
                if InstaScrape.trendConnectionID(bio,KEYWORD) == True or InstaScrape.trendConnectionID(InstaScrape.comment_Grab(self),KEYWORD) == True:
                    InstaScrape.likes_grab(self)
                else:
                    print("Keyword Not Found")
                try:
                    self.driver.find_element(By.CSS_SELECTOR, "div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button:nth-child(1)").click()#Close post
                except:
                    pass
                sleep(0.5)
    
  def likes_grab(self):#Navigate to post then call this function after
    try:
        likeNumstr = self.driver.find_element(By.CSS_SELECTOR, "div.Nm9Fw:nth-child(1) > button:nth-child(1) > span:nth-child(1)").text
        if likeNumstr.find(",") != -1:
            likeNumstr = likeNumstr.replace(',','')
        likeNum = int(likeNumstr)
        print("Number of likes : ", likeNum)
        self.driver.find_element(By.CSS_SELECTOR, "div.Nm9Fw:nth-child(1) > button:nth-child(1)").click()#Open likes
        sleep(2)
        source = ""
        userList = []
        cycleNum = ceil((10*likeNum) / 36) + 1 #Number of Cycles addition +1 cycle is performed for accuracy
        #currentUser = 11
        for x in range(cycleNum):
            InstaScrape.likes_scroll(self,10)#Set to 48 for subsequent total list transversal
            sleep(0.1)
            #print("CYCLE: ",x+1)
    
            for i in range(1,20):
                try:
                    source = self.driver.find_element(By.CSS_SELECTOR,"div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child({0}) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)".format(i)).text
                except NoSuchElementException:
                    pass
                if((source in userList)==False):
                    userList.append(source)
                    
       
        '''print("START OF ARRAY PRINT")
        for i in userList:
            print(i) '''
            
        print("userList Final Size: ",len(userList))
        self.driver.find_element(By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button").click()#Close likes
        sleep(0.5)
        #self.driver.find_element(By.CSS_SELECTOR, "div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button:nth-child(1)").click()#Close post
        for i in userList:
            if((i in self.allUserList)==False):#Ensures only new usernames are recorded, no repeats
                self.allUserList.append(i)
                
    except NoSuchElementException:
        print("No likes found")
        #self.driver.find_element(By.CSS_SELECTOR, "body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button").click()#Close post
  
  def likes_scroll(self,N_Tab): #N_Tab is number of times to press, set to 66 for total list transversal
    element = self.driver.find_element(By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    for i in range(N_Tab):
        actions.send_keys(Keys.TAB)
        
    actions.perform()    
    self.driver.execute_script("arguments[0].scrollIntoView();",element)
   
  def comment_Grab(self):
      try:
          firstComment = self.driver.find_element(By.CSS_SELECTOR,"div.C4VMK:nth-child(2) > span").text
          #print(firstComment)
          return firstComment
      except:
          pass
  def bio_Grab(self):
      try:
          bio = self.driver.find_element(By.CSS_SELECTOR,"#react-root > section > main > div > header > section > div.-vDIg > span").text
          #print(firstComment)
          return bio
      except:
          pass    
  def trendConnectionID(textData,substring):
      #print(textData)
      textData = str(textData)
      upper = substring.upper()
      lower = substring.lower()
      if textData.find(upper) !=-1 or textData.find(lower) !=-1:
          print("Found",substring)
          return True
      else:
         print(substring, "Not Found")
         return False
         
  def totalUsernamePrint(self):
    for i in self.allUserList:
        print(i)
    print("Total of All Usernames Collected: ",len(self.allUserList))
  
  def returnUsernameList(self):
      return self.allUserList
  
  def Insta_User_Branching(self, ROWS,COLUMNS,KEYWORD):
    for i in self.allUserList:
        print(i)
        URL = "https://www.instagram.com/"+i+"/"
        self.driver.get(URL)
        try:
            self.page_nav(ROWS,COLUMNS,KEYWORD)
        except NoSuchElementException:
            pass
        print("Total of All Usernames Collected: ",len(self.allUserList))
  def seedSelect(self):
      currentUrl = self.driver.current_url
      if currentUrl != self.seed :
          self.driver.get(self.seed)
      else:
          pass
  def userRedirect(self,url):
      self.driver.get(url)

  '''def multiThreadBranching(self, ROWS,COLUMNS,KEYWORD, currentUser):
      URL = "https://www.instagram.com/"+currentUser+"/"
      self.driver.get(URL)
      try:
          self.page_nav(ROWS,COLUMNS,KEYWORD)
      except NoSuchElementException:
          pass
      print("Total of All Usernames Collected: ",len(self.allUserList))'''
 
class botGenerator():
    def __init__(self,genType):
        self.genType = genType
        self.gmailURL = "https://accounts.google.com/signup/v2"
        self.driver =  webdriver.Chrome(ChromeDriverManager().install())
    
    def gmailCreation(self):
        self.driver.get(self.gmailURL)

class nodeClassifier():
    def __init__(self):
        self.node_df = pd.DataFrame(columns=["parent_node","username","connection_type"])
        
    def addNode(self,parent_node,username,connection_type):
        nodeBuffer = [parent_node,username,connection_type]
        self.node_df = self.node_df.append(pd.Series(nodeBuffer,index=self.node_df.columns),ignore_index=True)
        #print(self.node_df)
     
    def printNetwork(self):
        print(self.node_df)
     
    def exportNetwork(self):
        self.node_df.to_csv(r'C:\Users\emari\Documents\Engineering Design 1\Trend Network Mapper Prototype\Web Scraping\SNACC_Mapper\Output\output.csv',index=False)
       
class myThreads(threading.Thread):
   def __init__(self, threadID, name, counter, url, event):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.url = url
      #self.currentLoad = 0
      self.ROWS = 1
      self.COLUMNS = 1
      self.KEYWORD = "FAU"
      self.event_obj = event
      #self.startFlag = self.event_obj.wait()
      self.username = "ewltest99"
      self.password = "K6JTy5zFbVsN2gs"
      print("ACTIVE THREADS CURRENTLY: ", threading.active_count())
    
   def run(self):
      if(self.threadID==0):
          self.mainThread()
      else: 
          self.childThread()
          
   def mainThread(self):
      global userList
      global currentLoad
      global root_node
      global node_db
      node_db = nodeClassifier()
      print("Starting "+self.name)
      instance = InstaScrape(self.url)
      instance.login(username,password)
      instance.seedSelect()
      
      root_node = root_profile
      instance.page_nav(self.ROWS,self.COLUMNS,self.KEYWORD)# ROWS, COLUMNS
      userList = instance.returnUsernameList()
      print(userList)
      currentLoad = floor(len(userList) / 4)#CHANGE THIS 6 TO ADUST LOAD FOR RIGHT NOW
      #instance.Insta_User_Branching(3,1,KEYWORD)# ROWS, COLUMNS
      
      #sleep(5)
      print("Exiting ", self.name)
      instance.teardown_method()
      self.event_obj.set()
      #self.event_obj.clear()
      #sys.exit()
      
   def childThread(self):
      global node_db
      global userList
      global currentLoad
      global root_node
      index = ((self.threadID-1) * currentLoad)
      
      print("Starting "+self.name)
      #print(userList)
      if self.threadID==1:
          print("This is index", index)
          print("This is current load", currentLoad)
      currentURL = "https://www.instagram.com/"+userList[index]+"/"
      instance = InstaScrape(currentURL)
      instance.login(username,password)
      instance.seedSelect()
      for i in userList[index:(index*2)]:
          print(i)
          node_db.addNode(root_node, i,'unknown')
          currentURL = "https://www.instagram.com/"+i+"/"
          instance.userRedirect(currentURL)
          instance.page_nav(self.ROWS,self.COLUMNS, self.KEYWORD)
      
      
      print("Exiting ", self.name)
      instance.teardown_method()
      #instance.teardown_method()
      #sys.exit()
        
   def checkStartFlag(self):
       if self.event_obj.is_set()==True:
           print("Event triggered")
           self.event_obj.set()
           return True
       else:
           print("NO Trigger")
           return False
   def printGlobalUserList(self):
       global userList
       global node_db
       node_db.exportNetwork()
       node_db.printNetwork()
       print("Final user network list: ")
       for i in userList:
           print(i)
       sys.exit()











start = time.time()
#instance = botGenerator('instagram')
#instance.gmailCreation()



username = "ewltest99"
password = "K6JTy5zFbVsN2gs"
root_profile = "fauorientation"        
url = "https://www.instagram.com/"+root_profile+"/"#"https://www.instagram.com/explore/tags/als/"
#redirect_url = "https://www.instagram.com/fauhousing/live/"
output_location = r'C:\Users\emari\Documents\Engineering Design 1\Trend Network Mapper Prototype\Web Scraping\Scrapped Content'
KEYWORD = "FAU"
START_THREADS = threading.active_count()
MAX_THREADS = 4#Starts at 0, Must be at least 1
MAX_THREADS += 1
exit_flag = False

initialEvent = threading.Event()
threadArray = {}
threadArray[0] = myThreads(0,"Thread-0",0,url,initialEvent)
threadArray[0].start()

for i in range(1,MAX_THREADS):
    initialEvent.wait()
    threadArray[i] = myThreads(i,"Thread-%d"%i,i,url,initialEvent)
    print("Creating ", threadArray[i].name)
    #print("Initial thread complete")
    threadArray[i].start()
    #print("ACTIVE THREADS CURRENTLY: ",threadArray[i].active_count())
    #threadArray[i].join()

while not exit_flag:
    if not threading.active_count()>START_THREADS:
        exit_flag = True
        threadArray[MAX_THREADS+1] = myThreads(MAX_THREADS+1,"Final Thread",MAX_THREADS+1,url,initialEvent)
        threadArray[MAX_THREADS+1].printGlobalUserList()
        
#threadArray[MAX_THREADS+1] = myThreads(MAX_THREADS+1,"Final Thread",MAX_THREADS+1,url,initialEvent)
#threadArray[MAX_THREADS+1].printGlobalUserList()


#for i in range(1,6):
    #threadArray[i].start()

#instance.page_nav(3,1,KEYWORD)# ROWS, COLUMNS
#.Insta_User_Branching(3,1,KEYWORD)# ROWS, COLUMNS
  
#instance.totalUsernamePrint()

#instance.teardown_method()'''
end = time.time()
print("Execution Time: ",end-start, " seconds")


#Where nicknames on likes are stored
#div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) #Fourth "nth-child" tranverses username down
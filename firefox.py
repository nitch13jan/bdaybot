from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException   



driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("botbday@gmail.com")
elem = driver.find_element_by_name("pass")
elem.clear()
elem.send_keys("botbday56")
elem.send_keys(Keys.RETURN)
delay = 30

try:
    elem=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,"_2s25")))
    time.sleep(5);
    elem.click();
    print ("Successfully Logged in");
except TimeoutException:
    print ("Timeout or wrong email/password") ;
    driver.close();

def post_checker(post):
    hpylst = ['happy','hapy','hapi','appy','hpy','#appy']
    bdylst = ['birthday','bday','budday','b\'day','bdy','b\'day!']
    return any(word in post for word in hpylst) and any(word in post for word in bdylst)
posts=[]
try:
    WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,"_2s25")))
    
    count=0
    no_of_postliked=0
    posts=WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME,'userContentWrapper')))
    npt=0
    time.sleep(8)
    
    while 1:
         try:
         
          driver.find_element(By.CLASS_NAME,"_44b2").click()
          time.sleep(5)
         except NoSuchElementException:
          print(" All post unveiled!.....")
          break;
      
    count=0
    posts=driver.find_elements_by_class_name('userContentWrapper')
    print("Total ",len(posts)," element in posts....")
    for post in posts:
        count+=1
        #post.click()
        driver.execute_script("return arguments[0].scrollIntoView();", post)
        print("count=",count,"\n")
        post_text=post.find_element_by_xpath(".//div[@class='_5pbx userContent']").text.lower()
        time.sleep(3)
        if post_checker(post_text):
            try:
                 print("Current post text= ",post_text)
                 p=post.find_element_by_xpath(".//a[@class='UFILikeLink _4x9- _4x9_ _48-k']")
                 attr=p.get_attribute("aria-pressed")
                 print("attr=",attr)
                 if(attr=="false"):
                  try:   
                   sect=post.find_element_by_class_name("UFICommentContainer")
                   print("Sect found!")
                  except NoSuchElementException:
                   print(" NoSuchElementException Thrown while searching UFIcomeent Container")
                  try: 
                   p=sect.find_element_by_class_name("UFIInputContainer")
                   sect.find_element_by_class_name("UFIInputContainer").click()
                   
                  except NoSuchElementException:
                   print(" NoSuchElementException Thrown while searching UFIInput Container")
                  
                  
                  time.sleep(4)
                  try:
                   comm=p.find_element_by_class_name("_5rpb")
                   comm.click()
                   print("_5rpb found.....")
                   comm.send_keys("Thank You!! So much...."+Keys.RETURN)
                   print("1 comment done\n")
                    
                  except NoSuchElementException:
                   print(" NoSuchElementException Thrown while searching _5rpb")   
                  post.find_element_by_xpath(".//a[@class='UFILikeLink _4x9- _4x9_ _48-k']").click()
                  print("1 like done.... ")
                  no_of_postliked+=1
                  
                  
                #print("1 like done! \n")
                
            except:
                continue
    print("Total ", count, " posts found ")
    
     
    print ("Successfully liked and wrote the comment on relevant posts, ",no_of_postliked)
except TimeoutException:
    print ("Timeout") 
        

from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


# print("Welcome! Kindly fill the \nrequired fields 
# for login when it loads\nand press the login button")
print("opening site.....")

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
time.sleep(5)
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("botbday@gmail.com")
elem = driver.find_element_by_name("pass")
elem.clear()
elem.send_keys("botbday56"+Keys.RETURN)
# print("Please Enter Your Username and Password there and\n press the login button...... (30 sec wait time) ")
elem.send_keys(Keys.RETURN)
time.sleep(2)
delay = 60
breaklimit = 100

comment_list = ["Thank You So much!......", "Thanks", "Thank u", "Thnx buddy", "Thank you!!...."]
nc = len(comment_list)


try:
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "_2s25")))
    time.sleep(5);
    elem.click();
    print("Successfully Logged in");
    time.sleep(2)
except TimeoutException:
    print("Timeout or wrong email/password");
    driver.close();


def post_checker(post):
    hpylst = ['happy', 'hapy', 'hapi ', 'appy', 'hpy', '#appy']
    bdylst = ['birthday', 'bday', 'budday', 'b\'day', 'bdy', 'b\'day!']
    return any(word in post for word in hpylst) and any(word in post for word in bdylst)
posts = []
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "_2s25")))
    
    count = 0 
    no_of_postliked = 0
    time.sleep(8)
    posts = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'userContentWrapper')))
    npt = 0
    time.sleep(8)

    for x in range(4):
        try:
            driver.find_element(By.CLASS_NAME, "_44b2")
            break
        except NoSuchElementException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
    # To search for the bday post if it has not been loaded it will scroll down the page, max 4 times.      

    print("Searching for all the related post....\n This may take time depending on the number of bday post.")
    while 1:
        try:
            # print("Now it will search for _44b2")   
            p = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, '_44b2')))
            driver.execute_script("return arguments[0].scrollIntoView();", p )
            driver.execute_script("window.scrollBy(0, -100);")
            p.click()
            print("Found some more post.... plz wait....")
            # driver.execute_script("window.scrollTo(0, (scr++)*document.body.scrollHeight);")
            # driver.find_element(By.CLASS_NAME,"_44b2").click()
          
        # print("Check if page getting refreshed!..... input 1 to continue....")
        # inp=input()
            time.sleep(5)
        except TimeoutException:
            print(" Successfully Loaded all the related posts.!.....")
            break;
      
    count = 0
    posts = driver.find_elements_by_class_name('userContentWrapper')
    print("Total ", len(posts), " element in posts....")
    for post in posts:
        count += 1
        comment = comment_list[random.randrange(0, nc)]
        
        # post.click()
        driver.execute_script("return arguments[0].scrollIntoView();", post)
        driver.execute_script("window.scrollBy(0, -45);")
        print("count=", count, "\n")
        try:
            post_text=post.find_element_by_xpath(".//div[@class='_5pbx userContent']").text.lower()
        except NoSuchElementException:
            continue   
        #time.sleep(3)
        if post_checker(post_text):
            try:
                print("Current post text= ",post_text)
                p=post.find_element_by_xpath(".//a[@class='UFILikeLink _4x9- _4x9_ _48-k']")
                attr=p.get_attribute("aria-pressed")
                print("attr=",attr)
                 
                if(attr=="false"):
                     
                    try:   
                        sect=post.find_element_by_class_name("UFICommentContainer")
                        #time.sleep(2)
                        print("Sect found!")
                    except NoSuchElementException:
                        print(" NoSuchElementException Thrown while searching UFIcomeent Container")
                    try: 
                        p=sect.find_element_by_class_name("UFIInputContainer")
                        p.click()

                    # try:
                    # p.find_element_by_class_name("_1osa mentionsHidden").click()
                    # except NoSuchElementException:
                    # print(" NoSuchElementException Thrown while searching _1osa mentionsHidden") 
                        print("clicked on UFIInput container")
                   
                    except NoSuchElementException:
                        print(" NoSuchElementException Thrown while searching UFIInput Container")

                 
                    for x in range(0,50):
                        try:
                            comm=p.find_element_by_class_name("_5rpb")
                            # comm=WebDriverWait(driver,10).until(p.find_element_by_class_name("_5rpb"))
                   
                    
                        except NoSuchElementException:
                            #print(" NoSuchElementException Thrown while searching _5rpb")
                            p.click()
                            continue
                        except ElementNotVisibleException:
                            print(" ElementNotVisibleException Thrown while searching _5rpb")
                        except InvalidElementStateException:
                            print(" InvalidElementStateException Thrown while searching _5rpb")
                        except MoveTargetOutOfBoundsException:
                            print(" MoveTargetOutOfBoundsException Thrown while searching _5rpb")
                        except StaleElementReferenceException:
                            print(" StaleElementReferenceException Thrown while searching _5rpb") 

                        else:
                            print("No exception raised")   
                            comm.click()
                            print("_5rpb found.....")
                            comm.send_keys(comment+Keys.RETURN)
                            print("1 comment done\n")
                            break
                   
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

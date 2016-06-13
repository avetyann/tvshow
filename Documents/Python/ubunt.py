from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import time
start_time = time.time()


#URL for calendar
#Last id 1099395  
driver = webdriver.Chrome()



for id in range(1050000, 1050050):
	url = "http://tvnews.vanderbilt.edu/program.pl?ID=%d" % id
	driver.get(url)
	#time.sleep(1)


	try:
		title1 = driver.find_element_by_xpath("/html/body/div[@id='pageFrame']/h1").text
	except:
		title1 = "-2"

	try:
		title2 = driver.find_element_by_xpath("/html/body/div[@id='pageFrame']/h2/strong").text
	except:
		title2 = "-2"

	alternative_title = "-2"
	date_menu = "-2"
	network = "-2"
	summary = "-2"
	program_time = "-2"
	broadcast_type = "-2"
	program_length = "-2"
	record_number = "%d" % id

	row_number = len(driver.find_elements_by_xpath("/html/body/div[@id='pageFrame']/table/tbody/tr"))
	for i in range(1, row_number + 1):
		try:
			name = driver.find_element_by_xpath("/html/body/div[@id='pageFrame']/table/tbody/tr[(%d)]/th" %i).text
		except NoSuchElementException:
			name = "-2"

		try: 
			value = driver.find_element_by_xpath("/html/body/div[@id='pageFrame']/table/tbody/tr[%d]/td" %i).text
		except:
			value = "-2"

		if name == 'Alternate Title':
			alternative_title = value
		if name == 'Date:':
			date_menu = value
		if name == 'Network:':
			network = value
		if name == 'Summary:':
			summary = value
		if name == 'Program Time:':
			program_time = value
		if name == 'Broadcast Type:':
			broadcast_type = value
		if name == 'Program Length':
			program_length = value
		
	print title1
	#cur.execute("""INSERT INTO tv_show (title1, title2, alternative_title, date_menu, network, summary, program_time, broadcast_type, program_length, record_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (title1, title2, alternative_title, date_menu, network, summary, program_time, broadcast_type, program_length, record_number))



#conn.commit()
#cur.close()
#conn.close()

#driver.close()

print("--- %s seconds ---" % (time.time() - start_time))

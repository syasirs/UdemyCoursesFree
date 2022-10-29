import requests, time, contextlib
from bs4 import BeautifulSoup
from urllib.parse import urlencode 
from urllib.request import urlopen 
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
from datetime import datetime

todays_date = datetime.now()

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# f = open("Udemy_Courses.txt", "w")
# f.write('''Free Udemy Courses ('''+str(todays_date.strftime("%d"))+'''-'''+str(todays_date.strftime("%B"))+'''-'''+str(todays_date.strftime("%Y"))+''')
# NOTE: Udemy has changed its policy for free coupons. From 28 October 2021, the free coupons will be limited to 1000 enrollments for each course. \nSo be quick and catch the free coupon as fast as possible, coupons might be useless anytime.


# ''')
url0 = "https://answersq.com/udemy-paid-courses-for-free-with-certificate/"
req0 = requests.get(url0, headers)
soup0 = BeautifulSoup(req0.content, 'html.parser')

def url_shorten(url): 
	request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url})) 
	with contextlib.closing(urlopen(request_url)) as response: 
		return response.read().decode('utf-8')



def answersq(coure_number=1):
	f = open("Udemy_Courses.txt", "w")
	f.write('''Free Udemy Courses ('''+str(todays_date.strftime("%d"))+'''-'''+str(todays_date.strftime("%B"))+'''-'''+str(todays_date.strftime("%Y"))+''')\nNOTE: Udemy has changed its policy for free coupons.\nFrom 28 October 2021, the free coupons will be limited to 1000 enrollments for each course. \nSo be quick and catch the free coupon as fast as possible, coupons might be useless anytime.\n\n\n''')
	
	coure_number = coure_number

	section = soup0.findAll('section')[1]
	all_list_items = section.findAll('li')
	for course in all_list_items:
		course_name = course.findAll('span')[0].string
		course_name = course_name.replace(" –", "")
		if "christan" not in course_name.lower() and "drum" not in course_name.lower() and "wine" not in course_name.lower() and "movie" not in course_name.lower() and "film" not in course_name.lower() and "sound" not in course_name.lower() and "music" not in course_name.lower() and "flute" not in course_name.lower() and "piano" not in course_name.lower() and "guitar" not in course_name.lower() and "karoke" not in course_name.lower():
			
			# print(course_name)
			link = course.findAll('a')[0]
			link = link.get('href')
			tiny_url = url_shorten(link)
			print(course_name)
			print(link)
			print(tiny_url)
			print('\n')
			f.write(str(coure_number)+"- [100% Off] "+course_name)
			f.write('\n')
			f.write(tiny_url)
			f.write('\n')
			f.write('\n')
			coure_number = coure_number + 1
		
	f.close()



def answersq_table():
	f = open("Udemy_Courses.txt", "w")
	f.write('''Free Udemy Courses ('''+str(todays_date.strftime("%d"))+'''-'''+str(todays_date.strftime("%B"))+'''-'''+str(todays_date.strftime("%Y"))+''')\nNOTE: Udemy has changed its policy for free coupons.\nFrom 28 October 2021, the free coupons will be limited to 1000 enrollments for each course. \nSo be quick and catch the free coupon as fast as possible, coupons might be useless anytime.\n\n\n''')
	
	coure_number = 1
	
	scrap_all_cloumns = soup0.findChildren('elementor-text-editor elementor-clearfix')
	tables = 0
	# print(scrap_all_tables)
	for i in scrap_all_tables:
		# print("-------------",i)
		table_body = i.find("tbody")
		table_row = table_body.findAll("tr")
		
		for row in table_row:
			# print("+++++++++", row)
			link_name = row.findAll("a")[0]
			# print("----", link_name)
			course_name = link_name.string
			url = link_name.get('href')
			# print(course_name, url)
			if "wine" not in course_name.lower() and "movie" not in course_name.lower() and "film" not in course_name.lower() and "sound" not in course_name.lower() and "music" not in course_name.lower() and "flute" not in course_name.lower() and "piano" not in course_name.lower() and "guitar" not in course_name.lower() and "karoke" not in course_name.lower():
					
				try:
					f.write(str(coure_number)+"- "+course_name)
					f.write('\n')
					f.write(url)
					f.write('\n')
				
					# f.write("Link expires in "+find_left_time(a[j].get("href")))
					# f.write('\n')
				except:
					pass
				f.write('\n')
			
				coure_number = coure_number + 1
		tables = tables + 1
		if tables == 4:
			break
		
	f.close()



def realme():
	f = open("Real_me.txt", "w")
	f.write('''Free Udemy Courses ('''+str(todays_date.strftime("%d"))+'''-'''+str(todays_date.strftime("%B"))+'''-'''+str(todays_date.strftime("%Y"))+''')\nNOTE: Udemy has changed its policy for free coupons.\nFrom 28 October 2021, the free coupons will be limited to 1000 enrollments for each course. \nSo be quick and catch the free coupon as fast as possible, coupons might be useless anytime.\n\n\n''')
	coure_number = 1

	url = "https://www.real.discount/filter/?category=All&orderby=date&per_page=100&subcategory=All&store=Udemy&duration=All&price=All&rating=All&language=English&search=&free=1&submit=Filter&page={}"
	MAIN_URL = "https://www.real.discount"
	for i in range(1, 21):
		req = requests.get(url.format(i), headers)
		soup = BeautifulSoup(req.content, 'html.parser')
		links = soup.find( class_ = "row main-bg" )
		scrap_all_links = links.findChildren('a')
		# print(scrap_all_links)
		for link in scrap_all_links:
			
			# logic to handle expired courses but it is not 
			# handled py free=1 in the url but still leave 
			# this code here
			expired = link.find( class_ = "row card-bottom" )
			expired = expired.findAll('div')[0]
			expired = expired.findAll('div')[-1]
			if str(expired.string).strip() != "Expired":
				real_me_course_url = MAIN_URL + link.get('href')
				# print(real_me_course_url)
				req1 = requests.get(real_me_course_url, headers)
				soup1 = BeautifulSoup(req1.content, 'html.parser')
				course_name = soup1.find( class_ = "card-title" )
				course_name = course_name.string
				if course_name:
					course_name = course_name.replace("  Free  Course Coupon", "")
				# print(course_name)
				if "christan" not in course_name.lower() and "drum" not in course_name.lower() and "wine" not in course_name.lower() and "movie" not in course_name.lower() and "film" not in course_name.lower() and "sound" not in course_name.lower() and "music" not in course_name.lower() and "flute" not in course_name.lower() and "piano" not in course_name.lower() and "guitar" not in course_name.lower() and "karoke" not in course_name.lower():
					for udemy_link in soup1.find_all(href=True):
						course_udemy_link = udemy_link.get('href')
						if "udemy.com" in course_udemy_link:
							print(course_name)
							print(course_udemy_link)
							tiny_url = url_shorten(course_udemy_link)
							print(tiny_url)
							print('\n')
							f.write(str(coure_number)+"- "+course_name)
							f.write('\n')
							f.write(tiny_url)
							f.write('\n')
							f.write('\n')
							coure_number = coure_number + 1
		
	f.close()
	answersq(coure_number)


realme()
# answersq(72)
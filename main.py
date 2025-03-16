import psycopg2
import random
from tabulate import tabulate
from datetime import datetime

systemRun = True


def show_menu(menuList):
    print()
    print("------------------------")
    for i in range(len(menuList)):
        print(f"{i + 1}: {menuList[i]}")
    print("------------------------")


def choose_menu(menuList):
    valid_value = 0
    while True:
        try:
            mNum = int(input("제시된 항목들 중 원하는 선택지의 번호를 입력하세요: "))
        except ValueError:
            print("제시된 항목들 중 원하는 선택지에 해당된 정수 번호를 입력하세요.")
            valid_value = valid_value + 1
            if valid_value == 5:
                print("잘못된 값 5회 입력으로 프로그램을 종료합니다.")
                return None
            print()
            continue
        else:
            if mNum >= 1 and mNum <= len(menuList):
                print(f"선택한 항목: {menuList[mNum - 1]}")
                print()
                return mNum
            else:
                print("제시된 항목에 없는 번호입니다.")
                valid_value = valid_value + 1
                if valid_value == 5:
                    print("잘못된 값 5회 입력으로 프로그램을 종료합니다.")
                    return None
                print()


def string_valid_check(text, maxLenth):
    if len(text) > maxLenth:
        return None
    for i in text:
        if (i < '0' or i > '9') and (i < 'a' or i > 'z') and (i < 'A' or i > 'Z'):
            return None
    return True


def int_valid_check(value):
    try:
        value = int(value)
    except ValueError:
        return None
    else:
        return value

def float_valid_check(value):
    try:
        value = float(value)
    except ValueError:
        return None
    else:
        return value

def name_valid_check(text, maxLenth):
    if len(text) > maxLenth:
        return None
    for i in text:
        if (i < 'a' or i > 'z') and (i < 'A' or i > 'Z'):
            return None
    return True

def sector_valid_check(text, maxLenth):
    if len(text) > maxLenth:
        return None
    for i in text:
        if (i < 'a' or i > 'z') and (i < 'A' or i > 'Z') and (i != " "):
            return None
    return True


def input_name(text, lenth):
    valid_count = 0
    while True:
        name = input(f"{text} 입력: ")
        if name_valid_check(name, lenth):
            return name
        else:
            print("잘못된 입력입니다.")
            print("20자 이내의 알파벳으로 입력하세요.")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()


def input_year():
    valid_count = 0
    while True:
        year = input("연도 입력: ")
        year = int_valid_check(year)
        if year != None:
            if year >= 1900 and year <= 9999:
                return year
            else:
                print("잘못된 입력입니다.")
                print("1900 ~ 9999 사이의 값만 유효합니다.")
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return None
                print()
        else:
            print("잘못된 입력입니다.")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()

def input_positive_int(text):
    valid_count = 0
    while True:
        value = input(f"{text} 입력: ")
        value = int_valid_check(value)
        if value != None and value >= 0:
            return value
        else:
            print("잘못된 입력입니다.")
            print("0 이상의 정수 형태로 값을 입력해주세요.")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()


def input_natural_number(text):
    valid_count = 0
    while True:
        value = input(f"{text} 입력: ")
        value = int_valid_check(value)
        if value != None and value > 0:
            return value
        else:
            print("잘못된 입력입니다.")
            print("1 이상의 정수 형태로 값을 입력해주세요.")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()

def input_int(text):
    valid_count = 0
    while True:
        value = input(f"{text} 입력: ")
        value = int_valid_check(value)
        if value != None:
            return value
        else:
            print("잘못된 입력입니다.")
            print("정수 형태로 값을 입력해주세요.")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()

def input_float(text):
    valid_count = 0
    while True:
        value = input(f"{text} 입력: ")
        value = float_valid_check(value)
        if value != None:
            return value
        else:
            print("잘못된 입력입니다.")
            print("실수 형태로 값을 입력해주세요.")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()

def register_id(db, type):
    if type == "admin":
        table = "admin"
    else:
        table = "account"
    valid_count = 0
    while True:
        id = input("생성할 계정의 ID를 입력하세요(알파벳, 숫자 조합 10자 이내): ")
        if string_valid_check(id, 10):
            sql = "SELECT * FROM " + table + " WHERE id = %s"
            current_id = db.execute(sql, (id,))
            if current_id:
                print("이미 등록된 ID입니다.")
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return None
                print()
            else:
                print("사용 가능한 ID입니다.")
                return id
        else:
            print("유효하지 않은 ID입니다. (알파벳, 숫자 조합 10자 이내)")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()



def register_password():
    valid_count = 0
    while True:
        password = input("생성할 계정의 비밀번호를 입력하세요(알파벳, 숫자 조합 12자 이내): ")
        if string_valid_check(password, 12):
            return password
        else:
            print("유효하지 않은 비밀번호입니다. (알파벳, 숫자 조합 12자 이내)")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()


def register_name():
    valid_count = 0
    while True:
        name = input("이름을 입력하세요(알파벳 20자 이내): ")
        if name_valid_check(name, 20):
            return name
        else:
            print("유효하지 않은 이름입니다. (알파벳 20자 이내)")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()


def register_phone():
    valid_count = 0
    while True:
        phone = input("전화번호를 입력하세요(-을 제외한 010으로 시작하는 11자리 숫자로 입력하세요): ")
        if len(phone) != 11:
            print("유효하지 않은 길이입니다. (-을 제외한 11자리 숫자로 입력하세요)")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()
        else:
            if phone[:3] != "010":
                print("010으로 시작하는 11자리 숫자로 입력하세요")
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return None
                print()
                continue
            else:
                valid = True
                for i in phone:
                    if i < '0' or i > '9':
                        print("-을 제외한 숫자로만 입력하세요")
                        valid_count = valid_count + 1
                        if valid_count == 5:
                            print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                            return None
                        print()
                        valid = False
                        break
                if valid:
                    phone = phone[:3] + '-' + phone[3:7] + '-' + phone[7:]
                    return phone
                # else:
                # continue


def login_id():
    valid_count = 0
    while True:
        id = input("로그인할 계정의 ID를 입력하세요(알파벳, 숫자 조합 10자 이내): ")
        if string_valid_check(id, 10):
            return id
        else:
            print("유효하지 않은 ID입니다. (알파벳, 숫자 조합 10자 이내)")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()

def login_password():
    valid_count = 0
    while True:
        password = input("비밀번호를 입력하세요(알파벳, 숫자 조합 12자 이내): ")
        if string_valid_check(password, 12):
            return password
        else:
            print("유효하지 않은 비밀번호입니다. (알파벳, 숫자 조합 12자 이내)")
            valid_count = valid_count + 1
            if valid_count == 5:
                print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                return None
            print()





class DBManager:
    def __init__(self, userID, userPassword):
        self.conn = psycopg2.connect(
            database = 'mts_db',
            user = userID,
            password = userPassword,
            host='::1',
            port='5432'
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall() if self.cursor.description else None


    def close(self):
        self.cursor.close()
        self.conn.close()

class Admin:
    def __init__(self, db_manager):
        self.db = db_manager
        self.admin_id = ""
        self.type = "admin"


    def set_role(self):
        self.db.execute("RESET ROLE")
        self.db.execute("SET ROLE mts_admin")

    def register(self):
        admin_id = register_id(self.db, self.type)
        if admin_id == None:
            return
        password = register_password()
        if password == None:
            return

        try:
            self.db.execute("INSERT INTO admin (id, password, type) VALUES (%s, %s, %s)", (admin_id, password, self.type))
            self.db.conn.commit()
            print("계정 생성 성공")
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")

    def login(self):
        valid_count = 0
        admin_id = login_id()
        global systemRun
        while True:
            password = login_password()
            existent_id = self.db.execute("SELECT id FROM admin WHERE id = %s", (admin_id, ))
            if existent_id:
                login_result = self.db.execute("SELECT id FROM admin WHERE id = %s AND password = %s", (admin_id, password))
                if login_result:
                    break
                else:
                    print("비밀번호가 틀렸습니다.")
                    valid_count = valid_count + 1
                    if valid_count == 5:
                        systemRun = False
                        print("비밀번호가 5회 틀려 프로그램을 종료합니다.")
                        return None
                    print()
            else:
                print("존재하지 않는 ID입니다.")
                return None

        print(f"{login_result[0][0]} 계정 로그인 성공")
        self.admin_id = login_result[0][0]
        return login_result

    def show_company_list(self):
        companys = self.db.execute("SELECT name, price, stock_num FROM company")
        if len(companys) == 0:
            print("상장된 기업이 없습니다.")
            print()
            return
        try:
            for company in companys:
                name, price, stock_num = company
                self.db.execute("UPDATE company SET total_price = %s WHERE name = %s", (price*stock_num, name))
            self.db.conn.commit()
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")
            return
        companys = self.db.execute("SELECT name, price, stock_num, total_price, sector FROM company ORDER BY total_price DESC")

        print("상장 기업 목록")
        headers = ["Name", "Stock Price", "Stock Num", "Total Price", "Sector"]
        print(tabulate(companys, headers=headers, tablefmt="fancy_grid"))
        print()



    def tax_customer_list(self):
        sql = "CREATE OR REPLACE VIEW customer_capital_gain_view AS SELECT name, phone, capital_gain FROM account WHERE capital_gain > 2500000 AND type = %s"
        self.db.execute(sql, ("customer",))
        #results = self.db.execute("SELECT name, phone, capital_gain FROM account WHERE type = 'customer' AND capital_gain > 250000")
        results = self.db.execute("SELECT * FROM customer_capital_gain_view")
        if len(results) == 0:
            print("과세 대상 고객이 없습니다.")
            return

        headers = ["Name", "Phone", "Capital Gain"]
        print("과세 대상 고객 목록")
        print(tabulate(results, headers=headers, tablefmt="fancy_grid"))

    def update_sector(self):
        valid_count = 0
        while True:
            company_name = input("산업 분야를 수정할 기업 이름: ")
            if name_valid_check(company_name, 20):
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("20자 이내의 알파벳으로 입력하세요.")
                print()

        company_name = company_name.lower().capitalize()
        present_company = self.db.execute("SELECT name FROM company WHERE name = %s", (company_name,))
        if len(present_company) == 0:
            print("상장 기업 목록에 없는 기업입니다.")
            return

        valid_count = 0
        while True:
            sector = input("산업 분야: ")
            if sector_valid_check(sector, 25):
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("25자 이내의 알파벳으로 입력하세요.")
                print()
        try:
            self.db.execute("UPDATE company SET sector = %s WHERE name = %s", (sector, company_name))
            self.db.conn.commit()
            print(f"{company_name}의 Sector 수정: {sector}")
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")
    def register_company(self):
        valid_count = 0
        while True:
            company_name = input("상장할 기업 이름: ")
            if name_valid_check(company_name, 20):
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("20자 이내의 알파벳으로 입력하세요.")
                print()

        present_company = self.db.execute("SELECT name FROM company WHERE name = %s", (company_name, ))
        if present_company:
            print("이미 등록된 기업입니다.")
            return

        company_name = company_name.lower().capitalize()
        valid_count = 0
        while True:
            stock_price = input("주식 주당 가격: ")
            stock_price = int_valid_check(stock_price)
            if stock_price and stock_price > 0:
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("1 이상의 정수로 입력하세요.")
                print()

        valid_count = 0
        while True:
            stock_num = input("주식 수: ")
            stock_num = int_valid_check(stock_num)
            if stock_num and stock_num > 0:
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("1 이상의 정수로 입력하세요.")
                print()

        valid_count = 0
        while True:
            sector = input("산업 분야: ")
            if sector_valid_check(sector, 25):
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("25자 이내의 알파벳으로 입력하세요.")
                print()

        total_price = stock_price * stock_num
        try:
            self.db.execute("INSERT INTO company (name, price, stock_num, total_price, sector) VALUES (%s, %s, %s, %s, %s)",
                            (company_name, stock_price, stock_num, total_price, sector ))
            self.db.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(f"Error: {e}")

    def delete_company(self):
        valid_count = 0
        while True:
            company_name = input("상장 폐지할 기업 이름: ")
            if name_valid_check(company_name, 20):
                break
            else:
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print("잘못된 입력값입니다.")
                print("20자 이내의 알파벳으로 입력하세요.")
                print()

        company_name = company_name.lower().capitalize()
        present_company = self.db.execute("SELECT name FROM company WHERE name = %s", (company_name,))
        if len(present_company) == 0:
            print("상장 기업 목록에 없는 기업입니다.")
            return



        company_account = self.db.execute("SELECT a_number FROM account WHERE name = %s AND type = %s", (company_name, "company"))
        if len(company_account) == 0:
            try:
                self.db.execute("DELETE FROM company WHERE name = %s", (company_name,))
                self.db.conn.commit()
                print(f"기업 {company_name} 상장 폐지 완료")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")
            finally:
                return

        company_a_number = company_account[0][0]
        company_info = self.db.execute("SELECT stock_num, price FROM company WHERE name = %s", (company_name,))[0]
        balance = self.db.execute("SELECT stock_count FROM company_balance WHERE a_number = %s AND stock_name = %s", (company_a_number, company_name))[0]


        if balance[0] != company_info[0] :
            print("해당 기업이 보유하고 있는 자사주 지분이 부족합니다.")
            return

        try:
            self.db.execute("DELETE FROM financial_info WHERE name = %s", (company_name,))
            self.db.execute("DELETE FROM company WHERE name = %s", (company_name,))
            self.db.conn.commit()
            print(f"기업 {company_name} 상장 폐지 완료")
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")


class Account:
    def __init__(self, db_manager):
        self.db = db_manager
        self.account_id = ""
        self.account_type = ""
        self.account_name = ""
        self.account_num = ""


    def register(self, type):
        account_type = type
        name = register_name()
        if name == None:
            return
        # name 중복 검사 (company만 해당)
        if account_type == "company":
            name = name.lower().capitalize()
            name_check = self.db.execute("SELECT name FROM company WHERE name = %s", (name, ))
            if not name_check:
                print("상장 기업 목록에 없는 기업입니다.")
                return
            name_check = self.db.execute("SELECT name FROM account WHERE type = %s AND name = %s", (account_type, name))
            if name_check:
                print("이미 계정이 존재하는 기업입니다.")
                return

        account_id = register_id(self.db, type)
        if account_id == None:
            return
        password = register_password()
        if password == None:
            return
        phone = register_phone()
        if phone == None:
            return

        valid_count = 0
        while True:
            a_number = random.randint(10000000, 99999999)
            current_a_numbers = self.db.execute("SELECT a_number FROM account WHERE a_number = %s", (a_number, ))
            if current_a_numbers:
                valid_count = valid_count + 1
                # 랜덤 10번 실패하면 사용중인 번호 제외하고 랜덤하고 뽑기
                if valid_count == 10:
                    exclude_list = []
                    current_a_numbers = self.db.execute("SELECT a_number FROM account")
                    for current_number in current_a_numbers:
                        exclude_list.append(current_number[0])
                    all_8digit_numbers = set(range(10000000, 100000000))
                    exclude_set = set(exclude_list)
                    possible_numbers = list(all_8digit_numbers - exclude_set)
                    if not possible_numbers:
                        print("유효한 계좌번호를 모두 사용중입니다.")
                        return
                    a_number = random.choice(possible_numbers)
                    break
                continue
            else:
                break

        # 계정 생성
        if account_type == "customer":
            try:
                self.db.execute( "INSERT INTO account (id, password, a_number, type, name, phone, cash, capital_gain) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                 (account_id, password, a_number, account_type, name, phone, "0", "0"))
                self.db.conn.commit()
                print("계정 생성 성공")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")
        else:
            now = datetime.now()
            current_date = now.date()
            current_time = now.time()

            buy_list_number = self.db.execute("SELECT MAX(buy_list_number) FROM buy_list")[0][0]
            if buy_list_number == None:
                buy_list_number = 1
            else:
                buy_list_number = buy_list_number + 1

            stock_price, stock_num = self.db.execute("SELECT price, stock_num FROM company WHERE name = %s", (name, ))[0]

            try:
                self.db.execute("INSERT INTO account (id, password, a_number, type, name, phone, cash, capital_gain) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (account_id, password, a_number, account_type, name, phone, 0, 0))
                self.db.execute("INSERT INTO buy_list (buy_list_number, a_number, name, price, b_date, b_time, b_count, s_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (buy_list_number, a_number, name, stock_price, current_date, current_time, stock_num, 0))
                self.db.execute("INSERT INTO company_balance (a_number, stock_name, stock_count, avg_buy_price) VALUES (%s, %s, %s, %s)",
                                (a_number, name, stock_num, stock_price))
                self.db.conn.commit()
                print("계정 생성 성공")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")


    def login(self):
        valid_count = 0
        account_id = login_id()
        global systemRun
        while True:
            password = login_password()
            existent_id = self.db.execute("SELECT id FROM account WHERE id = %s", (account_id, ))
            if existent_id:
                login_result = self.db.execute("SELECT id, type, name, a_number FROM account WHERE id = %s AND password = %s", (account_id, password))
                if login_result:
                    break
                else:
                    print("비밀번호가 틀렸습니다.")
                    valid_count = valid_count + 1
                    if valid_count == 5:
                        systemRun = False
                        print("비밀번호가 5회 틀려 프로그램을 종료합니다.")
                        return None
                    print()
            else:
                print("존재하지 않는 ID입니다.")
                return None

        print(f"{login_result[0][0]} 계정 로그인 성공")
        self.account_id = login_result[0][0]
        self.account_type = login_result[0][1]
        self.account_name = login_result[0][2]
        self.account_num = login_result[0][3]
        return login_result


    def current_cash(self):
        cash = self.db.execute("SELECT cash FROM account WHERE a_number = %s", (self.account_num,))[0][0]
        #print(f"잔액: {cash}")
        return cash

    def deposit(self):
        amount = input_positive_int("입금할 금액")
        if amount == None:
            return
        if amount == 0:
            print("잔액의 변동이 없습니다.")
            return
        try:
            self.db.execute("UPDATE account SET cash = cash + %s WHERE id = %s", (amount, self.account_id))
            self.db.conn.commit()
            print(f"{amount}원 입금 완료")
            cash = self.current_cash()
            print(f"잔액: {cash}")
            print()
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")

    def withdrawal(self):
        amount = input_positive_int("출금할 금액")
        if amount == None:
            return
        if amount == 0:
            print("잔액의 변동이 없습니다.")
            return
        cash = self.db.execute("SELECT cash FROM account WHERE id = %s", (self.account_id,))[0][0]
        if cash < amount:
            print("잔액이 부족합니다")
            return

        try:
            self.db.execute("UPDATE account SET cash = cash - %s WHERE id = %s", (amount, self.account_id))
            self.db.conn.commit()
            print(f"{amount}원 출금 완료")
            cash = self.current_cash()
            print(f"잔액: {cash}")
            print()
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")

    def show_company_list(self):
        companys = self.db.execute("SELECT name, price, stock_num FROM company")
        if len(companys) == 0:
            print("상장된 기업이 없습니다.")
            print()
            return
        try:
            for company in companys:
                name, price, stock_num = company
                self.db.execute("UPDATE company SET total_price = %s WHERE name = %s", (price * stock_num, name))
            self.db.conn.commit()
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")
            return
        companys = self.db.execute(
            "SELECT name, price, stock_num, total_price, sector FROM company ORDER BY total_price DESC")

        print("상장 기업 목록")
        headers = ["Name", "Stock Price", "Stock Num", "Total Price", "Sector"]
        print(tabulate(companys, headers=headers, tablefmt="fancy_grid"))
        print()

    def show_company_info(self):
        name = input_name("정보를 확인할 기업의 이름", 20)
        if name == None:
            return
        name = name.lower().capitalize()
        company_list = self.db.execute("SELECT * FROM company WHERE name = %s", (name, ))
        if len(company_list) == 0:
            print("상장 기업 목록에 없는 기업 이름입니다.")
            print("상장 기업 목록의 이름을 정확히 입력하세요 (대소문자 구분X)")
            return

        financial_info = self.db.execute("SELECT year, sales, business_profits, pure_profits, EPS, BPS, PER, PBR FROM financial_info WHERE name = %s ORDER BY year DESC",
                                         (name,))
        if len(financial_info) == 0:
            print("등록된 재무정보가 없습니다.")
            return
        print()
        print(f"{name}의 재무제표")
        headers = ["Year", "Sales", "Business Profits", "Pure Profits", "EPS", "BPS", "PER", "PBR"]
        print(tabulate(financial_info, headers=headers, tablefmt="fancy_grid"))


    def show_company_order(self):
        if self.account_type == "company":
            name = self.account_name
        else:
            name = input_name("주문을 확인할 기업의 이름", 20)
            if name == None:
                return
            name = name.lower().capitalize()

            company_list = self.db.execute("SELECT * FROM company WHERE name = %s", (name,))
            if len(company_list) == 0:
                print("상장 기업 목록에 없는 기업 이름입니다.")
                print("상장 기업 목록의 이름을 정확히 입력하세요 (대소문자 구분X)")
                return

        company_buy_order_list = self.db.execute("SELECT price, count, type FROM order_list WHERE name = %s AND type = %s ORDER BY price DESC", (name, "buy"))
        company_sell_order_list = self.db.execute("SELECT price, count, type FROM order_list WHERE name = %s AND type = %s ORDER BY price DESC", (name, "sell"))

        if len(company_buy_order_list) == 0 and len(company_sell_order_list) == 0:
            print(f"{name} 기업에 대해 등록된 주문이 없습니다.")
            return

        if len(company_sell_order_list) > 0:
            print()
            print(f"{name} 매도 호가창")
            headers = ["Price", "Count", "Type"]
            print(tabulate(company_sell_order_list, headers=headers, tablefmt="fancy_grid"))
            if len(company_buy_order_list) > 0 and len(company_sell_order_list) > 0:
                print("--------------------------")

        if len(company_buy_order_list) > 0:
            print(f"{name} 매수 호가창")
            headers = ["Price", "Count", "Type"]
            print(tabulate(company_buy_order_list, headers=headers, tablefmt="fancy_grid"))
            print()



    def register_buy_order(self, name, price, count, order_number):
        self.db.execute("INSERT INTO order_list (a_number, type, name, price, count, order_number) VALUES (%s, %s, %s, %s, %s, %s)",
                        (self.account_num, "buy", name, price, count, order_number))

    def register_sell_order(self, name, price, count, order_number):
        self.db.execute("INSERT INTO order_list (a_number, type, name, price, count, order_number) VALUES (%s, %s, %s, %s, %s, %s)",
                        (self.account_num, "sell", name, price, count, order_number))

    def buy_contract_conclusion(self, a_number, name, price, count):
        a_type = self.db.execute("SELECT type FROM account WHERE a_number = %s", (a_number, ))[0][0]
        current_stock_price = self.db.execute("SELECT price FROM company WHERE name = %s", (name,))[0][0]

        if a_type == "customer":
            present_stock = self.db.execute("SELECT stock_count, avg_buy_price FROM customer_balance WHERE a_number = %s AND stock_name = %s",
                                            (a_number, name))
            if present_stock:
                stock_count = present_stock[0][0]
                avg_buy_price = present_stock[0][1]
                total_buy_price = stock_count * avg_buy_price + price * count

                avg_buy_price = total_buy_price / (stock_count + count)
                avg_buy_price = round(avg_buy_price, 2)

                sql = "UPDATE customer_balance SET stock_count = stock_count + %s, avg_buy_price = %s WHERE a_number = %s AND stock_name = %s"
            else:
                sql = "INSERT INTO customer_balance (a_number, stock_name, stock_count, avg_buy_price) VALUES (%s, %s, %s, %s)"
        else:
            present_stock = self.db.execute("SELECT stock_count, avg_buy_price FROM company_balance WHERE a_number = %s AND stock_name = %s",
                                            (a_number, name))
            if present_stock:
                stock_count = present_stock[0][0]
                avg_buy_price = present_stock[0][1]
                total_buy_price = stock_count * avg_buy_price + price * count

                avg_buy_price = total_buy_price / (stock_count + count)
                avg_buy_price = round(avg_buy_price, 2)

                sql = "UPDATE company_balance SET stock_count = stock_count + %s, avg_buy_price = %s WHERE a_number = %s AND stock_name = %s"
            else:
                sql = "INSERT INTO company_balance (a_number, stock_name, stock_count, avg_buy_price) VALUES (%s, %s, %s, %s)"

        now = datetime.now()
        current_date = now.date()
        current_time = now.time()

        buy_list_number = self.db.execute("SELECT MAX(buy_list_number) FROM buy_list")[0][0]
        if buy_list_number == None:
            buy_list_number = 1
        else:
            buy_list_number = buy_list_number + 1
        self.db.execute("INSERT INTO buy_list (buy_list_number, a_number, name, price, b_date, b_time, b_count, s_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (buy_list_number, a_number, name, price, current_date, current_time, count, 0))
        if present_stock:
            self.db.execute(sql, (count, avg_buy_price, a_number, name))
        else:
            self.db.execute(sql, (a_number, name, count, price))



    def sell_contract_conclusion(self, a_number, name, price, count):
        buy_contract = self.db.execute("SELECT buy_list_number, price, b_date, b_time, b_count, s_count FROM buy_list WHERE a_number = %s AND name = %s AND b_count > s_count ORDER BY b_date ASC, b_time ASC",
                                       (a_number, name))
        if buy_contract:
            now = datetime.now()
            current_date = now.date()
            current_time = now.time()
            cash = price * count
            sell_list_number = self.db.execute("SELECT MAX(sell_list_number) FROM sell_list")[0][0]
            if sell_list_number == None:
                sell_list_number = 0

            for contract in buy_contract:
                buy_list_number, b_price, b_date, b_time, b_count, s_count = contract
                stock_count = b_count - s_count
                capital_gain = price - b_price
                if count >= stock_count:
                    self.db.execute("UPDATE buy_list SET s_count = s_count + %s WHERE a_number = %s AND name = %s AND b_date = %s AND b_time = %s AND buy_list_number = %s",
                                    (stock_count, a_number, name, b_date, b_time, buy_list_number))
                    count = count - stock_count
                    order_count = stock_count
                else:
                    self.db.execute("UPDATE buy_list SET s_count = s_count + %s WHERE a_number = %s AND name = %s AND b_date = %s AND b_time = %s AND buy_list_number = %s",
                                    (count, a_number, name, b_date, b_time, buy_list_number))
                    order_count = count
                    count = 0
                sell_list_number = sell_list_number + 1
                self.db.execute("INSERT INTO sell_list (sell_list_number, a_number, name, b_price, s_price, s_date, s_time, s_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (sell_list_number, a_number, name, b_price, price, current_date, current_time, order_count))
                self.db.execute("UPDATE account SET capital_gain = capital_gain + %s WHERE a_number = %s", (capital_gain * order_count, a_number))
                if count == 0:
                    break
            self.db.execute("UPDATE account SET cash = cash + %s WHERE a_number = %s", (cash, a_number))

            account_type = self.db.execute("SELECT type FROM account WHERE a_number = %s", (a_number, ))[0][0]
            if account_type == "customer":
                after_conclusion_stock_count = self.db.execute("SELECT stock_count FROM customer_balance WHERE a_number = %s AND stock_name = %s",
                                                               (a_number, name))[0][0]
                remain_sell_order = self.db.execute("SELECT * FROM order_list WHERE a_number = %s AND type = %s AND name = %s",
                                                    (a_number, "sell", name))
                if after_conclusion_stock_count == 0 and len(remain_sell_order) == 0:
                    self.db.execute("DELETE FROM customer_balance WHERE a_number = %s AND stock_name = %s",
                                    (a_number, name))
            else:
                after_conclusion_stock_count = self.db.execute("SELECT stock_count FROM company_balance WHERE a_number = %s AND stock_name = %s",
                                                               (a_number, name))[0][0]
                remain_sell_order = self.db.execute( "SELECT * FROM order_list WHERE a_number = %s AND type = %s AND name = %s",
                                                     (a_number, "sell", name))
                if after_conclusion_stock_count == 0 and len(remain_sell_order) == 0:
                    self.db.execute("DELETE FROM company_balance WHERE a_number = %s AND stock_name = %s",
                                    (a_number, name))
        else:
            print("매도 가능한 매수체결 기록이 없음")
            return


    def buy(self):
        if self.account_type == "customer":
            name = input_name("매수할 기업의 이름", 20)
            if name == None:
                return
            name = name.lower().capitalize()
            company_list = self.db.execute("SELECT * FROM company WHERE name = %s", (name,))
            if len(company_list) == 0:
                print("상장 기업 목록에 없는 기업입니다.")
                return
        else:
            name = self.account_name
        price = input("주당 매수 가격을 입력하세요: ")
        price = int_valid_check(price)
        if price == None or price <= 0:
            print("잘못된 입력입니다.")
            print("매수 가격은 1 이상의 정수값으로 입력해주세요.")
            return
        order_count = input("매수할 개수를 입력하세요: ")
        order_count = int_valid_check(order_count)
        if order_count == None or order_count <= 0:
            print("잘못된 입력입니다.")
            print("매수 수량은 1 이상의 정수값으로 입력해주세요.")
            return

        count = order_count
        cash = price * order_count
        current_cash = self.current_cash()
        if cash > current_cash:
            print("잔액이 부족합니다.")
            print()
            return

        current_max_order_number = self.db.execute("SELECT MAX(order_number) FROM order_list")
        if current_max_order_number[0][0] == None:
            order_number = 1
        else:
            order_number = current_max_order_number[0][0] + 1

        present_sell_order = self.db.execute("SELECT a_number, count, order_number FROM order_list WHERE name = %s AND type = %s AND price = %s AND a_number != %s ORDER BY order_number",
                                     (name, "sell", price, self.account_num))
        if present_sell_order:
            try:
                self.db.execute("UPDATE account SET cash = cash - %s WHERE a_number = %s", (cash, self.account_num))
                for contract in present_sell_order:
                    a_number, sell_order_count, sell_order_number = contract
                    if count >= sell_order_count:
                        self.db.execute("DELETE FROM order_list WHERE order_number = %s", (sell_order_number,))
                        self.sell_contract_conclusion(a_number, name, price, sell_order_count)
                        count = count - sell_order_count
                    else:
                        self.db.execute("UPDATE order_list SET count = count - %s WHERE a_number = %s AND order_number = %s",
                                        (count, a_number, sell_order_number))
                        self.sell_contract_conclusion(a_number, name, price, count)
                        count = 0
                    if count == 0:
                        break
                if count > 0:
                    self.register_buy_order(name, price, count, order_number)
                conclusion_count = order_count - count
                self.buy_contract_conclusion(self.account_num, name, price, conclusion_count)
                self.db.execute("UPDATE company SET price = %s WHERE name = %s", (price, name))
                self.db.conn.commit()
                print(f"주문번호 {order_number}번 매수 주문 완료")
                print(f"{conclusion_count}주는 매수 주문 체결")
                print(f"미체결 잔여 물량: {count}주")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")
        else:
            try:
                self.db.execute("UPDATE account SET cash = cash - %s WHERE a_number = %s", (cash, self.account_num))
                self.register_buy_order(name, price, order_count, order_number)
                self.db.conn.commit()
                print(f"주문번호 {order_number}번 매수 주문 완료")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")


    def sell(self):
        if self.account_type == "customer":
            name = input_name("매도할 기업의 이름", 20)
            if name == None:
                return
            name = name.lower().capitalize()
            current_stock = self.db.execute("SELECT stock_count FROM customer_balance WHERE a_number = %s AND stock_name = %s", (self.account_num, name))
        else:
            name = self.account_name
            current_stock = self.db.execute("SELECT stock_count FROM company_balance WHERE a_number = %s AND stock_name = %s", (self.account_num, self.account_name))

        if len(current_stock) == 0:
            print("해당 주식을 보유하고 있지 않습니다.")
            return

        price = input("주당 매도 가격을 입력하세요: ")
        price = int_valid_check(price)
        if price == None or price <= 0:
            print("잘못된 입력입니다.")
            print("매도 가격은 1 이상의 정수값으로 입력해주세요.")
            return
        order_count = input("매도할 개수를 입력하세요: ")
        order_count = int_valid_check(order_count)
        if order_count == None or order_count <= 0:
            print("잘못된 입력입니다.")
            print("매도 수량은 1 이상의 정수값으로 입력해주세요.")
            return
        count = order_count
        stock_count = current_stock[0][0]
        if stock_count < order_count:
            print("보유 주식이 부족합니다.")
            return

        current_max_order_number = self.db.execute("SELECT MAX(order_number) FROM order_list")
        if current_max_order_number[0][0] == None:
            order_number = 1
        else:
            order_number = current_max_order_number[0][0] + 1

        present_buy_order = self.db.execute("SELECT a_number, count, order_number FROM order_list WHERE name = %s AND type = %s AND price = %s AND a_number != %s  ORDER BY order_number",
                                            (name, "buy", price, self.account_num))

        if present_buy_order:
            try:
                if self.account_type == "customer":
                    self.db.execute("UPDATE customer_balance SET stock_count = stock_count - %s WHERE a_number = %s AND stock_name = %s",
                                    (order_count, self.account_num, name))
                else:
                    self.db.execute("UPDATE company_balance SET stock_count = stock_count - %s WHERE a_number = %s AND stock_name = %s",
                                    (order_count, self.account_num, name))
                for contract in present_buy_order:
                    a_number, buy_order_count, buy_order_number = contract
                    if count >= buy_order_count:
                        self.db.execute("DELETE FROM order_list WHERE order_number = %s", (buy_order_number,))
                        self.buy_contract_conclusion(a_number, name, price, buy_order_count)
                        count = count - buy_order_count
                    else:
                        self.db.execute("UPDATE order_list SET count = count - %s WHERE a_number = %s AND order_number = %s",
                                        (count, a_number, buy_order_number))
                        self.buy_contract_conclusion(a_number, name, price, count)
                        count = 0
                        break
                if count > 0:
                    self.register_sell_order(name, price, count, order_number)

                conclusion_count = order_count - count
                self.sell_contract_conclusion(self.account_num, name, price, conclusion_count)
                self.db.execute("UPDATE company SET price = %s WHERE name = %s", (price, name))
                self.db.conn.commit()
                print(f"주문번호 {order_number}번 매도 주문 완료")
                print(f"{conclusion_count}주는 매도 주문 체결")
                print(f"미체결 잔여 물량: {count}주")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")
        else:
            try:
                if self.account_type == "customer":
                    self.db.execute("UPDATE customer_balance SET stock_count = stock_count - %s WHERE a_number = %s AND stock_name = %s", (order_count, self.account_num, name))
                else:
                    self.db.execute("UPDATE company_balance SET stock_count = stock_count - %s WHERE a_number = %s AND stock_name = %s", (order_count, self.account_num, name))
                self.register_sell_order(name, price, order_count, order_number)
                self.db.conn.commit()
                print(f"주문번호 {order_number}번 매도 주문 완료")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error: {e}")

    def show_order_list(self):
        order_list = self.db.execute("SELECT name, type, price, count, order_number FROM order_list WHERE a_number = %s",
                                     (self.account_num,))
        if order_list:
            headers = ["Company", "Type", "Price", "Count", "order_number"]
            print(tabulate(order_list, headers=headers, tablefmt="fancy_grid"))
        else:
            print("체결되지 않은 주문이 없습니다.")

    def cancel_order(self):
        order_number = input_natural_number("취소할 주문의 주문번호")
        if order_number == None:
            return
        current_order_info = self.db.execute("SELECT name, type, price, count FROM order_list WHERE order_number = %s AND a_number = %s",
                                     (order_number, self.account_num))

        if current_order_info:
            name, type, price, count = current_order_info[0]
            if type == "buy":
                cash = price * count
                try:
                    self.db.execute("DELETE FROM order_list WHERE order_number = %s", (order_number,))
                    self.db.execute("UPDATE account SET cash = cash + %s WHERE a_number = %s", (cash, self.account_num))
                    self.db.conn.commit()
                    print(f"주문번호 {order_number}번 취소 완료")
                except Exception as e:
                    self.db.conn.rollback()
                    print(f"Error: {e}")
            else:  # sell order cancel
                if self.account_type == "customer":
                    update_stock_count_sql = "UPDATE customer_balance SET stock_count = stock_count + %s WHERE a_number = %s and stock_name = %s"
                else:
                    update_stock_count_sql = "UPDATE company_balance SET stock_count = stock_count + %s WHERE a_number = %s and stock_name = %s"
                try:
                    self.db.execute("DELETE FROM order_list WHERE order_number = %s", (order_number,))
                    self.db.execute(update_stock_count_sql, (count, self.account_num, name))
                    self.db.conn.commit()
                    print(f"주문번호 {order_number}번 취소 완료")
                except Exception as e:
                    self.db.conn.rollback()
                    print(f"Error: {e}")
        else:
            print("해당 계좌의 주문 내역 중 해당하는 번호의 주문이 없습니다.")

    def show_balance_inquiry(self):
        account_info = self.db.execute("SELECT cash, capital_gain FROM account WHERE a_number = %s",
                                       (self.account_num,))[0]

        if self.account_type == "customer":
            balance = self.db.execute("SELECT stock_name, stock_count, avg_buy_price FROM customer_balance WHERE a_number = %s",
                                      (self.account_num,))
        else:
            balance = self.db.execute("SELECT stock_name, stock_count, avg_buy_price FROM company_balance WHERE a_number = %s",
                                      (self.account_num,))

        print(f"{self.account_name}님의 계좌 잔고")
        print(f"현금: {account_info[0]}, 누적 양도 소득: {account_info[1]}")
        if balance:
            for i in range(len(balance)):
                temp = list(balance[i])
                price = self.db.execute("SELECT price FROM company WHERE name = %s", (balance[i][0],))[0][0]
                valuation_amount = price * balance[i][1]
                temp.append(valuation_amount)
                balance[i] = temp
            headers = ["Stock", "Count", "Avg Buy Price", "Valuation Amount"]
            print(tabulate(balance, headers=headers, tablefmt="fancy_grid"))
        else:
            print("보유하고 있는 주식이 없습니다.")


class Customer(Account):
    def __init__(self, db_manager):
        Account.__init__(self, db_manager)

    def set_role(self):
        self.db.execute("RESET ROLE")
        self.db.execute("SET ROLE mts_customer")

    def portfolio_weight_inquiry(self):
        sql = "SELECT c.sector, SUM(ba.stock_count * c.price) AS valuation_amount FROM customer_balance ba JOIN company c ON ba.stock_name = c.name WHERE ba.a_number = %s GROUP BY c.sector"
        print(f"{self.account_name}님의 보유 주식 섹터별 비중")
        balance = self.db.execute(sql, (self.account_num, ))
        total_amount = 0
        portfolio_weight = []
        if balance:
            for stock in balance:
                total_amount = total_amount + stock[1]
            for stock in balance:
                weight = round(stock[1] / total_amount * 100, 2)
                weight = str(weight) + "%"
                sector = stock[0]
                portfolio_weight.append([sector, weight])
            headers = ["Sector", "Weight"]
            print(tabulate(portfolio_weight, headers=headers, tablefmt="fancy_grid"))
        else:
            print("보유하고 있는 주식이 없습니다.")

class Company(Account):
    def __init__(self, db_manager):
        Account.__init__(self, db_manager)

    def set_role(self):
        self.db.execute("RESET ROLE")
        self.db.execute("SET ROLE mts_company")

    def register_financial_info(self):
        year = input_year()
        if year == None:
            return
        sales = input_positive_int("매출")
        if sales == None:
            return
        business_profits = input_int("영업이익")
        if business_profits == None:
            return
        pure_profits = input_int("순이익")
        if pure_profits == None:
            return
        eps = input_float("EPS 값")
        if eps == None:
            return
        bps = input_float("BPS 값")
        if bps == None:
            return
        per = input_float("PER 값")
        if per == None:
            return
        pbr = input_float("PBR 값")
        if pbr == None:
            return

        exist_info = self.db.execute("SELECT * FROM financial_info WHERE name = %s AND year = %s", (self.account_name, year))
        try:
            if exist_info:
                self.db.execute("UPDATE financial_info SET sales = %s, business_profits = %s, pure_profits = %s, EPS = %s, BPS = %s, PER = %s, PBR = %s WHERE name = %s AND year = %s",
                                (sales, business_profits, pure_profits, eps, bps, per, pbr, self.account_name, year))
            else:
                self.db.execute("INSERT INTO financial_info (name, year, sales, business_profits, pure_profits, EPS, BPS, PER, PBR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (self.account_name, year, sales, business_profits, pure_profits, eps, bps, per, pbr))
            self.db.conn.commit()
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")

    def dividend_payment(self):
        price, total_stock_count = self.db.execute("SELECT price, stock_num FROM company WHERE name = %s", (self.account_name,))[0]
        have_stock_count = self.db.execute("SELECT stock_count FROM company_balance WHERE a_number = %s AND stock_name = %s",
                                           (self.account_num, self.account_name))[0][0]
        sell_order_count = self.db.execute("SELECT count FROM order_list WHERE name = %s AND a_number = %s AND type = %s", (self.account_name, self.account_num, "sell"))
        if sell_order_count:
            for sell_order in sell_order_count:
                have_stock_count = have_stock_count + sell_order[0]

        customer_stock_count = total_stock_count - have_stock_count
        if customer_stock_count == 0:
            print("100% 지분을 보유하고 있어 배당할 수 없습니다.")
            return

        valid_count = 0
        while True:
            dividend = input("주당 지급할 배당금을 입력하세요: ")
            dividend = int_valid_check(dividend)
            if dividend:
                break
            else:
                print("정수값으로 입력해주세요.")
                valid_count = valid_count + 1
                if valid_count == 5:
                    print("잘못된 값 5회 입력으로 메뉴로 돌아갑니다.")
                    return
                print()


        current_cash = self.current_cash()
        need_cash = customer_stock_count * dividend
        if current_cash < need_cash:
            print("배당금을 지급할 현금이 부족합니다.")
            return


        try:
            self.db.execute("UPDATE account SET cash = cash - %s WHERE a_number = %s", (need_cash, self.account_num))
            stock_have_customer = self.db.execute("SELECT a_number, stock_count FROM customer_balance WHERE stock_name = %s",
                                                  (self.account_name,))
            if stock_have_customer:
                for customer in stock_have_customer:
                    a_number = customer[0]
                    stock_count = customer[1]
                    add_cash = stock_count * dividend
                    self.db.execute("UPDATE account SET cash = cash + %s WHERE a_number = %s", (add_cash, a_number))

            stock_have_customer = self.db.execute("SELECT a_number, count FROM order_list WHERE name = %s AND type = %s AND a_number != %s",
                                                  (self.account_name, "sell", self.account_num))
            if stock_have_customer:
                for customer in stock_have_customer:
                    a_number = customer[0]
                    stock_count = customer[1]
                    add_cash = stock_count * dividend
                    self.db.execute("UPDATE account SET cash = cash + %s WHERE a_number = %s", (add_cash, a_number))
            self.db.conn.commit()
            print(f"주당 {dividend}씩 배당 완료")
        except Exception as e:
            self.db.conn.rollback()
            print(f"Error: {e}")



def main():

    # 자신이 생성한 user의 ID(name)와 password를 넣어주세요
    user = DBManager("user_ID", "user_password")
    accountType = "customer"
    menu = []

    admin = Admin(user)
    customer = Customer(user)
    company = Company(user)

    global systemRun
    while systemRun:
        menu = ["로그인", "회원가입", "프로그램 종료"]
        show_menu(menu)
        mNum = choose_menu(menu)

        if mNum == None:
            break
        elif menu[mNum-1] == "프로그램 종료": # 종료
            print("프로그램을 종료합니다.")
            user.close()
            systemRun = False
            break
        elif menu[mNum-1] == "회원가입": # 회원가입
            print("회원가입 계정 유형 선택")
            menu = ["일반고객", "증권사 직원", "기업"]
            show_menu(menu)
            mNum = choose_menu(menu)
            if mNum == None:
                break
            elif menu[mNum-1] == "일반고객": # 일반고객
                accountType = "customer"
                customer.set_role()
                customer.register(accountType)
            elif menu[mNum-1] == "증권사 직원": # 증권사 직원
                accountType = "admin"
                admin.set_role()
                admin.register()
            else: # 기업
                accountType = "company"
                company.set_role()
                company.register(accountType)
            continue # 회원가입 완료 후 다시 로그인 또는 회원가입 선택 메뉴로 이동

        elif menu[mNum-1] == "로그인":   # 로그인
            menu = ["일반고객", "증권사 직원", "기업"]
            show_menu(menu)
            mNum = choose_menu(menu)
            if mNum == None:
                break
            elif menu[mNum-1] == "일반고객":  # 일반고객
                customer.set_role()
                result = customer.login()
                accountType = "customer"
            elif menu[mNum-1] == "증권사 직원":  # 증권사 직원
                admin.set_role()
                result = admin.login()
                accountType = "admin"
            else:  # 기업
                company.set_role()
                result = company.login()
                accountType = "company"

        if systemRun == False:
            break

        if result == None:
            continue

        # 로그인 이후
        print()
        print("로그인 이후")
        print(f"로그인 계정 유형: {accountType}")


        if accountType == "admin":  # 증권사 직원(관리자) 계정
            while True:
                menu = ["기업 상장", "기업 상장 폐지", "상장 기업 목록 조회", "기업 섹터 수정", "양도세 납부 대상자 조회", "로그아웃"]
                show_menu(menu)
                mNum = choose_menu(menu)
                if mNum == None:
                    systemRun = False
                    break
                elif menu[mNum-1] == "기업 상장":
                    admin.register_company()
                elif menu[mNum-1] == "기업 상장 폐지":
                    admin.delete_company()
                elif menu[mNum-1] == "상장 기업 목록 조회":
                    admin.show_company_list()
                elif menu[mNum-1] == "기업 섹터 수정":
                    admin.update_sector()
                elif menu[mNum-1] == "양도세 납부 대상자 조회":
                    admin.tax_customer_list()
                else:
                    break
        elif accountType == "company":  # 기업 계정
            while True:
                menu = ["입금", "출금", "상장 기업 목록 조회", "기업 정보 조회", "기업 호가창 조회", "주식 매수", "주식 매도", "주문 조회", "주문 취소", "잔고 조회", "재무정보 등록", "배당금 지급", "로그아웃"]
                show_menu(menu)
                mNum = choose_menu(menu)
                if mNum == None:
                    systemRun = False
                    break
                elif menu[mNum-1] == "입금":
                    company.deposit()
                elif menu[mNum-1] == "출금":
                    company.withdrawal()
                elif menu[mNum-1] == "상장 기업 목록 조회":
                    company.show_company_list()
                elif menu[mNum-1] == "기업 정보 조회":
                    company.show_company_info()
                elif menu[mNum-1] == "기업 호가창 조회":
                    company.show_company_order()
                elif menu[mNum - 1] == "주식 매수":
                    company.buy()
                elif menu[mNum - 1] == "주식 매도":
                    company.sell()
                elif menu[mNum - 1] == "주문 조회":
                    company.show_order_list()
                elif menu[mNum - 1] == "주문 취소":
                    company.cancel_order()
                elif menu[mNum - 1] == "잔고 조회":
                    company.show_balance_inquiry()
                elif menu[mNum - 1] == "재무정보 등록":
                    company.register_financial_info()
                elif menu[mNum - 1] == "배당금 지급":
                    company.dividend_payment()
                else:
                    break
        else:   # 일반고객 계정
            while True:
                menu = ["입금", "출금", "상장 기업 목록 조회", "기업 정보 조회", "기업 호가창 조회", "주식 매수", "주식 매도", "주문 조회", "주문 취소", "잔고 조회", "포트폴리오 비중 조회", "로그아웃"]
                show_menu(menu)
                mNum = choose_menu(menu)
                if mNum == None:
                    systemRun = False
                    break
                elif menu[mNum-1] == "입금":
                    customer.deposit()
                elif menu[mNum-1] == "출금":
                    customer.withdrawal()
                elif menu[mNum-1] == "상장 기업 목록 조회":
                    customer.show_company_list()
                elif menu[mNum-1] == "기업 정보 조회":
                    customer.show_company_info()
                elif menu[mNum-1] == "기업 호가창 조회":
                    customer.show_company_order()
                elif menu[mNum - 1] == "주식 매수":
                    customer.buy()
                elif menu[mNum - 1] == "주식 매도":
                    customer.sell()
                elif menu[mNum - 1] == "주문 조회":
                    customer.show_order_list()
                elif menu[mNum - 1] == "주문 취소":
                    customer.cancel_order()
                elif menu[mNum - 1] == "잔고 조회":
                    customer.show_balance_inquiry()
                elif menu[mNum - 1] == "포트폴리오 비중 조회":
                    customer.portfolio_weight_inquiry()
                else:
                    break

if __name__ == '__main__':
    main()
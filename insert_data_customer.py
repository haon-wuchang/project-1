import json
import mysql.connector

# MySQL 연결 설정
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="customer_db"
)
cursor = db.cursor()

# JSON 데이터 (마지막 , 삭제됨)
json_data = """
[
  {
    "id": "1",
    "username": "gimminjun",
    "email": "ogsun68@google.com",
    "phone": "010-8725-8614",
    "name": "김주원",
    "password": "hashed_password_1",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-03-29",
        "quantity": 4
      },
      {
        "product_id": "12",
        "order_date": "2024-05-06",
        "quantity": 3
      }
    ],
    "cart": [],
    "favorites": [],
    "last_login": "2024-04-16",
    "address": "대전광역시 강남구 영동대0로 (우진한박면)",
    "birth_date": "1992-10-28",
    "membership_level": "Gold"
  },
  {
    "id": "2",
    "username": "areum92",
    "email": "iseonyeong@google.com",
    "phone": "010-1984-8509",
    "name": "김현우",
    "password": "hashed_password_2",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-02-18",
        "quantity": 2
      },
      {
        "product_id": "6",
        "order_date": "2024-12-31",
        "quantity": 5
      }
    ],
    "cart": [
      "15",
      "4",
      "18",
      "20",
      "10"
    ],
    "favorites": [
      "6",
      "7",
      "2",
      "18",
      "6"
    ],
    "last_login": "2025-01-30",
    "address": "울산광역시 성동구 봉은사길",
    "birth_date": "1982-08-28",
    "membership_level": "Silver"
  },
  {
    "id": "3",
    "username": "sgim",
    "email": "jihun68@daum.com",
    "phone": "010-7239-7158",
    "name": "이아름",
    "password": "hashed_password_3",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-08-08",
        "quantity": 2
      },
      {
        "product_id": "16",
        "order_date": "2024-09-23",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2024-03-09",
        "quantity": 5
      },
      {
        "product_id": "9",
        "order_date": "2025-01-12",
        "quantity": 1
      }
    ],
    "cart": [],
    "favorites": [
      "18",
      "9",
      "5",
      "5",
      "6"
    ],
    "last_login": "2024-12-10",
    "address": "대구광역시 동구 선릉가 (수진이이리)",
    "birth_date": "1966-01-25",
    "membership_level": "Silver"
  },
  {
    "id": "4",
    "username": "dohyeon80",
    "email": "yunseo90@naver.com",
    "phone": "010-9869-3468",
    "name": "송정자",
    "password": "hashed_password_4",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-04-30",
        "quantity": 1
      }
    ],
    "cart": [
      "4",
      "12",
      "3",
      "8",
      "10"
    ],
    "favorites": [
      "10"
    ],
    "last_login": "2024-06-10",
    "address": "전라남도 안성시 선릉거리 (준혁노마을)",
    "birth_date": "1963-04-16",
    "membership_level": "Silver"
  },
  {
    "id": "5",
    "username": "dohyeongim",
    "email": "baegseonghyeon@daum.com",
    "phone": "010-6388-7132",
    "name": "이서영",
    "password": "hashed_password_5",
    "orders": [
      {
        "product_id": "17",
        "order_date": "2024-05-29",
        "quantity": 4
      },
      {
        "product_id": "1",
        "order_date": "2024-09-26",
        "quantity": 1
      },
      {
        "product_id": "10",
        "order_date": "2025-01-13",
        "quantity": 3
      },
      {
        "product_id": "16",
        "order_date": "2024-07-27",
        "quantity": 1
      },
      {
        "product_id": "13",
        "order_date": "2024-09-29",
        "quantity": 4
      }
    ],
    "cart": [
      "17"
    ],
    "favorites": [
      "7",
      "11",
      "8",
      "17",
      "9"
    ],
    "last_login": "2024-12-16",
    "address": "경기도 연천군 봉은사3거리",
    "birth_date": "1990-11-11",
    "membership_level": "Platinum"
  },
  {
    "id": "6",
    "username": "bagareum",
    "email": "gwangsu27@daum.com",
    "phone": "010-6497-2011",
    "name": "김보람",
    "password": "hashed_password_6",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2024-08-07",
        "quantity": 3
      },
      {
        "product_id": "19",
        "order_date": "2024-11-23",
        "quantity": 1
      }
    ],
    "cart": [
      "2",
      "12",
      "20"
    ],
    "favorites": [
      "18",
      "3",
      "16",
      "5",
      "6"
    ],
    "last_login": "2024-06-29",
    "address": "세종특별자치시 강동구 가락거리 (지현김신동)",
    "birth_date": "1972-05-15",
    "membership_level": "Platinum"
  },
  {
    "id": "7",
    "username": "minjunbag",
    "email": "jihun90@daum.com",
    "phone": "010-8474-2664",
    "name": "백영순",
    "password": "hashed_password_7",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2024-06-26",
        "quantity": 3
      }
    ],
    "cart": [
      "13",
      "13",
      "3",
      "19"
    ],
    "favorites": [
      "7",
      "9",
      "20",
      "9",
      "13"
    ],
    "last_login": "2024-07-30",
    "address": "대전광역시 강남구 도산대5가 (영순나동)",
    "birth_date": "1948-03-02",
    "membership_level": "Platinum"
  },
  {
    "id": "8",
    "username": "jbag",
    "email": "bagminjae@daum.com",
    "phone": "010-1875-7033",
    "name": "김준호",
    "password": "hashed_password_8",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-10-28",
        "quantity": 5
      },
      {
        "product_id": "11",
        "order_date": "2024-06-26",
        "quantity": 1
      },
      {
        "product_id": "6",
        "order_date": "2024-08-01",
        "quantity": 3
      }
    ],
    "cart": [
      "1",
      "16",
      "15",
      "15",
      "9"
    ],
    "favorites": [
      "15",
      "4"
    ],
    "last_login": "2024-07-09",
    "address": "전라남도 횡성군 백제고분63거리",
    "birth_date": "1949-11-10",
    "membership_level": "Gold"
  },
  {
    "id": "9",
    "username": "mbag",
    "email": "heoogsun@naver.com",
    "phone": "010-3799-2177",
    "name": "하영길",
    "password": "hashed_password_9",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-07-28",
        "quantity": 4
      },
      {
        "product_id": "9",
        "order_date": "2024-10-08",
        "quantity": 4
      },
      {
        "product_id": "2",
        "order_date": "2024-02-05",
        "quantity": 3
      },
      {
        "product_id": "9",
        "order_date": "2024-12-27",
        "quantity": 2
      },
      {
        "product_id": "18",
        "order_date": "2024-11-03",
        "quantity": 5
      }
    ],
    "cart": [
      "5"
    ],
    "favorites": [
      "14",
      "4"
    ],
    "last_login": "2024-04-03",
    "address": "광주광역시 강동구 가락0로",
    "birth_date": "2006-06-05",
    "membership_level": "Gold"
  },
  {
    "id": "10",
    "username": "lheo",
    "email": "qgim@daum.com",
    "phone": "010-5209-7642",
    "name": "김재호",
    "password": "hashed_password_10",
    "orders": [],
    "cart": [
      "10"
    ],
    "favorites": [],
    "last_login": "2024-10-15",
    "address": "충청북도 안양시 동안구 가락길",
    "birth_date": "1999-06-14",
    "membership_level": "Gold"
  },
  {
    "id": "11",
    "username": "ono",
    "email": "seonghyeongim@google.com",
    "phone": "010-2395-3296",
    "name": "윤영수",
    "password": "hashed_password_11",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2024-10-03",
        "quantity": 5
      }
    ],
    "cart": [
      "19",
      "2",
      "6",
      "16"
    ],
    "favorites": [
      "4",
      "16"
    ],
    "last_login": "2024-04-16",
    "address": "충청남도 고성군 오금로",
    "birth_date": "1951-09-23",
    "membership_level": "Platinum"
  },
  {
    "id": "12",
    "username": "gimyeongsig",
    "email": "ygim@daum.com",
    "phone": "010-5390-7668",
    "name": "정영진",
    "password": "hashed_password_12",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2025-01-11",
        "quantity": 1
      },
      {
        "product_id": "4",
        "order_date": "2024-06-27",
        "quantity": 4
      },
      {
        "product_id": "16",
        "order_date": "2024-02-25",
        "quantity": 3
      }
    ],
    "cart": [],
    "favorites": [
      "11",
      "6"
    ],
    "last_login": "2024-02-18",
    "address": "전라북도 부천시 원미구 서초대0길",
    "birth_date": "1996-09-28",
    "membership_level": "Platinum"
  },
  {
    "id": "13",
    "username": "bbag",
    "email": "bagmiyeong@daum.com",
    "phone": "010-1478-9801",
    "name": "안승현",
    "password": "hashed_password_13",
    "orders": [
      {
        "product_id": "20",
        "order_date": "2024-03-31",
        "quantity": 5
      },
      {
        "product_id": "14",
        "order_date": "2024-04-25",
        "quantity": 5
      }
    ],
    "cart": [
      "20"
    ],
    "favorites": [],
    "last_login": "2024-11-22",
    "address": "대구광역시 남구 봉은사18거리",
    "birth_date": "1951-06-27",
    "membership_level": "Silver"
  },
  {
    "id": "14",
    "username": "sonjeongsug",
    "email": "seoyun69@daum.com",
    "phone": "010-3119-7152",
    "name": "김진호",
    "password": "hashed_password_14",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-10-29",
        "quantity": 1
      },
      {
        "product_id": "4",
        "order_date": "2024-12-19",
        "quantity": 2
      }
    ],
    "cart": [
      "10",
      "9",
      "6",
      "14"
    ],
    "favorites": [
      "16",
      "4",
      "16",
      "7",
      "6"
    ],
    "last_login": "2024-04-15",
    "address": "부산광역시 성동구 강남대길",
    "birth_date": "1946-10-08",
    "membership_level": "Gold"
  },
  {
    "id": "15",
    "username": "zjo",
    "email": "seoyeongim@naver.com",
    "phone": "010-2702-1143",
    "name": "이지민",
    "password": "hashed_password_15",
    "orders": [
      {
        "product_id": "2",
        "order_date": "2024-04-30",
        "quantity": 5
      },
      {
        "product_id": "8",
        "order_date": "2024-07-06",
        "quantity": 5
      }
    ],
    "cart": [
      "2",
      "10",
      "5",
      "15",
      "5"
    ],
    "favorites": [
      "1",
      "9"
    ],
    "last_login": "2024-06-18",
    "address": "세종특별자치시 서대문구 언주374가 (정숙김이마을)",
    "birth_date": "1957-07-10",
    "membership_level": "Silver"
  },
  {
    "id": "16",
    "username": "seomyeongja",
    "email": "coeogja@google.com",
    "phone": "010-4741-1388",
    "name": "강영수",
    "password": "hashed_password_16",
    "orders": [],
    "cart": [],
    "favorites": [
      "7",
      "6",
      "11",
      "20"
    ],
    "last_login": "2024-10-22",
    "address": "광주광역시 양천구 잠실가",
    "birth_date": "1997-07-12",
    "membership_level": "Gold"
  },
  {
    "id": "17",
    "username": "coeeunseo",
    "email": "jinugim@naver.com",
    "phone": "010-1436-6476",
    "name": "김민서",
    "password": "hashed_password_17",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2024-03-31",
        "quantity": 5
      },
      {
        "product_id": "12",
        "order_date": "2024-02-12",
        "quantity": 4
      }
    ],
    "cart": [
      "10",
      "9",
      "20",
      "18"
    ],
    "favorites": [
      "16",
      "17",
      "13",
      "13"
    ],
    "last_login": "2024-11-23",
    "address": "부산광역시 광진구 봉은사4거리 (하윤전면)",
    "birth_date": "1992-05-02",
    "membership_level": "Silver"
  },
  {
    "id": "18",
    "username": "sunog83",
    "email": "seoyeong29@naver.com",
    "phone": "010-7915-9524",
    "name": "이지현",
    "password": "hashed_password_18",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-07-19",
        "quantity": 2
      },
      {
        "product_id": "20",
        "order_date": "2024-12-16",
        "quantity": 1
      },
      {
        "product_id": "5",
        "order_date": "2024-09-30",
        "quantity": 2
      }
    ],
    "cart": [
      "20",
      "17",
      "1",
      "10"
    ],
    "favorites": [],
    "last_login": "2024-08-14",
    "address": "대전광역시 동대문구 서초대20가",
    "birth_date": "1945-01-04",
    "membership_level": "Gold"
  },
  {
    "id": "19",
    "username": "gimjia",
    "email": "mijeong32@daum.com",
    "phone": "010-2744-2766",
    "name": "손아름",
    "password": "hashed_password_19",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-04-19",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-06-26",
        "quantity": 2
      },
      {
        "product_id": "12",
        "order_date": "2025-01-06",
        "quantity": 3
      },
      {
        "product_id": "12",
        "order_date": "2024-08-18",
        "quantity": 5
      },
      {
        "product_id": "17",
        "order_date": "2024-07-15",
        "quantity": 5
      }
    ],
    "cart": [
      "12",
      "9"
    ],
    "favorites": [
      "13"
    ],
    "last_login": "2024-12-23",
    "address": "충청북도 안산시 상록구 학동가",
    "birth_date": "1996-05-14",
    "membership_level": "Bronze"
  },
  {
    "id": "20",
    "username": "yeongsigsong",
    "email": "ujini@google.com",
    "phone": "010-6884-8498",
    "name": "이동현",
    "password": "hashed_password_20",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2025-01-07",
        "quantity": 1
      },
      {
        "product_id": "18",
        "order_date": "2025-01-07",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2024-03-12",
        "quantity": 2
      },
      {
        "product_id": "8",
        "order_date": "2024-09-02",
        "quantity": 5
      }
    ],
    "cart": [
      "12",
      "10",
      "7",
      "6",
      "14"
    ],
    "favorites": [
      "20",
      "1",
      "16",
      "1"
    ],
    "last_login": "2024-05-13",
    "address": "전라남도 횡성군 서초대1로",
    "birth_date": "1998-01-02",
    "membership_level": "Platinum"
  },
  {
    "id": "21",
    "username": "jeongsu10",
    "email": "gimseongsu@google.com",
    "phone": "010-9574-5025",
    "name": "허승현",
    "password": "hashed_password_21",
    "orders": [],
    "cart": [
      "6"
    ],
    "favorites": [
      "8"
    ],
    "last_login": "2024-02-22",
    "address": "인천광역시 광진구 서초대거리 (예지윤읍)",
    "birth_date": "1968-05-07",
    "membership_level": "Silver"
  },
  {
    "id": "22",
    "username": "gwangsujang",
    "email": "oseohyeon@naver.com",
    "phone": "010-9733-6425",
    "name": "황미정",
    "password": "hashed_password_22",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-04-02",
        "quantity": 2
      },
      {
        "product_id": "11",
        "order_date": "2024-07-25",
        "quantity": 2
      }
    ],
    "cart": [
      "7",
      "9"
    ],
    "favorites": [
      "2",
      "12"
    ],
    "last_login": "2024-04-09",
    "address": "울산광역시 남구 선릉로 (영진김읍)",
    "birth_date": "1997-11-11",
    "membership_level": "Silver"
  },
  {
    "id": "23",
    "username": "pgim",
    "email": "jeongsun50@naver.com",
    "phone": "010-4708-8581",
    "name": "구수진",
    "password": "hashed_password_23",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-12-01",
        "quantity": 5
      },
      {
        "product_id": "12",
        "order_date": "2024-09-18",
        "quantity": 3
      },
      {
        "product_id": "8",
        "order_date": "2024-06-14",
        "quantity": 3
      },
      {
        "product_id": "20",
        "order_date": "2024-05-26",
        "quantity": 1
      },
      {
        "product_id": "3",
        "order_date": "2024-09-27",
        "quantity": 2
      }
    ],
    "cart": [],
    "favorites": [
      "12"
    ],
    "last_login": "2024-03-20",
    "address": "광주광역시 서초구 삼성5로",
    "birth_date": "1965-12-03",
    "membership_level": "Bronze"
  },
  {
    "id": "24",
    "username": "igim",
    "email": "cjeong@naver.com",
    "phone": "010-3900-8429",
    "name": "문서연",
    "password": "hashed_password_24",
    "orders": [],
    "cart": [
      "18",
      "16",
      "20"
    ],
    "favorites": [],
    "last_login": "2024-05-10",
    "address": "울산광역시 강서구 논현0로 (서윤김김마을)",
    "birth_date": "2001-09-28",
    "membership_level": "Platinum"
  },
  {
    "id": "25",
    "username": "minseo79",
    "email": "hyeonju44@naver.com",
    "phone": "010-8889-6492",
    "name": "홍영환",
    "password": "hashed_password_25",
    "orders": [],
    "cart": [
      "9",
      "19"
    ],
    "favorites": [
      "16"
    ],
    "last_login": "2024-05-27",
    "address": "서울특별시 양천구 백제고분가",
    "birth_date": "1968-09-07",
    "membership_level": "Bronze"
  },
  {
    "id": "26",
    "username": "jeonghun56",
    "email": "xgim@google.com",
    "phone": "010-8104-3834",
    "name": "한성수",
    "password": "hashed_password_26",
    "orders": [
      {
        "product_id": "11",
        "order_date": "2024-04-20",
        "quantity": 5
      },
      {
        "product_id": "6",
        "order_date": "2024-08-04",
        "quantity": 2
      }
    ],
    "cart": [
      "10",
      "6",
      "9"
    ],
    "favorites": [
      "7",
      "18"
    ],
    "last_login": "2024-02-12",
    "address": "광주광역시 동작구 삼성60거리",
    "birth_date": "1993-10-06",
    "membership_level": "Bronze"
  },
  {
    "id": "27",
    "username": "yeongja65",
    "email": "ci@google.com",
    "phone": "010-4131-3225",
    "name": "허진우",
    "password": "hashed_password_27",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-03-05",
        "quantity": 5
      },
      {
        "product_id": "14",
        "order_date": "2024-07-14",
        "quantity": 4
      },
      {
        "product_id": "3",
        "order_date": "2024-08-10",
        "quantity": 3
      }
    ],
    "cart": [
      "17",
      "7",
      "14",
      "19",
      "11"
    ],
    "favorites": [
      "10"
    ],
    "last_login": "2024-10-02",
    "address": "강원도 용인시 기흥구 서초중앙길",
    "birth_date": "2000-12-01",
    "membership_level": "Bronze"
  },
  {
    "id": "28",
    "username": "imigyeong",
    "email": "seoyun79@naver.com",
    "phone": "010-4704-4593",
    "name": "이서윤",
    "password": "hashed_password_28",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-03-13",
        "quantity": 5
      },
      {
        "product_id": "20",
        "order_date": "2024-07-28",
        "quantity": 2
      },
      {
        "product_id": "9",
        "order_date": "2024-08-04",
        "quantity": 3
      }
    ],
    "cart": [
      "1",
      "20",
      "15",
      "19",
      "7"
    ],
    "favorites": [
      "17",
      "7"
    ],
    "last_login": "2024-07-23",
    "address": "울산광역시 노원구 도산대길",
    "birth_date": "1948-12-10",
    "membership_level": "Silver"
  },
  {
    "id": "29",
    "username": "sumingo",
    "email": "iha@daum.com",
    "phone": "010-3827-9586",
    "name": "김서연",
    "password": "hashed_password_29",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2025-01-10",
        "quantity": 2
      },
      {
        "product_id": "12",
        "order_date": "2024-07-24",
        "quantity": 1
      },
      {
        "product_id": "2",
        "order_date": "2024-04-22",
        "quantity": 1
      },
      {
        "product_id": "4",
        "order_date": "2024-03-30",
        "quantity": 3
      },
      {
        "product_id": "16",
        "order_date": "2024-11-23",
        "quantity": 5
      }
    ],
    "cart": [
      "19"
    ],
    "favorites": [
      "17",
      "3",
      "3"
    ],
    "last_login": "2024-10-05",
    "address": "경상남도 수원시 장안구 테헤란길",
    "birth_date": "1993-10-11",
    "membership_level": "Platinum"
  },
  {
    "id": "30",
    "username": "yeonghyi69",
    "email": "jeongsujin@google.com",
    "phone": "010-8386-9336",
    "name": "최재호",
    "password": "hashed_password_30",
    "orders": [
      {
        "product_id": "17",
        "order_date": "2024-05-04",
        "quantity": 4
      }
    ],
    "cart": [
      "7",
      "14",
      "1",
      "5"
    ],
    "favorites": [
      "17",
      "17",
      "16",
      "4",
      "5"
    ],
    "last_login": "2024-10-17",
    "address": "경상북도 수원시 양재천0로",
    "birth_date": "1994-06-29",
    "membership_level": "Gold"
  },
  {
    "id": "31",
    "username": "seoyun51",
    "email": "fi@naver.com",
    "phone": "010-9315-9960",
    "name": "이유진",
    "password": "hashed_password_31",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-03-27",
        "quantity": 4
      },
      {
        "product_id": "5",
        "order_date": "2024-07-22",
        "quantity": 2
      },
      {
        "product_id": "12",
        "order_date": "2024-05-26",
        "quantity": 5
      },
      {
        "product_id": "9",
        "order_date": "2024-10-16",
        "quantity": 4
      },
      {
        "product_id": "11",
        "order_date": "2025-01-14",
        "quantity": 5
      }
    ],
    "cart": [
      "3",
      "17"
    ],
    "favorites": [
      "10"
    ],
    "last_login": "2024-04-08",
    "address": "경상남도 의왕시 반포대거리 (재현윤최리)",
    "birth_date": "1974-07-10",
    "membership_level": "Silver"
  },
  {
    "id": "32",
    "username": "tgim",
    "email": "ihyeonji@google.com",
    "phone": "010-5039-6231",
    "name": "최지우",
    "password": "hashed_password_32",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-06-26",
        "quantity": 3
      },
      {
        "product_id": "15",
        "order_date": "2024-07-25",
        "quantity": 1
      },
      {
        "product_id": "17",
        "order_date": "2024-07-31",
        "quantity": 4
      },
      {
        "product_id": "7",
        "order_date": "2024-08-13",
        "quantity": 2
      }
    ],
    "cart": [
      "9",
      "3"
    ],
    "favorites": [
      "7",
      "20",
      "10",
      "6",
      "7"
    ],
    "last_login": "2025-01-08",
    "address": "충청남도 안양시 만안구 논현97길 (중수황나리)",
    "birth_date": "1946-10-01",
    "membership_level": "Silver"
  },
  {
    "id": "33",
    "username": "ti",
    "email": "coejeonghun@naver.com",
    "phone": "010-2949-2404",
    "name": "배정남",
    "password": "hashed_password_33",
    "orders": [],
    "cart": [
      "11",
      "1",
      "6"
    ],
    "favorites": [
      "7",
      "3"
    ],
    "last_login": "2025-01-05",
    "address": "강원도 수원시 영통구 압구정73거리",
    "birth_date": "1981-06-05",
    "membership_level": "Gold"
  },
  {
    "id": "34",
    "username": "scoe",
    "email": "coeboram@naver.com",
    "phone": "010-9100-7843",
    "name": "김영희",
    "password": "hashed_password_34",
    "orders": [
      {
        "product_id": "3",
        "order_date": "2024-11-08",
        "quantity": 5
      },
      {
        "product_id": "16",
        "order_date": "2024-03-27",
        "quantity": 5
      },
      {
        "product_id": "8",
        "order_date": "2024-06-30",
        "quantity": 3
      }
    ],
    "cart": [
      "19",
      "6",
      "5"
    ],
    "favorites": [
      "6",
      "10",
      "1",
      "10",
      "19"
    ],
    "last_login": "2024-07-28",
    "address": "전라남도 보령시 양재천54가",
    "birth_date": "1992-11-13",
    "membership_level": "Gold"
  },
  {
    "id": "35",
    "username": "minjeongsu",
    "email": "lgim@daum.com",
    "phone": "010-8933-8647",
    "name": "이우진",
    "password": "hashed_password_35",
    "orders": [
      {
        "product_id": "3",
        "order_date": "2025-02-04",
        "quantity": 3
      },
      {
        "product_id": "8",
        "order_date": "2024-07-31",
        "quantity": 5
      }
    ],
    "cart": [
      "7",
      "7"
    ],
    "favorites": [
      "9",
      "19",
      "5",
      "19",
      "5"
    ],
    "last_login": "2024-08-10",
    "address": "인천광역시 성북구 오금거리 (은영김오동)",
    "birth_date": "1999-09-03",
    "membership_level": "Platinum"
  },
  {
    "id": "36",
    "username": "sunoggim",
    "email": "gimjimin@daum.com",
    "phone": "010-2452-9430",
    "name": "류시우",
    "password": "hashed_password_36",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2025-01-21",
        "quantity": 1
      },
      {
        "product_id": "15",
        "order_date": "2024-05-26",
        "quantity": 5
      },
      {
        "product_id": "10",
        "order_date": "2024-09-20",
        "quantity": 3
      }
    ],
    "cart": [
      "12",
      "13",
      "13"
    ],
    "favorites": [
      "11",
      "16"
    ],
    "last_login": "2024-05-15",
    "address": "부산광역시 영등포구 오금길",
    "birth_date": "1991-03-18",
    "membership_level": "Gold"
  },
  {
    "id": "37",
    "username": "suminseo",
    "email": "agim@google.com",
    "phone": "010-5977-9538",
    "name": "서병철",
    "password": "hashed_password_37",
    "orders": [
      {
        "product_id": "11",
        "order_date": "2024-05-20",
        "quantity": 2
      },
      {
        "product_id": "13",
        "order_date": "2024-02-26",
        "quantity": 3
      }
    ],
    "cart": [
      "17",
      "3"
    ],
    "favorites": [],
    "last_login": "2024-07-05",
    "address": "강원도 고양시 덕양구 잠실로",
    "birth_date": "2006-02-14",
    "membership_level": "Gold"
  },
  {
    "id": "38",
    "username": "pgim",
    "email": "junyeongryu@naver.com",
    "phone": "010-6472-9616",
    "name": "김예은",
    "password": "hashed_password_38",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-09-26",
        "quantity": 2
      },
      {
        "product_id": "6",
        "order_date": "2024-06-06",
        "quantity": 3
      },
      {
        "product_id": "18",
        "order_date": "2024-08-02",
        "quantity": 3
      }
    ],
    "cart": [],
    "favorites": [
      "4",
      "18",
      "19",
      "17",
      "9"
    ],
    "last_login": "2025-01-26",
    "address": "전라북도 횡성군 삼성60거리",
    "birth_date": "1975-08-26",
    "membership_level": "Platinum"
  },
  {
    "id": "39",
    "username": "junho50",
    "email": "eunji65@naver.com",
    "phone": "010-1955-7094",
    "name": "박하윤",
    "password": "hashed_password_39",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-05-06",
        "quantity": 4
      },
      {
        "product_id": "1",
        "order_date": "2025-01-31",
        "quantity": 5
      },
      {
        "product_id": "11",
        "order_date": "2024-04-26",
        "quantity": 1
      },
      {
        "product_id": "8",
        "order_date": "2025-01-31",
        "quantity": 1
      }
    ],
    "cart": [
      "7",
      "17"
    ],
    "favorites": [],
    "last_login": "2025-01-03",
    "address": "충청북도 안양시 만안구 영동대4로",
    "birth_date": "1953-06-22",
    "membership_level": "Platinum"
  },
  {
    "id": "40",
    "username": "jeongho18",
    "email": "hanmyeongsug@naver.com",
    "phone": "010-9841-1844",
    "name": "김상훈",
    "password": "hashed_password_40",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-03-08",
        "quantity": 2
      },
      {
        "product_id": "7",
        "order_date": "2024-03-22",
        "quantity": 2
      },
      {
        "product_id": "13",
        "order_date": "2024-03-19",
        "quantity": 2
      },
      {
        "product_id": "12",
        "order_date": "2024-08-07",
        "quantity": 4
      },
      {
        "product_id": "10",
        "order_date": "2024-02-29",
        "quantity": 1
      }
    ],
    "cart": [
      "10",
      "4",
      "8",
      "19"
    ],
    "favorites": [
      "9",
      "19"
    ],
    "last_login": "2024-06-20",
    "address": "울산광역시 노원구 백제고분거리 (민준최리)",
    "birth_date": "1982-03-31",
    "membership_level": "Bronze"
  }
]
"""

# JSON 파싱
data = json.loads(json_data, strict=False)  # JSON 제어 문자 허용

# 중복 제거를 위한 세트
existing_usernames = set()
existing_emails = set()

# 고객 데이터 삽입
for customer in data:
    customer_id = int(customer["id"])  # ID를 정수로 변환
    username = customer["username"]
    email = customer["email"]
    
# 전화번호를 20자로 제한
    phone = customer["phone"][:20]

    # 중복된 username 또는 email이 있으면 건너뛴다
    if username in existing_usernames or email in existing_emails:
        continue  # 중복이면 삽입하지 않음

    # 중복이 없으면 추가
    existing_usernames.add(username)
    existing_emails.add(email)

    cursor.execute("""
        INSERT INTO customers (id, username, email, phone, name, password, address, birth_date, membership_level, last_login)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        customer_id, username, email, customer["phone"],
        customer["name"], customer["password"], customer["address"],
        customer["birth_date"], customer["membership_level"], customer["last_login"]
    ))

    # 주문 데이터 삽입
    for order in customer["orders"]:
        cursor.execute("""
            INSERT INTO orders (customer_id, product_id, order_date, quantity)
            VALUES (%s, %s, %s, %s)
        """, (
            customer_id, int(order["product_id"]), order["order_date"], int(order["quantity"])
        ))

    # 장바구니 데이터 삽입
    for product_id in customer["cart"]:
        cursor.execute("""
            INSERT INTO cart (customer_id, product_id)
            VALUES (%s, %s)
        """, (customer_id, int(product_id)))

    # 좋아요 데이터 삽입
    for product_id in customer["favorites"]:
        cursor.execute("""
            INSERT INTO favorites (customer_id, product_id)
            VALUES (%s, %s)
        """, (customer_id, int(product_id)))

# 변경사항 저장
db.commit()

# 연결 닫기
cursor.close()
db.close()

print("데이터 삽입 완료! (연동 문제 해결됨 ✅)")

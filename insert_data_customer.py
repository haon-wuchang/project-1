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
  },
  {
    "id": "41",
    "username": "gimjiyeong",
    "email": "misugbag@naver.com",
    "phone": "010-1354-5990",
    "name": "이경희",
    "password": "hashed_password_41",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2024-11-20",
        "quantity": 5
      },
      {
        "product_id": "15",
        "order_date": "2024-09-30",
        "quantity": 4
      }
    ],
    "cart": [
      "4",
      "20"
    ],
    "favorites": [
      "1",
      "18",
      "4",
      "13",
      "1"
    ],
    "last_login": "2024-08-06",
    "address": "부산광역시 동구 가락36가 (지훈최조읍)",
    "birth_date": "1950-01-31",
    "membership_level": "Silver"
  },
  {
    "id": "42",
    "username": "rbag",
    "email": "rgim@daum.com",
    "phone": "010-8233-5567",
    "name": "이상현",
    "password": "hashed_password_42",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-04-02",
        "quantity": 4
      },
      {
        "product_id": "20",
        "order_date": "2024-06-06",
        "quantity": 2
      },
      {
        "product_id": "14",
        "order_date": "2024-07-15",
        "quantity": 3
      },
      {
        "product_id": "15",
        "order_date": "2024-02-19",
        "quantity": 4
      }
    ],
    "cart": [
      "6",
      "6"
    ],
    "favorites": [
      "2",
      "18",
      "17"
    ],
    "last_login": "2024-03-09",
    "address": "울산광역시 서대문구 양재천6거리 (중수김면)",
    "birth_date": "1973-03-24",
    "membership_level": "Bronze"
  },
  {
    "id": "43",
    "username": "pcoe",
    "email": "cgang@google.com",
    "phone": "010-6532-1158",
    "name": "김진호",
    "password": "hashed_password_43",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-09-10",
        "quantity": 1
      }
    ],
    "cart": [
      "1",
      "15"
    ],
    "favorites": [
      "3"
    ],
    "last_login": "2024-04-09",
    "address": "충청북도 횡성군 영동대길 (상현김마을)",
    "birth_date": "1978-06-18",
    "membership_level": "Bronze"
  },
  {
    "id": "44",
    "username": "junyeongjo",
    "email": "ijeongung@google.com",
    "phone": "010-4855-6107",
    "name": "이주원",
    "password": "hashed_password_44",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-02-14",
        "quantity": 2
      },
      {
        "product_id": "10",
        "order_date": "2024-10-09",
        "quantity": 2
      },
      {
        "product_id": "14",
        "order_date": "2025-01-29",
        "quantity": 5
      }
    ],
    "cart": [
      "1",
      "16",
      "11",
      "15",
      "16"
    ],
    "favorites": [
      "12",
      "19"
    ],
    "last_login": "2024-05-30",
    "address": "전라북도 당진시 잠실8가",
    "birth_date": "1945-11-06",
    "membership_level": "Gold"
  },
  {
    "id": "45",
    "username": "songjunseo",
    "email": "gbag@naver.com",
    "phone": "010-6252-9345",
    "name": "이정희",
    "password": "hashed_password_45",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-08-27",
        "quantity": 2
      },
      {
        "product_id": "9",
        "order_date": "2024-03-13",
        "quantity": 1
      },
      {
        "product_id": "18",
        "order_date": "2025-01-29",
        "quantity": 1
      }
    ],
    "cart": [
      "2"
    ],
    "favorites": [
      "3",
      "6"
    ],
    "last_login": "2024-04-06",
    "address": "경상북도 안양시 동안구 서초중앙43길 (성수김리)",
    "birth_date": "1966-07-17",
    "membership_level": "Silver"
  },
  {
    "id": "46",
    "username": "junyeong56",
    "email": "gimjongsu@naver.com",
    "phone": "010-7294-8524",
    "name": "이준혁",
    "password": "hashed_password_46",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-12-18",
        "quantity": 1
      },
      {
        "product_id": "7",
        "order_date": "2024-03-02",
        "quantity": 2
      },
      {
        "product_id": "13",
        "order_date": "2024-12-17",
        "quantity": 5
      },
      {
        "product_id": "10",
        "order_date": "2024-08-23",
        "quantity": 1
      }
    ],
    "cart": [
      "16",
      "13"
    ],
    "favorites": [],
    "last_login": "2024-12-01",
    "address": "광주광역시 노원구 서초중앙58로 (미경권이면)",
    "birth_date": "1987-03-09",
    "membership_level": "Platinum"
  },
  {
    "id": "47",
    "username": "yeongsu09",
    "email": "jeongsugbag@naver.com",
    "phone": "010-5556-9123",
    "name": "심준혁",
    "password": "hashed_password_47",
    "orders": [],
    "cart": [
      "4"
    ],
    "favorites": [
      "10",
      "9"
    ],
    "last_login": "2024-12-29",
    "address": "전라북도 수원시 영통구 영동대거리",
    "birth_date": "1999-05-17",
    "membership_level": "Silver"
  },
  {
    "id": "48",
    "username": "seungmingwag",
    "email": "gimdohyeon@google.com",
    "phone": "010-5026-5850",
    "name": "권준영",
    "password": "hashed_password_48",
    "orders": [
      {
        "product_id": "2",
        "order_date": "2025-01-10",
        "quantity": 1
      },
      {
        "product_id": "11",
        "order_date": "2024-04-18",
        "quantity": 4
      },
      {
        "product_id": "10",
        "order_date": "2024-08-12",
        "quantity": 5
      }
    ],
    "cart": [],
    "favorites": [
      "2"
    ],
    "last_login": "2024-07-01",
    "address": "울산광역시 도봉구 오금37가",
    "birth_date": "1970-06-14",
    "membership_level": "Gold"
  },
  {
    "id": "49",
    "username": "jeongsun46",
    "email": "jeongungbag@daum.com",
    "phone": "010-9302-6198",
    "name": "김하윤",
    "password": "hashed_password_49",
    "orders": [],
    "cart": [
      "6",
      "3",
      "9"
    ],
    "favorites": [
      "7",
      "8",
      "15",
      "4",
      "8"
    ],
    "last_login": "2024-08-19",
    "address": "대구광역시 동구 봉은사486가",
    "birth_date": "1957-12-18",
    "membership_level": "Bronze"
  },
  {
    "id": "50",
    "username": "sunja07",
    "email": "gimmyeongsug@naver.com",
    "phone": "010-4237-1708",
    "name": "진은경",
    "password": "hashed_password_50",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-08-07",
        "quantity": 2
      },
      {
        "product_id": "10",
        "order_date": "2024-08-25",
        "quantity": 4
      },
      {
        "product_id": "9",
        "order_date": "2024-12-28",
        "quantity": 1
      },
      {
        "product_id": "11",
        "order_date": "2024-03-20",
        "quantity": 1
      },
      {
        "product_id": "17",
        "order_date": "2024-06-19",
        "quantity": 2
      }
    ],
    "cart": [
      "5",
      "12",
      "20",
      "7",
      "11"
    ],
    "favorites": [
      "16",
      "12"
    ],
    "last_login": "2024-11-30",
    "address": "전라남도 이천시 봉은사9로",
    "birth_date": "1972-08-09",
    "membership_level": "Platinum"
  },
  {
    "id": "51",
    "username": "iseonghun",
    "email": "bagsangho@google.com",
    "phone": "010-7637-4024",
    "name": "권경희",
    "password": "hashed_password_51",
    "orders": [
      {
        "product_id": "20",
        "order_date": "2024-02-13",
        "quantity": 2
      },
      {
        "product_id": "7",
        "order_date": "2024-02-23",
        "quantity": 1
      }
    ],
    "cart": [
      "13",
      "18",
      "9"
    ],
    "favorites": [
      "1",
      "2"
    ],
    "last_login": "2025-01-23",
    "address": "경상북도 화성시 삼성거리",
    "birth_date": "1981-12-29",
    "membership_level": "Silver"
  },
  {
    "id": "52",
    "username": "hyeonjun96",
    "email": "yujin21@google.com",
    "phone": "010-2177-6347",
    "name": "김정훈",
    "password": "hashed_password_52",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-11-17",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2024-12-26",
        "quantity": 3
      },
      {
        "product_id": "8",
        "order_date": "2024-03-27",
        "quantity": 1
      },
      {
        "product_id": "9",
        "order_date": "2024-10-02",
        "quantity": 4
      }
    ],
    "cart": [
      "15"
    ],
    "favorites": [
      "19",
      "2",
      "14",
      "5",
      "17"
    ],
    "last_login": "2024-03-05",
    "address": "대구광역시 금천구 봉은사길",
    "birth_date": "1989-05-08",
    "membership_level": "Bronze"
  },
  {
    "id": "53",
    "username": "yeonghohan",
    "email": "gyeongsugbag@naver.com",
    "phone": "010-1087-1296",
    "name": "김도현",
    "password": "hashed_password_53",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-02-26",
        "quantity": 1
      },
      {
        "product_id": "6",
        "order_date": "2024-12-22",
        "quantity": 5
      },
      {
        "product_id": "6",
        "order_date": "2024-03-20",
        "quantity": 1
      },
      {
        "product_id": "14",
        "order_date": "2024-04-27",
        "quantity": 3
      }
    ],
    "cart": [
      "12",
      "3",
      "15"
    ],
    "favorites": [
      "16",
      "14",
      "4",
      "8",
      "10"
    ],
    "last_login": "2024-10-19",
    "address": "대구광역시 마포구 압구정로 (상현고송리)",
    "birth_date": "1992-08-27",
    "membership_level": "Platinum"
  },
  {
    "id": "54",
    "username": "hyeonui",
    "email": "ygim@naver.com",
    "phone": "010-6414-2426",
    "name": "이경자",
    "password": "hashed_password_54",
    "orders": [],
    "cart": [
      "8",
      "13"
    ],
    "favorites": [
      "7",
      "15",
      "12",
      "16"
    ],
    "last_login": "2024-06-16",
    "address": "세종특별자치시 동작구 양재천거리",
    "birth_date": "1965-12-03",
    "membership_level": "Platinum"
  },
  {
    "id": "55",
    "username": "seoyeongyang",
    "email": "gimcunja@daum.com",
    "phone": "010-5359-8254",
    "name": "김종수",
    "password": "hashed_password_55",
    "orders": [],
    "cart": [],
    "favorites": [
      "17",
      "1",
      "18",
      "6",
      "9"
    ],
    "last_login": "2024-05-10",
    "address": "경상남도 양주시 언주거리",
    "birth_date": "1996-04-25",
    "membership_level": "Gold"
  },
  {
    "id": "56",
    "username": "gimgyeongsug",
    "email": "munjiu@google.com",
    "phone": "010-5379-8632",
    "name": "김정웅",
    "password": "hashed_password_56",
    "orders": [
      {
        "product_id": "13",
        "order_date": "2024-06-04",
        "quantity": 2
      },
      {
        "product_id": "12",
        "order_date": "2024-08-07",
        "quantity": 3
      }
    ],
    "cart": [
      "7",
      "1",
      "7"
    ],
    "favorites": [
      "17",
      "17",
      "17",
      "10"
    ],
    "last_login": "2024-11-20",
    "address": "울산광역시 관악구 논현가",
    "birth_date": "1972-05-09",
    "membership_level": "Platinum"
  },
  {
    "id": "57",
    "username": "jeonghyi68",
    "email": "jeongja36@naver.com",
    "phone": "010-9347-6953",
    "name": "강영숙",
    "password": "hashed_password_57",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2025-01-17",
        "quantity": 4
      },
      {
        "product_id": "17",
        "order_date": "2024-06-19",
        "quantity": 4
      },
      {
        "product_id": "16",
        "order_date": "2025-01-04",
        "quantity": 3
      },
      {
        "product_id": "1",
        "order_date": "2024-03-17",
        "quantity": 5
      },
      {
        "product_id": "4",
        "order_date": "2024-12-11",
        "quantity": 5
      }
    ],
    "cart": [
      "2",
      "6"
    ],
    "favorites": [
      "16",
      "2",
      "7"
    ],
    "last_login": "2024-12-31",
    "address": "인천광역시 강동구 석촌호수7길 (지영박조마을)",
    "birth_date": "1956-04-19",
    "membership_level": "Silver"
  },
  {
    "id": "58",
    "username": "seoyeoneom",
    "email": "igyeongja@google.com",
    "phone": "010-3373-2329",
    "name": "이종수",
    "password": "hashed_password_58",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-04-22",
        "quantity": 4
      },
      {
        "product_id": "19",
        "order_date": "2024-11-18",
        "quantity": 1
      },
      {
        "product_id": "12",
        "order_date": "2024-07-15",
        "quantity": 2
      },
      {
        "product_id": "17",
        "order_date": "2024-12-16",
        "quantity": 2
      },
      {
        "product_id": "18",
        "order_date": "2024-10-01",
        "quantity": 2
      }
    ],
    "cart": [
      "12",
      "4",
      "5",
      "12"
    ],
    "favorites": [
      "18"
    ],
    "last_login": "2024-04-23",
    "address": "전라북도 안산시 상록구 서초대길 (영길김동)",
    "birth_date": "1973-04-16",
    "membership_level": "Bronze"
  },
  {
    "id": "59",
    "username": "bagsugja",
    "email": "xbag@google.com",
    "phone": "010-2735-2506",
    "name": "신서영",
    "password": "hashed_password_59",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-03-03",
        "quantity": 4
      },
      {
        "product_id": "10",
        "order_date": "2025-01-14",
        "quantity": 1
      },
      {
        "product_id": "14",
        "order_date": "2024-03-22",
        "quantity": 5
      }
    ],
    "cart": [
      "6",
      "7"
    ],
    "favorites": [
      "7",
      "4",
      "18",
      "18"
    ],
    "last_login": "2025-02-04",
    "address": "울산광역시 은평구 백제고분89가",
    "birth_date": "1967-04-08",
    "membership_level": "Bronze"
  },
  {
    "id": "60",
    "username": "wbag",
    "email": "umun@naver.com",
    "phone": "010-9197-6494",
    "name": "김광수",
    "password": "hashed_password_60",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2024-09-01",
        "quantity": 2
      },
      {
        "product_id": "1",
        "order_date": "2024-03-24",
        "quantity": 1
      }
    ],
    "cart": [
      "4",
      "13",
      "14",
      "13",
      "6"
    ],
    "favorites": [
      "9",
      "3",
      "20"
    ],
    "last_login": "2024-04-30",
    "address": "제주특별자치도 양구군 삼성250길 (예지김면)",
    "birth_date": "1951-03-01",
    "membership_level": "Silver"
  },
  {
    "id": "61",
    "username": "yeonghwan91",
    "email": "cbae@naver.com",
    "phone": "010-5583-3196",
    "name": "박미정",
    "password": "hashed_password_61",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2025-01-04",
        "quantity": 3
      },
      {
        "product_id": "13",
        "order_date": "2024-11-19",
        "quantity": 5
      }
    ],
    "cart": [
      "8",
      "5"
    ],
    "favorites": [
      "7",
      "13",
      "18",
      "8",
      "7"
    ],
    "last_login": "2024-09-16",
    "address": "대전광역시 송파구 영동대456가",
    "birth_date": "1971-10-11",
    "membership_level": "Bronze"
  },
  {
    "id": "62",
    "username": "rbag",
    "email": "boramgim@naver.com",
    "phone": "010-9187-4475",
    "name": "이정자",
    "password": "hashed_password_62",
    "orders": [],
    "cart": [
      "3",
      "5"
    ],
    "favorites": [
      "4",
      "15"
    ],
    "last_login": "2024-05-09",
    "address": "인천광역시 관악구 양재천873길 (지영고이동)",
    "birth_date": "1974-03-26",
    "membership_level": "Bronze"
  },
  {
    "id": "63",
    "username": "subin54",
    "email": "ejo@naver.com",
    "phone": "010-9126-1664",
    "name": "김성훈",
    "password": "hashed_password_63",
    "orders": [
      {
        "product_id": "2",
        "order_date": "2024-02-09",
        "quantity": 4
      },
      {
        "product_id": "7",
        "order_date": "2024-07-04",
        "quantity": 4
      },
      {
        "product_id": "2",
        "order_date": "2024-11-08",
        "quantity": 2
      },
      {
        "product_id": "6",
        "order_date": "2024-08-31",
        "quantity": 4
      }
    ],
    "cart": [
      "5",
      "6",
      "19",
      "11",
      "4"
    ],
    "favorites": [
      "6",
      "10",
      "2"
    ],
    "last_login": "2024-07-07",
    "address": "부산광역시 중구 양재천가",
    "birth_date": "1986-11-22",
    "membership_level": "Silver"
  },
  {
    "id": "64",
    "username": "eungyeong35",
    "email": "gweonyeongmi@daum.com",
    "phone": "010-6801-8594",
    "name": "오건우",
    "password": "hashed_password_64",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-06-13",
        "quantity": 1
      },
      {
        "product_id": "18",
        "order_date": "2024-06-16",
        "quantity": 3
      }
    ],
    "cart": [
      "6",
      "16",
      "5",
      "5",
      "1"
    ],
    "favorites": [
      "12",
      "9"
    ],
    "last_login": "2025-01-30",
    "address": "전라북도 괴산군 테헤란로",
    "birth_date": "1945-08-20",
    "membership_level": "Bronze"
  },
  {
    "id": "65",
    "username": "hyeonjun66",
    "email": "jeongnamcoe@daum.com",
    "phone": "010-6384-8386",
    "name": "허미숙",
    "password": "hashed_password_65",
    "orders": [
      {
        "product_id": "11",
        "order_date": "2024-03-30",
        "quantity": 2
      }
    ],
    "cart": [
      "16",
      "15",
      "14"
    ],
    "favorites": [],
    "last_login": "2024-12-13",
    "address": "전라남도 용인시 석촌호수길",
    "birth_date": "1967-10-22",
    "membership_level": "Bronze"
  },
  {
    "id": "66",
    "username": "iyeongsig",
    "email": "junyeongmun@google.com",
    "phone": "010-3761-4849",
    "name": "이정훈",
    "password": "hashed_password_66",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-05-13",
        "quantity": 2
      },
      {
        "product_id": "4",
        "order_date": "2024-11-20",
        "quantity": 2
      },
      {
        "product_id": "10",
        "order_date": "2024-12-28",
        "quantity": 4
      },
      {
        "product_id": "17",
        "order_date": "2024-08-16",
        "quantity": 1
      }
    ],
    "cart": [
      "20",
      "10"
    ],
    "favorites": [
      "20"
    ],
    "last_login": "2025-01-29",
    "address": "부산광역시 관악구 개포로 (옥자한마을)",
    "birth_date": "1991-10-18",
    "membership_level": "Silver"
  },
  {
    "id": "67",
    "username": "mgim",
    "email": "gimdoyun@google.com",
    "phone": "010-7686-2249",
    "name": "황상호",
    "password": "hashed_password_67",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2025-01-28",
        "quantity": 5
      },
      {
        "product_id": "4",
        "order_date": "2024-08-24",
        "quantity": 2
      },
      {
        "product_id": "7",
        "order_date": "2024-07-01",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-05-17",
        "quantity": 2
      },
      {
        "product_id": "7",
        "order_date": "2024-11-25",
        "quantity": 3
      }
    ],
    "cart": [
      "6",
      "1",
      "13",
      "4"
    ],
    "favorites": [
      "11",
      "8",
      "18",
      "18",
      "11"
    ],
    "last_login": "2024-02-23",
    "address": "대전광역시 남구 석촌호수260로",
    "birth_date": "1958-05-15",
    "membership_level": "Bronze"
  },
  {
    "id": "68",
    "username": "yeongjin44",
    "email": "seonghun94@daum.com",
    "phone": "010-6136-8476",
    "name": "김미숙",
    "password": "hashed_password_68",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-08-19",
        "quantity": 3
      },
      {
        "product_id": "10",
        "order_date": "2024-10-29",
        "quantity": 4
      },
      {
        "product_id": "14",
        "order_date": "2024-05-09",
        "quantity": 2
      }
    ],
    "cart": [
      "4"
    ],
    "favorites": [
      "18"
    ],
    "last_login": "2024-06-15",
    "address": "경상남도 괴산군 영동대856가 (유진이이동)",
    "birth_date": "1952-05-06",
    "membership_level": "Bronze"
  },
  {
    "id": "69",
    "username": "siu01",
    "email": "gangyeongsun@google.com",
    "phone": "010-8745-1867",
    "name": "이성호",
    "password": "hashed_password_69",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-03-09",
        "quantity": 1
      },
      {
        "product_id": "20",
        "order_date": "2024-12-11",
        "quantity": 5
      },
      {
        "product_id": "12",
        "order_date": "2024-11-08",
        "quantity": 3
      }
    ],
    "cart": [
      "11",
      "7"
    ],
    "favorites": [],
    "last_login": "2024-10-11",
    "address": "강원도 부천시 오정구 영동대가 (정희서김마을)",
    "birth_date": "1976-06-16",
    "membership_level": "Gold"
  },
  {
    "id": "70",
    "username": "junyeongyun",
    "email": "seonghoseo@google.com",
    "phone": "010-2898-6674",
    "name": "김준영",
    "password": "hashed_password_70",
    "orders": [
      {
        "product_id": "13",
        "order_date": "2025-01-18",
        "quantity": 1
      },
      {
        "product_id": "13",
        "order_date": "2024-12-05",
        "quantity": 5
      },
      {
        "product_id": "5",
        "order_date": "2025-01-07",
        "quantity": 5
      },
      {
        "product_id": "9",
        "order_date": "2024-02-29",
        "quantity": 5
      },
      {
        "product_id": "7",
        "order_date": "2024-04-22",
        "quantity": 4
      }
    ],
    "cart": [
      "10",
      "13"
    ],
    "favorites": [
      "18",
      "10"
    ],
    "last_login": "2024-12-09",
    "address": "세종특별자치시 종로구 테헤란6거리",
    "birth_date": "1999-08-06",
    "membership_level": "Silver"
  },
  {
    "id": "71",
    "username": "eomeunji",
    "email": "lhwang@daum.com",
    "phone": "010-8588-3178",
    "name": "송도윤",
    "password": "hashed_password_71",
    "orders": [
      {
        "product_id": "3",
        "order_date": "2024-10-31",
        "quantity": 4
      }
    ],
    "cart": [
      "13",
      "19"
    ],
    "favorites": [
      "2",
      "10",
      "11"
    ],
    "last_login": "2024-10-06",
    "address": "대구광역시 영등포구 백제고분900길 (건우김오읍)",
    "birth_date": "1969-02-22",
    "membership_level": "Bronze"
  },
  {
    "id": "72",
    "username": "ijihu",
    "email": "igim@google.com",
    "phone": "010-7221-1700",
    "name": "서영식",
    "password": "hashed_password_72",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-06-19",
        "quantity": 1
      },
      {
        "product_id": "7",
        "order_date": "2025-01-22",
        "quantity": 2
      },
      {
        "product_id": "9",
        "order_date": "2024-12-01",
        "quantity": 1
      },
      {
        "product_id": "17",
        "order_date": "2024-08-19",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2025-01-09",
        "quantity": 4
      }
    ],
    "cart": [
      "20",
      "5",
      "7"
    ],
    "favorites": [
      "15",
      "4",
      "16",
      "2",
      "11"
    ],
    "last_login": "2024-04-15",
    "address": "경상북도 양양군 압구정가",
    "birth_date": "1955-06-02",
    "membership_level": "Silver"
  },
  {
    "id": "73",
    "username": "namisug",
    "email": "yejicoe@daum.com",
    "phone": "010-5476-5900",
    "name": "김현숙",
    "password": "hashed_password_73",
    "orders": [
      {
        "product_id": "11",
        "order_date": "2024-11-19",
        "quantity": 4
      }
    ],
    "cart": [
      "9"
    ],
    "favorites": [
      "19"
    ],
    "last_login": "2024-08-10",
    "address": "울산광역시 강북구 도산대길 (중수권읍)",
    "birth_date": "1959-05-16",
    "membership_level": "Silver"
  },
  {
    "id": "74",
    "username": "mbag",
    "email": "boram91@daum.com",
    "phone": "010-8634-9508",
    "name": "홍서준",
    "password": "hashed_password_74",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-12-07",
        "quantity": 4
      },
      {
        "product_id": "10",
        "order_date": "2024-08-31",
        "quantity": 5
      },
      {
        "product_id": "17",
        "order_date": "2024-07-30",
        "quantity": 4
      },
      {
        "product_id": "14",
        "order_date": "2024-04-18",
        "quantity": 3
      }
    ],
    "cart": [
      "9",
      "3",
      "6",
      "3"
    ],
    "favorites": [],
    "last_login": "2024-06-30",
    "address": "경상남도 예산군 도산대로",
    "birth_date": "1990-11-27",
    "membership_level": "Platinum"
  },
  {
    "id": "75",
    "username": "fgim",
    "email": "yeongil31@naver.com",
    "phone": "010-8337-9140",
    "name": "안지영",
    "password": "hashed_password_75",
    "orders": [],
    "cart": [
      "12"
    ],
    "favorites": [
      "19",
      "20"
    ],
    "last_login": "2024-04-28",
    "address": "서울특별시 강서구 잠실길",
    "birth_date": "1979-09-28",
    "membership_level": "Silver"
  },
  {
    "id": "76",
    "username": "jiweongim",
    "email": "hseo@google.com",
    "phone": "010-6546-1819",
    "name": "김정호",
    "password": "hashed_password_76",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-06-03",
        "quantity": 1
      },
      {
        "product_id": "6",
        "order_date": "2024-11-05",
        "quantity": 2
      },
      {
        "product_id": "16",
        "order_date": "2024-03-23",
        "quantity": 4
      },
      {
        "product_id": "3",
        "order_date": "2024-08-03",
        "quantity": 4
      },
      {
        "product_id": "17",
        "order_date": "2024-12-17",
        "quantity": 2
      }
    ],
    "cart": [],
    "favorites": [
      "7",
      "6",
      "17",
      "14",
      "17"
    ],
    "last_login": "2024-09-24",
    "address": "전라남도 부천시 소사구 언주로 (순자이남마을)",
    "birth_date": "1975-06-03",
    "membership_level": "Platinum"
  },
  {
    "id": "77",
    "username": "vi",
    "email": "zi@naver.com",
    "phone": "010-3996-4060",
    "name": "김정남",
    "password": "hashed_password_77",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-04-12",
        "quantity": 2
      },
      {
        "product_id": "11",
        "order_date": "2025-01-20",
        "quantity": 2
      }
    ],
    "cart": [
      "17",
      "6",
      "6"
    ],
    "favorites": [
      "3",
      "7"
    ],
    "last_login": "2024-10-27",
    "address": "전라남도 가평군 개포길 (성수김리)",
    "birth_date": "1966-12-14",
    "membership_level": "Gold"
  },
  {
    "id": "78",
    "username": "pyun",
    "email": "yeonggil40@daum.com",
    "phone": "010-5360-8377",
    "name": "이준서",
    "password": "hashed_password_78",
    "orders": [],
    "cart": [
      "11",
      "6",
      "5"
    ],
    "favorites": [
      "11",
      "19"
    ],
    "last_login": "2024-06-20",
    "address": "강원도 성남시 중원구 잠실가",
    "birth_date": "1987-12-21",
    "membership_level": "Gold"
  },
  {
    "id": "79",
    "username": "fbag",
    "email": "fi@google.com",
    "phone": "010-1985-4063",
    "name": "김상현",
    "password": "hashed_password_79",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-06-02",
        "quantity": 1
      }
    ],
    "cart": [
      "11",
      "9",
      "17",
      "6",
      "18"
    ],
    "favorites": [],
    "last_login": "2024-10-07",
    "address": "부산광역시 마포구 압구정가",
    "birth_date": "2003-07-30",
    "membership_level": "Gold"
  },
  {
    "id": "80",
    "username": "ksong",
    "email": "migyeong84@naver.com",
    "phone": "010-2068-8602",
    "name": "이현우",
    "password": "hashed_password_80",
    "orders": [],
    "cart": [
      "1",
      "20",
      "16",
      "20",
      "19"
    ],
    "favorites": [
      "20"
    ],
    "last_login": "2024-12-13",
    "address": "광주광역시 성북구 잠실64길 (동현이김읍)",
    "birth_date": "1996-05-30",
    "membership_level": "Bronze"
  },
  {
    "id": "81",
    "username": "jeonghyi39",
    "email": "kha@google.com",
    "phone": "010-9918-8569",
    "name": "김영순",
    "password": "hashed_password_81",
    "orders": [],
    "cart": [
      "1",
      "13",
      "5",
      "4"
    ],
    "favorites": [
      "4",
      "10",
      "15"
    ],
    "last_login": "2024-12-03",
    "address": "경상남도 양평군 오금26길",
    "birth_date": "1987-08-07",
    "membership_level": "Bronze"
  },
  {
    "id": "82",
    "username": "eyun",
    "email": "coejungsu@google.com",
    "phone": "010-7039-6630",
    "name": "윤준호",
    "password": "hashed_password_82",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-06-06",
        "quantity": 3
      },
      {
        "product_id": "7",
        "order_date": "2024-08-26",
        "quantity": 4
      },
      {
        "product_id": "4",
        "order_date": "2024-06-16",
        "quantity": 2
      },
      {
        "product_id": "15",
        "order_date": "2024-12-27",
        "quantity": 2
      },
      {
        "product_id": "4",
        "order_date": "2024-02-06",
        "quantity": 3
      }
    ],
    "cart": [
      "5",
      "9"
    ],
    "favorites": [
      "2",
      "10"
    ],
    "last_login": "2024-11-29",
    "address": "울산광역시 도봉구 봉은사67거리",
    "birth_date": "1955-10-25",
    "membership_level": "Platinum"
  },
  {
    "id": "83",
    "username": "haeun44",
    "email": "bagyejin@google.com",
    "phone": "010-3135-6186",
    "name": "이상현",
    "password": "hashed_password_83",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2024-07-16",
        "quantity": 2
      }
    ],
    "cart": [
      "11",
      "17",
      "19",
      "14"
    ],
    "favorites": [],
    "last_login": "2024-09-23",
    "address": "광주광역시 도봉구 잠실47길",
    "birth_date": "2006-08-17",
    "membership_level": "Gold"
  },
  {
    "id": "84",
    "username": "cunjagang",
    "email": "ti@daum.com",
    "phone": "010-2003-6447",
    "name": "김영식",
    "password": "hashed_password_84",
    "orders": [],
    "cart": [
      "15",
      "5",
      "8",
      "16",
      "12"
    ],
    "favorites": [
      "7",
      "5",
      "18"
    ],
    "last_login": "2024-05-30",
    "address": "전라남도 고양시 개포35길 (승민장마을)",
    "birth_date": "1957-12-27",
    "membership_level": "Gold"
  },
  {
    "id": "85",
    "username": "yeonghwan02",
    "email": "eungyeongjeon@naver.com",
    "phone": "010-6683-6546",
    "name": "박영순",
    "password": "hashed_password_85",
    "orders": [],
    "cart": [
      "16",
      "2",
      "3",
      "3",
      "15"
    ],
    "favorites": [],
    "last_login": "2024-04-15",
    "address": "서울특별시 중랑구 삼성가",
    "birth_date": "1970-07-22",
    "membership_level": "Platinum"
  },
  {
    "id": "86",
    "username": "hyejinseong",
    "email": "sonogsun@daum.com",
    "phone": "010-8242-6618",
    "name": "박미숙",
    "password": "hashed_password_86",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-10-15",
        "quantity": 4
      },
      {
        "product_id": "20",
        "order_date": "2024-07-19",
        "quantity": 1
      },
      {
        "product_id": "16",
        "order_date": "2024-11-27",
        "quantity": 5
      }
    ],
    "cart": [
      "18",
      "19",
      "17",
      "17"
    ],
    "favorites": [
      "16",
      "12"
    ],
    "last_login": "2024-11-03",
    "address": "울산광역시 금천구 개포062가",
    "birth_date": "1967-04-20",
    "membership_level": "Bronze"
  },
  {
    "id": "87",
    "username": "jungsu22",
    "email": "yeweon15@daum.com",
    "phone": "010-7776-8523",
    "name": "손수빈",
    "password": "hashed_password_87",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2024-07-01",
        "quantity": 2
      },
      {
        "product_id": "17",
        "order_date": "2024-03-28",
        "quantity": 1
      },
      {
        "product_id": "13",
        "order_date": "2024-12-09",
        "quantity": 3
      },
      {
        "product_id": "20",
        "order_date": "2024-03-08",
        "quantity": 2
      },
      {
        "product_id": "4",
        "order_date": "2024-05-04",
        "quantity": 3
      }
    ],
    "cart": [
      "10",
      "12",
      "6",
      "16",
      "11"
    ],
    "favorites": [
      "8",
      "11",
      "16",
      "4",
      "8"
    ],
    "last_login": "2024-10-29",
    "address": "전라북도 포천시 선릉549거리 (채원권읍)",
    "birth_date": "1978-10-23",
    "membership_level": "Gold"
  },
  {
    "id": "88",
    "username": "myeongja41",
    "email": "dgim@naver.com",
    "phone": "010-1894-2142",
    "name": "이영숙",
    "password": "hashed_password_88",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2025-02-04",
        "quantity": 4
      },
      {
        "product_id": "8",
        "order_date": "2024-06-03",
        "quantity": 1
      },
      {
        "product_id": "2",
        "order_date": "2024-03-15",
        "quantity": 1
      }
    ],
    "cart": [
      "16",
      "10",
      "8",
      "8"
    ],
    "favorites": [
      "20",
      "17",
      "11",
      "19"
    ],
    "last_login": "2024-09-17",
    "address": "광주광역시 강동구 영동대로 (상현우황면)",
    "birth_date": "1971-10-30",
    "membership_level": "Bronze"
  },
  {
    "id": "89",
    "username": "songminseog",
    "email": "jeongsug31@naver.com",
    "phone": "010-6606-6937",
    "name": "심서영",
    "password": "hashed_password_89",
    "orders": [
      {
        "product_id": "2",
        "order_date": "2024-10-24",
        "quantity": 1
      },
      {
        "product_id": "12",
        "order_date": "2024-03-04",
        "quantity": 1
      },
      {
        "product_id": "6",
        "order_date": "2024-03-03",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2025-01-18",
        "quantity": 3
      }
    ],
    "cart": [
      "12",
      "5",
      "14"
    ],
    "favorites": [
      "18",
      "12",
      "18"
    ],
    "last_login": "2024-08-31",
    "address": "경상북도 시흥시 잠실가",
    "birth_date": "1945-09-04",
    "membership_level": "Bronze"
  },
  {
    "id": "90",
    "username": "seonghyeon37",
    "email": "useo@naver.com",
    "phone": "010-6739-9944",
    "name": "박서현",
    "password": "hashed_password_90",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2024-03-05",
        "quantity": 2
      }
    ],
    "cart": [
      "19"
    ],
    "favorites": [
      "20",
      "1",
      "2"
    ],
    "last_login": "2024-05-02",
    "address": "부산광역시 북구 잠실658로 (미영김김마을)",
    "birth_date": "1970-06-29",
    "membership_level": "Gold"
  },
  {
    "id": "91",
    "username": "coejihun",
    "email": "yeongjin10@daum.com",
    "phone": "010-8832-5103",
    "name": "홍서연",
    "password": "hashed_password_91",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-12-03",
        "quantity": 3
      },
      {
        "product_id": "19",
        "order_date": "2024-02-17",
        "quantity": 1
      },
      {
        "product_id": "18",
        "order_date": "2024-09-28",
        "quantity": 3
      },
      {
        "product_id": "10",
        "order_date": "2024-06-02",
        "quantity": 3
      },
      {
        "product_id": "10",
        "order_date": "2024-10-01",
        "quantity": 2
      }
    ],
    "cart": [
      "4"
    ],
    "favorites": [],
    "last_login": "2024-06-27",
    "address": "충청북도 군포시 압구정로 (정자권우마을)",
    "birth_date": "1976-03-03",
    "membership_level": "Gold"
  },
  {
    "id": "92",
    "username": "sumingim",
    "email": "jiyeong73@daum.com",
    "phone": "010-4708-1363",
    "name": "이민준",
    "password": "hashed_password_92",
    "orders": [
      {
        "product_id": "13",
        "order_date": "2024-10-29",
        "quantity": 2
      }
    ],
    "cart": [
      "6",
      "12"
    ],
    "favorites": [
      "13"
    ],
    "last_login": "2024-09-28",
    "address": "충청남도 구리시 논현가 (민준이리)",
    "birth_date": "1952-04-02",
    "membership_level": "Silver"
  },
  {
    "id": "93",
    "username": "jihyeon42",
    "email": "gimjeongsu@daum.com",
    "phone": "010-1080-1369",
    "name": "오미정",
    "password": "hashed_password_93",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-03-20",
        "quantity": 3
      },
      {
        "product_id": "19",
        "order_date": "2024-08-15",
        "quantity": 3
      },
      {
        "product_id": "5",
        "order_date": "2025-01-07",
        "quantity": 5
      },
      {
        "product_id": "18",
        "order_date": "2024-06-18",
        "quantity": 1
      },
      {
        "product_id": "14",
        "order_date": "2024-10-28",
        "quantity": 1
      }
    ],
    "cart": [
      "19",
      "15"
    ],
    "favorites": [
      "7",
      "9",
      "3"
    ],
    "last_login": "2024-06-21",
    "address": "광주광역시 중구 백제고분로 (민석김동)",
    "birth_date": "1968-09-29",
    "membership_level": "Bronze"
  },
  {
    "id": "94",
    "username": "jeongsugi",
    "email": "jia05@google.com",
    "phone": "010-2660-7346",
    "name": "안정수",
    "password": "hashed_password_94",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2024-11-29",
        "quantity": 5
      },
      {
        "product_id": "15",
        "order_date": "2024-09-08",
        "quantity": 5
      },
      {
        "product_id": "7",
        "order_date": "2024-03-12",
        "quantity": 5
      }
    ],
    "cart": [
      "8",
      "9",
      "7"
    ],
    "favorites": [
      "14",
      "8",
      "9",
      "3"
    ],
    "last_login": "2024-08-12",
    "address": "전라남도 청주시 상당구 석촌호수5가 (준호서김마을)",
    "birth_date": "1963-02-21",
    "membership_level": "Silver"
  },
  {
    "id": "95",
    "username": "hayun61",
    "email": "hongbyeongceol@daum.com",
    "phone": "010-9719-5354",
    "name": "신민재",
    "password": "hashed_password_95",
    "orders": [],
    "cart": [
      "16",
      "4",
      "13",
      "2",
      "16"
    ],
    "favorites": [
      "5",
      "15",
      "9",
      "12",
      "4"
    ],
    "last_login": "2024-10-02",
    "address": "울산광역시 서초구 영동대001가",
    "birth_date": "1970-06-17",
    "membership_level": "Bronze"
  },
  {
    "id": "96",
    "username": "jbae",
    "email": "tan@naver.com",
    "phone": "010-7289-7891",
    "name": "김유진",
    "password": "hashed_password_96",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-06-10",
        "quantity": 5
      },
      {
        "product_id": "9",
        "order_date": "2024-05-05",
        "quantity": 5
      }
    ],
    "cart": [
      "10",
      "8",
      "19",
      "5",
      "15"
    ],
    "favorites": [
      "7",
      "6",
      "19"
    ],
    "last_login": "2024-08-12",
    "address": "광주광역시 북구 양재천75가",
    "birth_date": "1958-02-19",
    "membership_level": "Silver"
  },
  {
    "id": "97",
    "username": "bagjinho",
    "email": "coehayun@naver.com",
    "phone": "010-9416-3683",
    "name": "성영숙",
    "password": "hashed_password_97",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-10-13",
        "quantity": 3
      },
      {
        "product_id": "8",
        "order_date": "2024-10-18",
        "quantity": 4
      }
    ],
    "cart": [
      "8",
      "5",
      "20",
      "9"
    ],
    "favorites": [
      "11",
      "2",
      "12",
      "18",
      "16"
    ],
    "last_login": "2024-02-05",
    "address": "광주광역시 북구 역삼거리 (정자이리)",
    "birth_date": "1978-07-14",
    "membership_level": "Silver"
  },
  {
    "id": "98",
    "username": "gryu",
    "email": "doyunhwang@naver.com",
    "phone": "010-5470-6757",
    "name": "서하은",
    "password": "hashed_password_98",
    "orders": [
      {
        "product_id": "17",
        "order_date": "2024-11-01",
        "quantity": 5
      },
      {
        "product_id": "9",
        "order_date": "2024-02-11",
        "quantity": 4
      },
      {
        "product_id": "2",
        "order_date": "2024-04-27",
        "quantity": 2
      },
      {
        "product_id": "13",
        "order_date": "2024-05-19",
        "quantity": 4
      },
      {
        "product_id": "4",
        "order_date": "2024-06-19",
        "quantity": 4
      }
    ],
    "cart": [
      "10",
      "14",
      "12"
    ],
    "favorites": [],
    "last_login": "2024-02-17",
    "address": "전라남도 화천군 압구정9로",
    "birth_date": "1977-11-05",
    "membership_level": "Silver"
  },
  {
    "id": "99",
    "username": "gimjaehyeon",
    "email": "zmin@google.com",
    "phone": "010-6581-7497",
    "name": "배경수",
    "password": "hashed_password_99",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2025-01-25",
        "quantity": 3
      },
      {
        "product_id": "4",
        "order_date": "2024-10-05",
        "quantity": 5
      }
    ],
    "cart": [
      "19",
      "13",
      "20",
      "15",
      "5"
    ],
    "favorites": [
      "15",
      "7",
      "10",
      "13"
    ],
    "last_login": "2024-07-21",
    "address": "경상북도 연천군 가락251가 (영철이최마을)",
    "birth_date": "1994-12-30",
    "membership_level": "Bronze"
  },
  {
    "id": "100",
    "username": "junhyeogi",
    "email": "subinbag@naver.com",
    "phone": "010-3852-1063",
    "name": "이준호",
    "password": "hashed_password_100",
    "orders": [],
    "cart": [
      "13"
    ],
    "favorites": [],
    "last_login": "2025-01-07",
    "address": "경상남도 괴산군 역삼길",
    "birth_date": "1979-02-27",
    "membership_level": "Platinum"
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

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
    "id": "4",
    "username": "jcurtis",
    "email": "hmoyer@gmail.com",
    "phone": "(402)583-7650x2073",
    "name": "이명숙",
    "password": "hashed_password_4",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-09-04",
        "quantity": 5
      },
      {
        "product_id": "13",
        "order_date": "2024-10-07",
        "quantity": 1
      },
      {
        "product_id": "1",
        "order_date": "2024-06-21",
        "quantity": 4
      },
      {
        "product_id": "14",
        "order_date": "2024-09-24",
        "quantity": 5
      }
    ],
    "cart": [
      "4",
      "14",
      "7",
      "19",
      "9"
    ],
    "favorites": [
      "10",
      "20",
      "11"
    ],
    "last_login": "2024-03-15",
    "address": "028 Bradley Land\nSouth Daniel, MI 34108",
    "birth_date": "1948-05-05",
    "membership_level": "Gold"
  },
  {
    "id": "5",
    "username": "hollycox",
    "email": "laura65@tucker.com",
    "phone": "103-187-8269",
    "name": "문민준",
    "password": "hashed_password_5",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-12-13",
        "quantity": 3
      },
      {
        "product_id": "20",
        "order_date": "2024-08-27",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-05-11",
        "quantity": 2
      },
      {
        "product_id": "3",
        "order_date": "2024-10-17",
        "quantity": 5
      }
    ],
    "cart": [
      "16",
      "10",
      "15",
      "15"
    ],
    "favorites": [
      "2",
      "3"
    ],
    "last_login": "2024-08-28",
    "address": "24762 John Shore\nJamesbury, NH 78884",
    "birth_date": "1968-01-23",
    "membership_level": "Silver"
  },
  {
    "id": "6",
    "username": "kwilliams",
    "email": "staceystrickland@jones.com",
    "phone": "436-449-3792",
    "name": "전주원",
    "password": "hashed_password_6",
    "orders": [],
    "cart": [
      "13",
      "17",
      "20",
      "16",
      "2"
    ],
    "favorites": [],
    "last_login": "2024-04-14",
    "address": "Unit 6932 Box 0762\nDPO AE 68939",
    "birth_date": "2002-12-13",
    "membership_level": "Gold"
  },
  {
    "id": "7",
    "username": "sevans",
    "email": "belindadavis@knight-small.com",
    "phone": "7019034999",
    "name": "류종수",
    "password": "hashed_password_7",
    "orders": [],
    "cart": [
      "16"
    ],
    "favorites": [
      "16",
      "20",
      "1",
      "20",
      "20"
    ],
    "last_login": "2024-10-04",
    "address": "7741 Fernandez Cove Suite 398\nJenniferview, RI 20955",
    "birth_date": "1973-06-30",
    "membership_level": "Bronze"
  },
  {
    "id": "8",
    "username": "jeremy93",
    "email": "tluna@hotmail.com",
    "phone": "533.791.4811x10289",
    "name": "오경수",
    "password": "hashed_password_8",
    "orders": [],
    "cart": [
      "8",
      "14",
      "14"
    ],
    "favorites": [
      "5",
      "7"
    ],
    "last_login": "2025-02-02",
    "address": "20792 Rojas Locks\nDannyview, MT 70977",
    "birth_date": "1972-11-01",
    "membership_level": "Gold"
  },
  {
    "id": "9",
    "username": "carolyn90",
    "email": "willismatthew@gmail.com",
    "phone": "6886300535",
    "name": "윤중수",
    "password": "hashed_password_9",
    "orders": [
      {
        "product_id": "20",
        "order_date": "2024-05-08",
        "quantity": 2
      },
      {
        "product_id": "10",
        "order_date": "2024-09-16",
        "quantity": 3
      }
    ],
    "cart": [],
    "favorites": [
      "19",
      "1"
    ],
    "last_login": "2024-03-24",
    "address": "0147 Bonnie Summit\nMarkmouth, PA 61291",
    "birth_date": "1962-03-23",
    "membership_level": "Platinum"
  },
  {
    "id": "10",
    "username": "isaacknight",
    "email": "david38@chang.com",
    "phone": "(317)031-5787x158",
    "name": "송성수",
    "password": "hashed_password_10",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-08-06",
        "quantity": 5
      }
    ],
    "cart": [
      "8",
      "15",
      "12",
      "8"
    ],
    "favorites": [
      "17",
      "18",
      "8",
      "7",
      "5"
    ],
    "last_login": "2025-01-17",
    "address": "Unit 9203 Box 4050\nDPO AE 22990",
    "birth_date": "1976-12-23",
    "membership_level": "Platinum"
  },
  {
    "id": "11",
    "username": "bclark",
    "email": "gsantiago@hotmail.com",
    "phone": "153-687-7313x3347",
    "name": "김영철",
    "password": "hashed_password_11",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-03-24",
        "quantity": 5
      },
      {
        "product_id": "6",
        "order_date": "2024-09-17",
        "quantity": 1
      },
      {
        "product_id": "8",
        "order_date": "2024-12-01",
        "quantity": 5
      }
    ],
    "cart": [
      "9",
      "7"
    ],
    "favorites": [
      "5",
      "1",
      "3"
    ],
    "last_login": "2024-04-12",
    "address": "500 Jeremy Parkways Apt. 451\nNew Pamelafurt, MS 36864",
    "birth_date": "1961-02-04",
    "membership_level": "Gold"
  },
  {
    "id": "12",
    "username": "savannah73",
    "email": "thobbs@hotmail.com",
    "phone": "(032)348-9979x74860",
    "name": "김정식",
    "password": "hashed_password_12",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-08-17",
        "quantity": 4
      }
    ],
    "cart": [
      "14",
      "17",
      "19",
      "10"
    ],
    "favorites": [],
    "last_login": "2024-10-04",
    "address": "9190 Carrie Mall\nCastanedatown, DC 43663",
    "birth_date": "1985-03-17",
    "membership_level": "Platinum"
  },
  {
    "id": "13",
    "username": "joanngraves",
    "email": "wilkinsronald@pineda.info",
    "phone": "001-652-525-1979x52556",
    "name": "이성진",
    "password": "hashed_password_13",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2025-01-12",
        "quantity": 4
      }
    ],
    "cart": [
      "12"
    ],
    "favorites": [
      "6",
      "9"
    ],
    "last_login": "2024-03-07",
    "address": "0902 Latasha Highway Suite 796\nHallside, CO 62022",
    "birth_date": "1999-01-01",
    "membership_level": "Silver"
  },
  {
    "id": "14",
    "username": "kellymary",
    "email": "hmorrison@davis.biz",
    "phone": "001-564-689-4772x6094",
    "name": "홍시우",
    "password": "hashed_password_14",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-04-30",
        "quantity": 5
      },
      {
        "product_id": "4",
        "order_date": "2024-07-18",
        "quantity": 5
      },
      {
        "product_id": "19",
        "order_date": "2024-12-27",
        "quantity": 5
      },
      {
        "product_id": "5",
        "order_date": "2024-09-18",
        "quantity": 4
      },
      {
        "product_id": "13",
        "order_date": "2025-01-23",
        "quantity": 3
      }
    ],
    "cart": [
      "9",
      "20"
    ],
    "favorites": [
      "11",
      "20",
      "3",
      "19"
    ],
    "last_login": "2024-12-25",
    "address": "713 Thompson Mall\nNorth David, TX 28487",
    "birth_date": "1970-09-30",
    "membership_level": "Silver"
  },
  {
    "id": "15",
    "username": "veronicaclark",
    "email": "lori37@wagner.com",
    "phone": "0435112757",
    "name": "김미경",
    "password": "hashed_password_15",
    "orders": [
      {
        "product_id": "2",
        "order_date": "2024-04-02",
        "quantity": 4
      },
      {
        "product_id": "1",
        "order_date": "2024-04-23",
        "quantity": 1
      },
      {
        "product_id": "5",
        "order_date": "2024-03-25",
        "quantity": 5
      },
      {
        "product_id": "8",
        "order_date": "2024-08-19",
        "quantity": 2
      }
    ],
    "cart": [
      "13",
      "2",
      "2"
    ],
    "favorites": [
      "18",
      "7"
    ],
    "last_login": "2024-05-23",
    "address": "14895 Brown Mall\nMasonport, NE 82567",
    "birth_date": "1979-03-10",
    "membership_level": "Gold"
  },
  {
    "id": "16",
    "username": "lopeztimothy",
    "email": "aliciacrosby@acosta-holloway.net",
    "phone": "703.570.0390",
    "name": "김우진",
    "password": "hashed_password_16",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2024-04-30",
        "quantity": 2
      },
      {
        "product_id": "19",
        "order_date": "2024-10-26",
        "quantity": 1
      },
      {
        "product_id": "11",
        "order_date": "2024-11-02",
        "quantity": 3
      },
      {
        "product_id": "1",
        "order_date": "2025-01-15",
        "quantity": 1
      },
      {
        "product_id": "3",
        "order_date": "2024-05-22",
        "quantity": 5
      }
    ],
    "cart": [
      "5",
      "6",
      "4"
    ],
    "favorites": [
      "13"
    ],
    "last_login": "2024-06-30",
    "address": "08189 Young Neck\nMeyershire, TX 47157",
    "birth_date": "1972-09-07",
    "membership_level": "Bronze"
  },
  {
    "id": "17",
    "username": "zgardner",
    "email": "amyharris@nixon-thomas.biz",
    "phone": "001-994-266-6530x835",
    "name": "최경숙",
    "password": "hashed_password_17",
    "orders": [
      {
        "product_id": "16",
        "order_date": "2024-07-14",
        "quantity": 1
      },
      {
        "product_id": "3",
        "order_date": "2025-01-30",
        "quantity": 3
      },
      {
        "product_id": "4",
        "order_date": "2024-11-02",
        "quantity": 1
      },
      {
        "product_id": "15",
        "order_date": "2024-10-01",
        "quantity": 1
      },
      {
        "product_id": "14",
        "order_date": "2024-07-02",
        "quantity": 5
      }
    ],
    "cart": [
      "4",
      "5",
      "20",
      "2"
    ],
    "favorites": [
      "16"
    ],
    "last_login": "2024-02-12",
    "address": "743 Samuel Skyway\nHarveyport, MN 09485",
    "birth_date": "1963-05-13",
    "membership_level": "Gold"
  },
  {
    "id": "18",
    "username": "boydlawrence",
    "email": "heathermartin@gmail.com",
    "phone": "001-008-173-0145x465",
    "name": "이중수",
    "password": "hashed_password_18",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-02-18",
        "quantity": 4
      },
      {
        "product_id": "15",
        "order_date": "2024-11-30",
        "quantity": 4
      },
      {
        "product_id": "19",
        "order_date": "2024-09-10",
        "quantity": 4
      },
      {
        "product_id": "17",
        "order_date": "2024-11-26",
        "quantity": 5
      }
    ],
    "cart": [
      "4"
    ],
    "favorites": [
      "18",
      "7",
      "1",
      "5",
      "8"
    ],
    "last_login": "2024-12-15",
    "address": "6645 Timothy View\nNorth Sara, TN 11636",
    "birth_date": "1987-11-04",
    "membership_level": "Silver"
  },
  {
    "id": "19",
    "username": "audrey13",
    "email": "cathy20@yahoo.com",
    "phone": "001-501-778-7970",
    "name": "심상훈",
    "password": "hashed_password_19",
    "orders": [],
    "cart": [
      "17"
    ],
    "favorites": [
      "4"
    ],
    "last_login": "2024-08-22",
    "address": "15865 Brian Junction\nNorth Matthewshire, CT 82313",
    "birth_date": "1981-04-03",
    "membership_level": "Platinum"
  },
  {
    "id": "20",
    "username": "jamesdeborah",
    "email": "murphydana@gmail.com",
    "phone": "824.484.9150x4285",
    "name": "송준영",
    "password": "hashed_password_20",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2025-01-22",
        "quantity": 1
      },
      {
        "product_id": "18",
        "order_date": "2024-11-07",
        "quantity": 2
      }
    ],
    "cart": [
      "8",
      "15",
      "11"
    ],
    "favorites": [
      "11",
      "11",
      "17"
    ],
    "last_login": "2024-02-21",
    "address": "591 Garrett Spurs\nAarontown, KY 98703",
    "birth_date": "1950-10-19",
    "membership_level": "Silver"
  },
  {
    "id": "21",
    "username": "dchambers",
    "email": "michellebrooks@solis.com",
    "phone": "981-799-8028x9686",
    "name": "박아름",
    "password": "hashed_password_21",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-08-23",
        "quantity": 3
      },
      {
        "product_id": "16",
        "order_date": "2024-07-27",
        "quantity": 5
      },
      {
        "product_id": "5",
        "order_date": "2024-12-13",
        "quantity": 4
      },
      {
        "product_id": "12",
        "order_date": "2024-06-16",
        "quantity": 2
      }
    ],
    "cart": [],
    "favorites": [
      "13",
      "6",
      "5",
      "8"
    ],
    "last_login": "2024-10-27",
    "address": "2182 Taylor Field Suite 335\nRosefort, ID 13943",
    "birth_date": "1972-02-29",
    "membership_level": "Gold"
  },
  {
    "id": "22",
    "username": "eduardo36",
    "email": "hmartin@hotmail.com",
    "phone": "950.661.5562x54598",
    "name": "김지후",
    "password": "hashed_password_22",
    "orders": [],
    "cart": [
      "1"
    ],
    "favorites": [
      "13",
      "1"
    ],
    "last_login": "2024-02-11",
    "address": "48331 Perry Via\nWest Kimberlystad, ND 52074",
    "birth_date": "1946-03-16",
    "membership_level": "Platinum"
  },
  {
    "id": "23",
    "username": "tgarcia",
    "email": "jeremiah68@gmail.com",
    "phone": "885.012.9619",
    "name": "이정희",
    "password": "hashed_password_23",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-09-02",
        "quantity": 1
      },
      {
        "product_id": "16",
        "order_date": "2025-01-25",
        "quantity": 2
      }
    ],
    "cart": [
      "15",
      "16",
      "7",
      "13"
    ],
    "favorites": [],
    "last_login": "2024-10-13",
    "address": "PSC 4576, Box 4573\nAPO AE 66406",
    "birth_date": "1977-11-12",
    "membership_level": "Gold"
  },
  {
    "id": "24",
    "username": "xpugh",
    "email": "lisa56@sheppard.com",
    "phone": "397.412.9853x79451",
    "name": "손현지",
    "password": "hashed_password_24",
    "orders": [],
    "cart": [
      "7"
    ],
    "favorites": [
      "11",
      "6",
      "5",
      "9"
    ],
    "last_login": "2024-12-30",
    "address": "4467 Daniel Shores\nPhilipside, SC 82426",
    "birth_date": "1954-09-28",
    "membership_level": "Silver"
  },
  {
    "id": "25",
    "username": "kwilson",
    "email": "dunnterry@smith.com",
    "phone": "573-115-6426x08627",
    "name": "박진우",
    "password": "hashed_password_25",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-12-08",
        "quantity": 3
      },
      {
        "product_id": "17",
        "order_date": "2024-04-13",
        "quantity": 1
      },
      {
        "product_id": "7",
        "order_date": "2024-12-21",
        "quantity": 3
      },
      {
        "product_id": "3",
        "order_date": "2024-08-03",
        "quantity": 1
      },
      {
        "product_id": "8",
        "order_date": "2025-01-30",
        "quantity": 3
      }
    ],
    "cart": [
      "11",
      "16",
      "11",
      "16",
      "15"
    ],
    "favorites": [],
    "last_login": "2024-06-16",
    "address": "28746 Michael Road Apt. 042\nSouth Norman, WA 22574",
    "birth_date": "2002-08-11",
    "membership_level": "Silver"
  },
  {
    "id": "26",
    "username": "flemingrobert",
    "email": "willie68@yahoo.com",
    "phone": "(887)422-0140",
    "name": "박민재",
    "password": "hashed_password_26",
    "orders": [
      {
        "product_id": "20",
        "order_date": "2025-01-20",
        "quantity": 3
      },
      {
        "product_id": "5",
        "order_date": "2024-03-27",
        "quantity": 3
      },
      {
        "product_id": "18",
        "order_date": "2024-09-29",
        "quantity": 2
      },
      {
        "product_id": "10",
        "order_date": "2024-04-01",
        "quantity": 1
      },
      {
        "product_id": "18",
        "order_date": "2024-09-01",
        "quantity": 4
      }
    ],
    "cart": [
      "8",
      "2",
      "1"
    ],
    "favorites": [
      "17",
      "19",
      "4",
      "16"
    ],
    "last_login": "2024-07-06",
    "address": "84158 Gibbs Road Suite 999\nKnappstad, ND 57084",
    "birth_date": "1999-09-21",
    "membership_level": "Bronze"
  },
  {
    "id": "27",
    "username": "derekmcbride",
    "email": "wallerkelly@schmitt.com",
    "phone": "811.814.1760x0939",
    "name": "하진우",
    "password": "hashed_password_27",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-11-06",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2024-05-24",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-05-05",
        "quantity": 5
      },
      {
        "product_id": "18",
        "order_date": "2024-06-13",
        "quantity": 1
      }
    ],
    "cart": [
      "15",
      "19"
    ],
    "favorites": [
      "12"
    ],
    "last_login": "2024-11-23",
    "address": "916 Martin Meadows\nGrahamhaven, MT 29171",
    "birth_date": "1979-12-28",
    "membership_level": "Platinum"
  },
  {
    "id": "28",
    "username": "michellegonzalez",
    "email": "jessicasmith@yahoo.com",
    "phone": "593.219.4941",
    "name": "김성훈",
    "password": "hashed_password_28",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-03-21",
        "quantity": 3
      },
      {
        "product_id": "7",
        "order_date": "2024-07-18",
        "quantity": 1
      },
      {
        "product_id": "1",
        "order_date": "2024-03-30",
        "quantity": 3
      },
      {
        "product_id": "18",
        "order_date": "2024-10-02",
        "quantity": 3
      }
    ],
    "cart": [
      "20",
      "18",
      "5"
    ],
    "favorites": [
      "3",
      "10",
      "5",
      "19",
      "8"
    ],
    "last_login": "2024-08-27",
    "address": "8766 Brian Pine\nNorth Maria, WV 93156",
    "birth_date": "1945-03-02",
    "membership_level": "Platinum"
  },
  {
    "id": "29",
    "username": "john91",
    "email": "palmercollin@gmail.com",
    "phone": "+1-931-310-2862x1442",
    "name": "김은주",
    "password": "hashed_password_29",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-05-29",
        "quantity": 2
      },
      {
        "product_id": "11",
        "order_date": "2024-09-21",
        "quantity": 4
      },
      {
        "product_id": "4",
        "order_date": "2024-11-08",
        "quantity": 5
      }
    ],
    "cart": [
      "17",
      "17",
      "14",
      "15",
      "12"
    ],
    "favorites": [],
    "last_login": "2024-06-04",
    "address": "USNS Sherman\nFPO AP 64620",
    "birth_date": "2006-09-03",
    "membership_level": "Silver"
  },
  {
    "id": "30",
    "username": "zanderson",
    "email": "shoffman@gmail.com",
    "phone": "406-287-3006x34526",
    "name": "이채원",
    "password": "hashed_password_30",
    "orders": [],
    "cart": [
      "6"
    ],
    "favorites": [
      "1",
      "6",
      "17"
    ],
    "last_login": "2024-03-01",
    "address": "61760 Brian Canyon Apt. 491\nBrookeborough, WV 26368",
    "birth_date": "1981-01-28",
    "membership_level": "Gold"
  },
  {
    "id": "31",
    "username": "galvanmark",
    "email": "walkerlydia@wood.com",
    "phone": "631.422.2904x221",
    "name": "엄은서",
    "password": "hashed_password_31",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-03-04",
        "quantity": 4
      },
      {
        "product_id": "16",
        "order_date": "2024-10-17",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-12-22",
        "quantity": 1
      },
      {
        "product_id": "13",
        "order_date": "2024-08-17",
        "quantity": 5
      }
    ],
    "cart": [
      "1",
      "6",
      "13"
    ],
    "favorites": [
      "11",
      "9",
      "16",
      "18"
    ],
    "last_login": "2024-06-19",
    "address": "Unit 5430 Box 8945\nDPO AP 57660",
    "birth_date": "1968-01-20",
    "membership_level": "Silver"
  },
  {
    "id": "32",
    "username": "hbell",
    "email": "francisalexis@lawson.org",
    "phone": "+1-838-781-1151x12895",
    "name": "장영미",
    "password": "hashed_password_32",
    "orders": [],
    "cart": [
      "1",
      "6",
      "8",
      "10",
      "20"
    ],
    "favorites": [],
    "last_login": "2025-01-31",
    "address": "198 Veronica Centers Suite 471\nCarlshire, OR 84657",
    "birth_date": "1973-02-15",
    "membership_level": "Gold"
  },
  {
    "id": "33",
    "username": "ronald05",
    "email": "dwayneshields@hotmail.com",
    "phone": "(849)626-2888",
    "name": "노미경",
    "password": "hashed_password_33",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-08-23",
        "quantity": 5
      },
      {
        "product_id": "12",
        "order_date": "2024-10-15",
        "quantity": 3
      },
      {
        "product_id": "13",
        "order_date": "2024-10-11",
        "quantity": 1
      }
    ],
    "cart": [],
    "favorites": [
      "7",
      "1",
      "12"
    ],
    "last_login": "2024-03-21",
    "address": "96493 Carlson Pines\nWilsonview, NY 57207",
    "birth_date": "1969-09-30",
    "membership_level": "Platinum"
  },
  {
    "id": "34",
    "username": "staceymedina",
    "email": "abigailpowers@hotmail.com",
    "phone": "(958)618-6039",
    "name": "장은정",
    "password": "hashed_password_34",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-09-01",
        "quantity": 1
      },
      {
        "product_id": "1",
        "order_date": "2024-09-21",
        "quantity": 4
      },
      {
        "product_id": "9",
        "order_date": "2024-10-18",
        "quantity": 5
      },
      {
        "product_id": "10",
        "order_date": "2024-10-14",
        "quantity": 1
      },
      {
        "product_id": "5",
        "order_date": "2024-07-05",
        "quantity": 5
      }
    ],
    "cart": [
      "3"
    ],
    "favorites": [
      "19",
      "3",
      "6",
      "18"
    ],
    "last_login": "2024-05-26",
    "address": "8796 Jonathan Knoll\nLeahville, PA 38870",
    "birth_date": "1984-02-14",
    "membership_level": "Gold"
  },
  {
    "id": "35",
    "username": "gordonjuan",
    "email": "stephanie27@yahoo.com",
    "phone": "885.165.6401x843",
    "name": "박은경",
    "password": "hashed_password_35",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-08-08",
        "quantity": 5
      }
    ],
    "cart": [
      "19",
      "19",
      "17"
    ],
    "favorites": [
      "5"
    ],
    "last_login": "2024-05-26",
    "address": "0180 William Unions\nCherylchester, TN 18481",
    "birth_date": "1989-09-15",
    "membership_level": "Bronze"
  },
  {
    "id": "36",
    "username": "fordabigail",
    "email": "robertsjames@simpson.net",
    "phone": "387.008.1814",
    "name": "박은정",
    "password": "hashed_password_36",
    "orders": [],
    "cart": [],
    "favorites": [
      "11",
      "16"
    ],
    "last_login": "2024-04-26",
    "address": "241 James Walks Apt. 824\nSouth Jennifer, SD 98267",
    "birth_date": "1957-01-19",
    "membership_level": "Gold"
  },
  {
    "id": "37",
    "username": "paularodriguez",
    "email": "mannjacqueline@yahoo.com",
    "phone": "+1-084-949-7735x87542",
    "name": "홍지민",
    "password": "hashed_password_37",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-06-22",
        "quantity": 3
      },
      {
        "product_id": "15",
        "order_date": "2024-05-15",
        "quantity": 5
      },
      {
        "product_id": "12",
        "order_date": "2024-10-24",
        "quantity": 1
      },
      {
        "product_id": "2",
        "order_date": "2025-01-02",
        "quantity": 2
      }
    ],
    "cart": [
      "8"
    ],
    "favorites": [
      "16",
      "8"
    ],
    "last_login": "2024-08-25",
    "address": "Unit 5297 Box 0197\nDPO AP 73880",
    "birth_date": "1955-12-06",
    "membership_level": "Gold"
  },
  {
    "id": "38",
    "username": "gjones",
    "email": "michellenolan@padilla.net",
    "phone": "372-622-3107x9086",
    "name": "김윤서",
    "password": "hashed_password_38",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-03-06",
        "quantity": 5
      }
    ],
    "cart": [
      "12",
      "8"
    ],
    "favorites": [
      "13"
    ],
    "last_login": "2024-04-17",
    "address": "822 Lisa Rapid\nMelissaton, AR 18440",
    "birth_date": "1966-09-16",
    "membership_level": "Bronze"
  },
  {
    "id": "39",
    "username": "ojenkins",
    "email": "dsmith@huff.com",
    "phone": "598-176-7452",
    "name": "김진호",
    "password": "hashed_password_39",
    "orders": [],
    "cart": [
      "11",
      "13"
    ],
    "favorites": [],
    "last_login": "2024-02-18",
    "address": "4912 Rodriguez Unions Suite 676\nNorth William, AR 88634",
    "birth_date": "1964-03-13",
    "membership_level": "Bronze"
  },
  {
    "id": "40",
    "username": "hthompson",
    "email": "fullerkathleen@peterson-velez.com",
    "phone": "515-467-1126x4839",
    "name": "고옥자",
    "password": "hashed_password_40",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-04-21",
        "quantity": 1
      },
      {
        "product_id": "1",
        "order_date": "2024-11-05",
        "quantity": 3
      },
      {
        "product_id": "7",
        "order_date": "2024-03-25",
        "quantity": 2
      }
    ],
    "cart": [
      "4",
      "19"
    ],
    "favorites": [
      "8"
    ],
    "last_login": "2024-12-05",
    "address": "87760 Woods Shoal\nLake Sarah, WY 65520",
    "birth_date": "1946-07-11",
    "membership_level": "Platinum"
  },
  {
    "id": "41",
    "username": "garciaashley",
    "email": "loweryphillip@gmail.com",
    "phone": "601.138.5797x992",
    "name": "하수진",
    "password": "hashed_password_41",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2025-01-11",
        "quantity": 4
      },
      {
        "product_id": "4",
        "order_date": "2024-03-02",
        "quantity": 3
      },
      {
        "product_id": "1",
        "order_date": "2024-02-28",
        "quantity": 2
      },
      {
        "product_id": "6",
        "order_date": "2024-07-01",
        "quantity": 1
      },
      {
        "product_id": "17",
        "order_date": "2024-09-01",
        "quantity": 1
      }
    ],
    "cart": [
      "8"
    ],
    "favorites": [
      "11"
    ],
    "last_login": "2025-01-27",
    "address": "388 James Common\nOliverfort, NV 22460",
    "birth_date": "1961-04-09",
    "membership_level": "Gold"
  },
  {
    "id": "42",
    "username": "andrew46",
    "email": "richardle@yahoo.com",
    "phone": "001-607-546-5035",
    "name": "이현숙",
    "password": "hashed_password_42",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2024-08-05",
        "quantity": 2
      }
    ],
    "cart": [
      "18",
      "4",
      "3",
      "10"
    ],
    "favorites": [
      "18",
      "10",
      "17",
      "6"
    ],
    "last_login": "2024-05-27",
    "address": "5013 Anthony Ford\nPort Xavierfort, GA 38457",
    "birth_date": "2001-04-14",
    "membership_level": "Bronze"
  },
  {
    "id": "43",
    "username": "kcarlson",
    "email": "shawmaureen@watts.com",
    "phone": "219.483.4129",
    "name": "손명자",
    "password": "hashed_password_43",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-05-31",
        "quantity": 4
      },
      {
        "product_id": "20",
        "order_date": "2024-05-08",
        "quantity": 4
      },
      {
        "product_id": "1",
        "order_date": "2024-11-13",
        "quantity": 5
      }
    ],
    "cart": [
      "5",
      "6",
      "17"
    ],
    "favorites": [
      "9"
    ],
    "last_login": "2024-08-06",
    "address": "0031 Arthur Roads\nMaldonadohaven, ID 35264",
    "birth_date": "1970-11-23",
    "membership_level": "Gold"
  },
  {
    "id": "44",
    "username": "wilsontaylor",
    "email": "landrycandace@davis.com",
    "phone": "4755339410",
    "name": "박지현",
    "password": "hashed_password_44",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-02-21",
        "quantity": 5
      },
      {
        "product_id": "13",
        "order_date": "2024-12-29",
        "quantity": 4
      }
    ],
    "cart": [],
    "favorites": [],
    "last_login": "2024-11-20",
    "address": "8568 Martin Skyway Suite 687\nJasonberg, MT 76997",
    "birth_date": "1947-04-29",
    "membership_level": "Bronze"
  },
  {
    "id": "45",
    "username": "ymcdowell",
    "email": "dflores@baldwin.info",
    "phone": "(943)837-0050",
    "name": "양정웅",
    "password": "hashed_password_45",
    "orders": [],
    "cart": [
      "13"
    ],
    "favorites": [
      "9",
      "9",
      "17",
      "19",
      "4"
    ],
    "last_login": "2024-05-06",
    "address": "95062 Watson Ferry\nSouth Kendraborough, MO 21288",
    "birth_date": "1983-07-09",
    "membership_level": "Bronze"
  },
  {
    "id": "46",
    "username": "kevinschultz",
    "email": "kennethyoung@anderson.info",
    "phone": "983.546.0595x3539",
    "name": "신정순",
    "password": "hashed_password_46",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-06-10",
        "quantity": 5
      },
      {
        "product_id": "10",
        "order_date": "2024-06-27",
        "quantity": 5
      },
      {
        "product_id": "3",
        "order_date": "2024-02-14",
        "quantity": 2
      }
    ],
    "cart": [
      "18",
      "19",
      "5",
      "11"
    ],
    "favorites": [
      "12"
    ],
    "last_login": "2024-11-07",
    "address": "596 Mills Parkways\nMartinezland, MN 11579",
    "birth_date": "2000-11-16",
    "membership_level": "Bronze"
  },
  {
    "id": "47",
    "username": "jasonford",
    "email": "tclark@hotmail.com",
    "phone": "001-345-127-9461x8035",
    "name": "김진호",
    "password": "hashed_password_47",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-08-30",
        "quantity": 4
      },
      {
        "product_id": "2",
        "order_date": "2024-02-18",
        "quantity": 3
      },
      {
        "product_id": "9",
        "order_date": "2024-03-05",
        "quantity": 2
      }
    ],
    "cart": [
      "18",
      "19",
      "12"
    ],
    "favorites": [],
    "last_login": "2024-07-04",
    "address": "438 Tammy Estates Suite 109\nAaronmouth, ND 81877",
    "birth_date": "1964-09-25",
    "membership_level": "Gold"
  },
  {
    "id": "48",
    "username": "ricestephen",
    "email": "ndeleon@cox.com",
    "phone": "+1-031-375-3288x13866",
    "name": "박영일",
    "password": "hashed_password_48",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-06-24",
        "quantity": 1
      },
      {
        "product_id": "3",
        "order_date": "2024-07-18",
        "quantity": 4
      },
      {
        "product_id": "11",
        "order_date": "2024-11-27",
        "quantity": 1
      },
      {
        "product_id": "16",
        "order_date": "2024-12-15",
        "quantity": 3
      }
    ],
    "cart": [
      "10",
      "11",
      "13"
    ],
    "favorites": [
      "11",
      "2"
    ],
    "last_login": "2024-11-12",
    "address": "169 Tanner Extension Apt. 627\nNew Lisa, CO 44179",
    "birth_date": "1961-01-30",
    "membership_level": "Bronze"
  },
  {
    "id": "49",
    "username": "scottchristopher",
    "email": "allisonrobertson@smith.org",
    "phone": "559.999.5612x1049",
    "name": "박병철",
    "password": "hashed_password_49",
    "orders": [],
    "cart": [
      "18",
      "19",
      "16",
      "8"
    ],
    "favorites": [
      "17",
      "10",
      "12",
      "17",
      "19"
    ],
    "last_login": "2024-07-23",
    "address": "USS Scott\nFPO AP 21636",
    "birth_date": "1966-02-08",
    "membership_level": "Gold"
  },
  {
    "id": "50",
    "username": "danielscrystal",
    "email": "vhoward@hotmail.com",
    "phone": "(807)559-9290",
    "name": "백준혁",
    "password": "hashed_password_50",
    "orders": [
      {
        "product_id": "9",
        "order_date": "2024-05-11",
        "quantity": 2
      },
      {
        "product_id": "18",
        "order_date": "2024-04-19",
        "quantity": 2
      },
      {
        "product_id": "16",
        "order_date": "2024-05-25",
        "quantity": 1
      },
      {
        "product_id": "11",
        "order_date": "2024-10-10",
        "quantity": 1
      }
    ],
    "cart": [
      "5"
    ],
    "favorites": [
      "10",
      "9",
      "14",
      "3",
      "3"
    ],
    "last_login": "2024-04-30",
    "address": "49134 Eric Street\nNorth Darleneport, WA 89688",
    "birth_date": "1947-01-20",
    "membership_level": "Gold"
  },
  {
    "id": "51",
    "username": "zrodriguez",
    "email": "ubecker@alexander.org",
    "phone": "(743)461-1487",
    "name": "엄선영",
    "password": "hashed_password_51",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-06-28",
        "quantity": 4
      },
      {
        "product_id": "16",
        "order_date": "2025-01-24",
        "quantity": 1
      },
      {
        "product_id": "9",
        "order_date": "2024-05-18",
        "quantity": 5
      },
      {
        "product_id": "10",
        "order_date": "2024-03-05",
        "quantity": 2
      },
      {
        "product_id": "1",
        "order_date": "2024-02-14",
        "quantity": 3
      }
    ],
    "cart": [
      "13",
      "15",
      "4",
      "10",
      "5"
    ],
    "favorites": [
      "13",
      "2"
    ],
    "last_login": "2024-04-06",
    "address": "275 Devin Island Suite 354\nDanielmouth, VT 88415",
    "birth_date": "1962-08-01",
    "membership_level": "Platinum"
  },
  {
    "id": "52",
    "username": "sbutler",
    "email": "christopher81@martinez-simpson.biz",
    "phone": "+1-811-614-3834",
    "name": "주지혜",
    "password": "hashed_password_52",
    "orders": [],
    "cart": [
      "7",
      "5",
      "19",
      "17",
      "19"
    ],
    "favorites": [
      "2"
    ],
    "last_login": "2024-04-12",
    "address": "756 Kristen Flat\nSouth Christopherview, FL 35538",
    "birth_date": "1967-09-06",
    "membership_level": "Silver"
  },
  {
    "id": "53",
    "username": "vanessa55",
    "email": "vwilliams@zuniga-johnson.com",
    "phone": "(065)363-5336",
    "name": "황미영",
    "password": "hashed_password_53",
    "orders": [
      {
        "product_id": "2",
        "order_date": "2024-04-26",
        "quantity": 2
      },
      {
        "product_id": "11",
        "order_date": "2024-04-13",
        "quantity": 1
      },
      {
        "product_id": "13",
        "order_date": "2024-05-07",
        "quantity": 1
      },
      {
        "product_id": "6",
        "order_date": "2024-10-13",
        "quantity": 3
      }
    ],
    "cart": [
      "15",
      "18",
      "1",
      "11"
    ],
    "favorites": [],
    "last_login": "2024-12-21",
    "address": "72427 Moore Stravenue Suite 834\nHarveyfurt, WV 96736",
    "birth_date": "1995-03-10",
    "membership_level": "Gold"
  },
  {
    "id": "54",
    "username": "angelica91",
    "email": "ianwhite@lee.com",
    "phone": "(327)153-5949x03474",
    "name": "이미정",
    "password": "hashed_password_54",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-08-13",
        "quantity": 3
      },
      {
        "product_id": "3",
        "order_date": "2024-11-07",
        "quantity": 3
      }
    ],
    "cart": [],
    "favorites": [],
    "last_login": "2024-02-11",
    "address": "06390 Hill Creek Apt. 419\nBensonland, OK 85888",
    "birth_date": "1955-01-16",
    "membership_level": "Silver"
  },
  {
    "id": "55",
    "username": "russellcoleman",
    "email": "qgonzalez@johnson.com",
    "phone": "(458)759-6113x9573",
    "name": "김서영",
    "password": "hashed_password_55",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-08-26",
        "quantity": 2
      },
      {
        "product_id": "4",
        "order_date": "2024-08-13",
        "quantity": 4
      }
    ],
    "cart": [
      "17",
      "2",
      "11"
    ],
    "favorites": [
      "17",
      "17",
      "20",
      "9",
      "7"
    ],
    "last_login": "2024-06-04",
    "address": "478 Jennifer Street Suite 261\nMichellehaven, ND 69390",
    "birth_date": "2000-06-14",
    "membership_level": "Platinum"
  },
  {
    "id": "56",
    "username": "bhodges",
    "email": "fhaley@phillips-macdonald.com",
    "phone": "219-447-4374x76880",
    "name": "이지훈",
    "password": "hashed_password_56",
    "orders": [],
    "cart": [
      "17"
    ],
    "favorites": [],
    "last_login": "2024-04-06",
    "address": "6883 Cassandra Inlet\nWest Pattyport, OK 48476",
    "birth_date": "1993-01-26",
    "membership_level": "Platinum"
  },
  {
    "id": "57",
    "username": "awilson",
    "email": "cynthia33@cunningham.com",
    "phone": "930-803-1187",
    "name": "김명자",
    "password": "hashed_password_57",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-04-25",
        "quantity": 4
      },
      {
        "product_id": "10",
        "order_date": "2024-10-16",
        "quantity": 5
      }
    ],
    "cart": [
      "15"
    ],
    "favorites": [],
    "last_login": "2024-09-13",
    "address": "326 Griffin Wall\nNorth Justinland, VA 09372",
    "birth_date": "1989-04-30",
    "membership_level": "Platinum"
  },
  {
    "id": "58",
    "username": "johnsonmichelle",
    "email": "jonesjames@wiggins.com",
    "phone": "636.920.1824x44223",
    "name": "이서연",
    "password": "hashed_password_58",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-05-24",
        "quantity": 2
      },
      {
        "product_id": "6",
        "order_date": "2024-04-25",
        "quantity": 3
      }
    ],
    "cart": [
      "3",
      "1",
      "20",
      "14"
    ],
    "favorites": [
      "4",
      "12"
    ],
    "last_login": "2024-10-09",
    "address": "Unit 1793 Box 4404\nDPO AP 24789",
    "birth_date": "1995-05-03",
    "membership_level": "Bronze"
  },
  {
    "id": "59",
    "username": "brandon22",
    "email": "mcknightdenise@yahoo.com",
    "phone": "471.449.4596x0156",
    "name": "박주원",
    "password": "hashed_password_59",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2024-05-02",
        "quantity": 2
      },
      {
        "product_id": "10",
        "order_date": "2024-05-23",
        "quantity": 3
      },
      {
        "product_id": "1",
        "order_date": "2024-04-23",
        "quantity": 2
      },
      {
        "product_id": "1",
        "order_date": "2024-09-13",
        "quantity": 2
      }
    ],
    "cart": [
      "15"
    ],
    "favorites": [
      "8",
      "15",
      "6",
      "9"
    ],
    "last_login": "2024-11-06",
    "address": "86088 Rebecca Mountain Apt. 512\nEast Alexandria, IA 88269",
    "birth_date": "1989-06-18",
    "membership_level": "Silver"
  },
  {
    "id": "60",
    "username": "richardsonblake",
    "email": "tirwin@yahoo.com",
    "phone": "(007)227-5642",
    "name": "김명숙",
    "password": "hashed_password_60",
    "orders": [],
    "cart": [
      "20",
      "16"
    ],
    "favorites": [],
    "last_login": "2024-03-21",
    "address": "USNV Sparks\nFPO AE 39054",
    "birth_date": "1983-04-04",
    "membership_level": "Bronze"
  },
  {
    "id": "61",
    "username": "amysmith",
    "email": "valerie15@gmail.com",
    "phone": "001-682-369-8694x4686",
    "name": "양현우",
    "password": "hashed_password_61",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-04-26",
        "quantity": 3
      },
      {
        "product_id": "7",
        "order_date": "2024-11-14",
        "quantity": 3
      },
      {
        "product_id": "3",
        "order_date": "2024-07-14",
        "quantity": 1
      }
    ],
    "cart": [
      "13"
    ],
    "favorites": [
      "9",
      "6"
    ],
    "last_login": "2024-11-17",
    "address": "8537 Erickson Flat\nAshleystad, MD 24683",
    "birth_date": "1996-03-05",
    "membership_level": "Platinum"
  },
  {
    "id": "62",
    "username": "ashley02",
    "email": "johnsoncharles@gmail.com",
    "phone": "(336)260-7912x468",
    "name": "성춘자",
    "password": "hashed_password_62",
    "orders": [
      {
        "product_id": "15",
        "order_date": "2024-05-23",
        "quantity": 5
      },
      {
        "product_id": "13",
        "order_date": "2024-06-03",
        "quantity": 1
      }
    ],
    "cart": [],
    "favorites": [
      "18",
      "9",
      "7"
    ],
    "last_login": "2024-08-29",
    "address": "235 Andrew Springs\nPort Brianburgh, GA 85494",
    "birth_date": "1980-07-22",
    "membership_level": "Silver"
  },
  {
    "id": "63",
    "username": "baxtereric",
    "email": "lori51@brewer.org",
    "phone": "+1-841-453-0591x29637",
    "name": "권진우",
    "password": "hashed_password_63",
    "orders": [
      {
        "product_id": "3",
        "order_date": "2024-03-16",
        "quantity": 5
      },
      {
        "product_id": "16",
        "order_date": "2024-02-15",
        "quantity": 3
      },
      {
        "product_id": "3",
        "order_date": "2024-04-07",
        "quantity": 4
      },
      {
        "product_id": "16",
        "order_date": "2024-08-15",
        "quantity": 1
      },
      {
        "product_id": "11",
        "order_date": "2024-03-21",
        "quantity": 1
      }
    ],
    "cart": [
      "18",
      "10",
      "4",
      "17",
      "11"
    ],
    "favorites": [],
    "last_login": "2024-11-24",
    "address": "0179 Gary Ramp\nWest Elizabethchester, NE 57145",
    "birth_date": "1978-09-11",
    "membership_level": "Bronze"
  },
  {
    "id": "64",
    "username": "latasha85",
    "email": "april04@riley-williams.com",
    "phone": "+1-823-651-7065x9638",
    "name": "이정수",
    "password": "hashed_password_64",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-08-08",
        "quantity": 4
      }
    ],
    "cart": [
      "6",
      "14"
    ],
    "favorites": [],
    "last_login": "2024-09-29",
    "address": "767 Martinez Rapids\nOwensport, OK 75129",
    "birth_date": "1960-08-22",
    "membership_level": "Silver"
  },
  {
    "id": "65",
    "username": "keithwilson",
    "email": "cesar61@hotmail.com",
    "phone": "6554825319",
    "name": "고영길",
    "password": "hashed_password_65",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-10-19",
        "quantity": 2
      },
      {
        "product_id": "9",
        "order_date": "2024-08-01",
        "quantity": 3
      },
      {
        "product_id": "17",
        "order_date": "2024-05-02",
        "quantity": 5
      },
      {
        "product_id": "18",
        "order_date": "2024-05-02",
        "quantity": 5
      }
    ],
    "cart": [
      "9",
      "13",
      "14",
      "9"
    ],
    "favorites": [
      "9",
      "15"
    ],
    "last_login": "2024-08-29",
    "address": "USNV Alexander\nFPO AE 07760",
    "birth_date": "1949-03-01",
    "membership_level": "Bronze"
  },
  {
    "id": "66",
    "username": "hdeleon",
    "email": "lnelson@knapp.info",
    "phone": "001-468-345-7447",
    "name": "허우진",
    "password": "hashed_password_66",
    "orders": [
      {
        "product_id": "19",
        "order_date": "2024-05-14",
        "quantity": 2
      },
      {
        "product_id": "1",
        "order_date": "2024-08-06",
        "quantity": 1
      }
    ],
    "cart": [
      "6",
      "15"
    ],
    "favorites": [
      "11",
      "5",
      "5",
      "7",
      "4"
    ],
    "last_login": "2024-12-25",
    "address": "05471 Randall Freeway\nNew Travisfort, MT 66352",
    "birth_date": "2004-04-01",
    "membership_level": "Bronze"
  },
  {
    "id": "67",
    "username": "ashley56",
    "email": "greendawn@andrews.com",
    "phone": "497.694.4638",
    "name": "황중수",
    "password": "hashed_password_67",
    "orders": [
      {
        "product_id": "10",
        "order_date": "2024-03-11",
        "quantity": 5
      },
      {
        "product_id": "18",
        "order_date": "2024-10-28",
        "quantity": 5
      },
      {
        "product_id": "15",
        "order_date": "2024-11-06",
        "quantity": 1
      },
      {
        "product_id": "7",
        "order_date": "2024-09-27",
        "quantity": 5
      }
    ],
    "cart": [
      "10",
      "18",
      "9",
      "11",
      "16"
    ],
    "favorites": [],
    "last_login": "2024-06-02",
    "address": "8760 Bennett Forges Suite 091\nEast Christopher, CT 76258",
    "birth_date": "1967-07-18",
    "membership_level": "Bronze"
  },
  {
    "id": "68",
    "username": "yulouis",
    "email": "deborah06@hotmail.com",
    "phone": "001-925-922-7699",
    "name": "권채원",
    "password": "hashed_password_68",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2025-01-05",
        "quantity": 4
      },
      {
        "product_id": "12",
        "order_date": "2024-11-10",
        "quantity": 3
      }
    ],
    "cart": [
      "17",
      "4",
      "8"
    ],
    "favorites": [
      "19",
      "20",
      "9"
    ],
    "last_login": "2024-09-25",
    "address": "2630 William Trail\nJacksonland, NH 08942",
    "birth_date": "2005-09-01",
    "membership_level": "Gold"
  },
  {
    "id": "69",
    "username": "william00",
    "email": "conleybrian@hotmail.com",
    "phone": "+1-420-302-8760x071",
    "name": "노경희",
    "password": "hashed_password_69",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-02-19",
        "quantity": 5
      },
      {
        "product_id": "4",
        "order_date": "2024-03-04",
        "quantity": 4
      }
    ],
    "cart": [
      "12",
      "12"
    ],
    "favorites": [
      "7"
    ],
    "last_login": "2024-10-28",
    "address": "93157 Eric Harbor Suite 558\nNorth Aaronmouth, DC 02587",
    "birth_date": "1954-01-19",
    "membership_level": "Platinum"
  },
  {
    "id": "70",
    "username": "caseyrandall",
    "email": "jamesanderson@austin-larson.com",
    "phone": "+1-595-285-3475",
    "name": "최민재",
    "password": "hashed_password_70",
    "orders": [
      {
        "product_id": "4",
        "order_date": "2024-12-08",
        "quantity": 1
      }
    ],
    "cart": [
      "15",
      "7",
      "7",
      "7",
      "16"
    ],
    "favorites": [
      "8"
    ],
    "last_login": "2024-11-23",
    "address": "4552 Carmen Underpass Apt. 534\nJohntown, DE 79152",
    "birth_date": "1988-03-24",
    "membership_level": "Gold"
  },
  {
    "id": "71",
    "username": "stephanierowe",
    "email": "tjackson@foster.info",
    "phone": "593.855.5448",
    "name": "송영수",
    "password": "hashed_password_71",
    "orders": [
      {
        "product_id": "4",
        "order_date": "2024-09-23",
        "quantity": 4
      },
      {
        "product_id": "15",
        "order_date": "2024-11-04",
        "quantity": 3
      },
      {
        "product_id": "2",
        "order_date": "2024-02-08",
        "quantity": 2
      },
      {
        "product_id": "2",
        "order_date": "2024-07-27",
        "quantity": 4
      }
    ],
    "cart": [
      "20",
      "9",
      "10",
      "16"
    ],
    "favorites": [
      "5",
      "17",
      "17"
    ],
    "last_login": "2024-07-29",
    "address": "48006 Denise Garden\nSouth Wendy, KY 71007",
    "birth_date": "1999-08-19",
    "membership_level": "Platinum"
  },
  {
    "id": "72",
    "username": "tammy61",
    "email": "diane96@stafford-robinson.net",
    "phone": "001-319-510-7201x509",
    "name": "서유진",
    "password": "hashed_password_72",
    "orders": [
      {
        "product_id": "8",
        "order_date": "2024-12-01",
        "quantity": 2
      },
      {
        "product_id": "2",
        "order_date": "2025-01-15",
        "quantity": 4
      }
    ],
    "cart": [
      "19"
    ],
    "favorites": [
      "9",
      "4",
      "4",
      "5"
    ],
    "last_login": "2024-03-27",
    "address": "4392 Nelson Spring\nNicholasmouth, VT 16130",
    "birth_date": "1995-11-11",
    "membership_level": "Silver"
  },
  {
    "id": "73",
    "username": "nwiggins",
    "email": "brandy88@marsh-martin.net",
    "phone": "+1-075-362-4729x12615",
    "name": "백서연",
    "password": "hashed_password_73",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-05-09",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-02-24",
        "quantity": 3
      },
      {
        "product_id": "2",
        "order_date": "2024-08-17",
        "quantity": 1
      },
      {
        "product_id": "13",
        "order_date": "2024-02-16",
        "quantity": 5
      },
      {
        "product_id": "13",
        "order_date": "2024-10-08",
        "quantity": 1
      }
    ],
    "cart": [
      "18",
      "14"
    ],
    "favorites": [],
    "last_login": "2024-09-03",
    "address": "919 Ray Extensions Suite 600\nSouth Stacy, NV 67006",
    "birth_date": "1948-07-04",
    "membership_level": "Bronze"
  },
  {
    "id": "74",
    "username": "olsonjenna",
    "email": "agraham@jensen-pratt.com",
    "phone": "+1-494-557-2628x97114",
    "name": "이수민",
    "password": "hashed_password_74",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2024-10-19",
        "quantity": 2
      },
      {
        "product_id": "11",
        "order_date": "2024-08-23",
        "quantity": 5
      },
      {
        "product_id": "15",
        "order_date": "2024-10-11",
        "quantity": 1
      }
    ],
    "cart": [
      "12",
      "15",
      "7"
    ],
    "favorites": [],
    "last_login": "2024-08-14",
    "address": "Unit 6305 Box 6981\nDPO AE 10422",
    "birth_date": "1971-04-04",
    "membership_level": "Gold"
  },
  {
    "id": "75",
    "username": "aadams",
    "email": "myersanthony@mccoy.com",
    "phone": "(054)613-8623",
    "name": "박성진",
    "password": "hashed_password_75",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2025-01-07",
        "quantity": 4
      },
      {
        "product_id": "19",
        "order_date": "2024-12-10",
        "quantity": 3
      },
      {
        "product_id": "7",
        "order_date": "2024-04-10",
        "quantity": 4
      },
      {
        "product_id": "18",
        "order_date": "2024-10-18",
        "quantity": 2
      },
      {
        "product_id": "9",
        "order_date": "2024-06-04",
        "quantity": 3
      }
    ],
    "cart": [
      "17",
      "16"
    ],
    "favorites": [
      "5",
      "2",
      "10",
      "3"
    ],
    "last_login": "2025-01-15",
    "address": "888 Walker Radial Suite 507\nLake Rebekah, MN 80217",
    "birth_date": "1982-03-25",
    "membership_level": "Silver"
  },
  {
    "id": "76",
    "username": "vtucker",
    "email": "christina90@hotmail.com",
    "phone": "591.426.2339x3942",
    "name": "고예은",
    "password": "hashed_password_76",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-11-20",
        "quantity": 5
      },
      {
        "product_id": "15",
        "order_date": "2024-09-02",
        "quantity": 4
      },
      {
        "product_id": "10",
        "order_date": "2024-02-28",
        "quantity": 4
      },
      {
        "product_id": "15",
        "order_date": "2024-06-26",
        "quantity": 5
      },
      {
        "product_id": "1",
        "order_date": "2025-01-27",
        "quantity": 4
      }
    ],
    "cart": [
      "5",
      "2",
      "12",
      "4"
    ],
    "favorites": [
      "3",
      "2"
    ],
    "last_login": "2024-11-13",
    "address": "951 Bentley Orchard Apt. 609\nMillerborough, KY 55007",
    "birth_date": "1999-06-11",
    "membership_level": "Platinum"
  },
  {
    "id": "77",
    "username": "hunterleslie",
    "email": "lindseykim@hotmail.com",
    "phone": "370-631-9865x16133",
    "name": "이숙자",
    "password": "hashed_password_77",
    "orders": [],
    "cart": [
      "15"
    ],
    "favorites": [
      "3",
      "4",
      "13",
      "11",
      "2"
    ],
    "last_login": "2024-08-24",
    "address": "985 Adkins Lock Suite 433\nSantoshaven, OK 60205",
    "birth_date": "1958-03-25",
    "membership_level": "Bronze"
  },
  {
    "id": "78",
    "username": "melvinwilson",
    "email": "vanthony@gibson.com",
    "phone": "(878)995-1995x46301",
    "name": "이민지",
    "password": "hashed_password_78",
    "orders": [],
    "cart": [
      "4",
      "4"
    ],
    "favorites": [],
    "last_login": "2024-05-25",
    "address": "USNS Wright\nFPO AP 08024",
    "birth_date": "1985-05-19",
    "membership_level": "Bronze"
  },
  {
    "id": "79",
    "username": "balvarez",
    "email": "brownchristine@gmail.com",
    "phone": "002.775.9362x266",
    "name": "박순자",
    "password": "hashed_password_79",
    "orders": [
      {
        "product_id": "3",
        "order_date": "2024-11-05",
        "quantity": 1
      },
      {
        "product_id": "11",
        "order_date": "2024-10-05",
        "quantity": 5
      },
      {
        "product_id": "1",
        "order_date": "2024-10-07",
        "quantity": 2
      },
      {
        "product_id": "6",
        "order_date": "2024-07-10",
        "quantity": 1
      },
      {
        "product_id": "19",
        "order_date": "2024-03-08",
        "quantity": 1
      }
    ],
    "cart": [
      "1",
      "4"
    ],
    "favorites": [],
    "last_login": "2024-08-10",
    "address": "338 Alicia Falls Suite 132\nJohnsonborough, SD 78994",
    "birth_date": "1953-06-16",
    "membership_level": "Bronze"
  },
  {
    "id": "80",
    "username": "alexandra07",
    "email": "rcolon@yahoo.com",
    "phone": "6892963304",
    "name": "김승현",
    "password": "hashed_password_80",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-05-28",
        "quantity": 4
      }
    ],
    "cart": [
      "20",
      "7"
    ],
    "favorites": [],
    "last_login": "2024-02-18",
    "address": "PSC 1627, Box 7561\nAPO AE 78421",
    "birth_date": "1980-07-05",
    "membership_level": "Bronze"
  },
  {
    "id": "81",
    "username": "schwartzryan",
    "email": "hoovercarolyn@yahoo.com",
    "phone": "186.351.4590x28733",
    "name": "김순자",
    "password": "hashed_password_81",
    "orders": [],
    "cart": [
      "2",
      "19",
      "3",
      "13"
    ],
    "favorites": [
      "3",
      "1"
    ],
    "last_login": "2024-06-27",
    "address": "4131 Green Drive Suite 307\nLake Chelsea, OK 38648",
    "birth_date": "1964-07-02",
    "membership_level": "Silver"
  },
  {
    "id": "82",
    "username": "crawfordgerald",
    "email": "zjohnson@hotmail.com",
    "phone": "+1-147-615-1678x551",
    "name": "최경희",
    "password": "hashed_password_82",
    "orders": [
      {
        "product_id": "14",
        "order_date": "2024-12-28",
        "quantity": 2
      },
      {
        "product_id": "18",
        "order_date": "2024-11-11",
        "quantity": 5
      }
    ],
    "cart": [
      "2",
      "20"
    ],
    "favorites": [],
    "last_login": "2024-03-14",
    "address": "62620 Christina Forks\nSouth Ronaldside, MD 76482",
    "birth_date": "1992-10-05",
    "membership_level": "Gold"
  },
  {
    "id": "83",
    "username": "sandovaljessica",
    "email": "booneshawn@perry-donovan.com",
    "phone": "902-280-0135x17865",
    "name": "이준혁",
    "password": "hashed_password_83",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-09-29",
        "quantity": 1
      },
      {
        "product_id": "4",
        "order_date": "2024-05-30",
        "quantity": 3
      },
      {
        "product_id": "19",
        "order_date": "2024-03-01",
        "quantity": 3
      },
      {
        "product_id": "17",
        "order_date": "2024-06-22",
        "quantity": 2
      }
    ],
    "cart": [
      "12"
    ],
    "favorites": [
      "10",
      "2"
    ],
    "last_login": "2024-03-17",
    "address": "57283 Rachel Islands\nBrianberg, LA 32068",
    "birth_date": "1948-10-12",
    "membership_level": "Gold"
  },
  {
    "id": "84",
    "username": "sbarnes",
    "email": "susananderson@hotmail.com",
    "phone": "966.717.5408x4625",
    "name": "김정호",
    "password": "hashed_password_84",
    "orders": [],
    "cart": [
      "20",
      "2",
      "6",
      "14",
      "19"
    ],
    "favorites": [
      "1",
      "11",
      "14",
      "7"
    ],
    "last_login": "2024-02-08",
    "address": "39176 Taylor Well\nWest Michaelton, NV 97978",
    "birth_date": "1960-02-17",
    "membership_level": "Gold"
  },
  {
    "id": "85",
    "username": "helenjohnson",
    "email": "gavin59@vargas-watson.biz",
    "phone": "247.082.4505x96324",
    "name": "박명숙",
    "password": "hashed_password_85",
    "orders": [
      {
        "product_id": "11",
        "order_date": "2024-08-17",
        "quantity": 2
      },
      {
        "product_id": "5",
        "order_date": "2024-04-22",
        "quantity": 3
      },
      {
        "product_id": "11",
        "order_date": "2024-09-08",
        "quantity": 2
      }
    ],
    "cart": [
      "1",
      "2",
      "9"
    ],
    "favorites": [
      "2"
    ],
    "last_login": "2024-12-02",
    "address": "319 Rhodes Plaza\nMichaelburgh, VT 35920",
    "birth_date": "1962-04-18",
    "membership_level": "Gold"
  },
  {
    "id": "86",
    "username": "natashabailey",
    "email": "uwatson@hotmail.com",
    "phone": "(736)117-9089x15307",
    "name": "이성현",
    "password": "hashed_password_86",
    "orders": [
      {
        "product_id": "13",
        "order_date": "2024-11-28",
        "quantity": 1
      },
      {
        "product_id": "7",
        "order_date": "2024-07-25",
        "quantity": 4
      },
      {
        "product_id": "6",
        "order_date": "2024-03-30",
        "quantity": 4
      },
      {
        "product_id": "9",
        "order_date": "2024-07-18",
        "quantity": 3
      }
    ],
    "cart": [
      "19",
      "1",
      "19",
      "4"
    ],
    "favorites": [],
    "last_login": "2024-04-21",
    "address": "23350 Bell Tunnel Suite 174\nEast Ianhaven, WV 13955",
    "birth_date": "1983-10-23",
    "membership_level": "Silver"
  },
  {
    "id": "87",
    "username": "ucohen",
    "email": "juliemartin@ford.com",
    "phone": "(230)372-1695x04237",
    "name": "김현준",
    "password": "hashed_password_87",
    "orders": [],
    "cart": [
      "9",
      "11",
      "8",
      "4"
    ],
    "favorites": [
      "18",
      "5",
      "7",
      "17"
    ],
    "last_login": "2024-04-19",
    "address": "6383 Matthew Road\nNorth Leonardberg, MT 44744",
    "birth_date": "1998-06-30",
    "membership_level": "Gold"
  },
  {
    "id": "88",
    "username": "allisongray",
    "email": "gsalas@gmail.com",
    "phone": "215.424.2265x222",
    "name": "곽지훈",
    "password": "hashed_password_88",
    "orders": [
      {
        "product_id": "12",
        "order_date": "2024-03-13",
        "quantity": 3
      },
      {
        "product_id": "3",
        "order_date": "2024-09-03",
        "quantity": 2
      }
    ],
    "cart": [
      "7",
      "19",
      "18"
    ],
    "favorites": [
      "2",
      "19",
      "2",
      "3",
      "2"
    ],
    "last_login": "2024-09-06",
    "address": "51806 Ashley Ford\nPort Juan, OH 26088",
    "birth_date": "1963-12-20",
    "membership_level": "Gold"
  },
  {
    "id": "89",
    "username": "landrywhitney",
    "email": "rsimon@yahoo.com",
    "phone": "001-271-249-6020",
    "name": "김영길",
    "password": "hashed_password_89",
    "orders": [
      {
        "product_id": "5",
        "order_date": "2024-12-18",
        "quantity": 4
      },
      {
        "product_id": "4",
        "order_date": "2024-06-09",
        "quantity": 3
      },
      {
        "product_id": "4",
        "order_date": "2024-12-07",
        "quantity": 1
      },
      {
        "product_id": "10",
        "order_date": "2024-02-29",
        "quantity": 2
      }
    ],
    "cart": [
      "15",
      "15",
      "3",
      "17",
      "5"
    ],
    "favorites": [
      "1",
      "5",
      "2",
      "3"
    ],
    "last_login": "2024-11-24",
    "address": "44263 Chase Prairie Apt. 971\nGilmoreton, ID 81210",
    "birth_date": "1970-12-19",
    "membership_level": "Bronze"
  },
  {
    "id": "90",
    "username": "heather80",
    "email": "charles19@reyes.com",
    "phone": "+1-235-209-5612x993",
    "name": "손예은",
    "password": "hashed_password_90",
    "orders": [
      {
        "product_id": "7",
        "order_date": "2024-09-01",
        "quantity": 5
      },
      {
        "product_id": "18",
        "order_date": "2025-01-01",
        "quantity": 5
      }
    ],
    "cart": [],
    "favorites": [
      "5"
    ],
    "last_login": "2024-02-06",
    "address": "583 Perry Lake Suite 410\nEast Donna, AK 43654",
    "birth_date": "2002-06-12",
    "membership_level": "Platinum"
  },
  {
    "id": "91",
    "username": "jaygreen",
    "email": "barrettjulia@gmail.com",
    "phone": "+1-377-188-2377x032",
    "name": "김서준",
    "password": "hashed_password_91",
    "orders": [
      {
        "product_id": "13",
        "order_date": "2024-09-19",
        "quantity": 1
      },
      {
        "product_id": "8",
        "order_date": "2024-09-01",
        "quantity": 2
      },
      {
        "product_id": "15",
        "order_date": "2025-01-27",
        "quantity": 4
      }
    ],
    "cart": [
      "15",
      "17",
      "4",
      "20"
    ],
    "favorites": [
      "20"
    ],
    "last_login": "2024-11-04",
    "address": "888 Juan Inlet Apt. 995\nNorth Scottstad, IN 96295",
    "birth_date": "1990-08-30",
    "membership_level": "Bronze"
  },
  {
    "id": "92",
    "username": "qbrooks",
    "email": "michaelstone@flores.info",
    "phone": "(817)417-5420",
    "name": "남지원",
    "password": "hashed_password_92",
    "orders": [
      {
        "product_id": "4",
        "order_date": "2024-10-26",
        "quantity": 5
      },
      {
        "product_id": "7",
        "order_date": "2024-06-25",
        "quantity": 1
      }
    ],
    "cart": [],
    "favorites": [
      "12",
      "7",
      "9",
      "16"
    ],
    "last_login": "2024-06-10",
    "address": "Unit 4069 Box 7186\nDPO AE 12896",
    "birth_date": "1952-09-04",
    "membership_level": "Gold"
  },
  {
    "id": "93",
    "username": "hamiltonelizabeth",
    "email": "kenneth45@yahoo.com",
    "phone": "(447)436-0740",
    "name": "임지민",
    "password": "hashed_password_93",
    "orders": [],
    "cart": [
      "16",
      "9",
      "16"
    ],
    "favorites": [],
    "last_login": "2024-06-30",
    "address": "2144 Steven Ferry\nNorth Linda, MA 53950",
    "birth_date": "1957-05-08",
    "membership_level": "Bronze"
  },
  {
    "id": "94",
    "username": "loweleslie",
    "email": "gomezrebecca@garcia.com",
    "phone": "+1-715-474-1232",
    "name": "이아름",
    "password": "hashed_password_94",
    "orders": [
      {
        "product_id": "18",
        "order_date": "2024-04-03",
        "quantity": 5
      },
      {
        "product_id": "11",
        "order_date": "2025-01-13",
        "quantity": 3
      },
      {
        "product_id": "1",
        "order_date": "2024-04-23",
        "quantity": 1
      }
    ],
    "cart": [
      "13"
    ],
    "favorites": [
      "4"
    ],
    "last_login": "2024-07-22",
    "address": "9971 Padilla Common\nMcconnellmouth, OH 01953",
    "birth_date": "1953-09-29",
    "membership_level": "Bronze"
  },
  {
    "id": "95",
    "username": "vaughanmichael",
    "email": "justinmurray@yahoo.com",
    "phone": "039-577-6689x120",
    "name": "최서준",
    "password": "hashed_password_95",
    "orders": [
      {
        "product_id": "4",
        "order_date": "2024-05-19",
        "quantity": 2
      }
    ],
    "cart": [
      "6",
      "12",
      "9",
      "16",
      "5"
    ],
    "favorites": [
      "10",
      "17",
      "6"
    ],
    "last_login": "2025-02-03",
    "address": "3811 Wright Gardens Apt. 154\nGarcialand, RI 40604",
    "birth_date": "1958-05-12",
    "membership_level": "Platinum"
  },
  {
    "id": "96",
    "username": "bridget05",
    "email": "stephaniedelgado@taylor-flynn.com",
    "phone": "483.375.4561",
    "name": "김정희",
    "password": "hashed_password_96",
    "orders": [
      {
        "product_id": "3",
        "order_date": "2024-05-08",
        "quantity": 4
      },
      {
        "product_id": "7",
        "order_date": "2024-11-25",
        "quantity": 4
      },
      {
        "product_id": "11",
        "order_date": "2024-10-24",
        "quantity": 1
      },
      {
        "product_id": "19",
        "order_date": "2024-12-16",
        "quantity": 3
      }
    ],
    "cart": [
      "17",
      "18"
    ],
    "favorites": [
      "13",
      "20",
      "7",
      "5",
      "7"
    ],
    "last_login": "2024-03-25",
    "address": "19619 Bryant Villages\nWest Elizabeth, DC 58022",
    "birth_date": "1950-09-11",
    "membership_level": "Bronze"
  },
  {
    "id": "97",
    "username": "floresdaniel",
    "email": "mcleanpaul@price-farrell.com",
    "phone": "994-798-7806",
    "name": "곽준호",
    "password": "hashed_password_97",
    "orders": [],
    "cart": [
      "12",
      "19"
    ],
    "favorites": [
      "5",
      "17",
      "8",
      "3"
    ],
    "last_login": "2024-07-16",
    "address": "6097 Richard Ford\nWest Rebeccamouth, AK 60764",
    "birth_date": "1970-06-21",
    "membership_level": "Gold"
  },
  {
    "id": "98",
    "username": "candrews",
    "email": "katherinebuckley@gmail.com",
    "phone": "379.073.1450x61781",
    "name": "김영환",
    "password": "hashed_password_98",
    "orders": [
      {
        "product_id": "17",
        "order_date": "2024-09-14",
        "quantity": 2
      },
      {
        "product_id": "18",
        "order_date": "2024-06-14",
        "quantity": 5
      },
      {
        "product_id": "13",
        "order_date": "2024-11-18",
        "quantity": 5
      },
      {
        "product_id": "9",
        "order_date": "2025-01-19",
        "quantity": 3
      }
    ],
    "cart": [
      "18",
      "3",
      "4"
    ],
    "favorites": [
      "15"
    ],
    "last_login": "2024-03-15",
    "address": "68284 Matthew Key Suite 452\nLake Aaronstad, WA 19182",
    "birth_date": "1953-01-31",
    "membership_level": "Gold"
  },
  {
    "id": "99",
    "username": "christopher18",
    "email": "xsparks@nelson-franklin.com",
    "phone": "789-110-4361x70695",
    "name": "이현주",
    "password": "hashed_password_99",
    "orders": [
      {
        "product_id": "1",
        "order_date": "2024-11-27",
        "quantity": 5
      },
      {
        "product_id": "5",
        "order_date": "2024-09-26",
        "quantity": 2
      }
    ],
    "cart": [],
    "favorites": [],
    "last_login": "2024-03-30",
    "address": "5931 Boyd Ridge\nPort Michelle, LA 09669",
    "birth_date": "1989-05-15",
    "membership_level": "Silver"
  },
  {
    "id": "100",
    "username": "leslie66",
    "email": "kevin09@yahoo.com",
    "phone": "+1-091-869-8841x79340",
    "name": "이성훈",
    "password": "hashed_password_100",
    "orders": [
      {
        "product_id": "6",
        "order_date": "2024-12-22",
        "quantity": 1
      }
    ],
    "cart": [
      "16",
      "16",
      "6",
      "16"
    ],
    "favorites": [
      "17",
      "18",
      "5",
      "14",
      "10"
    ],
    "last_login": "2024-09-25",
    "address": "848 Stone Grove\nKimberlyfort, FL 53978",
    "birth_date": "1973-12-04",
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

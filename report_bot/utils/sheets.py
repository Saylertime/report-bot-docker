from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pg_maker import all_authors
import os

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SAMPLE_SPREADSHEET_ID = "14rfetnaiqgiT3o0TsLC-yi3EICobIH5rNljilhDS70M"

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())


def rep_month(month):
  SAMPLE_RANGE_NAME = f"{month}!A2:G"

  try:
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    dct = dict()

    for row in values:
      try:
        key = row[2]
        value = int(row[6])
        if key in dct:
          current_sum, current_count = dct[key]
          dct[key] = (current_sum + value, current_count + 1)
        else:
          dct[key] = (value, 1)
      except:
        pass

    msg = ''
    sorted_dct = sorted(dct.items(), key=lambda item: item[1][0], reverse=True)
    for author, summa in sorted_dct:
        msg += f"{author} — {summa[0]} руб.\nТекстов за месяц — {summa[1]}\n\n"
    return msg

  except HttpError as err:
    return str(err)


def rep_name_and_month(name, month='Январь 2024'):
    SAMPLE_RANGE_NAME = f"{month}!A2:G"

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        dct = dict()
        dct_texts = dict()
        for row in values:
            try:
                title = f"{row[0]} {row[1]}"
                money = int(row[6])
                if name == row[2]:
                    if name in dct or name in dct_texts:
                        value_money, current_count = dct[name]
                        dct_texts[name].append(title)
                        dct[name] = (value_money + money, current_count + 1)
                    else:
                        dct[name] = (money, 1)
                        dct_texts[name] = [title]
            except:
                pass
        msg = ''
        sorted_dct = sorted(dct.items(), key=lambda item: item[1][0], reverse=True)
        for author, summa in sorted_dct:
            msg += f"Гонорар за {month} — {summa[0]} руб.\nТекстов за месяц — {summa[1]}\n\nВсе тексты: \n"

        msg_texts = ''
        for title in dct_texts[name]:
            msg_texts += f"\n— {title}\n"
        msg += msg_texts
        return msg

    except HttpError as err:
        print(err)
        return str(err)


def who_is_free():
    SAMPLE_RANGE_NAME = "Февраль 2024!A2:C"

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        all_nicknames = [(i[1], i[2]) for i in all_authors()]
        for row in values:
            try:
                author = str(row[2])
                link = row[1]
                if author and not link:
                    for nickname_tuple in all_nicknames:
                        if author in nickname_tuple:
                            all_nicknames.remove(nickname_tuple)
            except:
                pass

        return all_nicknames

    except HttpError as err:
        print(err)
        return str(err)



def brief_is_free():
    SAMPLE_RANGE_NAME = "Февраль 2024!A2:J"
    print(SAMPLE_RANGE_NAME)

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        all_briefs = []
        for row in values:
            try:
                title = row[0]
                brief = row[3]
                author = row[2]
                money = str(row[6])
                symbs = str(row[8])
                print(symbs)
                if brief and not author:
                    temp_row = f"{title}\n" \
                               f"{brief}\n" \
                               f"Объем: {symbs} тыс. символов\n" \
                               f"Гонорар: {money}\n\n"
                    all_briefs.append(temp_row)
            except:
                pass

        msg = ''
        for num, brief in enumerate(all_briefs, start=1):
            msg += f"{num}. {brief}"

        return msg

    except HttpError as err:
        print(err)
        return str(err)






def stats_for_month(month):
    SAMPLE_RANGE_NAME = f"{month}!A2:G"
    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return


        all_symbs = 0
        all_texts = 0
        seo_count = 0
        seo_symbs = 0
        plain_count = 0
        plain_symbs = 0
        for row in values:
            try:
                symbols = row[4]
                type = row[5]
                link = row[1]
                if link:
                    print(type)
                    all_texts += 1
                    all_symbs += float(symbols)
                    if type == 'СЕО':
                        seo_count += 1
                        seo_symbs += symbols
                    if type == 'Простая' or type == 'Новость':
                        plain_count += 1
                        plain_symbs += symbols
            except:
                pass


        msg = f'Всего текстов за месяц: {all_texts} \n' \
              f'Всего символов за все тексты: {all_symbs}\n ' \
              f'СЕО ТЕКСТОВ — {seo_count} и {seo_symbs} символов\n' \
              f'ПРОСТЫХ ТЕКСТОВ — {plain_count} и {plain_symbs} символов'

        return msg


    except HttpError as err:
        print(err)
        return str(err)




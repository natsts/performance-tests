import httpx
import time

create_user_payload = {
  "email": f'user{time.time()}@example.com',
  "lastName": "Ivanov",
  "firstName": "Ivan",
  "middleName": "Ivanovich",
  "phoneNumber": "123123123"
}

create_user_response = httpx.post(url='http://localhost:8003/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

open_deposit_account_payload = {
  "userId": user_id
}

open_deposit_account_response = httpx.post(url='http://localhost:8003/api/v1/accounts/open-deposit-account',
                                           json=open_deposit_account_payload)
open_deposit_account_response_data = open_deposit_account_response.json()

print(open_deposit_account_response_data)
print(open_deposit_account_response.status_code)

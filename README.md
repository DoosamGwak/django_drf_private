# django_drf_private

## Introduction
- Projectname : spartamarket drf
- Build shoping mall back-end with using django-DRF
 
## Contributors
- Seungju Yi
- Yeonjae Park(readme reference)

## Duration
- 2024.08.28 ~ Now

## TechStack
- Back-End
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 3.10.11
- framework
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> 4.2
- database
  <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">


## Installation
1. Clone the repo
```
git clone https://github.com/github_username/repo_name.git
```
2. Install pip packages
```
pip install -r requirements.txt
```
3. check settings.py
```
SECRET_KEY = "enter SECRET_KEY"
DEBUG = env("DEBUG")
```

## Architecture
- erd
![image](./images/erd.png)

- project architecture
```
📦 
├─ .gitignore
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ permissions.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ validators.py
│  └─ views.py
├─ manage.py
├─ products
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ paginations.py
│  ├─ permissions.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirements.txt
└─ spartamarket_DRF
   ├─ __init__.py
   ├─ asgi.py
   ├─ settings.py
   ├─ urls.py
   └─ wsgi.py
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)


## How to use
### accounts
  <details>
    <summary>signup</summary>
    <div markdown="1">

   - endpoint : api/accounts/
   - method : POST
   - input in body
     - Required: username, password, email, name, nickname, birthday
     - Optional: sex(choice: M, W, N(default)), introduce
   - access
     - Over 15 years old can signup

   case1: signup_sucess
   ![image](./images/accounts_signup_sucess.png)
   
   case2: username validation fail
   ![image](./images/accounts_signup_username_fail.png)

   case3: email validation fail
   ![image](./images/accounts_signup_email_fail.png)

   case4: birthday validation fail
   ![image](./images/accounts_signup_birthday_fail.png)

   </div>
  </details>
  

  <details>
    <summary>login</summary>
    <div markdown="1">

   - endpoint : api/accounts/login/
   - method : POST
   - input in body
     - Required: password

  ![image](./images/accounts_login.png)
    </div>
  </details>
  

  <details>
    <summary>logout</summary>
    <div markdown="1">

   - Endpoint : api/accounts/logout/
   - method : POST
   - input in header
     - Required: access_token
   - input in body
     - Required: No need

   ![image](./images/accounts_logout.png)

   </div>
  </details>
  

  <details>
    <summary>refresh</summary>
    <div markdown="1">

    - Endpoint : api/accounts/refresh/
    - method : POST
    - input in header
      - Required: access_token
    - input in body
      - Required: refresh(it means refresh_token)

  ![image](./images/accounts_refresh.png)
      
   </div>
  </details>


  <details>
    <summary>profile detail inquiry</summary>
    <div markdown="1">

   - Endpoint : api/accounts/profile/&#60;str:username>/
   - method : GET
   - input in header
     - Required: access_token
   - input in body
     - Required: No need

  case1:
  ![image](./images/account_profile_detail.png)

      
   </div>
  </details>


  <details>
    <summary>profile update</summary>
    <div markdown="1">

   - Endpoint : api/accounts/profile/&#60;str:username>/
   - method : PUT
   - input in header
     - Required: access_token
   - input in body
     - Optional: email, name, nickname, birthday, sex(choice:M, W, N(default)), introduce 
   - access
     - Owner only


  case1: Not owner
  ![image](./images/account_profile_update_url_fail.png)

  case2: validation fail
  ![image](./images/account_profile_update_fail_1.png)

  case3: sucess
  ![image](./images/account_profile_update_sucess.png)
      
    </div>
  </details>


  <details>
    <summary>profile delete</summary>
    <div markdown="1">

   - Endpoint : api/accounts/profile/
   - method : DELETE
   - input in header
     - Required: access_token
   - input in body
     - Required: password, refresh(means refresh_token)
   - access
     - Owner only

  case1: fail 1 
  ![image](./images/account_delete_fail.png)

  case2: fail 2
  ![image](./images/account_delete_fail_2.png)
  
  case3: sucess
  ![image](./images/account_delete_sucess.png)
      
   </div>
  </details>


  <details>
    <summary>password change</summary>
    <div markdown="1">

   - Endpoint : api/accounts/password/
   - method : PUT
   - input in header
     - Required: access_token
   - input in body
     - Required: old_password, password1, password2 (password1 and password2 mean new password you want to set)
   - access
     - Owner only

  case1: new password validation fail1
  ![image](./images/account_change_password_fail_1.png)

  case2: new password validation fail2
  ![image](./images/account_change_password_fail_2.png)

  case3: old password validation fail
  ![image](./images/account_change_password_fail_3.png)

  case4: sucess
  ![image](./images/account_change_password_sucess.png)
      
   </div>
  </details>


  <details>
    <summary>follow</summary>
    <div markdown="1">

   - Endpoint : api/accounts/follow/&#60;str:username>/
   - method : POST
   - input in header
     - Required: access_token
   - input in body
     - Required: No need
   - access
     - Owner only

  case1: already followed
  ![image](./images/follow_fail1.png)

  case2: can't follow self
  ![image](./images/follow_fail2.png)

  case3: sucess
  ![image](./images/follow_sucess.png)
      
   </div>
  </details>


  <details>
    <summary>unfollow</summary>
    <div markdown="1">

   - Endpoint : api/accounts/follow/&#60;str:username>/
   - method : DELETE
   - input in header
     - Required: access_token
   - input in body
     - Required: No need
   - access
     - Owner only

   case1: didn't follow
   ![image](./images/unfollow_fail2.png)

   case2: can't unfollow self
   ![image](./images/unfollow_fail1.png)

   case3: sucess
   ![image](./images/unfollow_sucess.png)
     
   </div>
  </details>


### product

  <details>
    <summary>product registration</summary>
    <div markdown="1">

   - endpoint : api/products/
   - method : POST
   - input in header
     - Required: access_token
   - input in body
     - Required: title, content
     - Optional: image

   ![image](./images/products_create.png)

   </div>
  </details>


  <details>
    <summary>product list inquiry</summary>
    <div markdown="1">

   - endpoint : api/products/list/
   - method : GET
   - input in header
     - Required: No need
   - input in body
     - Required: No need

   ![image](./images/products_list.png)

   -additional features
     -pagenation
       - There are 10 products on one page, and the page number is entered through query string. ex -> end of url add "?page=2"
       ![image](./images/products_list_page.png)

     -filtering
       - It can be filtered by title, content, and the search term is passed through query string
       ![image](./images/products_list_search.png)

   </div>
  </details>
  

  <details>
    <summary>product detail inquiry</summary>
    <div markdown="1">

   - endpoint : /api/products/&#60;int:productID>
   - method : GET
   - input in header
     - Required: access_token
   - input in body
     - Required: No need

   ![image](./images/products_detail.png)

   </div>
  </details>


  <details>
    <summary>product update</summary>
    <div markdown="1">

   - endpoint : /api/products/&#60;int:productID>
   - method : PUT
   - input in header
     - Required: access_token
   - input in body
     - Required: title, content
     - Optional: image, tags
   - access
     - Owner only

   case1: Not owner
   ![image](./images/products_update_fail.png)

   case2: sucess
   ![image](./images/products_update_sucess.png)

   </div>
  </details>


  <details>
    <summary>product delete</summary>
    <div markdown="1">

   - endpoint : /api/products/&#60;int:productID>
   - method : DELETE
   - input in header
     - Required: access_token
   - input in body
     - Required: No need
   - access
     - Owner only

   case1: Not Owner
   ![image](./images/products_delete_fail.png)

   case2: sucess
   ![image](./images/products_delete_sucess.png)

   </div>
  </details>


  <details>
    <summary>product like</summary>
    <div markdown="1">

   - endpoint : /api/products/&#60;int:productID>/like/
   - method : POST
   - input in header
     - Required: access_token
   - input in body
     - Required: No need
   - access
     - Owner only

   case1: Not Owner
   ![image](./images/products_delete_fail.png)

   case2: sucess
   ![image](./images/products_delete_sucess.png)

   </div>
  </details>


  <details>
    <summary>product like cancel</summary>/like/
    <div markdown="1">

   - endpoint : /api/products/&#60;int:productID>
   - method : DELETE
   - input in header
     - Required: access_token
   - input in body
     - Required: No need
   - access
     - Owner only

   case1: Not Owner
   ![image](./images/products_delete_fail.png)

   case2: sucess
   ![image](./images/products_delete_sucess.png)

   </div>
  </details>

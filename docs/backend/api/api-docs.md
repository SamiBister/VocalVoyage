---
title: VocabVoyage v0.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="vocabvoyage">VocabVoyage v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="vocabvoyage-default">Default</h1>

## set_mode_set_mode__post

<a id="opIdset_mode_set_mode__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /set_mode/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /set_mode/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "mode": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/set_mode/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/set_mode/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/set_mode/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/set_mode/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/set_mode/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/set_mode/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /set_mode/`

*Set Mode*

Sets the quiz mode.

Parameters
----------
request : ModeRequest
    The request containing the desired mode.

Raises
------
HTTPException
    If the mode is not 'normal' or 'infinite'.

Returns
-------
JSONResponse
    A response indicating the mode has been set.

> Body parameter

```json
{
  "mode": "string"
}
```

<h3 id="set_mode_set_mode__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ModeRequest](#schemamoderequest)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="set_mode_set_mode__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="set_mode_set_mode__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## start_quiz_start_quiz__post

<a id="opIdstart_quiz_start_quiz__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /start_quiz/ \
  -H 'Accept: application/json'

```

```http
POST /start_quiz/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/start_quiz/',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/start_quiz/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/start_quiz/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/start_quiz/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/start_quiz/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/start_quiz/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /start_quiz/`

*Start Quiz*

Endpoint to start a new quiz session.

This endpoint resets the current quiz session and starts a new one. It clears any
previous quiz data and prepares the system for a new quiz session. This can be 
useful when a user wants to restart the quiz from the beginning.

Returns
-------
    JSONResponse: A response indicating that the quiz has started.

> Example responses

> 200 Response

```json
null
```

<h3 id="start_quiz_start_quiz__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="start_quiz_start_quiz__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## end_quiz_end_quiz__post

<a id="opIdend_quiz_end_quiz__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /end_quiz/ \
  -H 'Accept: application/json'

```

```http
POST /end_quiz/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/end_quiz/',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/end_quiz/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/end_quiz/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/end_quiz/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/end_quiz/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/end_quiz/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /end_quiz/`

*End Quiz*

Endpoint to end the current quiz session and log the results.

This endpoint marks the end of the current quiz session. It triggers the logging
of the quiz results, including the number of correct and incorrect answers, and 
any other relevant statistics. This can be useful for tracking user performance 
and providing feedback.

Returns
-------
    JSONResponse: A response indicating that the quiz has ended and results have been logged.

> Example responses

> 200 Response

```json
null
```

<h3 id="end_quiz_end_quiz__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="end_quiz_end_quiz__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_next_word_words_next_get

<a id="opIdget_next_word_words_next_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /words/next \
  -H 'Accept: application/json'

```

```http
GET /words/next HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/words/next',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/words/next',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/words/next', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/words/next', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/words/next");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/words/next", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /words/next`

*Get Next Word*

Endpoint to retrieve the next word in the quiz.

Returns
-------
    Optional[Word]: The next word in the quiz, or None if there are no more words.

> Example responses

> 200 Response

```json
{
  "foreign_term": "string",
  "native_translation": "string"
}
```

<h3 id="get_next_word_words_next_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_next_word_words_next_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Next Word Words Next Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Get Next Word Words Next Get|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[Word](#schemaword)|false|none|Represents a word with its foreign term and native translation.<br><br>Attributes:<br>    foreign_term (str): The word in the foreign language.<br>    native_translation (str): The translation of the foreign term in the native language.|
|»» foreign_term|string|true|none|none|
|»» native_translation|string|true|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## check_answer_check__post

<a id="opIdcheck_answer_check__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /check/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /check/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "word": {
    "foreign_term": "string",
    "native_translation": "string"
  },
  "user_input": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/check/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/check/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/check/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/check/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/check/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/check/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /check/`

*Check Answer*

Check if the user's answer is correct.

Parameters
----------
answer : AnswerRequest
    The user's answer request containing the word and user input.

Returns
-------
dict
    A dictionary with a key 'is_correct' indicating whether the user's answer is correct.

> Body parameter

```json
{
  "word": {
    "foreign_term": "string",
    "native_translation": "string"
  },
  "user_input": "string"
}
```

<h3 id="check_answer_check__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AnswerRequest](#schemaanswerrequest)|true|none|

> Example responses

> 200 Response

```json
{}
```

<h3 id="check_answer_check__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="check_answer_check__post-responseschema">Response Schema</h3>

Status Code **200**

*Response Check Answer Check  Post*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## get_results_results__get

<a id="opIdget_results_results__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /results/ \
  -H 'Accept: application/json'

```

```http
GET /results/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/results/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/results/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/results/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/results/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/results/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/results/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /results/`

*Get Results*

Endpoint to get current quiz statistics.

> Example responses

> 200 Response

```json
{}
```

<h3 id="get_results_results__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_results_results__get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Results Results  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

<aside class="success">
This operation does not require authentication
</aside>

## upload_words_upload_words__post

<a id="opIdupload_words_upload_words__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /upload_words/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /upload_words/ HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "files": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/upload_words/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/upload_words/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/upload_words/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/upload_words/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/upload_words/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/upload_words/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /upload_words/`

*Upload Words*

Endpoint to upload new word files.

This endpoint allows users to upload new word files in CSV format. It clears any
existing word files in the data directory and replaces them with the newly uploaded
files. The words from the new files are then loaded into the system.

Parameters
----------
files : List[UploadFile]
    A list of uploaded files. Each file must be in CSV format.

Raises
------
HTTPException
    If any of the uploaded files is not a CSV file.

Returns
-------
dict
    A message indicating that the word files have been uploaded and the word list has been updated.

> Body parameter

```yaml
files:
  - string

```

<h3 id="upload_words_upload_words__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_upload_words_upload_words__post](#schemabody_upload_words_upload_words__post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="upload_words_upload_words__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="upload_words_upload_words__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AnswerRequest">AnswerRequest</h2>
<!-- backwards compatibility -->
<a id="schemaanswerrequest"></a>
<a id="schema_AnswerRequest"></a>
<a id="tocSanswerrequest"></a>
<a id="tocsanswerrequest"></a>

```json
{
  "word": {
    "foreign_term": "string",
    "native_translation": "string"
  },
  "user_input": "string"
}

```

AnswerRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|word|[Word](#schemaword)|true|none|Represents a word with its foreign term and native translation.<br><br>Attributes:<br>    foreign_term (str): The word in the foreign language.<br>    native_translation (str): The translation of the foreign term in the native language.|
|user_input|string|true|none|none|

<h2 id="tocS_Body_upload_words_upload_words__post">Body_upload_words_upload_words__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_upload_words_upload_words__post"></a>
<a id="schema_Body_upload_words_upload_words__post"></a>
<a id="tocSbody_upload_words_upload_words__post"></a>
<a id="tocsbody_upload_words_upload_words__post"></a>

```json
{
  "files": [
    "string"
  ]
}

```

Body_upload_words_upload_words__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|files|[string]|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ModeRequest">ModeRequest</h2>
<!-- backwards compatibility -->
<a id="schemamoderequest"></a>
<a id="schema_ModeRequest"></a>
<a id="tocSmoderequest"></a>
<a id="tocsmoderequest"></a>

```json
{
  "mode": "string"
}

```

ModeRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mode|string|true|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_Word">Word</h2>
<!-- backwards compatibility -->
<a id="schemaword"></a>
<a id="schema_Word"></a>
<a id="tocSword"></a>
<a id="tocsword"></a>

```json
{
  "foreign_term": "string",
  "native_translation": "string"
}

```

Word

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|foreign_term|string|true|none|none|
|native_translation|string|true|none|none|

